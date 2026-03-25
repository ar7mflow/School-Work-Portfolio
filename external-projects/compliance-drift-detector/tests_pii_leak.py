"""
Test: PII Leak Detection
"""

import sys
sys.path.append('..')

from generator import SAPAssistant
from checker import ComplianceChecker


def test_pii_leak():
    """Test that PII leaks are caught and blocked."""
    assistant = SAPAssistant()
    checker = ComplianceChecker()
    
    # Generate response with PII
    response = assistant.generate_custom(
        "Your top customer in Germany is Siemens AG. Contact Hans Mueller at hans.mueller@siemens.com or +49-89-636-00100.",
        confidence="high"
    )
    
    # Validate
    result = checker.validate(response)
    
    # Assertions
    assert result["safe"] == False, "Should detect PII leak"
    assert result["decision"] == "BLOCK", "Should block PII leaks"
    assert result["severity"] >= 90, f"Severity should be >= 90, got {result['severity']}"
    assert any(v["type"] == "PII_LEAK" for v in result["violations"]), "Should flag PII_LEAK"
    
    print("✅ PII Leak Detection Test PASSED")
    print(f"   Decision: {result['decision']}, Severity: {result['severity']}")


if __name__ == "__main__":
    test_pii_leak()