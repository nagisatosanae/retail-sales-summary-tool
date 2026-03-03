"""
US-01: Data Loading and Cleaning Module

Loads the superstore.csv dataset and performs cleaning operations
to ensure data quality and consistency for downstream analysis.
"""

import pandas as pd
import os


def load_dataset(filepath: str = None) -> pd.DataFrame:
    """Load the superstore CSV dataset from the given filepath.

    Args:
        filepath: Path to the CSV file. Defaults to data/superstore.csv.

    Returns:
        Raw pandas DataFrame loaded from the CSV.
    """
    if filepath is None:
        filepath = os.path.join(os.path.dirname(__file__), "..", "data", "superstore.csv")
    return pd.read_csv(filepath, encoding="latin-1")


def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """Clean the raw dataset by fixing types, handling missing values, and
    standardizing columns.

    Steps:
        1. Convert date columns to datetime.
        2. Fill missing numeric values with 0.
        3. Strip whitespace from string columns.
        4. Replace 'N/A' city entries with 'Unknown'.
        5. Ensure Discount column is numeric.

    Args:
        df: Raw DataFrame from load_dataset.

    Returns:
        Cleaned DataFrame ready for analysis.
    """
    df = df.copy()

    # Convert date columns
    df["Order Date"] = pd.to_datetime(df["Order Date"], format="mixed", dayfirst=False)
    df["Ship Date"] = pd.to_datetime(df["Ship Date"], format="mixed", dayfirst=False)

    # Handle missing numeric values
    for col in ["Sales", "Quantity", "Discount", "Profit"]:
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

    # Clean string columns — strip whitespace and normalize extra spaces
    str_cols = df.select_dtypes(include="object").columns
    for col in str_cols:
        df[col] = df[col].str.strip().str.replace(r"\s+", " ", regex=True)

    # Standardize case-sensitive inconsistencies
    df["Category"] = df["Category"].str.title()
    df["Segment"] = df["Segment"].str.title()

    # Replace N/A cities
    df["City"] = df["City"].replace("N/A", "Unknown")

    # Add derived columns useful for analysis
    df["Order Year"] = df["Order Date"].dt.year
    df["Order Month"] = df["Order Date"].dt.month
    df["Order Quarter"] = df["Order Date"].dt.quarter
    df["Delivery Days"] = (df["Ship Date"] - df["Order Date"]).dt.days

    return df


def get_clean_data(filepath: str = None) -> pd.DataFrame:
    """Convenience function: load and clean in one step.

    Args:
        filepath: Optional path to the CSV file.

    Returns:
        Cleaned DataFrame.
    """
    raw = load_dataset(filepath)
    return clean_dataset(raw)


def get_dataset_summary(df: pd.DataFrame) -> dict:
    """Return a high-level summary of the dataset.

    Args:
        df: Cleaned DataFrame.

    Returns:
        Dictionary with row count, date range, unique counts, etc.
    """
    return {
        "total_rows": len(df),
        "total_orders": df["Order ID"].nunique(),
        "total_customers": df["Customer ID"].nunique(),
        "total_products": df["Product ID"].nunique(),
        "date_range": (df["Order Date"].min(), df["Order Date"].max()),
        "categories": df["Category"].unique().tolist(),
        "regions": df["Region"].unique().tolist(),
        "segments": df["Segment"].unique().tolist(),
    }
