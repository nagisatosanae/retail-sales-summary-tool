"""Tests for the sales_summary module (US-02)."""

import pytest
import pandas as pd
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.data_loader import get_clean_data
from src.sales_summary import (
    sales_by_category,
    sales_by_region,
    sales_by_subcategory,
    sales_by_segment,
    sales_by_state,
)


DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "superstore.csv")


@pytest.fixture(scope="module")
def df():
    return get_clean_data(DATA_PATH)


class TestSalesByCategory:
    def test_returns_dataframe(self, df):
        result = sales_by_category(df)
        assert isinstance(result, pd.DataFrame)

    def test_has_three_categories(self, df):
        result = sales_by_category(df)
        assert len(result) == 3

    def test_sales_are_positive(self, df):
        result = sales_by_category(df)
        assert (result["Total_Sales"] > 0).all()


class TestSalesByRegion:
    def test_returns_dataframe(self, df):
        result = sales_by_region(df)
        assert isinstance(result, pd.DataFrame)

    def test_has_four_regions(self, df):
        result = sales_by_region(df)
        assert len(result) == 4


class TestSalesByState:
    def test_top_n_works(self, df):
        result = sales_by_state(df, top_n=5)
        assert len(result) == 5

    def test_sorted_descending(self, df):
        result = sales_by_state(df, top_n=10)
        sales_list = result["Total_Sales"].tolist()
        assert sales_list == sorted(sales_list, reverse=True)
