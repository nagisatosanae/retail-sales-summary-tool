"""
US-02: Sales Summary Module

Produces sales summaries grouped by category, region, sub-category,
and segment. All functions return pandas DataFrames for reuse.
"""

import pandas as pd


def sales_by_category(df: pd.DataFrame) -> pd.DataFrame:
    """Total sales, quantity, and order count by product category.

    Args:
        df: Cleaned superstore DataFrame.

    Returns:
        DataFrame with Category, Total Sales, Total Quantity, Order Count.
    """
    result = df.groupby("Category").agg(
        Total_Sales=("Sales", "sum"),
        Total_Quantity=("Quantity", "sum"),
        Order_Count=("Order ID", "nunique"),
    ).reset_index()
    return result.sort_values("Total_Sales", ascending=False)


def sales_by_region(df: pd.DataFrame) -> pd.DataFrame:
    """Total sales and profit by region.

    Args:
        df: Cleaned superstore DataFrame.

    Returns:
        DataFrame with Region, Total Sales, Total Profit.
    """
    result = df.groupby("Region").agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Order_Count=("Order ID", "nunique"),
    ).reset_index()
    return result.sort_values("Total_Sales", ascending=False)


def sales_by_subcategory(df: pd.DataFrame) -> pd.DataFrame:
    """Total sales by sub-category, ranked from highest to lowest.

    Args:
        df: Cleaned superstore DataFrame.

    Returns:
        DataFrame with Sub-Category, Total Sales, Avg Discount.
    """
    result = df.groupby("Sub-Category").agg(
        Total_Sales=("Sales", "sum"),
        Avg_Discount=("Discount", "mean"),
        Total_Quantity=("Quantity", "sum"),
    ).reset_index()
    return result.sort_values("Total_Sales", ascending=False)


def sales_by_segment(df: pd.DataFrame) -> pd.DataFrame:
    """Total sales by customer segment.

    Args:
        df: Cleaned superstore DataFrame.

    Returns:
        DataFrame with Segment, Total Sales, Total Profit, Order Count.
    """
    result = df.groupby("Segment").agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Order_Count=("Order ID", "nunique"),
    ).reset_index()
    return result.sort_values("Total_Sales", ascending=False)


def sales_by_state(df: pd.DataFrame, top_n: int = 10) -> pd.DataFrame:
    """Top N states by total sales.

    Args:
        df: Cleaned superstore DataFrame.
        top_n: Number of top states to return.

    Returns:
        DataFrame with State, Total Sales, Total Profit.
    """
    result = df.groupby("State").agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
    ).reset_index()
    return result.sort_values("Total_Sales", ascending=False).head(top_n)
