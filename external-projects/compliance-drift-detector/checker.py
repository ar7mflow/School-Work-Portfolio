"""
Compliance Checker
Validates LLM outputs against PII, hallucination, and policy rules
"""

import re
import json
from typing import Dict, List, Any
from config import (
    APPROVED_TCODES, APPROVED_MODULES, APPROVED_TABLES, APPROVED_VENDORS,
    POLICY_RULES, PII_PATTERNS, SAFE_EXAMPLES, SEVERITY_THRESHOLDS, DECISION_THRESHOLDS
)


class ComplianceChecker:
    """
    Two-layer validation system:
    Layer 1: Deterministic pattern matching
    Layer 2: LLM reasoning (simulated for demo)
    """
    
    def __init__(self):
        self.approved_tcodes = set(APPROVED_TCODES)
        self.approved_modules = set(APPROVED_MODULES)
        self.approved_tables = set(APPROVED_TABLES)
        self.approved_vendors = set(APPROVED_VENDORS)
        self.policy_rules = POLICY_RULES
    
    def validate(self, response: Dict[str, Any]) -> Dict[str, Any]:
        """
        Main validation function.
        Returns compliance report with decision, severity, violations.
        """
        answer = response.get("answer", "")
        violations = []
        
        # Layer 1: Deterministic checks
        pii_violations = self._check_pii(answer)
        sap_violations = self._check_sap_terms(answer)
        policy_violations = self._check_policy(answer)
        
        violations.extend(pii_violations)
        violations.extend(sap_violations)
        violations.extend(policy_violations)
        
        # Calculate severity
        severity = self._calculate_severity(violations)
        
        # Determine decision
        decision = self._make_decision(severity)
        
        return {
            "safe": len(violations) == 0,
            "decision": decision,
            "severity": severity,
            "violations": violations
        }
    
    def _check_pii(self, text: str) -> List[Dict[str, str]]:
        """Check for PII leakage."""
        violations = []
        
        # Check email patterns
        emails = re.findall(PII_PATTERNS["email"], text)
        emails = [e for e in emails if e not in SAFE_EXAMPLES["emails"]]
        
        if emails:
            violations.append({
                "type": "PII_LEAK",
                "evidence": f"Email address: {emails[0]}",
                "impact": "GDPR violation - sharing personal contact details without authorization",
                "recommendation": "Remove PII. Suggest user request introduction through proper channels."
            })
        
        # Check phone patterns
        phones = re.findall(PII_PATTERNS["phone_intl"], text)
        if not phones:
            phones = re.findall(PII_PATTERNS["phone_us"], text)
        phones = [p for p in phones if p not in SAFE_EXAMPLES["phones"]]
        
        if phones:
            violations.append({
                "type": "PII_LEAK",
                "evidence": f"Phone number: {phones[0]}",
                "impact": "Privacy breach - exposing personal contact information",
                "recommendation": "Provide general contact methods only"
            })
        
        return violations
    
    def _check_sap_terms(self, text: str) -> List[Dict[str, str]]:
        """Check for unverified SAP terms."""
        violations = []
        
        # Extract potential T-codes (pattern: 2-4 uppercase letters followed by 2-4 digits/letters)
        potential_tcodes = re.findall(r'\b[A-Z]{2,4}[0-9]{1,4}[A-Z]?\b', text)
        
        for tcode in potential_tcodes:
            if tcode not in self.approved_tcodes:
                # Check if it's used as instruction
                is_instruction = any(phrase in text.lower() for phrase in 
                                   [f"use {tcode.lower()}", f"run {tcode.lower()}", 
                                    f"execute {tcode.lower()}", f"transaction {tcode.lower()}"])
                
                violations.append({
                    "type": "UNVERIFIED_SAP_TERM",
                    "evidence": f"Transaction code {tcode}",
                    "impact": f"Non-existent transaction code will cause system error{'and halt workflow' if is_instruction else ''}",
                    "recommendation": "Verify against SAP documentation or use approved transaction codes"
                })
        
        return violations
    
    def _check_policy(self, text: str) -> List[Dict[str, str]]:
        """Check for policy violations."""
        violations = []
        
        # Check for unapproved vendors
        text_lower = text.lower()
        for vendor in self.approved_vendors:
            if vendor.lower() in text_lower:
                return []  # Found approved vendor, no violation
        
        # Look for vendor recommendations
        if any(word in text_lower for word in ["recommend", "vendor", "supplier", "company"]):
            # Extract potential vendor names (simple heuristic)
            if "ltd" in text_lower or "inc" in text_lower or "gmbh" in text_lower or "corp" in text_lower:
                violations.append({
                    "type": "POLICY_VIOLATION",
                    "evidence": "Vendor recommendation not on approved list",
                    "impact": "Procurement policy breach - bypasses vendor vetting process",
                    "recommendation": f"Use only approved vendors: {', '.join(list(self.approved_vendors)[:2])}, etc."
                })
        
        return violations
    
    def _calculate_severity(self, violations: List[Dict[str, str]]) -> int:
        """Calculate severity score (0-100)."""
        if not violations:
            return 0
        
        # Get base severity for each violation type
        scores = []
        for v in violations:
            vtype = v["type"]
            scores.append(SEVERITY_THRESHOLDS.get(vtype, 50))
        
        # Take highest score
        max_score = max(scores)
        
        # Add penalty for multiple violations
        if len(violations) > 1:
            max_score = min(100, max_score + 10)
        
        return max_score
    
    def _make_decision(self, severity: int) -> str:
        """Determine action based on severity."""
        if severity >= DECISION_THRESHOLDS["BLOCK"][0]:
            return "BLOCK"
        elif severity >= DECISION_THRESHOLDS["REVIEW"][0]:
            return "REVIEW"
        else:
            return "PASS"


# Example usage
if __name__ == "__main__":
    checker = ComplianceChecker()
    
    # Test with PII leak
    test_response = {
        "answer": "Contact Hans Mueller at hans.mueller@siemens.com",
        "confidence": "high"
    }
    
    result = checker.validate(test_response)
    print(json.dumps(result, indent=2))