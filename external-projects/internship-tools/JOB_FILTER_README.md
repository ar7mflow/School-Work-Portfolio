# Mass Job Filter (QUIP + AI Criteria)

This tool filters and ranks jobs from LinkedIn/manual CSV rows and Greenhouse URLs using your hard constraints:
- QUIP only (12–16 months)
- Canada focus
- GPA/transcript barriers
- AI relevance + skill fit + leverage + urgency scoring

## Files
- `job_filter.py` — scoring/filter engine
- `job_filter_criteria.json` — all rules and keyword weights
- `jobs_input_template.csv` — LinkedIn/manual input format
- `greenhouse_urls_template.txt` — one Greenhouse URL per line

## Quick Start

## 1) Prepare inputs
- Copy `jobs_input_template.csv` and paste your LinkedIn/manual jobs
- Optional: copy `greenhouse_urls_template.txt` and paste Greenhouse job links

## 2) Run

```powershell
python "Ar7 & Internship Search/05_Tools/job_filter.py" \
  --criteria "Ar7 & Internship Search/05_Tools/job_filter_criteria.json" \
  --jobs-csv "Ar7 & Internship Search/05_Tools/jobs_input_template.csv" \
  --greenhouse-urls "Ar7 & Internship Search/05_Tools/greenhouse_urls_template.txt" \
  --out-csv "Ar7 & Internship Search/02_Core-Docs/Knowledge-Base/job_filter_ranked.csv" \
  --out-md "Ar7 & Internship Search/02_Core-Docs/Knowledge-Base/job_filter_summary.md"
```

If you only have CSV or only Greenhouse URLs, omit the other flag.

## Output
- `job_filter_ranked.csv` — full ranked list with component scores and block reasons
- `job_filter_summary.md` — top 10 eligible + blocked jobs table

## Important Notes
- LinkedIn pages are often anti-scrape, so use copied descriptions or exported rows in CSV
- Greenhouse links are fetchable directly by URL in most cases
- You can tune strictness in `job_filter_criteria.json` (e.g., allow transcript-required roles)

## Most Useful Tweaks
- `quip_only`: true/false
- `min_duration_months` / `max_duration_months`
- `user_gpa`
- `allow_transcript_required`
- keyword lists for AI relevance and skill match
