# Implementation Guide

This guide explains every major step of the PythonSparks project.

## 1) Data Sources and Business Use Case

The project models an eCommerce pipeline with:
- `sales.csv` — line items with order, product, quantity, and price
- `customers.json` — customer profile data
- `products.csv` — product catalog and cost details
- `orders.json` — shipping and payment metadata

Business goal: combine sales, customer, product, and order data into a fact table for analytics and generate revenue insights.

## 2) Ingestion with PySpark

The `src/ingest.py` module creates a local Spark session and reads raw files.

Key ideas:
- `SparkSession` is the entry point for PySpark applications
- Use `inferSchema` for CSV files in a beginner project
- Use `multiline=false` for line-delimited JSON

## 3) Cleaning and Validation

The `src/clean_transform.py` module shows data cleaning best practices:
- cast data types explicitly
- convert dates with `to_date`
- filter invalid or missing numeric values
- normalize text fields like email and shipping city
- deduplicate dimension data by key

Common mistakes to avoid:
- trusting CSV headers without checking them
- ignoring null values before joins
- leaving string numbers uncasted

## 4) Data Transformation

The transformation creates business facts by joining:
- sales line items
- customer dimension
- product dimension
- order metadata

The fact table includes metrics such as:
- `sales_amount`
- `gross_margin`
- `payment_type`
- `shipping_city`
- `validation_status`

## 5) Aggregation and Reporting

The pipeline saves:
- fact table as Parquet for efficient analytics
- category metrics as aggregated Parquet
- text summary report

The `src/report.py` script reads aggregated parquet and generates a human-readable summary.

## 6) Running Locally

Use these commands:

```powershell
python .\src\etl_pipeline.py
python .\src\report.py
```

Verify locally by opening the generated file:
- `output/reports/summary_report.txt`

## 7) Testing Modules Locally

The `tests/` folder contains PySpark tests that confirm:
- ingestion reads the expected number of rows
- cleaning preserves valid rows and drops invalid ones
- transformation creates the expected columns

Run tests with:

```powershell
pytest
```

## 8) Databricks Transition

To move this project into Databricks:
- upload the sample datasets to DBFS or the Databricks Filesystem
- copy the notebook in `notebooks/` to Databricks
- use the SQL queries in `sql/analysis_queries.sql`
- create a job workflow in Databricks to run `src/etl_pipeline.py` and `src/report.py`
