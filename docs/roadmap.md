# 6-Week Data Engineering Learning Roadmap

This roadmap is designed for a senior backend developer with strong PHP experience who wants to transition into Data Engineering.

## Week 1: Python for Data Engineering

Concepts:
- Python syntax, functions, modules, and virtual environments
- `pandas` basics and working with CSV/JSON
- Python file I/O on Windows

Hands-on:
- Create the project folder
- Explore `datasets/` with Python
- Write a small script that loads `sales.csv` and prints totals

Resources:
- Python official tutorial
- Real Python beginner guides

## Week 2: Spark Fundamentals

Concepts:
- What is Apache Spark?
- Spark architecture, driver, and executors
- Spark DataFrames vs RDDs
- Creating a `SparkSession`

Hands-on:
- Run `src/ingest.py`
- Inspect raw DataFrames with `.show()` and `.printSchema()`
- Add a new sample record and rerun ingestion

Resources:
- Databricks free tutorials
- PySpark quickstart

## Week 3: ETL and Data Cleaning

Concepts:
- ETL pipeline design
- data validation and type casting
- handling missing values and bad records
- join strategy for fact and dimension tables

Hands-on:
- Inspect `src/clean_transform.py`
- Add a bad row to `sales.csv` and see how the cleaning step removes it
- Expand validation logic for shipping states

## Week 4: Analytics and SQL

Concepts:
- Spark SQL and temporary views
- aggregation functions, GROUP BY, ORDER BY
- time-series and revenue trend queries
- writing reusable SQL query files

Hands-on:
- Run `src/etl_pipeline.py` and query the fact table
- Use the SQL file in Databricks or a local Spark SQL session
- Add a revenue-by-country query

## Week 5: Reporting and Databricks

Concepts:
- report generation from analytics data
- Parquet storage format and why it matters
- Databricks Community Edition workspace setup
- notebooks and job workflows

Hands-on:
- Run `src/report.py`
- Upload datasets to Databricks and run the notebook
- Create a workflow that executes the ETL job

## Week 6: Portfolio and Resume Work

Concepts:
- documenting projects for GitHub
- capturing screenshots and writing a case study
- aligning the project with data engineering roles
- preparing for SQL and Spark interview questions

Hands-on:
- Fill README sections with your learnings
- Create a `demo/` screenshot folder
- Publish the repo to GitHub and update LinkedIn

## Stretch goals

- Add data quality checks for duplicate orders
- Build a small Flask dashboard running from `localhost`
- Add a new dataset for inventory levels or supplier data
