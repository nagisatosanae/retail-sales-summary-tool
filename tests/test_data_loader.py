"""Tests for the data_loader module (US-01)."""

import pytest
import pandas as pd
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.data_loader import load_dataset, clean_dataset, get_clean_data, get_dataset_summary


DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "superstore.csv")


class TestLoadDataset:
    def test_returns_dataframe(self):
        df = load_dataset(DATA_PATH)
        assert isinstance(df, pd.DataFrame)

    def test_has_expected_columns(self):
        df = load_dataset(DATA_PATH)
        expected = ["Order ID", "Sales", "Profit", "Category", "Region"]
        for col in expected:
            assert col in df.columns

    def test_not_empty(self):
        df = load_dataset(DATA_PATH)
        assert len(df) > 0


class TestCleanDataset:
    @pytest.fixture
    def raw_df(self):
        return load_dataset(DATA_PATH)

    def test_date_columns_are_datetime(self, raw_df):
        cleaned = clean_dataset(raw_df)
        assert pd.api.types.is_datetime64_any_dtype(cleaned["Order Date"])
        assert pd.api.types.is_datetime64_any_dtype(cleaned["Ship Date"])

    def test_no_na_in_sales(self, raw_df):
        cleaned = clean_dataset(raw_df)
        assert cleaned["Sales"].isna().sum() == 0

    def test_derived_columns_added(self, raw_df):
        cleaned = clean_dataset(raw_df)
        assert "Order Year" in cleaned.columns
        assert "Order Month" in cleaned.columns
        assert "Delivery Days" in cleaned.columns

    def test_city_na_replaced(self, raw_df):
        cleaned = clean_dataset(raw_df)
        assert "N/A" not in cleaned["City"].values


class TestGetDatasetSummary:
    def test_summary_keys(self):
        df = get_clean_data(DATA_PATH)
        summary = get_dataset_summary(df)
        assert "total_rows" in summary
        assert "total_orders" in summary
        assert "categories" in summary
        assert "regions" in summary

    def test_summary_values_positive(self):
        df = get_clean_data(DATA_PATH)
        summary = get_dataset_summary(df)
        assert summary["total_rows"] > 0
        assert summary["total_orders"] > 0
