"""Tests for the profit_analysis module (US-03)."""

import pytest
import pandas as pd
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.data_loader import get_clean_data
from src.profit_analysis import (
    profit_by_category,
    profit_by_subcategory,
    top_products_by_profit,
    bottom_products_by_profit,
    discount_impact_analysis,
)


DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "superstore.csv")


@pytest.fixture(scope="module")
def df():
    return get_clean_data(DATA_PATH)


class TestProfitByCategory:
    def test_has_profit_margin(self, df):
        result = profit_by_category(df)
        assert "Profit_Margin_%" in result.columns

    def test_margin_is_reasonable(self, df):
        result = profit_by_category(df)
        assert (result["Profit_Margin_%"] > -100).all()
        assert (result["Profit_Margin_%"] < 100).all()


class TestTopProducts:
    def test_top_products_positive_profit(self, df):
        result = top_products_by_profit(df, top_n=5)
        assert (result["Total_Profit"] > 0).all()

    def test_bottom_products_sorted_ascending(self, df):
        result = bottom_products_by_profit(df, top_n=5)
        profits = result["Total_Profit"].tolist()
        assert profits == sorted(profits)


class TestDiscountImpact:
    def test_returns_dataframe(self, df):
        result = discount_impact_analysis(df)
        assert isinstance(result, pd.DataFrame)

    def test_has_discount_bands(self, df):
        result = discount_impact_analysis(df)
        assert len(result) > 0
        assert "Discount_Band" in result.columns
