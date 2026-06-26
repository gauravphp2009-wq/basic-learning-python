# Databricks Community Edition Workflow Guidance

## 1) Create a Databricks Community Edition account

- Go to https://community.cloud.databricks.com/
- Sign up or log in
- Create a free workspace

## 2) Upload sample datasets

- In Databricks, open Data > Add Data > Upload File
- Upload `datasets/sales.csv`, `datasets/customers.json`, `datasets/products.csv`, `datasets/orders.json`
- Use the default DBFS path or copy the file location to use in the notebook

## 3) Create a notebook

- Create a new notebook and choose Python
- Use the notebook content in `notebooks/Databricks_Ecommerce_ETL.ipynb` as a reference
- Set the cluster to a small single-node cluster

## 4) Run the ETL flow in Databricks

- Read the files from DBFS or raw file paths
- Apply the same cleaning and join logic from `src/clean_transform.py`
- Save results as Delta tables or parquet under `/tmp` or `dbfs:/tmp/python_sparks`

## 5) Build a Databricks job workflow

- In Databricks, go to Jobs > Create Job
- Add tasks to:
  1. execute the notebook
  2. run SQL analysis queries
- Schedule the job on demand for testing

## 6) Use SQL queries for analytics

- In Databricks SQL Editor, use queries from `sql/analysis_queries.sql`
- Use `CREATE OR REPLACE TEMP VIEW fact_orders AS ...` if needed

## 7) Validate results

- Verify row counts after each stage with `.count()`
- Use `display()` in notebooks for easy debugging
- Compare results locally with the `output/` data

## 8) Notes for Windows developers

- Databricks is cloud-based, so the local WAMP installation does not matter here
- Use Databricks notebooks for the same PySpark API you run locally
- When you graduate to production, use `dbfs:/` paths and Delta Lake tables
