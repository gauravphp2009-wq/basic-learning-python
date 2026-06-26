# Complete Windows 11 Setup Guide for PythonSparks

## A. System Requirements and Preparation

### 1) Verify Python and Java

The project requires Python 3.11+ and Java 17+ (for PySpark).

**Check Python:**
```powershell
python --version
# Expected: Python 3.11.9 or later
```

**Install Python** (if needed):
- Download from https://www.python.org/downloads/
- Check "Add Python to PATH" during installation

**Check Java:**
```powershell
java -version
# Expected: openjdk 17, 21, or later
```

**Install Java** (if needed):
- Download OpenJDK from https://adoptium.net/
- Set `JAVA_HOME` environment variable in Windows Settings > Environment Variables
  - Variable name: `JAVA_HOME`
  - Variable value: `C:\Program Files\Eclipse Adoptium\jdk-21.0.x` (or your installation path)

### 2) Create Project Directory

The project is already located at `d:\wamp\www\PythonSparks`. 

**Why here?** Because you already have WAMP installed, this folder keeps data engineering work alongside your PHP projects in the www directory. Python and PySpark run independently from WAMP, so there are no conflicts.

---

## B. Creating and Activating a Virtual Environment

Virtual environments isolate Python dependencies for this project.

```powershell
cd d:\wamp\www\PythonSparks

# Create virtual environment
python -m venv .venv

# Activate it
.venv\Scripts\Activate.ps1
```

**If PowerShell blocks the activation script:**
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

After activation, you should see `(.venv)` in your terminal prompt.

---

## C. Installing Project Dependencies

```powershell
# Upgrade pip
python -m pip install --upgrade pip

# Install from requirements.txt
python -m pip install -r requirements.txt
```

This installs:
- `pyspark==3.5.0` — Spark distributed computing framework
- `pandas==2.2.3` — Data manipulation (optional, for Python scripts)
- `pytest==8.4.2` — Testing framework

---

## D. Project Structure Overview

```
PythonSparks/
├── README.md                          # Project overview
├── requirements.txt                   # Python dependencies
├── .gitignore                         # Git ignore rules
│
├── datasets/                          # Sample raw data
│   ├── sales.csv                      # Orders and line items
│   ├── customers.json                 # Customer profiles
│   ├── products.csv                   # Product catalog
│   └── orders.json                    # Shipping and payment metadata
│
├── src/                               # ETL and reporting code
│   ├── __init__.py
│   ├── ingest.py                      # Data ingestion (CSV/JSON reading)
│   ├── clean_transform.py             # Cleaning and transformation logic
│   ├── etl_pipeline.py                # Main pipeline orchestration
│   └── report.py                      # Report generation
│
├── sql/                               # SQL query examples
│   └── analysis_queries.sql           # Reusable Spark SQL queries
│
├── notebooks/                         # Databricks notebook
│   └── Databricks_Ecommerce_ETL.ipynb # Notebook for Databricks
│
├── docs/                              # Learning and setup guides
│   ├── setup_testing_instructions.md  # Setup steps
│   ├── implementation_guide.md        # Explanation of each stage
│   ├── roadmap.md                     # 6-week learning plan
│   ├── github_portfolio_guide.md      # Portfolio and resume tips
│   └── databricks_workflow.md         # Moving to Databricks
│
├── tests/                             # Unit tests for ETL logic
│   ├── __init__.py
│   └── test_etl_pipeline.py           # Pytest test cases
│
└── output/                            # Generated output (not tracked by Git)
    ├── parquet/                       # Parquet data files
    └── reports/                       # Generated reports
```

---

## E. Running the ETL Pipeline

### Step 1: Verify Data Files

Check that sample datasets exist:
```powershell
ls datasets/
# You should see: sales.csv, customers.json, products.csv, orders.json
```

### Step 2: Run the Full Pipeline

```powershell
python .\src\etl_pipeline.py
```

**Expected output:**
```
1) Ingesting raw datasets
2) Cleaning and validating datasets
3) Building business fact table
4) Showing sample output
[metrics DataFrame]
Saved transformed parquet to output/parquet/fact_orders
Saved aggregated metrics to output/parquet/category_metrics
```

### Step 3: Verify Output

Check generated files:
```powershell
ls output/parquet/
# You should see directories: fact_orders, category_metrics
```

### Step 4: Generate Report

```powershell
python .\src\report.py
```

Check the report:
```powershell
cat output/reports/summary_report.txt
```

---

## F. Testing the Project

Run automated tests:
```powershell
pytest tests/ -v
```

**Expected output:**
```
test_etl_pipeline.py::test_ingest_reads_sales PASSED
test_etl_pipeline.py::test_clean_sales_filters_invalid_rows PASSED
test_etl_pipeline.py::test_build_business_facts_has_expected_columns PASSED
test_etl_pipeline.py::test_validate_data_produces_status PASSED
```

---

## G. Understanding Each Module

### `src/ingest.py`
- **Purpose:** Read CSV and JSON files into Spark DataFrames
- **Key functions:**
  - `create_spark_session()` — Initialize Spark
  - `read_csv_data()` — Load CSV with automatic schema inference
  - `read_json_data()` — Load line-delimited JSON

### `src/clean_transform.py`
- **Purpose:** Clean, validate, and transform data
- **Key functions:**
  - `clean_sales()` — Cast types, compute sales_amount, filter invalid rows
  - `clean_customers()` — Normalize emails, create full names, deduplicate
  - `clean_products()` — Cast prices and costs, deduplicate
  - `clean_orders()` — Normalize cities and states, deduplicate
  - `build_business_facts()` — Join dimension tables and compute gross_margin
  - `validate_data()` — Add a validation column for data quality

### `src/etl_pipeline.py`
- **Purpose:** Orchestrate the entire pipeline
- **Flow:**
  1. Ingest raw datasets
  2. Clean and validate each dataset
  3. Build a unified fact table
  4. Aggregate by category
  5. Save as Parquet files
  6. Display summary metrics

### `src/report.py`
- **Purpose:** Generate human-readable reports from aggregated data
- **Output:** Text summary file with revenue by category

---

## H. Running SQL Analysis Queries

The `sql/analysis_queries.sql` file contains reusable queries. To use them:

### Locally with Spark SQL:
```python
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Analysis").getOrCreate()

# Create a view from the fact table
fact_df = spark.read.parquet("output/parquet/fact_orders")
fact_df.createOrReplaceTempView("fact_orders")

# Run a query
spark.sql("""
    SELECT category, SUM(sales_amount) AS revenue
    FROM fact_orders
    GROUP BY category
    ORDER BY revenue DESC
""").show()
```

### In Databricks:
Copy the query from `sql/analysis_queries.sql` and paste it into a Databricks SQL cell.

---

## I. Common Debugging Steps

### PySpark takes a long time to start
- Normal! Spark builds the JVM on first run. Subsequent runs are faster.
- Ensure Java is in your PATH: `java -version`

### JSON load fails
- Check JSON file format: each line must be valid JSON (newline-delimited)
- Use a JSON validator: https://jsonlint.com/

### Type casting errors
- Inspect raw data first:
  ```python
  df = spark.read.option('header', 'true').csv('datasets/sales.csv')
  df.printSchema()  # Shows inferred types
  df.show(5)        # Shows sample rows
  ```

### "Cannot find Spark installation"
- Set `SPARK_HOME` environment variable or ensure Java and Python are in PATH

### Tests fail
- Activate the virtual environment: `.venv\Scripts\Activate.ps1`
- Reinstall dependencies: `python -m pip install -r requirements.txt`

---

## J. Adding More Sample Data

To expand the project with new datasets:

1. **Create a new CSV or JSON file** in `datasets/`
2. **Write a cleaning function** in `src/clean_transform.py`
3. **Join it into the fact table** in `build_business_facts()`
4. **Test with pytest**
5. **Update SQL queries** in `sql/analysis_queries.sql`

Example: Add `inventory.csv` with product stock levels and join on `product_id`.

---

## K. Deactivating the Virtual Environment

When finished working:
```powershell
deactivate
```

To reactivate next time:
```powershell
.venv\Scripts\Activate.ps1
```

---

## L. Next Steps: Moving to Databricks

See `docs/databricks_workflow.md` for detailed instructions on:
- Setting up a Databricks Community Edition workspace
- Uploading datasets to DBFS
- Running the notebook
- Creating a job workflow

---

## M. Troubleshooting Summary

| Issue | Solution |
|-------|----------|
| `python: command not found` | Add Python to PATH or use full path `C:\Program Files\Python311\python.exe` |
| `ModuleNotFoundError: pyspark` | Activate `.venv` and reinstall: `python -m pip install pyspark==3.5.0` |
| `JAVA_HOME` not set | Set environment variable to JDK installation path (e.g., `C:\Program Files\Eclipse Adoptium\jdk-21`) |
| Spark takes forever to start | First run is slow. Subsequent runs are faster. |
| Parquet files not created | Check terminal output for errors. Ensure `output/` directory has write permissions. |

---

## N. Project Completion Checklist

- [ ] Python 3.11+ installed and in PATH
- [ ] Java 17+ installed with JAVA_HOME set
- [ ] Virtual environment created and activated
- [ ] Dependencies installed: `python -m pip install -r requirements.txt`
- [ ] ETL pipeline runs: `python .\src\etl_pipeline.py`
- [ ] Report generated: `python .\src\report.py`
- [ ] Tests pass: `pytest tests/ -v`
- [ ] Output files created in `output/parquet/` and `output/reports/`
- [ ] SQL queries understood (reviewed `sql/analysis_queries.sql`)
- [ ] Databricks account created for next phase

---

## Questions?

Refer to the guides in `docs/`:
- `implementation_guide.md` — Code explanations
- `roadmap.md` — 6-week learning plan
- `databricks_workflow.md` — Databricks setup
- `github_portfolio_guide.md` — Portfolio presentation

Happy learning!
