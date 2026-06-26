"""Data ingestion utilities for the PythonSparks eCommerce pipeline."""

from pyspark.sql import SparkSession


def create_spark_session(app_name: str = "PythonSparks ETL") -> SparkSession:
    """Create or return a SparkSession for local PySpark execution."""
    return SparkSession.builder.appName(app_name).getOrCreate()


def read_csv_data(spark: SparkSession, path: str):
    """Read a CSV file into a Spark DataFrame with header and inferred schema."""
    return (
        spark.read.format("csv")
        .option("header", "true")
        .option("inferSchema", "true")
        .option("mode", "PERMISSIVE")
        .load(path)
    )


def read_json_data(spark: SparkSession, path: str):
    """Read JSON data into a Spark DataFrame."""
    return (
        spark.read.format("json")
        .option("multiline", "false")
        .option("mode", "PERMISSIVE")
        .load(path)
    )
