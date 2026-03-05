# Sprint 1 Report

## Course Information

| Item | Details |
|-----|-----|
| Course | CPSC-620-3 Agile Software Development |
| Term | Winter 2026 |
| Sprint Duration | March 2 – March 8, 2026 |

---

## Team Members

| Name |
|-----|
| Eun Soo Park |
| Sunghoon Ahn |
| Mohammad Shoaib |
| Sannibhai Indradeepbhai Garasiya |

---

# 1. Team Liftoff Summary

Our team held a liftoff meeting to align on project scope, expectations, and collaboration methods.

We discussed our strengths:
- Python data analysis
- Git workflow experience
- Documentation and organization

This allowed us to distribute tasks effectively.

---

## Team Charter

### Mission

Build a modular Python tool that transforms raw retail data into actionable business insights while practicing real Agile collaboration.

### Success Criteria

- All team members contribute through code, reviews, or documentation
- The tool produces correct results from the Superstore dataset
- Agile artifacts remain traceable (stories, commits, tasks)

### Definition of Done

- Feature code reviewed and merged via Pull Request
- Functions contain docstrings
- Tests pass
- Taiga task moved to **Closed**

---

# 2. Sprint Goal

Develop a modular retail sales summary tool capable of:

- loading and cleaning the dataset
- generating sales summaries
- performing profit analysis
- providing reusable visualization functions

---

# 3. User Stories

| ID | User Story | Story Points | Owner |
|----|------------|-------------|------|
| US-01 | Load and clean dataset | 3 | Eun Soo Park |
| US-02 | Sales summary by category and region | 5 | Eun Soo Park |
| US-03 | Profit margin analysis | 5 | Sunghoon Ahn |
| US-04 | Customer purchasing pattern analysis | 3 | Sannibhai Garasiya |
| US-05 | Sales trend analysis | 5 | Eun Soo Park |
| US-06 | Reusable visualization functions | 3 | Sunghoon Ahn |
| US-07 | Shipping analysis | 3 | Mohammad Shoaib |

**Total Sprint Capacity: 27 Story Points**

---

# 4. Sprint Execution

## GitHub Workflow

The repository uses the following branching strategy:

- `main` → stable release
- `develop` → integration branch
- `feature branches` → user story development

Each user story followed this process:

1. Create feature branch
2. Implement feature
3. Submit Pull Request
4. Peer review
5. Merge into `develop`

---

## Taiga Board Workflow

Tasks moved through the following states:

- **New**
- **In Progress**
- **Ready for Test**
- **Closed**

---

# 5. Tool Demonstration Summary

## Data Pipeline (US-01)

- Loads **10,001 rows** from `superstore.csv`
- Cleans data types
- Handles missing values
- Produces dataset summary

## Sales Analysis (US-02)

- Technology category leads total sales
- West region produces highest revenue

## Profit Analysis (US-03)

- Technology has highest margin
- Furniture lowest margin
- Tables category shows negative profitability

## Customer Insights (US-04)

- 793 unique customers identified
- Repeat buyers show higher lifetime value

## Trend Analysis (US-05)

- Sales increased steadily from **2015–2018**
- **Q4** shows the strongest seasonal performance

## Visualization (US-06)

Reusable chart functions returning:
