"""
cac_payback_evaluator.py - Calculates CAC payback period in months based on customer acquisition cost and monthly gross profit
"""
import sys
import json


def evaluate_cac_payback(cac_data_json: str, max_payback_months: int = 12):
    import json
    data = json.loads(cac_data_json) if isinstance(cac_data_json, str) else cac_data_json
    cac = data.get("customer_acquisition_cost", 600.0)
    monthly_gp = max(data.get("monthly_gross_profit", 100.0), 1.0)
    payback = cac / monthly_gp
    sustainable = payback <= max_payback_months
    return {
        "cac": cac,
        "monthly_gp": monthly_gp,
        "payback_months": round(payback, 1),
        "sustainable": sustainable,
        "status": "CAC_PAYBACK_HEALTHY" if sustainable else "EXCESSIVE_CAC_PAYBACK"
    }


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "cac-payback-evaluator"}))
