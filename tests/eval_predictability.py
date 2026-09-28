"""
eval_predictability.py - Checkpoint 02 Benchmark Suite for GitAdBudgetOpt.
"""
import os, sys, unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tools.roas_efficiency_calculator import *
from tools.cac_payback_evaluator import *
from tools.budget_reallocation_optimizer import *

class TestGitAdBudgetOptPredictability(unittest.TestCase):

    def test_roas_efficiency_calculator(self):
        res = calculate_roas('{"attributed_revenue": 4500, "total_ad_spend": 2000}')
        self.assertTrue(res["meets_hurdle"])
        self.assertEqual(res["status"], "CAMPAIGN_PERFORMING")

    def test_cac_payback_evaluator(self):
        res = evaluate_cac_payback('{"customer_acquisition_cost": 500, "monthly_gross_profit": 100}')
        self.assertTrue(res["sustainable"])
        self.assertEqual(res["status"], "CAC_PAYBACK_HEALTHY")

    def test_budget_reallocation_optimizer(self):
        res = optimize_budget_shift('{"current_daily_budget": 1000, "proposed_daily_budget": 1150}')
        self.assertTrue(res["safe_shift"])
        self.assertEqual(res["status"], "BUDGET_SHIFT_APPROVED")


if __name__ == "__main__":
    unittest.main()
