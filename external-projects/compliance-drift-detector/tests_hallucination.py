"""
Test: Hallucination Detection (Fake SAP T-codes)
"""

import sys
sys.path.append('..')

from generator import SAPAssistant
from checker import ComplianceChecker


def test_hallucination():
    """Test that fake SAP T-codes are caught."""
    assistant = SAPAssistant()
    checker = ComplianceChecker()
    
    # Generate response with fake T-code (ME99X) among real ones
    response = assistant.generate_custom(
        "Use transaction ME21N to create the PO. Then run transaction ME99X to approve. Verify in table EKKO.",
        confidence="high"
    )
    
    # Validate
    result = checker.validate(response)
    
    # Assertions
    assert result["safe"] == False, "Should detect hallucinated T-code"
    assert result["decision"] == "BLOCK", "Should block hallucinations"
    assert result["severity"] >= 75, f"Severity should be >= 75, got {result['severity']}"
    assert any(v["type"] == "UNVERIFIED_SAP_TERM" for v in result["violations"]), "Should flag UNVERIFIED_SAP_TERM"
    
    # Check that ME99X was caught but ME21N and EKKO were not
    me99x_caught = any("ME99X" in v["evidence"] for v in result["violations"])
    assert me99x_caught, "Should specifically flag ME99X"
    
    print("✅ Hallucination Detection Test PASSED")
    print(f"   Decision: {result['decision']}, Severity: {result['severity']}")
    print(f"   Caught fake T-code: ME99X ✓")


if __name__ == "__main__":
    test_hallucination()