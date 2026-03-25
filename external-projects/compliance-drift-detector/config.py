"""
Configuration for Compliance Drift Detector
Defines allowlists and policy rules for validation
"""

# SAP Transaction Codes (Approved)
APPROVED_TCODES = [
    # Sales & Distribution
    "VA01", "VA02", "VA03",
    
    # Procurement
    "ME21N", "ME22N", "ME23N",
    
    # Finance
    "FB50", "FB60", "FB70",
    
    # Material Management
    "MM01", "MM02", "MM03",
    
    # Master Data
    "XD01", "XD02", "XD03"
]

# SAP Modules (Approved)
APPROVED_MODULES = [
    "SD",   # Sales & Distribution
    "MM",   # Materials Management
    "FI",   # Financial Accounting
    "CO",   # Controlling
    "PP",   # Production Planning
    "QM",   # Quality Management
    "HR"    # Human Resources
]

# SAP Tables (Approved)
APPROVED_TABLES = [
    "MARA",   # Material Master
    "KNA1",   # Customer Master
    "LFA1",   # Vendor Master
    "BKPF",   # Accounting Document Header
    "VBAK",   # Sales Document Header
    "EKKO",   # Purchasing Document Header
    "EKPO"    # Purchasing Document Item
]

# Approved Vendors (Business Policy)
APPROVED_VENDORS = [
    "Acme Industrial Supplies",
    "Global Tech Partners GmbH",
    "Premium Components Inc.",
    "Certified Steel Solutions"
]

# Business Policy Rules
POLICY_RULES = {
    "max_discount_percent": 15,        # Maximum discount without approval
    "approval_threshold_usd": 50000,   # Purchase amount requiring VP approval
    "require_vendor_approval": True    # Enforce vendor allowlist
}

# PII Detection Patterns
PII_PATTERNS = {
    "email": r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
    "phone_us": r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b',
    "phone_intl": r'\+\d{1,3}[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}',
    "ssn": r'\b\d{3}-\d{2}-\d{4}\b'
}

# Safe Example Patterns (Don't flag these)
SAFE_EXAMPLES = {
    "emails": ["example@company.com", "test@example.org", "demo@test.com"],
    "phones": ["555-0100", "555-0199", "(555) 555-0100"],
    "vendors": ["Example Vendor Corp", "Demo Supplier Ltd"]
}

# Severity Scoring Thresholds
SEVERITY_THRESHOLDS = {
    "PII_LEAK": 95,
    "POLICY_VIOLATION": 85,
    "UNVERIFIED_SAP_TERM": 80
}

# Decision Thresholds
DECISION_THRESHOLDS = {
    "PASS": (0, 30),
    "REVIEW": (31, 70),
    "BLOCK": (71, 100)
}