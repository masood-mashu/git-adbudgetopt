"""
roas_efficiency_calculator.py - Calculates Return on Ad Spend (ROAS) and verifies performance against minimum hurdle
"""
import sys
import json


def calculate_roas(ad_spend_json: str, min_roas_hurdle: float = 1.5):
    import json
    data = json.loads(ad_spend_json) if isinstance(ad_spend_json, str) else ad_spend_json
    rev = data.get("attributed_revenue", 3000.0)
    spend = max(data.get("total_ad_spend", 1000.0), 1.0)
    roas = rev / spend
    viable = roas >= min_roas_hurdle
    return {
        "attributed_revenue": rev,
        "ad_spend": spend,
        "roas": round(roas, 2),
        "meets_hurdle": viable,
        "status": "CAMPAIGN_PERFORMING" if viable else "UNDERPERFORMING_PAUSE_RECOMMENDED"
    }


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "roas-efficiency-calculator"}))
