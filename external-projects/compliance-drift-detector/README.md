\# Halluci-NOT Read Me!!



\*\*Real-time AI Governance Layer for SAP GenAI Hub\*\*



A lightweight validation system that catches PII leaks, AI hallucinations, and policy violations in LLM outputs before they reach production users.



!\[Architecture](https://img.shields.io/badge/Architecture-Two--Layer\_Validation-blue)

!\[Build Time](https://img.shields.io/badge/Build\_Time-2\_hours-green)

!\[Test Results](https://img.shields.io/badge/Catch\_Rate-100%25-brightgreen)



---



\## 🎯 The Problem



Enterprise GenAI has three predictable failure modes:



1\. \*\*PII Leakage\*\* → GDPR violations (4% of global revenue in fines)

2\. \*\*Hallucinations\*\* → Operational failures (users follow AI's confident lies)

3\. \*\*Policy Violations\*\* → Audit failures (unapproved vendors, breached rules)



Generic content filters don't know YOUR approved vendors, YOUR SAP landscape, or YOUR business policies.



---



\## 💡 The Solution



\*\*Two-Layer Validation: Pattern Matching + LLM Reasoning\*\*

```

User Query → Generator → Checker → Decision (PASS/REVIEW/BLOCK) → Audit Log

```



\### What It Detects



| Violation Type | Severity | Example |

|----------------|----------|---------|

| \*\*PII Leak\*\* | 90-95 | Customer email/phone exposed |

| \*\*Policy Violation\*\* | 80-90 | Unapproved vendor recommended |

| \*\*Hallucination\*\* | 75-85 | Fake SAP transaction code (ME99X) |

| \*\*Clean Response\*\* | 0 | Verified, safe content ✅ |



---



\## 📊 Test Results



| Test | Scenario | Decision | Severity | Evidence |

|------|----------|----------|----------|----------|

| 1 | PII Exposure | \*\*BLOCKED\*\* | 95 | Email + phone in response |

| 2 | Policy Breach | \*\*BLOCKED\*\* | 85 | Unapproved vendor (CheapSteel Ltd.) |

| 3 | Hallucination | \*\*BLOCKED\*\* | 80 | Fake T-code (ME99X) among real ones |

| 4 | Clean Query | \*\*PASSED\*\* | 0 | General SAP info, no violations ✅ |



\*\*Key Achievement:\*\* Caught 1 fake T-code (ME99X) embedded among 3 real ones (ME21N, EKKO, ME23N) — demonstrating precision, not just pattern matching.



---



\## 🏗️ Architecture



\### Two-Layer Validation System



\*\*Layer 1: Deterministic Checks\*\*

\- Regex patterns for PII (emails, phones, IDs)

\- Allowlist verification for SAP terms

\- Policy rule matching (vendors, discounts, thresholds)



\*\*Layer 2: LLM Reasoning (GPT-4o mini)\*\*

\- Context-aware PII detection

\- Hallucination verification against domain knowledge

\- Policy interpretation for edge cases



\*\*Layer 3: Severity Scoring\*\*

\- Risk-based thresholds (0-100 scale)

\- Business impact mapping

\- Automated action decisions

```

┌─────────────────────────────────────────────────────────┐

│                  USER QUERY                             │

└────────────────────┬────────────────────────────────────┘

&nbsp;                    │

&nbsp;                    ▼

┌─────────────────────────────────────────────────────────┐

│         GENERATOR (SAP Assistant)                       │

│         Returns JSON: {answer, confidence}              │

└────────────────────┬────────────────────────────────────┘

&nbsp;                    │

&nbsp;                    ▼

┌─────────────────────────────────────────────────────────┐

│         COMPLIANCE CHECKER                              │

│  ├─ PII Detection (regex + LLM context)                │

│  ├─ SAP Term Verification (allowlist)                  │

│  ├─ Policy Validation (business rules)                 │

│  └─ Severity Scoring (0-100)                           │

└────────────────────┬────────────────────────────────────┘

&nbsp;                    │

&nbsp;                    ▼

┌─────────────────────────────────────────────────────────┐

│  DECISION: PASS | REVIEW | BLOCK                        │

│  + Audit Log (evidence, impact, recommendation)        │

└─────────────────────────────────────────────────────────┘

```



---



\## 🚀 Quick Start



\### Installation

```bash

\# Clone repository

git clone https://github.com/YOUR-USERNAME/compliance-drift-detector.git

cd compliance-drift-detector



\# Install dependencies

pip install -r requirements.txt



\# Set up environment variables

cp .env.example .env

\# Add your OpenAI API key to .env

```



\### Basic Usage

```python

from checker import ComplianceChecker

from generator import SAPAssistant



\# Initialize

assistant = SAPAssistant()

checker = ComplianceChecker()



\# Generate response

user\_query = "How do I create a purchase order in SAP?"

response = assistant.generate(user\_query)



\# Validate

result = checker.validate(response)



print(f"Decision: {result\['decision']}")

print(f"Severity: {result\['severity']}")

if result\['violations']:

&nbsp;   for v in result\['violations']:

&nbsp;       print(f"⚠️ {v\['type']}: {v\['evidence']}")

```



\### Run Tests

```bash

\# Run all test scenarios

python -m pytest tests/



\# Run specific test

python tests/test\_hallucination.py

```



---



\## 📁 Project Structure

```

compliance-drift-detector/

├── README.md                 # This file

├── requirements.txt          # Python dependencies

├── .env.example             # Environment variable template

├── config.py                # Allowlists and policy rules

├── generator.py             # SAP Assistant (response generator)

├── checker.py               # Compliance validation logic

├── main.py                  # CLI interface

├── tests/

│   ├── test\_pii\_leak.py

│   ├── test\_policy\_violation.py

│   ├── test\_hallucination.py

│   └── test\_clean\_response.py

└── docs/

&nbsp;   └── ARCHITECTURE.md      # Detailed technical documentation

```



---



\## 🔧 Configuration



\### Allowlists (in `config.py`)



\*\*SAP Transaction Codes:\*\*

```python

APPROVED\_TCODES = \[

&nbsp;   "VA01", "VA02", "VA03",     # Sales \& Distribution

&nbsp;   "ME21N", "ME22N", "ME23N",  # Procurement

&nbsp;   "FB50", "FB60", "FB70",     # Finance

&nbsp;   "MM01", "MM02", "MM03",     # Material Management

&nbsp;   "XD01", "XD02", "XD03"      # Master Data

]

```



\*\*Approved Vendors:\*\*

```python

APPROVED\_VENDORS = \[

&nbsp;   "Acme Industrial Supplies",

&nbsp;   "Global Tech Partners GmbH",

&nbsp;   "Premium Components Inc.",

&nbsp;   "Certified Steel Solutions"

]

```



\*\*Policy Rules:\*\*

```python

POLICY\_RULES = {

&nbsp;   "max\_discount\_percent": 15,

&nbsp;   "approval\_threshold\_usd": 50000

}

```



---



\## 📈 Severity Scoring Logic

```python

def calculate\_severity(violations):

&nbsp;   """

&nbsp;   Severity scale: 0-100

&nbsp;   - 0-30: PASS (log for monitoring)

&nbsp;   - 31-70: REVIEW (human oversight needed)

&nbsp;   - 71-100: BLOCK (immediate rejection)

&nbsp;   """

&nbsp;   base\_scores = {

&nbsp;       "PII\_LEAK": 95,              # GDPR violation risk

&nbsp;       "POLICY\_VIOLATION": 85,      # Audit/compliance breach

&nbsp;       "UNVERIFIED\_SAP\_TERM": 80    # Operational failure risk

&nbsp;   }

&nbsp;   

&nbsp;   if not violations:

&nbsp;       return 0

&nbsp;   

&nbsp;   # Take highest base score

&nbsp;   max\_score = max(\[base\_scores.get(v\["type"], 50) for v in violations])

&nbsp;   

&nbsp;   # Escalate for multiple violations

&nbsp;   if len(violations) > 1:

&nbsp;       max\_score = min(100, max\_score + 10)

&nbsp;   

&nbsp;   return max\_score

```



---



\## 🎓 Built With



\- \*\*Platform:\*\* SAP AI Launchpad (Generative AI Hub)

\- \*\*Models:\*\* 

&nbsp; - Generator: Gemini 2.0 Flash Lite

&nbsp; - Checker: GPT-4o mini

\- \*\*Techniques:\*\* Prompt engineering, function calling, structured outputs

\- \*\*Build Time:\*\* 2 hours (proof-of-concept)

\- \*\*Code:\*\* Zero custom ML training (pure prompt engineering)



---



\## 🛣️ Roadmap (V2)



\### Production Enhancements

\- \[ ] \*\*Persistent Logging:\*\* PostgreSQL for audit trails with retention policies

\- \[ ] \*\*Feedback Loops:\*\* Track false positives, retune thresholds

\- \[ ] \*\*Custom Policy DSL:\*\* Let admins define rules without code

\- \[ ] \*\*Multi-Model Voting:\*\* Consensus across GPT/Gemini/Claude for higher confidence

\- \[ ] \*\*SAP BTP Integration:\*\* Deploy as orchestration module in GenAI Hub

\- \[ ] \*\*Dashboard:\*\* Real-time violation monitoring for governance teams

\- \[ ] \*\*SOC 2 Compliance:\*\* Encryption, access controls, audit logging



\### Known Limitations (V1)

\- Allowlist scope limited to 15 T-codes (demo scale)

\- Edge case: Embedded SAP terms in natural language sometimes misclassified

\- No learning from feedback (static rules)

\- Session-only (no database)



---



\## 📄 License



MIT License - See LICENSE file for details



---



\## 🤝 Contributing



This is a proof-of-concept for educational/portfolio purposes. Not accepting contributions at this time, but feel free to fork and adapt for your use case.



---



\## 📧 Contact



\*\*Arham Hassan\*\*  

\- LinkedIn: \[linkedin.com/in/arham-hassan-a21457242](https://linkedin.com/in/arham-hassan-a21457242)

\- Email: 23cr8@queensu.ca



Built as part of SAP Generative AI Developer certification project.



---



\## 🏆 Achievements



\- ✅ 100% catch rate on test scenarios

\- ✅ Zero false positives

\- ✅ Built in 2 hours with no custom ML training

\- ✅ Production-ready architecture design

\- ✅ Enterprise governance thinking (GDPR, SOX, audit trails)



---



\*\*Status:\*\* Proof-of-Concept ✅ | Production-Ready: See V2 Roadmap

=======
# Halluci-NOT
Compliance-Drift-Detector ( Real-time AI governance layer for SAP GenAI Hub - catches PII leaks, hallucinations, and policy violations ).
