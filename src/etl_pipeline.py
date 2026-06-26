"""End-to-end ETL pipeline entry point for PythonSparks eCommerce analytics."""

import os
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from pyspark.sql import SparkSession
from src.ingest import create_spark_session, read_csv_data, read_json_data
from src.clean_transform import (
    clean_customers,
    clean_orders,
    clean_products,
    clean_sales,
    build_business_facts,
    aggregate_metrics,
    validate_data,
)


def create_output_dirs(base_dir: str = "output") -> None:
    """Create output directories if they do not exist."""
    os.makedirs(os.path.join(base_dir, "parquet"), exist_ok=True)
    os.makedirs(os.path.join(base_dir, "reports"), exist_ok=True)


def run_etl(spark: SparkSession, data_dir: str = "datasets", output_dir: str = "output") -> None:
    """Run the complete ETL pipeline from raw datasets to clean analytics output."""
    create_output_dirs(output_dir)

    print("1) Ingesting raw datasets")
    sales_raw = read_csv_data(spark, os.path.join(data_dir, "sales.csv"))
    customers_raw = read_json_data(spark, os.path.join(data_dir, "customers.json"))
    products_raw = read_csv_data(spark, os.path.join(data_dir, "products.csv"))
    orders_raw = read_json_data(spark, os.path.join(data_dir, "orders.json"))

    print("2) Cleaning and validating datasets")
    sales_clean = clean_sales(sales_raw)
    customers_clean = clean_customers(customers_raw)
    products_clean = clean_products(products_raw)
    orders_clean = clean_orders(orders_raw)

    print("3) Building business fact table")
    full_df = build_business_facts(sales_clean, customers_clean, products_clean, orders_clean)
    validated_df = validate_data(full_df)

    validated_df.write.mode("overwrite").parquet(os.path.join(output_dir, "parquet", "fact_orders"))
    print(f"Saved transformed parquet to {output_dir}/parquet/fact_orders")

    metrics_df = aggregate_metrics(validated_df)
    metrics_df.write.mode("overwrite").parquet(os.path.join(output_dir, "parquet", "category_metrics"))
    print(f"Saved aggregated metrics to {output_dir}/parquet/category_metrics")

    print("4) Showing sample output")
    metrics_df.show(truncate=False)


if __name__ == "__main__":
    spark = create_spark_session()
    try:
        run_etl(spark)
    finally:
        spark.stop()
