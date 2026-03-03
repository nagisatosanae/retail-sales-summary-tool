"""
US-03: Profit Analysis Module

Analyzes profit margins across products, categories, and segments
to identify high and low performers.
"""

import pandas as pd


def profit_by_category(df: pd.DataFrame) -> pd.DataFrame:
    """Profit summary by category including profit margin.

    Args:
        df: Cleaned superstore DataFrame.

    Returns:
        DataFrame with Category, Total Profit, Total Sales, Profit Margin %.
    """
    result = df.groupby("Category").agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
    ).reset_index()
    result["Profit_Margin_%"] = (result["Total_Profit"] / result["Total_Sales"] * 100).round(2)
    return result.sort_values("Total_Profit", ascending=False)


def profit_by_subcategory(df: pd.DataFrame) -> pd.DataFrame:
    """Profit summary by sub-category to identify winners and losers.

    Args:
        df: Cleaned superstore DataFrame.

    Returns:
        DataFrame with Sub-Category, Total Profit, Profit Margin %, sorted by profit.
    """
    result = df.groupby("Sub-Category").agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Avg_Discount=("Discount", "mean"),
    ).reset_index()
    result["Profit_Margin_%"] = (result["Total_Profit"] / result["Total_Sales"] * 100).round(2)
    return result.sort_values("Total_Profit", ascending=False)


def top_products_by_profit(df: pd.DataFrame, top_n: int = 10) -> pd.DataFrame:
    """Top N most profitable products.

    Args:
        df: Cleaned superstore DataFrame.
        top_n: Number of products to return.

    Returns:
        DataFrame with Product Name, Total Profit, Total Sales.
    """
    result = df.groupby("Product Name").agg(
        Total_Profit=("Profit", "sum"),
        Total_Sales=("Sales", "sum"),
        Times_Sold=("Quantity", "sum"),
    ).reset_index()
    return result.sort_values("Total_Profit", ascending=False).head(top_n)


def bottom_products_by_profit(df: pd.DataFrame, top_n: int = 10) -> pd.DataFrame:
    """Top N least profitable (loss-making) products.

    Args:
        df: Cleaned superstore DataFrame.
        top_n: Number of products to return.

    Returns:
        DataFrame with Product Name, Total Profit (negative), Total Sales.
    """
    result = df.groupby("Product Name").agg(
        Total_Profit=("Profit", "sum"),
        Total_Sales=("Sales", "sum"),
        Times_Sold=("Quantity", "sum"),
    ).reset_index()
    return result.sort_values("Total_Profit", ascending=True).head(top_n)


def discount_impact_analysis(df: pd.DataFrame) -> pd.DataFrame:
    """Analyze the relationship between discount levels and profitability.

    Groups transactions into discount bands and shows average profit per band.

    Args:
        df: Cleaned superstore DataFrame.

    Returns:
        DataFrame with Discount Band, Avg Profit, Avg Sales, Transaction Count.
    """
    df = df.copy()
    bins = [0, 0.0001, 0.1, 0.2, 0.3, 0.5, 1.0]
    labels = ["No Discount", "1-10%", "11-20%", "21-30%", "31-50%", "50%+"]
    df["Discount_Band"] = pd.cut(df["Discount"], bins=bins, labels=labels, include_lowest=True)

    result = df.groupby("Discount_Band", observed=True).agg(
        Avg_Profit=("Profit", "mean"),
        Avg_Sales=("Sales", "mean"),
        Total_Profit=("Profit", "sum"),
        Transaction_Count=("Profit", "count"),
    ).reset_index()
    return result
