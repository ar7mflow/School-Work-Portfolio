"""
Main CLI interface for Compliance Drift Detector
"""

import json
import argparse
from generator import SAPAssistant
from checker import ComplianceChecker


def main():
    parser = argparse.ArgumentParser(description="Compliance Drift Detector - AI Governance for SAP GenAI")
    parser.add_argument("query", type=str, help="User query to process")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show detailed output")
    
    args = parser.parse_args()
    
    # Initialize
    assistant = SAPAssistant()
    checker = ComplianceChecker()
    
    print("\n" + "="*60)
    print("COMPLIANCE DRIFT DETECTOR")
    print("="*60)
    
    # Generate response
    print(f"\n📝 User Query: {args.query}")
    print("\n⏳ Generating response...")
    
    response = assistant.generate(args.query)
    
    if args.verbose:
        print(f"\n🤖 Generated Response:")
        print(json.dumps(response, indent=2))
    
    # Validate
    print("\n🔍 Running compliance check...")
    result = checker.validate(response)
    
    # Display results
    print("\n" + "="*60)
    print("COMPLIANCE REPORT")
    print("="*60)
    
    status_emoji = "✅" if result["safe"] else "⚠️"
    print(f"\n{status_emoji} Status: {result['decision']}")
    print(f"📊 Severity: {result['severity']}/100")
    
    if result["violations"]:
        print(f"\n🚨 Violations Detected: {len(result['violations'])}")
        for i, v in enumerate(result["violations"], 1):
            print(f"\n  {i}. {v['type']}")
            print(f"     Evidence: {v['evidence']}")
            print(f"     Impact: {v['impact']}")
            print(f"     Fix: {v['recommendation']}")
    else:
        print("\n✅ No violations detected")
    
    print("\n" + "="*60)
    
    if args.verbose:
        print("\nFull JSON Output:")
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()