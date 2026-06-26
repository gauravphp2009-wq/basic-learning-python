# Quick Command Reference for Windows 11

## Initial Setup (One-time)

```powershell
# Navigate to project
cd d:\wamp\www\PythonSparks

# Create virtual environment
python -m venv .venv

# Activate it
.\.venv\Scripts\Activate.ps1

# Upgrade pip
python -m pip install --upgrade pip

# Install dependencies
python -m pip install -r requirements.txt
```

## Regular Workflow

```powershell
# Always start by activating the virtual environment
.\.venv\Scripts\Activate.ps1

# Validate setup (no Java required)
python validate_setup.py

# Run the complete ETL pipeline
python src/etl_pipeline.py

# Generate a report
python src/report.py

# Run automated tests
pytest tests/ -v

# View the generated report
cat output/reports/summary_report.txt

# Deactivate when done
deactivate
```

## Fixing Common Issues

```powershell
# PowerShell blocks script execution
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

# Reinstall dependencies
python -m pip install --upgrade pip
python -m pip install -r requirements.txt --force-reinstall

# Check Python version
python --version

# Check Java installation
java -version

# Clear Spark temporary files (if issues persist)
rmdir -r "C:\Users\$env:USERNAME\AppData\Local\Temp\spark-*" -Force

# Run only a subset of tests
pytest tests/test_etl_pipeline.py::test_clean_sales_filters_invalid_rows -v
```

## Exploring the Data

```powershell
# Open a Python interactive shell
python

# Then in Python:
from src.ingest import create_spark_session, read_csv_data
spark = create_spark_session()
sales = read_csv_data(spark, "datasets/sales.csv")
sales.show(5)
sales.printSchema()
spark.stop()
```

## Environment Variables (Windows)

Set JAVA_HOME if Java is installed:

1. Open "Edit the system environment variables" (System Properties)
2. Click "Environment Variables..."
3. Click "New..." under System variables
4. Variable name: `JAVA_HOME`
5. Variable value: `C:\Program Files\Eclipse Adoptium\jdk-21.0.x` (or your JDK path)
6. Click OK and restart terminal

Verify:
```powershell
$env:JAVA_HOME
echo %JAVA_HOME%
```

## File Locations

```powershell
# Project root
d:\wamp\www\PythonSparks

# Source code
d:\wamp\www\PythonSparks\src

# Raw data
d:\wamp\www\PythonSparks\datasets

# Generated outputs
d:\wamp\www\PythonSparks\output\parquet    # Parquet data files
d:\wamp\www\PythonSparks\output\reports    # Generated reports

# Tests
d:\wamp\www\PythonSparks\tests
```

## Documentation Navigation

| Document | Purpose | When to Read |
|----------|---------|----------|
| MASTER_GUIDE.md | Overview and learning path | First! |
| complete_windows_setup_guide.md | Detailed Windows setup | Setup issues |
| implementation_guide.md | Explanation of code | Learning code structure |
| roadmap.md | 6-week study plan | Planning your learning |
| databricks_workflow.md | Moving to Databricks | Ready to use cloud |
| github_portfolio_guide.md | Portfolio and resume | Before publishing |

## Project Verification Checklist

After setup, verify everything works:

```powershell
# 1. Validation script passes
python validate_setup.py

# 2. Can import Spark (but may fail without Java)
python -c "from pyspark.sql import SparkSession; print('PySpark OK')"

# 3. Data files exist and are readable
Get-ChildItem datasets/
Get-Content datasets/sales.csv | Select-Object -First 3

# 4. All tests can at least load (even if Spark tests skip)
pytest tests/ --collect-only

# 5. Source code has no syntax errors
python -m py_compile src/etl_pipeline.py
python -m py_compile src/clean_transform.py
python -m py_compile src/ingest.py
python -m py_compile src/report.py
```

## Tips for Success

1. **Always activate the virtual environment first:** `(. .\.venv\Scripts\Activate.ps1)`
2. **Java takes time:** First Spark run is slow (building JVM). Wait 2-5 minutes.
3. **Check error messages carefully:** They tell you what's missing.
4. **Restart terminal after environment variable changes**
5. **Use `.show()` to preview data:** `df.show(5)` shows first 5 rows
6. **Use `.count()` to check row counts:** `df.count()` before and after cleaning
7. **Tests are your friend:** `pytest` confirms everything works
8. **Check output files:** `ls output/parquet/` and `ls output/reports/`

## Learning Progression

Start here → MASTER_GUIDE.md
Then → Complete project validation
Then → Run ETL pipeline
Then → Read implementation_guide.md
Then → Follow roadmap.md
Finally → Deploy to Databricks

## Staying Organized

```powershell
# Keep track of your changes
git init
git add .
git commit -m "Initial project setup"

# Check status
git status

# View changes
git log --oneline

# Before pushing to GitHub, create .gitignore entries for:
.venv/
__pycache__/
*.pyc
output/
.pytest_cache/
```

## Deactivating and Returning

```powershell
# When done for the day
deactivate

# Next time you work on the project
cd d:\wamp\www\PythonSparks
.\.venv\Scripts\Activate.ps1
python src/etl_pipeline.py
```

---

**Need more help?** See the guides in `docs/` folder.
