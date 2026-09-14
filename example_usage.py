import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import AutomatedCompliancePolicyEvaluatorClient

def main():
    client = AutomatedCompliancePolicyEvaluatorClient()
    res = client.evaluate_policy_compliance()
    print("=== Automated Compliance Policy Evaluator Output ===")
    print(f"Compliance Score: {res['compliance_score']}/100 | Status: {res['compliance_status']}")
    print(f"Violations Count: {res['violations_detected_count']}")
    print("\nRemediation Actions:")
    for v in res['remediation_actions']:
        print(f"  - [{v['violation_category']}] Flagged: '{v['flagged_token']}' -> {v['remediation']}")

if __name__ == '__main__':
    main()
