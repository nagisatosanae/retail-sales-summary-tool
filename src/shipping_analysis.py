"""
US-07: Shipping and Order Analysis Module

Analyzes shipping modes, delivery times, and order patterns
to provide operational logistics insights.
"""

import pandas as pd


def shipping_mode_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Summary of orders and sales by shipping mode.

    Args:
        df: Cleaned superstore DataFrame.

    Returns:
        DataFrame with Ship Mode, Order Count, Total Sales, Avg Delivery Days.
    """
    result = df.groupby("Ship Mode").agg(
        Order_Count=("Order ID", "nunique"),
        Total_Sales=("Sales", "sum"),
        Avg_Delivery_Days=("Delivery Days", "mean"),
    ).reset_index()
    result["Avg_Delivery_Days"] = result["Avg_Delivery_Days"].round(1)
    return result.sort_values("Order_Count", ascending=False)


def delivery_time_analysis(df: pd.DataFrame) -> pd.DataFrame:
    """Delivery time statistics by shipping mode.

    Args:
        df: Cleaned superstore DataFrame.

    Returns:
        DataFrame with Ship Mode, Min/Max/Avg/Median delivery days.
    """
    result = df.groupby("Ship Mode").agg(
        Min_Days=("Delivery Days", "min"),
        Max_Days=("Delivery Days", "max"),
        Avg_Days=("Delivery Days", "mean"),
        Median_Days=("Delivery Days", "median"),
    ).reset_index()
    result["Avg_Days"] = result["Avg_Days"].round(1)
    return result


def orders_by_region_and_ship_mode(df: pd.DataFrame) -> pd.DataFrame:
    """Cross-tabulation of order count by region and shipping mode.

    Args:
        df: Cleaned superstore DataFrame.

    Returns:
        Pivot DataFrame with regions as rows and ship modes as columns.
    """
    cross = df.groupby(["Region", "Ship Mode"]).agg(
        Order_Count=("Order ID", "nunique"),
    ).reset_index()

    result = cross.pivot(index="Region", columns="Ship Mode", values="Order_Count").fillna(0)
    result = result.astype(int)
    return result


def late_shipment_rate(df: pd.DataFrame, threshold_days: int = 7) -> dict:
    """Calculate the percentage of orders that took longer than threshold to ship.

    Args:
        df: Cleaned superstore DataFrame.
        threshold_days: Number of days beyond which a shipment is considered late.

    Returns:
        Dictionary with total orders, late orders, and late percentage.
    """
    total = len(df)
    late = len(df[df["Delivery Days"] > threshold_days])
    return {
        "total_line_items": total,
        "late_items": late,
        "late_percentage": round(late / total * 100, 2) if total > 0 else 0,
        "threshold_days": threshold_days,
    }
