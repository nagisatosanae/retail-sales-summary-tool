"""
US-04: Customer Insights Module

Analyzes customer purchasing patterns, segmentation, and
identifies top customers by various metrics.
"""

import pandas as pd


def top_customers_by_sales(df: pd.DataFrame, top_n: int = 10) -> pd.DataFrame:
    """Top N customers ranked by total sales.

    Args:
        df: Cleaned superstore DataFrame.
        top_n: Number of customers to return.

    Returns:
        DataFrame with Customer Name, Segment, Total Sales, Total Profit, Order Count.
    """
    result = df.groupby(["Customer Name", "Segment"]).agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Order_Count=("Order ID", "nunique"),
    ).reset_index()
    return result.sort_values("Total_Sales", ascending=False).head(top_n)


def customer_segment_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Summary statistics by customer segment (Consumer, Corporate, Home Office).

    Args:
        df: Cleaned superstore DataFrame.

    Returns:
        DataFrame with Segment, Customer Count, Total Sales, Avg Sales per Customer.
    """
    cust_segment = df.groupby(["Customer ID", "Segment"]).agg(
        Total_Sales=("Sales", "sum"),
    ).reset_index()

    result = cust_segment.groupby("Segment").agg(
        Customer_Count=("Customer ID", "nunique"),
        Total_Sales=("Total_Sales", "sum"),
        Avg_Sales_per_Customer=("Total_Sales", "mean"),
    ).reset_index()
    return result.sort_values("Total_Sales", ascending=False)


def customer_purchase_frequency(df: pd.DataFrame) -> pd.DataFrame:
    """Analyze how frequently each customer makes purchases.

    Args:
        df: Cleaned superstore DataFrame.

    Returns:
        DataFrame with Customer Name, Order Count, Total Sales, First/Last Order.
    """
    result = df.groupby("Customer Name").agg(
        Order_Count=("Order ID", "nunique"),
        Total_Sales=("Sales", "sum"),
        First_Order=("Order Date", "min"),
        Last_Order=("Order Date", "max"),
        Items_Purchased=("Quantity", "sum"),
    ).reset_index()
    return result.sort_values("Order_Count", ascending=False)


def repeat_vs_single_buyers(df: pd.DataFrame) -> dict:
    """Compare single-order customers vs repeat customers.

    Args:
        df: Cleaned superstore DataFrame.

    Returns:
        Dictionary with counts and average spend for each group.
    """
    cust_orders = df.groupby("Customer ID").agg(
        Order_Count=("Order ID", "nunique"),
        Total_Sales=("Sales", "sum"),
    ).reset_index()

    single = cust_orders[cust_orders["Order_Count"] == 1]
    repeat = cust_orders[cust_orders["Order_Count"] > 1]

    return {
        "single_buyers": {
            "count": len(single),
            "avg_sales": round(single["Total_Sales"].mean(), 2),
        },
        "repeat_buyers": {
            "count": len(repeat),
            "avg_sales": round(repeat["Total_Sales"].mean(), 2),
            "avg_orders": round(repeat["Order_Count"].mean(), 2),
        },
    }
