"""
budget_reallocation_optimizer.py - Audits proposed percentage shift in daily advertising budget between channels
"""
import sys
import json


def optimize_budget_shift(shift_data_json: str, max_shift_pct: float = 25.0):
    import json
    data = json.loads(shift_data_json) if isinstance(shift_data_json, str) else shift_data_json
    curr = max(data.get("current_daily_budget", 1000.0), 1.0)
    prop = data.get("proposed_daily_budget", 1200.0)
    shift_pct = abs(prop - curr) / curr * 100.0
    safe = shift_pct <= max_shift_pct
    return {
        "current_budget": curr,
        "proposed_budget": prop,
        "shift_pct": round(shift_pct, 2),
        "safe_shift": safe,
        "status": "BUDGET_SHIFT_APPROVED" if safe else "EXCESSIVE_BUDGET_VOLATILITY"
    }


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "budget-reallocation-optimizer"}))
