import os

import pytest
from pyspark.sql import SparkSession

from src.clean_transform import (
    build_business_facts,
    clean_customers,
    clean_orders,
    clean_products,
    clean_sales,
    validate_data,
)
from src.ingest import create_spark_session, read_csv_data, read_json_data


@pytest.fixture(scope="session")
def spark():
    spark = SparkSession.builder.master("local[2]").appName("PythonSparksTest").getOrCreate()
    yield spark
    spark.stop()


def test_ingest_reads_sales(spark):
    data_dir = os.path.join(os.path.dirname(__file__), "..", "datasets")
    sales_df = read_csv_data(spark, os.path.join(data_dir, "sales.csv"))
    assert sales_df.count() >= 10
    assert "order_id" in sales_df.columns


def test_clean_sales_filters_invalid_rows(spark):
    data_dir = os.path.join(os.path.dirname(__file__), "..", "datasets")
    sales_df = read_csv_data(spark, os.path.join(data_dir, "sales.csv"))
    clean_df = clean_sales(sales_df)
    assert clean_df.filter("quantity <= 0").count() == 0
    assert clean_df.filter("price < 0").count() == 0


def test_build_business_facts_has_expected_columns(spark):
    data_dir = os.path.join(os.path.dirname(__file__), "..", "datasets")
    sales_df = clean_sales(read_csv_data(spark, os.path.join(data_dir, "sales.csv")))
    customers_df = clean_customers(read_json_data(spark, os.path.join(data_dir, "customers.json")))
    products_df = clean_products(read_csv_data(spark, os.path.join(data_dir, "products.csv")))
    orders_df = clean_orders(read_json_data(spark, os.path.join(data_dir, "orders.json")))
    facts_df = build_business_facts(sales_df, customers_df, products_df, orders_df)
    assert "gross_margin" in facts_df.columns
    assert facts_df.count() > 0


def test_validate_data_produces_status(spark):
    data_dir = os.path.join(os.path.dirname(__file__), "..", "datasets")
    sales_df = clean_sales(read_csv_data(spark, os.path.join(data_dir, "sales.csv")))
    customers_df = clean_customers(read_json_data(spark, os.path.join(data_dir, "customers.json")))
    products_df = clean_products(read_csv_data(spark, os.path.join(data_dir, "products.csv")))
    orders_df = clean_orders(read_json_data(spark, os.path.join(data_dir, "orders.json")))
    facts_df = build_business_facts(sales_df, customers_df, products_df, orders_df)
    validated_df = validate_data(facts_df)
    assert "validation_status" in validated_df.columns
