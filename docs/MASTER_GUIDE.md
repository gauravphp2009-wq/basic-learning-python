# PythonSparks Learning & Portfolio Project — Master Guide

## Welcome!

This is a **complete, production-ready Data Engineering portfolio project** designed for a senior backend developer (PHP/Laravel/CodeIgniter) transitioning into Data Engineering using Python, PySpark, SQL, and Databricks.

---

## Quick Start (5 minutes)

If you're eager to see it work:

```powershell
# 1. Activate virtual environment (if not already active)
d:\wamp\www\PythonSparks\.venv\Scripts\Activate.ps1

# 2. Run the ETL pipeline
python .\src\etl_pipeline.py

# 3. Generate a report
python .\src\report.py

# 4. View the report
cat output/reports/summary_report.txt
```

If this works, skip to **Section C: What's in this Project?**

---

## A. Initial Setup (If Starting Fresh)

### A.1 System Check

```powershell
python --version      # Should be 3.11+
java -version        # Should be 17+
```

### A.2 If Java is Missing

1. Download from https://adoptium.net/
2. Install and set `JAVA_HOME` in Windows Settings > Environment Variables
3. Add to path value: `C:\Program Files\Eclipse Adoptium\jdk-21.0.x`
4. Verify: `java -version`

### A.3 Create and Activate Virtual Environment

```powershell
cd d:\wamp\www\PythonSparks
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# If blocked by PowerShell:
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

### A.4 Install Dependencies

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

---

## B. Verify the Project Works

Run all three commands and look for "Successfully completed" messages:

```powershell
# Test 1: Run the ETL pipeline
python .\src\etl_pipeline.py

# Test 2: Generate report
python .\src\report.py

# Test 3: Run automated tests
pytest tests/ -v
```

If all three succeed, you're ready to learn!

---

## C. What's in This Project?

### The Business Problem
You have eCommerce data in four sources: sales transactions, customer profiles, product catalog, and order metadata. You need to **ingest, clean, transform, and analyze** this data to generate business insights like revenue by category.

### What You'll Learn

| Week | Concept | What You'll Do |
|------|---------|---|
| 1 | Python Basics | Load CSV/JSON files, use virtual environments |
| 2 | Spark Fundamentals | Create DataFrames, explore schemas, use Spark SQL |
| 3 | Data Cleaning & ETL | Type casting, null handling, joins, validation |
| 4 | SQL Analytics | Write aggregation queries, create insights |
| 5 | Reporting & Databricks | Generate reports, use cloud infrastructure |
| 6 | Portfolio & Resume | Document your project, present on LinkedIn |

Full details: See [roadmap.md](roadmap.md)

---

## D. Project Folder Breakdown

### `datasets/` — Raw source data
- `sales.csv` — Transaction line items
- `customers.json` — Customer profiles  
- `products.csv` — Product catalog with costs
- `orders.json` — Shipping and payment info

### `src/` — Core ETL code
- `ingest.py` — Reads CSV/JSON into Spark
- `clean_transform.py` — Cleaning, validation, joins
- `etl_pipeline.py` — Orchestrates the full flow
- `report.py` — Generates text reports from aggregated data

### `sql/` — Reusable analytics queries
- Queries for revenue, top customers, trends, and data quality checks

### `notebooks/` — Databricks notebook
- Template for running the same pipeline in Databricks

### `docs/` — Learning guides
- **complete_windows_setup_guide.md** — Detailed setup for Windows
- **implementation_guide.md** — Explains every stage of the pipeline
- **roadmap.md** — 6-week study plan
- **databricks_workflow.md** — Moving to Databricks
- **github_portfolio_guide.md** — Repository and resume tips

### `tests/` — Automated tests
- `test_etl_pipeline.py` — pytest cases for ingestion, cleaning, joins

### `output/` — Generated files (not tracked by Git)
- Parquet fact table, aggregated metrics, reports

---

## E. Understanding the ETL Pipeline

### Step 1: Ingestion
```python
# Load raw files from disk
sales_raw = read_csv_data(spark, "datasets/sales.csv")
customers_raw = read_json_data(spark, "datasets/customers.json")
products_raw = read_csv_data(spark, "datasets/products.csv")
orders_raw = read_json_data(spark, "datasets/orders.json")
```

### Step 2: Cleaning
```python
# Cast types, normalize, filter invalid rows
sales_clean = clean_sales(sales_raw)
customers_clean = clean_customers(customers_raw)
products_clean = clean_products(products_raw)
orders_clean = clean_orders(orders_raw)
```

### Step 3: Building the Fact Table
```python
# Join dimensions into one analytics table
fact_orders = build_business_facts(
    sales_clean, customers_clean, products_clean, orders_clean
)
# Compute metrics: gross_margin, validation_status
```

### Step 4: Aggregation
```python
# Group by category and sum revenue, units, margin
metrics = aggregate_metrics(fact_orders)
```

### Step 5: Output
```python
# Save as Parquet (efficient columnar format)
fact_orders.write.parquet("output/parquet/fact_orders")
metrics.write.parquet("output/parquet/category_metrics")
```

---

## F. Running Each Module Independently

### Just read the raw data:
```python
from src.ingest import create_spark_session, read_csv_data
spark = create_spark_session()
sales = read_csv_data(spark, "datasets/sales.csv")
sales.show(5)
```

### Just clean sales data:
```python
from src.clean_transform import clean_sales
sales_clean = clean_sales(sales_raw)
print(f"Before: {sales_raw.count()} rows, After: {sales_clean.count()} rows")
```

### Just run SQL queries:
```python
spark.sql("""
    SELECT category, SUM(sales_amount) AS revenue
    FROM fact_orders
    GROUP BY category
    ORDER BY revenue DESC
""").show()
```

---

## G. Testing Your Code

Run tests to verify everything works:
```powershell
pytest tests/test_etl_pipeline.py -v
```

Add your own tests:
```python
# In tests/test_etl_pipeline.py
def test_custom_logic(spark):
    # Write a test here
    assert True
```

---

## H. Debugging Common Issues

### Spark takes a long time to initialize
Normal! First run builds the JVM. Subsequent runs are much faster.

### "ModuleNotFoundError: pyspark"
```powershell
# Ensure virtual environment is active
.\.venv\Scripts\Activate.ps1
# Reinstall
python -m pip install pyspark==3.5.0
```

### JSON parsing fails
- Check that each line is valid JSON (newline-delimited, not array)
- Use https://jsonlint.com/ to validate

### "JAVA_HOME not set"
```powershell
# Set environment variable in Windows
setx JAVA_HOME "C:\Program Files\Eclipse Adoptium\jdk-21.0.x"
# Restart terminal
```

---

## I. Expanding the Project

### Add a new dataset:
1. Create `datasets/inventory.csv`
2. Write `clean_inventory()` in `src/clean_transform.py`
3. Join it in `build_business_facts()`
4. Add tests in `tests/test_etl_pipeline.py`

### Add new metrics:
1. Write aggregations in `src/clean_transform.py`
2. Compute in `src/etl_pipeline.py`
3. Include in report generation

### Add a dashboard:
1. Load Parquet files with pandas
2. Create visualizations with matplotlib/plotly
3. Export as static HTML

---

## J. Preparing for Databricks

The project is designed to move seamlessly to Databricks:

1. **Notebooks:** Copy `notebooks/Databricks_Ecommerce_ETL.ipynb` to Databricks
2. **Data:** Upload `datasets/` to DBFS
3. **Code:** Use the same functions, just change file paths to `/dbfs/...`
4. **Jobs:** Create a Databricks workflow to orchestrate the pipeline
5. **SQL:** Run queries in Databricks SQL Editor

Full guide: See [databricks_workflow.md](databricks_workflow.md)

---

## K. Portfolio & GitHub Setup

### Repository Structure
```
PythonSparks/
├── README.md               # Project overview
├── requirements.txt        # Dependencies
├── docs/                   # Setup and learning guides
├── datasets/               # Sample data
├── src/                    # ETL code
├── sql/                    # Analytics queries
├── notebooks/              # Databricks notebook
├── tests/                  # Test cases
└── .gitignore             # Ignore output/ and .venv/
```

### README.md sections:
- Project overview
- Technologies used (Python, PySpark, SQL, Databricks)
- Business problem and solution
- Setup and run instructions
- Testing steps
- What you learned

### LinkedIn Post Example:
> "Just built an end-to-end eCommerce analytics pipeline using PySpark and Databricks. Ingested 100K+ transactions, performed multi-table joins, and generated business insights on category revenue. This project marks my transition from PHP backend to Data Engineering. [Link to GitHub] #DataEngineering #PySpark #Databricks"

Full guide: See [github_portfolio_guide.md](github_portfolio_guide.md)

---

## L. Learning Path Timeline

### Week 1: Python & Environment
- [ ] Setup Python, Java, virtual environment
- [ ] Understand folder structure
- [ ] Run the full pipeline
- [ ] Read `implementation_guide.md`

### Week 2: Spark Fundamentals
- [ ] Explore raw data with `.show()` and `.printSchema()`
- [ ] Understand DataFrames vs RDDs
- [ ] Modify one cleaning function and rerun
- [ ] Read Databricks Spark docs

### Week 3: Data Quality & ETL
- [ ] Add a bad row to `sales.csv` and see it filtered
- [ ] Expand validation logic
- [ ] Write a new test in `tests/`
- [ ] Try a different type of join

### Week 4: SQL Analytics
- [ ] Run each query in `sql/analysis_queries.sql`
- [ ] Write a new aggregation query
- [ ] Understand GROUP BY, aggregation functions
- [ ] Build a revenue trend query

### Week 5: Reporting & Databricks
- [ ] Create a Databricks Community account
- [ ] Upload datasets to DBFS
- [ ] Copy the notebook and run it
- [ ] Create a Databricks job

### Week 6: Portfolio & Presentation
- [ ] Push to GitHub
- [ ] Write a comprehensive README
- [ ] Take screenshots of the pipeline and results
- [ ] Post on LinkedIn with a project summary
- [ ] Update resume

---

## M. Key Concepts to Master

### Data Engineering
- **ETL:** Extract → Transform → Load
- **Data Quality:** Null handling, duplicates, type validation
- **Fact & Dimension Tables:** Organizing data for analytics
- **Parquet:** Columnar storage format optimized for analytics

### Apache Spark
- **SparkSession:** Entry point for Spark applications
- **DataFrame:** Distributed, immutable table-like structure
- **Lazy Evaluation:** Transformations only execute with `.collect()` or `.write()`
- **Partitioning:** Data split across multiple executors for parallel processing

### SQL
- **SELECT, WHERE, GROUP BY, ORDER BY**
- **Aggregation:** SUM, COUNT, AVG, MAX, MIN
- **Joins:** LEFT, INNER, FULL OUTER
- **Window Functions:** ROW_NUMBER(), RANK(), LAG()

### Databricks
- **Notebooks:** Interactive development environment
- **DBFS:** Distributed file system
- **Jobs:** Scheduled or on-demand workflows
- **SQL Editor:** Query Parquet and Delta tables

---

## N. Recommended Free Resources

### Python
- Real Python: https://realpython.com/
- Python Official Docs: https://docs.python.org/3/

### Apache Spark
- Databricks Academy: https://academy.databricks.com/ (free tier)
- Spark Official Docs: https://spark.apache.org/docs/latest/
- YouTube: "Spark Crash Course" channels

### SQL
- Mode Analytics SQL Tutorial: https://mode.com/sql-tutorial/
- LeetCode SQL: https://leetcode.com/problemset/database/

### Data Engineering
- dbt Learn: https://learn.getdbt.com/
- Fundamentals of Data Engineering (Book)

---

## O. Common Next Steps

After completing this project:

1. **Expand the data:** Add inventory, shipping, returns datasets
2. **Build a dashboard:** Use Streamlit or Dash with Parquet data
3. **Learn Delta Lake:** Use Delta tables instead of Parquet in Databricks
4. **Master SQL:** Write complex window functions and CTEs
5. **Real datasets:** Use public datasets like NYC taxi, AWS OpenData
6. **Real platforms:** Move to production Databricks, AWS S3, or Azure

---

## P. Troubleshooting Checklist

Before asking for help, verify:
- [ ] Python is installed: `python --version`
- [ ] Java is installed: `java -version`
- [ ] Virtual environment is active: `(.venv)` in prompt
- [ ] Dependencies are installed: `pip list | grep pyspark`
- [ ] Raw data files exist: `ls datasets/`
- [ ] Run the pipeline: `python .\src\etl_pipeline.py`
- [ ] Check error output carefully

---

## Q. Getting Help

1. **Setup issues:** See `docs/complete_windows_setup_guide.md`
2. **Code questions:** See `docs/implementation_guide.md`
3. **Databricks:** See `docs/databricks_workflow.md`
4. **Portfolio:** See `docs/github_portfolio_guide.md`
5. **Learning plan:** See `docs/roadmap.md`

---

## R. Final Checklist Before Moving to Databricks

- [ ] ETL pipeline runs locally without errors
- [ ] All tests pass: `pytest tests/ -v`
- [ ] Report is generated: `output/reports/summary_report.txt`
- [ ] Parquet files are created: `output/parquet/`
- [ ] SQL queries work correctly
- [ ] Code is well-commented and documented
- [ ] README.md is complete
- [ ] Project is pushed to GitHub
- [ ] LinkedIn post is published

---

## Next Steps

**Start here based on where you are:**

- **Never used PySpark?** → Read `docs/implementation_guide.md`
- **Need to set up?** → Follow `docs/complete_windows_setup_guide.md`
- **Ready to learn?** → Follow `docs/roadmap.md` (6-week plan)
- **Deploying to Databricks?** → Read `docs/databricks_workflow.md`
- **Building portfolio?** → See `docs/github_portfolio_guide.md`

---

## Success!

When you complete this project, you'll have:
✅ A working ETL pipeline
✅ Real data engineering experience
✅ A GitHub portfolio project
✅ Understanding of Spark and SQL
✅ Databricks knowledge
✅ A resume bullet point that impresses recruiters

---

**Happy learning! 🚀**

Last updated: June 2026
Version: 1.0 (Complete and tested)
