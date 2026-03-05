"""
Retail Sales Summary Tool - Main Entry Point

Demonstrates all analysis modules by loading the superstore dataset,
running each analysis function, and printing key results to console.
Optionally saves charts to the output/ directory.

Usage:
    python main.py
    python main.py --save-charts
"""

import argparse
import os
import sys

from src.data_loader import get_clean_data, get_dataset_summary
from src.sales_summary import (
    sales_by_category,
    sales_by_region,
    sales_by_subcategory,
    sales_by_segment,
    sales_by_state,
)
from src.profit_analysis import (
    profit_by_category,
    profit_by_subcategory,
    top_products_by_profit,
    bottom_products_by_profit,
    discount_impact_analysis,
)
from src.customer_insights import (
    top_customers_by_sales,
    customer_segment_summary,
    repeat_vs_single_buyers,
)
from src.trend_analysis import (
    yearly_sales_trend,
    quarterly_sales_trend,
    seasonal_pattern,
    yoy_comparison,
)
from src.shipping_analysis import (
    shipping_mode_summary,
    delivery_time_analysis,
    late_shipment_rate,
)
from src.visualization import (
    plot_sales_by_category,
    plot_profit_by_subcategory,
    plot_monthly_trend,
    plot_sales_by_region,
    plot_discount_vs_profit,
    plot_yearly_growth,
)
from src.trend_analysis import monthly_sales_trend


def print_section(title: str):
    """Print a formatted section header."""
    print(f"\n{'=' * 60}")
    print(f"  {title}")
    print(f"{'=' * 60}")


def main():
    parser = argparse.ArgumentParser(description="Retail Sales Summary Tool")
    parser.add_argument("--save-charts", action="store_true", help="Save charts to output/ directory")
    args = parser.parse_args()

    # --- Step 1: Load and Clean Data ---
    print_section("1. LOADING AND CLEANING DATA")
    df = get_clean_data()
    summary = get_dataset_summary(df)
    print(f"  Rows loaded:      {summary['total_rows']:,}")
    print(f"  Unique orders:    {summary['total_orders']:,}")
    print(f"  Unique customers: {summary['total_customers']:,}")
    print(f"  Unique products:  {summary['total_products']:,}")
    print(f"  Date range:       {summary['date_range'][0].date()} to {summary['date_range'][1].date()}")
    print(f"  Categories:       {', '.join(summary['categories'])}")
    print(f"  Regions:          {', '.join(summary['regions'])}")

    # --- Step 2: Sales Summary ---
    print_section("2. SALES SUMMARY")

    print("\n  Sales by Category:")
    print(sales_by_category(df).to_string(index=False))

    print("\n  Sales by Region:")
    print(sales_by_region(df).to_string(index=False))

    print("\n  Sales by Segment:")
    print(sales_by_segment(df).to_string(index=False))

    print("\n  Top 10 States by Sales:")
    print(sales_by_state(df, top_n=10).to_string(index=False))

    # --- Step 3: Profit Analysis ---
    print_section("3. PROFIT ANALYSIS")

    print("\n  Profit by Category:")
    print(profit_by_category(df).to_string(index=False))

    print("\n  Profit by Sub-Category:")
    print(profit_by_subcategory(df).to_string(index=False))

    print("\n  Top 5 Most Profitable Products:")
    print(top_products_by_profit(df, top_n=5).to_string(index=False))

    print("\n  Top 5 Least Profitable Products:")
    print(bottom_products_by_profit(df, top_n=5).to_string(index=False))

    print("\n  Discount Impact on Profit:")
    print(discount_impact_analysis(df).to_string(index=False))

    # --- Step 4: Customer Insights ---
    print_section("4. CUSTOMER INSIGHTS")

    print("\n  Top 10 Customers by Sales:")
    print(top_customers_by_sales(df, top_n=10).to_string(index=False))

    print("\n  Customer Segment Summary:")
    print(customer_segment_summary(df).to_string(index=False))

    print("\n  Repeat vs Single Buyers:")
    buyer_data = repeat_vs_single_buyers(df)
    print(f"    Single buyers: {buyer_data['single_buyers']['count']} "
          f"(avg spend: ${buyer_data['single_buyers']['avg_sales']:,.2f})")
    print(f"    Repeat buyers: {buyer_data['repeat_buyers']['count']} "
          f"(avg spend: ${buyer_data['repeat_buyers']['avg_sales']:,.2f}, "
          f"avg orders: {buyer_data['repeat_buyers']['avg_orders']})")

    # --- Step 5: Trend Analysis ---
    print_section("5. TREND ANALYSIS")

    print("\n  Yearly Sales Trend:")
    print(yearly_sales_trend(df).to_string(index=False))

    print("\n  Seasonal Pattern (Avg Sales by Month):")
    print(seasonal_pattern(df).to_string(index=False))

    print("\n  Year-over-Year Sales by Category:")
    print(yoy_comparison(df).to_string())

    # --- Step 6: Shipping Analysis ---
    print_section("6. SHIPPING ANALYSIS")

    print("\n  Shipping Mode Summary:")
    print(shipping_mode_summary(df).to_string(index=False))

    print("\n  Delivery Time Analysis:")
    print(delivery_time_analysis(df).to_string(index=False))

    print("\n  Late Shipment Rate (>7 days):")
    late = late_shipment_rate(df, threshold_days=7)
    print(f"    Late items: {late['late_items']} / {late['total_line_items']} "
          f"({late['late_percentage']}%)")

    # --- Step 7: Save Charts (optional) ---
    if args.save_charts:
        print_section("7. SAVING CHARTS")
        output_dir = os.path.join(os.path.dirname(__file__), "output")
        os.makedirs(output_dir, exist_ok=True)

        charts = {
            "sales_by_category.png": plot_sales_by_category(sales_by_category(df)),
            "profit_by_subcategory.png": plot_profit_by_subcategory(profit_by_subcategory(df)),
            "monthly_sales_trend.png": plot_monthly_trend(monthly_sales_trend(df)),
            "sales_by_region.png": plot_sales_by_region(sales_by_region(df)),
            "discount_vs_profit.png": plot_discount_vs_profit(discount_impact_analysis(df)),
            "yearly_growth.png": plot_yearly_growth(yearly_sales_trend(df)),
        }

        for filename, fig in charts.items():
            path = os.path.join(output_dir, filename)
            fig.savefig(path, dpi=150)
            print(f"  Saved: {path}")

    print_section("DONE")
    print("  Retail Sales Summary Tool completed successfully.\n")


if __name__ == "__main__":
    main()
