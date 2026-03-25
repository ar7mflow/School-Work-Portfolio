"""
Test: Policy Violation Detection
"""

import sys
sys.path.append('..')

from generator import SAPAssistant
from checker import ComplianceChecker


def test_policy_violation():
    """Test that unapproved vendor recommendations are caught."""
    assistant = SAPAssistant()
    checker = ComplianceChecker()
    
    # Generate response with unapproved vendor
    response = assistant.generate_custom(
        "I recommend CheapSteel International Ltd. They offer 30% discount.",
        confidence="medium"
    )
    
    # Validate
    result = checker.validate(response)
    
    # Assertions
    assert result["safe"] == False, "Should detect policy violation"
    assert result["decision"] == "BLOCK", "Should block policy violations"
    assert result["severity"] >= 80, f"Severity should be >= 80, got {result['severity']}"
    assert any(v["type"] == "POLICY_VIOLATION" for v in result["violations"]), "Should flag POLICY_VIOLATION"
    
    print("✅ Policy Violation Test PASSED")
    print(f"   Decision: {result['decision']}, Severity: {result['severity']}")


if __name__ == "__main__":
    test_policy_violation()