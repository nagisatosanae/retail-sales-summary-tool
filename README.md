# Retail Sales Summary Tool

A modular Python tool that reads, cleans, and summarizes the Superstore retail dataset, producing actionable sales, profit, customer, and logistics insights through reusable functions.

## Sprint Goal

> Deliver a functional, modular Python tool that processes the Superstore dataset and provides meaningful business summaries across sales, profit, customer behavior, time-based trends, and shipping — all built collaboratively using Agile practices within one sprint.

## Project Structure

```
retail-sales-summary-tool/
├── main.py                  # Entry point - runs all analyses
├── requirements.txt         # Python dependencies
├── .gitignore
├── data/
│   └── superstore.csv       # Source dataset (10,001 rows)
├── src/
│   ├── __init__.py
│   ├── data_loader.py       # US-01: Data loading & cleaning
│   ├── sales_summary.py     # US-02: Sales summaries by category/region
│   ├── profit_analysis.py   # US-03: Profit margin analysis
│   ├── customer_insights.py # US-04: Customer behavior analysis
│   ├── trend_analysis.py    # US-05: Time-based trend analysis
│   ├── visualization.py     # US-06: Reusable chart functions
│   └── shipping_analysis.py # US-07: Shipping & logistics analysis
├── tests/
│   ├── test_data_loader.py
│   ├── test_sales_summary.py
│   └── test_profit_analysis.py
└── output/                  # Generated charts (when --save-charts used)
```

## Setup and Installation

```bash
# Clone the repository
git clone https://github.com/nagisatosanae/retail-sales-summary-tool.git
cd retail-sales-summary-tool

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt
```

## How to Run

```bash
# Run the full analysis (console output)
python main.py

# Run with chart generation
python main.py --save-charts

# Run tests
pytest tests/ -v
```

## Features

| Module | User Story | Description |
|--------|-----------|-------------|
| `data_loader.py` | US-01 | Load CSV, clean data types, handle missing values, add derived columns |
| `sales_summary.py` | US-02 | Sales totals by category, region, segment, sub-category, state |
| `profit_analysis.py` | US-03 | Profit margins, top/bottom products, discount impact analysis |
| `customer_insights.py` | US-04 | Top customers, segment analysis, repeat vs single buyer comparison |
| `trend_analysis.py` | US-05 | Monthly/quarterly/yearly trends, seasonal patterns, YoY growth |
| `visualization.py` | US-06 | Reusable matplotlib figure-returning functions for all key metrics |
| `shipping_analysis.py` | US-07 | Shipping mode comparison, delivery times, late shipment rates |

## Dataset Notes

The Superstore dataset is at the **line-item level**, not the order level. Each row represents one product within an order. A single `Order ID` may span multiple rows. Aggregation functions in this tool account for this structure.

## Team
W2026-CPSC-620 - 1
- Ahn, Sunghoon
- Garasiya, Sannibhai Indradeepbhai
- PARk, EUN SOO (nagisatosanae)
- Shoaib, Mohammad

## Course

CPSC-620-3 Agile Software Development — Winter 2026
