# Segregation of Duties (SOD) Policy: GitAdBudgetOpt

This document establishes the role boundaries and segregation of duties for the GitAdBudgetOpt agent.

## Role Separation

### 1. Maker
The Maker role is responsible for authoring campaign targeting rules, configuring ad channel budgets, and preparing automated spend reallocation diffs.
This role cannot approve or merge its own changes into protected growth marketing branches.

### 2. Checker
The Checker role is responsible for reviewing, auditing, and validating incoming ad performance reports, ROAS metrics, and CAC payback timelines.
This role operates as an impartial auditor to verify compliance with enterprise marketing efficiency benchmarks.

### 3. Approver
The Approver role is strictly reserved for human VPs of Growth Marketing and Chief Marketing Officers.
Human approval is required for all new channel activations, macro budget changes, and ROAS hurdle overrides.
