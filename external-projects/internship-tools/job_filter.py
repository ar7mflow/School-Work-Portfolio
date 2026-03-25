#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import re
import sys
import urllib.request
from dataclasses import dataclass
from html import unescape
from pathlib import Path
from typing import Dict, List, Optional, Tuple


@dataclass
class JobRecord:
    source: str
    job_id: str
    title: str
    company: str
    location: str
    url: str
    deadline: str
    duration_months: Optional[int]
    gpa_requirement: Optional[float]
    transcript_required: Optional[bool]
    description: str


def parse_bool(value: str) -> Optional[bool]:
    v = (value or "").strip().lower()
    if v in {"yes", "true", "1", "y"}:
        return True
    if v in {"no", "false", "0", "n"}:
        return False
    return None


def parse_date(value: str) -> Optional[dt.date]:
    v = (value or "").strip()
    if not v:
        return None
    for fmt in ("%Y-%m-%d", "%b %d, %Y", "%B %d, %Y", "%Y/%m/%d"):
        try:
            return dt.datetime.strptime(v, fmt).date()
        except ValueError:
            pass
    return None


def days_until(deadline: str) -> Optional[int]:
    d = parse_date(deadline)
    if d is None:
        return None
    return (d - dt.date.today()).days


def strip_html(raw: str) -> str:
    raw = re.sub(r"<script.*?</script>", " ", raw, flags=re.I | re.S)
    raw = re.sub(r"<style.*?</style>", " ", raw, flags=re.I | re.S)
    raw = re.sub(r"<[^>]+>", " ", raw)
    raw = unescape(raw)
    raw = re.sub(r"\s+", " ", raw)
    return raw.strip()


def infer_duration_months(text: str) -> Optional[int]:
    t = (text or "").lower()
    m = re.search(r"\b(12|16)\s*[-–]?\s*(month|months|mo|mos)\b", t)
    if m:
        return int(m.group(1))
    if "spring/summer" in t or "summer term" in t or "4 month" in t or "4-month" in t:
        return 4
    return None


def infer_gpa_requirement(text: str) -> Optional[float]:
    t = (text or "").lower()
    # examples: 2.7+, 3.0/4.0, minimum GPA 3.0
    m = re.search(r"(?:gpa[^\d]{0,20})?(\d\.\d)\s*(?:\+|/\s*4\.0|minimum|min)", t)
    if m:
        try:
            return float(m.group(1))
        except ValueError:
            return None
    return None


def infer_transcript_required(text: str) -> Optional[bool]:
    t = (text or "").lower()
    if "unofficial transcript" in t or "uploading an unofficial copy" in t or "transcript required" in t:
        return True
    if "no transcript" in t:
        return False
    return None


def keyword_score(text: str, keywords: List[str]) -> int:
    t = (text or "").lower()
    count = 0
    for kw in keywords:
        if kw.lower() in t:
            count += 1
    return count


def score_ai_relevance(job: JobRecord, cfg: Dict) -> int:
    text = f"{job.title} {job.description}".lower()
    direct = keyword_score(text, cfg["direct_ai_keywords"])
    adjacent = keyword_score(text, cfg["adjacent_ai_keywords"])
    base = min(50, direct * 5 + adjacent * 2)
    return base


def score_skill_match(job: JobRecord, cfg: Dict) -> int:
    text = f"{job.title} {job.description}".lower()
    hits = keyword_score(text, cfg["candidate_skills_keywords"])
    return min(30, hits * 2)


def score_career_leverage(job: JobRecord, cfg: Dict) -> int:
    company = (job.company or "").lower()
    top = {c.lower() for c in cfg["top_brand_companies"]}
    strong = {c.lower() for c in cfg["strong_brand_companies"]}
    if any(k in company for k in top):
        return 10
    if any(k in company for k in strong):
        return 8
    return 4


def score_urgency(job: JobRecord) -> int:
    du = days_until(job.deadline)
    if du is None:
        return 3
    if du < 0:
        return 0
    if du < 5:
        return 10
    if du <= 14:
        return 7
    return 4


def decision(score: int) -> str:
    if score >= 80:
        return "APPLY NOW"
    if score >= 65:
        return "Apply if bandwidth"
    return "SKIP"


def should_block(job: JobRecord, cfg: Dict) -> Tuple[bool, List[str]]:
    reasons: List[str] = []

    if cfg.get("quip_only", True):
        if job.duration_months is not None and not (cfg["min_duration_months"] <= job.duration_months <= cfg["max_duration_months"]):
            reasons.append(f"Duration {job.duration_months}m is outside QUIP {cfg['min_duration_months']}-{cfg['max_duration_months']}m")

    user_gpa = cfg.get("user_gpa")
    if user_gpa is not None and job.gpa_requirement is not None and job.gpa_requirement > user_gpa:
        reasons.append(f"GPA min {job.gpa_requirement} > profile GPA threshold {user_gpa}")

    if not cfg.get("allow_transcript_required", False) and job.transcript_required is True:
        reasons.append("Transcript required (currently blocked)")

    if cfg.get("canada_only", True):
        location = (job.location or "").lower()
        if location and not any(k in location for k in ["on", "ontario", "canada", "remote"]):
            reasons.append("Outside Canada/Ontario focus")

    return (len(reasons) > 0, reasons)


def load_jobs_csv(path: Path) -> List[JobRecord]:
    rows: List[JobRecord] = []
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for r in reader:
            description = r.get("description", "")
            title = r.get("title", "")
            duration = r.get("duration_months", "").strip()
            duration_months = int(duration) if duration.isdigit() else infer_duration_months(f"{title} {description}")
            gpa_raw = r.get("gpa_requirement", "").strip()
            gpa_req = float(gpa_raw) if gpa_raw else infer_gpa_requirement(description)
            transcript = parse_bool(r.get("transcript_required", ""))
            if transcript is None:
                transcript = infer_transcript_required(description)
            rows.append(
                JobRecord(
                    source=r.get("source", "unknown"),
                    job_id=r.get("job_id", ""),
                    title=title,
                    company=r.get("company", ""),
                    location=r.get("location", ""),
                    url=r.get("url", ""),
                    deadline=r.get("deadline", ""),
                    duration_months=duration_months,
                    gpa_requirement=gpa_req,
                    transcript_required=transcript,
                    description=description,
                )
            )
    return rows


def fetch_url_text(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        html = resp.read().decode("utf-8", errors="ignore")
    return html


def parse_greenhouse_job(url: str) -> Optional[JobRecord]:
    try:
        html = fetch_url_text(url)
    except Exception:
        return None

    title = ""
    company = ""
    location = ""

    mt = re.search(r"<meta property=\"og:title\" content=\"([^\"]+)\"", html, flags=re.I)
    if mt:
        title = mt.group(1)
    mc = re.search(r"<meta property=\"og:site_name\" content=\"([^\"]+)\"", html, flags=re.I)
    if mc:
        company = mc.group(1)
    ml = re.search(r"location\"\s*:\s*\"([^\"]+)\"", html, flags=re.I)
    if ml:
        location = ml.group(1)

    body_text = strip_html(html)
    duration = infer_duration_months(body_text)
    gpa_req = infer_gpa_requirement(body_text)
    transcript = infer_transcript_required(body_text)

    jid_match = re.search(r"jobs/(\d+)", url)
    jid = jid_match.group(1) if jid_match else ""

    return JobRecord(
        source="greenhouse",
        job_id=jid,
        title=title,
        company=company,
        location=location,
        url=url,
        deadline="",
        duration_months=duration,
        gpa_requirement=gpa_req,
        transcript_required=transcript,
        description=body_text[:15000],
    )


def load_greenhouse_urls(path: Path) -> List[JobRecord]:
    jobs: List[JobRecord] = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            url = line.strip()
            if not url or url.startswith("#"):
                continue
            job = parse_greenhouse_job(url)
            if job:
                jobs.append(job)
    return jobs


def write_ranked_csv(path: Path, rows: List[Dict]):
    fieldnames = [
        "rank",
        "score_total",
        "decision",
        "blocked",
        "block_reasons",
        "source",
        "job_id",
        "title",
        "company",
        "location",
        "deadline",
        "duration_months",
        "gpa_requirement",
        "transcript_required",
        "score_ai_relevance",
        "score_skill_match",
        "score_career_leverage",
        "score_urgency",
        "url",
    ]
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for i, row in enumerate(rows, start=1):
            out = dict(row)
            out["rank"] = i
            writer.writerow(out)


def write_summary_md(path: Path, rows: List[Dict]):
    top = [r for r in rows if not r["blocked"]][:10]
    blocked = [r for r in rows if r["blocked"]]

    lines = [
        "# Job Filter Summary",
        "",
        f"Generated: {dt.datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"Total jobs processed: {len(rows)}",
        f"Eligible jobs: {len(rows) - len(blocked)}",
        f"Blocked jobs: {len(blocked)}",
        "",
        "## Top Eligible Targets",
        "",
        "| Rank | Score | Decision | Role | Company | Location | Duration | Deadline |",
        "|---:|---:|---|---|---|---|---:|---|",
    ]

    for i, row in enumerate(top, start=1):
        lines.append(
            f"| {i} | {row['score_total']} | {row['decision']} | {row['title']} | {row['company']} | {row['location']} | {row['duration_months'] or 'TBD'} | {row['deadline'] or 'TBD'} |"
        )

    lines.extend([
        "",
        "## Blocked Jobs (Hard Filters)",
        "",
        "| Role | Company | Reasons |",
        "|---|---|---|",
    ])

    for row in blocked[:25]:
        lines.append(f"| {row['title']} | {row['company']} | {row['block_reasons']} |")

    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Mass job filter for QUIP + AI-targeting workflow")
    parser.add_argument("--jobs-csv", type=Path, help="CSV file of jobs (LinkedIn/manual exports)")
    parser.add_argument("--greenhouse-urls", type=Path, help="Text file with Greenhouse job URLs (one per line)")
    parser.add_argument("--criteria", type=Path, required=True, help="JSON criteria file")
    parser.add_argument("--out-csv", type=Path, required=True, help="Output ranked CSV path")
    parser.add_argument("--out-md", type=Path, required=True, help="Output markdown summary path")
    args = parser.parse_args()

    cfg = json.loads(args.criteria.read_text(encoding="utf-8"))

    jobs: List[JobRecord] = []
    if args.jobs_csv:
        jobs.extend(load_jobs_csv(args.jobs_csv))
    if args.greenhouse_urls:
        jobs.extend(load_greenhouse_urls(args.greenhouse_urls))

    if not jobs:
        print("No jobs loaded. Provide --jobs-csv and/or --greenhouse-urls", file=sys.stderr)
        return 1

    scored: List[Dict] = []
    for job in jobs:
        ai = score_ai_relevance(job, cfg)
        skill = score_skill_match(job, cfg)
        leverage = score_career_leverage(job, cfg)
        urgency = score_urgency(job)
        total = ai + skill + leverage + urgency
        blocked, reasons = should_block(job, cfg)
        scored.append(
            {
                "score_total": total,
                "decision": decision(total) if not blocked else "BLOCKED",
                "blocked": blocked,
                "block_reasons": "; ".join(reasons),
                "source": job.source,
                "job_id": job.job_id,
                "title": job.title,
                "company": job.company,
                "location": job.location,
                "deadline": job.deadline,
                "duration_months": job.duration_months,
                "gpa_requirement": job.gpa_requirement,
                "transcript_required": job.transcript_required,
                "score_ai_relevance": ai,
                "score_skill_match": skill,
                "score_career_leverage": leverage,
                "score_urgency": urgency,
                "url": job.url,
            }
        )

    scored.sort(key=lambda x: (x["blocked"], -x["score_total"]))

    args.out_csv.parent.mkdir(parents=True, exist_ok=True)
    args.out_md.parent.mkdir(parents=True, exist_ok=True)
    write_ranked_csv(args.out_csv, scored)
    write_summary_md(args.out_md, scored)

    print(f"Done. Ranked jobs: {args.out_csv}")
    print(f"Summary: {args.out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
