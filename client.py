import json
import re
from typing import List, Dict, Any, Optional

class AutomatedCompliancePolicyEvaluatorClient:
    """
    Production-grade e-commerce & content compliance policy evaluator.
    Scans for prohibited claims, trademark infringement, and regulatory non-compliance.
    """
    PROHIBITED_CLAIMS = {
        "medical_treatment": [r"\bcures?\b", r"\btreats?\b", r"\bheals?\b", r"\bmedical miracle\b"],
        "unsubstantiated_guarantee": [r"\b100% guaranteed profit\b", r"\brisk[- ]free investment\b", r"\bunlimited lifetime cash\b"],
        "trademark_abuse": [r"\bofficial apple\b", r"\bgenuine rolex\b"]
    }

    def evaluate_policy_compliance(self, text_content: Optional[str] = None, category: str = "Consumer Electronics") -> Dict[str, Any]:
        if not text_content:
            text_content = "This smart vacuum cures all dust allergies and offers a 100% guaranteed clean home forever."

        violations = []
        for cat, patterns in self.PROHIBITED_CLAIMS.items():
            for pat in patterns:
                matches = re.findall(pat, text_content, re.IGNORECASE)
                if matches:
                    violations.append({
                        "violation_category": cat,
                        "flagged_token": matches[0],
                        "severity": "HIGH",
                        "remediation": f"Remove unverified claim '{matches[0]}' to comply with FTC/FDA advertising standards."
                    })

        score = max(0, 100 - (len(violations) * 35))
        status = "COMPLIANT_APPROVED" if score >= 85 else "FLAGGED_MODERATION_REQUIRED" if score >= 50 else "REJECTED_POLICY_BREACH"

        return {
            "evaluation_id": "cmp_evl_4402",
            "category": category,
            "compliance_score": score,
            "compliance_status": status,
            "violations_detected_count": len(violations),
            "remediation_actions": violations
        }
