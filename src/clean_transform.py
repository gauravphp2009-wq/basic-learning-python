"""Cleaning and transformation logic for PythonSparks data engineering."""

from pyspark.sql import DataFrame
from pyspark.sql.functions import col, concat_ws, expr, lit, lower, to_date


def clean_sales(sales_df: DataFrame) -> DataFrame:
    """Clean raw sales line items coming from CSV."""
    return (
        sales_df
        .withColumn("order_id", col("order_id").cast("integer"))
        .withColumn("customer_id", col("customer_id").cast("integer"))
        .withColumn("product_id", col("product_id").cast("integer"))
        .withColumn("quantity", col("quantity").cast("integer"))
        .withColumn("price", col("price").cast("double"))
        .withColumn("order_date", to_date(col("order_date"), "yyyy-MM-dd"))
        .withColumn("sales_amount", col("quantity") * col("price"))
        .filter(col("order_id").isNotNull() & col("customer_id").isNotNull())
        .filter(col("quantity") > 0)
        .filter(col("price") >= 0)
    )


def clean_customers(customers_df: DataFrame) -> DataFrame:
    """Clean raw customer JSON data and normalize fields."""
    return (
        customers_df
        .withColumn("customer_id", col("customer_id").cast("integer"))
        .withColumn("signup_date", to_date(col("signup_date"), "yyyy-MM-dd"))
        .withColumn("email", lower(col("email")))
        .withColumn("full_name", concat_ws(" ", col("first_name"), col("last_name")))
        .filter(col("customer_id").isNotNull())
        .dropDuplicates(["customer_id"])
    )


def clean_products(products_df: DataFrame) -> DataFrame:
    """Clean raw product data from CSV and prepare for joins."""
    return (
        products_df
        .withColumn("product_id", col("product_id").cast("integer"))
        .withColumn("price", col("price").cast("double"))
        .withColumn("cost", col("cost").cast("double"))
        .filter(col("product_id").isNotNull())
        .dropDuplicates(["product_id"])
    )


def clean_orders(orders_df: DataFrame) -> DataFrame:
    """Clean raw order metadata and standardize shipping information."""
    return (
        orders_df
        .withColumn("order_id", col("order_id").cast("integer"))
        .withColumn("shipping_city", lower(col("shipping_city")))
        .withColumn("shipping_state", lower(col("shipping_state")))
        .withColumn("payment_type", lower(col("payment_type")))
        .filter(col("order_id").isNotNull())
        .dropDuplicates(["order_id"])
    )


def build_business_facts(sales_df: DataFrame, customers_df: DataFrame, products_df: DataFrame, orders_df: DataFrame) -> DataFrame:
    """Join cleaned datasets and create a fact table for analytics."""
    joined = (
        sales_df.alias("sales")
        .join(customers_df.alias("cust"), "customer_id", "left")
        .join(products_df.alias("prod"), "product_id", "left")
        .join(orders_df.alias("ord"), "order_id", "left")
        .select(
            col("sales.order_id"),
            col("sales.order_date"),
            col("customer_id"),
            col("cust.full_name"),
            col("cust.email"),
            col("prod.product_id"),
            col("prod.product_name"),
            col("prod.category"),
            col("sales.quantity"),
            col("sales.price"),
            col("sales.sales_amount"),
            col("ord.payment_type"),
            col("ord.shipping_city"),
            col("ord.shipping_state"),
            col("prod.cost"),
        )
    )

    return joined.withColumn("gross_margin", col("sales_amount") - (col("quantity") * col("cost")))


def aggregate_metrics(full_df: DataFrame) -> DataFrame:
    """Aggregate high-level business metrics for reporting."""
    return (
        full_df.groupBy("category")
        .agg(
            expr("sum(sales_amount) as total_revenue"),
            expr("sum(quantity) as total_units"),
            expr("sum(gross_margin) as total_margin"),
        )
        .orderBy(col("total_revenue").desc())
    )


def validate_data(full_df: DataFrame) -> DataFrame:
    """Add a validation column to expose rows with missing join data."""
    return full_df.withColumn(
        "validation_status",
        expr("CASE WHEN full_name IS NULL OR product_name IS NULL THEN 'MISSING_DIMENSION' ELSE 'OK' END"),
    )
