"""
US-05: Time-based Trend Analysis Module

Provides sales and profit trends over time (monthly, quarterly, yearly)
and year-over-year comparisons for identifying seasonal patterns.
"""

import pandas as pd


def monthly_sales_trend(df: pd.DataFrame) -> pd.DataFrame:
    """Monthly sales and profit trend.

    Args:
        df: Cleaned superstore DataFrame.

    Returns:
        DataFrame with Year-Month, Total Sales, Total Profit, Order Count.
    """
    df = df.copy()
    df["Year_Month"] = df["Order Date"].dt.to_period("M")

    result = df.groupby("Year_Month").agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Order_Count=("Order ID", "nunique"),
    ).reset_index()
    result["Year_Month"] = result["Year_Month"].astype(str)
    return result


def quarterly_sales_trend(df: pd.DataFrame) -> pd.DataFrame:
    """Quarterly sales and profit trend.

    Args:
        df: Cleaned superstore DataFrame.

    Returns:
        DataFrame with Year, Quarter, Total Sales, Total Profit.
    """
    result = df.groupby(["Order Year", "Order Quarter"]).agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Order_Count=("Order ID", "nunique"),
    ).reset_index()
    result["Period"] = result["Order Year"].astype(str) + "-Q" + result["Order Quarter"].astype(str)
    return result


def yearly_sales_trend(df: pd.DataFrame) -> pd.DataFrame:
    """Yearly sales and profit trend.

    Args:
        df: Cleaned superstore DataFrame.

    Returns:
        DataFrame with Year, Total Sales, Total Profit, YoY Growth %.
    """
    result = df.groupby("Order Year").agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Order_Count=("Order ID", "nunique"),
        Customer_Count=("Customer ID", "nunique"),
    ).reset_index()

    result["Sales_YoY_Growth_%"] = result["Total_Sales"].pct_change() * 100
    result["Sales_YoY_Growth_%"] = result["Sales_YoY_Growth_%"].round(2)
    return result


def seasonal_pattern(df: pd.DataFrame) -> pd.DataFrame:
    """Average sales by month across all years to identify seasonal patterns.

    Args:
        df: Cleaned superstore DataFrame.

    Returns:
        DataFrame with Month (1-12), Avg Sales, Avg Profit.
    """
    monthly = df.groupby(["Order Year", "Order Month"]).agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
    ).reset_index()

    result = monthly.groupby("Order Month").agg(
        Avg_Sales=("Total_Sales", "mean"),
        Avg_Profit=("Total_Profit", "mean"),
    ).reset_index()
    result["Avg_Sales"] = result["Avg_Sales"].round(2)
    result["Avg_Profit"] = result["Avg_Profit"].round(2)
    return result


def yoy_comparison(df: pd.DataFrame) -> pd.DataFrame:
    """Year-over-year comparison by category.

    Args:
        df: Cleaned superstore DataFrame.

    Returns:
        Pivot DataFrame with categories as rows and years as columns.
    """
    yearly_cat = df.groupby(["Order Year", "Category"]).agg(
        Total_Sales=("Sales", "sum"),
    ).reset_index()

    result = yearly_cat.pivot(index="Category", columns="Order Year", values="Total_Sales")
    result = result.round(2)
    return result
