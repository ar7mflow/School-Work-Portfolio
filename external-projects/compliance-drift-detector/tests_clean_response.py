"""
Test: Clean Response (No Violations)
"""

import sys
sys.path.append('..')

from generator import SAPAssistant
from checker import ComplianceChecker


def test_clean_response():
    """Test that clean responses pass validation."""
    assistant = SAPAssistant()
    checker = ComplianceChecker()
    
    # Generate clean response
    response = assistant.generate_custom(
        "SAP ERP is an integrated software system for managing business processes.",
        confidence="high"
    )
    
    # Validate
    result = checker.validate(response)
    
    # Assertions
    assert result["safe"] == True, "Should pass clean response"
    assert result["decision"] == "PASS", "Should pass with no violations"
    assert result["severity"] == 0, f"Severity should be 0, got {result['severity']}"
    assert len(result["violations"]) == 0, "Should have no violations"
    
    print("✅ Clean Response Test PASSED")
    print(f"   Decision: {result['decision']}, Severity: {result['severity']}")


if __name__ == "__main__":
    test_clean_response()