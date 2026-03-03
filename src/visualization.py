"""
US-06: Visualization Helper Module

Provides reusable functions that return matplotlib figure objects.
These can be used standalone or integrated into dashboards (e.g., Streamlit).
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")


def plot_sales_by_category(df: pd.DataFrame) -> plt.Figure:
    """Bar chart of total sales by product category.

    Args:
        df: Summary DataFrame with Category and Total_Sales columns.

    Returns:
        matplotlib Figure object.
    """
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(df["Category"], df["Total_Sales"], color=["#2196F3", "#4CAF50", "#FF9800"])
    ax.set_title("Total Sales by Category")
    ax.set_ylabel("Sales ($)")
    ax.set_xlabel("Category")
    for i, v in enumerate(df["Total_Sales"]):
        ax.text(i, v + v * 0.02, f"${v:,.0f}", ha="center", fontsize=9)
    plt.tight_layout()
    return fig


def plot_profit_by_subcategory(df: pd.DataFrame) -> plt.Figure:
    """Horizontal bar chart of profit by sub-category.

    Args:
        df: Summary DataFrame with Sub-Category and Total_Profit columns.

    Returns:
        matplotlib Figure object.
    """
    df_sorted = df.sort_values("Total_Profit", ascending=True)
    colors = ["#f44336" if x < 0 else "#4CAF50" for x in df_sorted["Total_Profit"]]

    fig, ax = plt.subplots(figsize=(10, 7))
    ax.barh(df_sorted["Sub-Category"], df_sorted["Total_Profit"], color=colors)
    ax.set_title("Profit by Sub-Category")
    ax.set_xlabel("Profit ($)")
    ax.axvline(x=0, color="black", linewidth=0.5)
    plt.tight_layout()
    return fig


def plot_monthly_trend(df: pd.DataFrame) -> plt.Figure:
    """Line chart of monthly sales trend.

    Args:
        df: DataFrame with Year_Month and Total_Sales columns.

    Returns:
        matplotlib Figure object.
    """
    fig, ax = plt.subplots(figsize=(14, 5))
    ax.plot(range(len(df)), df["Total_Sales"], marker="o", markersize=3, linewidth=1.5, color="#2196F3")
    ax.set_title("Monthly Sales Trend")
    ax.set_ylabel("Sales ($)")
    ax.set_xlabel("Month")

    # Show every 6th label to avoid crowding
    tick_positions = range(0, len(df), 6)
    ax.set_xticks(tick_positions)
    ax.set_xticklabels([df["Year_Month"].iloc[i] for i in tick_positions], rotation=45)
    ax.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    return fig


def plot_sales_by_region(df: pd.DataFrame) -> plt.Figure:
    """Pie chart of sales distribution by region.

    Args:
        df: Summary DataFrame with Region and Total_Sales columns.

    Returns:
        matplotlib Figure object.
    """
    fig, ax = plt.subplots(figsize=(7, 7))
    colors = ["#2196F3", "#4CAF50", "#FF9800", "#f44336"]
    ax.pie(
        df["Total_Sales"],
        labels=df["Region"],
        autopct="%1.1f%%",
        colors=colors,
        startangle=90,
    )
    ax.set_title("Sales Distribution by Region")
    plt.tight_layout()
    return fig


def plot_discount_vs_profit(df: pd.DataFrame) -> plt.Figure:
    """Bar chart showing average profit by discount band.

    Args:
        df: DataFrame with Discount_Band and Avg_Profit columns.

    Returns:
        matplotlib Figure object.
    """
    colors = ["#4CAF50" if x >= 0 else "#f44336" for x in df["Avg_Profit"]]
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(df["Discount_Band"].astype(str), df["Avg_Profit"], color=colors)
    ax.set_title("Average Profit by Discount Level")
    ax.set_ylabel("Avg Profit ($)")
    ax.set_xlabel("Discount Band")
    ax.axhline(y=0, color="black", linewidth=0.5)
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig


def plot_yearly_growth(df: pd.DataFrame) -> plt.Figure:
    """Grouped bar chart of yearly sales and profit.

    Args:
        df: DataFrame with Order Year, Total_Sales, Total_Profit columns.

    Returns:
        matplotlib Figure object.
    """
    fig, ax = plt.subplots(figsize=(8, 5))
    x = range(len(df))
    width = 0.35
    ax.bar([i - width / 2 for i in x], df["Total_Sales"], width, label="Sales", color="#2196F3")
    ax.bar([i + width / 2 for i in x], df["Total_Profit"], width, label="Profit", color="#4CAF50")
    ax.set_title("Yearly Sales vs Profit")
    ax.set_ylabel("Amount ($)")
    ax.set_xticks(x)
    ax.set_xticklabels(df["Order Year"].astype(int))
    ax.legend()
    plt.tight_layout()
    return fig
