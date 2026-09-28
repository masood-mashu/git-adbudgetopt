# GitAdBudgetOpt Explainability Specification

This document provides a transparent, verifiable architectural breakdown of how **GitAdBudgetOpt** operates, processes input, makes decisions, and enforces security boundaries.

---

## 1. Input Data and Data Sources Used

GitAdBudgetOpt consumes paid advertising performance analytics, campaign spend logs, conversion pixel telemetry, and subscription revenue ledgers. These data sources include impression counts, click-through rates (CTR), cost-per-click (CPC), customer acquisition numbers, and attributed revenue figures. The agent ingests these inputs in raw JSON, CSV, and marketing API format and parses them into standardized growth performance vectors for downstream budget optimization. Attribution modeling rules and customer lifetime value (LTV) projections are also monitored as sensitive data sources to ensure growth capital efficiency is strictly maintained.

---

## 2. How It Decides and Reasoning Process

The decision making process follows a deterministic, five-stage analytical pipeline designed to eliminate ambiguity and hallucination. When an advertising performance batch is ingested, the agent first evaluates campaign profitability using the roas-efficiency-calculator tool to verify that return on ad spend meets the minimum 1.5x threshold. Next, the reasoning engine invokes the cac-payback-evaluator tool to audit acquisition payback velocity against customer lifetime value benchmarks. Furthermore, daily reallocation shifts are audited using the budget-reallocation-optimizer tool. Finally, the agent correlates all growth metrics against predefined marketing policies to issue a conclusive verdict of APPROVED, BLOCKED, or NEEDS_REVIEW alongside an automated budget adjustment dispatch.

---

## 3. Constraints, Limitations, and Known Issues

GitAdBudgetOpt operates under strict operational constraints to prevent false positives and non-deterministic behavior across different agent frameworks. GitAdBudgetOpt operates under strict operational constraints to prevent marketing capital waste and ad platform algorithmic disruption. The agent is deliberately limited to quantitative performance attribution and budget arithmetic and cannot design creative ad imagery or author marketing copy. Another known issue and limitation is that complex multi-touch offline attribution without clear digital tracking parameters may require secondary human review rather than autonomous blocking. Furthermore, the agent enforces a low temperature constraint of 0.1 to maintain strict predictability across all supported export frameworks.
