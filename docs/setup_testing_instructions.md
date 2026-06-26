# Setup and Testing Instructions for Windows 11

## 1) Project folder location

You can keep the project in:
- `d:\wamp\www\PythonSparks`
- or a dedicated directory such as `d:\projects\PythonSparks`

Because you already use WAMP, keep this project separate from PHP code if you want a clean workspace.

## 2) WAMP and this project

- WAMP is not required for this project.
- Python, PySpark, and Databricks run independently of Apache, MySQL, and PHP.
- Use WAMP only if you later build a dashboard or API that needs a local web server.
- Localhost can serve a static HTML report or a separate Flask app, but it is not needed for ETL.

## 3) Install Python and Java

### Python
1. Download Python 3.11 or 3.12 from https://www.python.org/downloads/windows/
2. Enable `Add Python to PATH` during install.
3. Verify in PowerShell or VS Code terminal:

```powershell
python --version
```

### Java for PySpark
1. Install OpenJDK 17 or 21 from https://adoptium.net/
2. Set `JAVA_HOME` in Windows Environment Variables.
3. Verify:

```powershell
java -version
```

## 4) Create and activate a virtual environment

```powershell
cd d:\wamp\www\PythonSparks
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks the script, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

## 5) Install dependencies

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## 6) Run PySpark locally in VS Code terminal

```powershell
python .\src\etl_pipeline.py
```

If Spark starts successfully, you should see a Spark UI log and summary output.

## 7) Run SQL scripts locally

This project uses Spark SQL through the PySpark workflow. Use the SQL query file for Databricks or a local Spark SQL session.

Example commands for a Spark shell are covered in `docs/implementation_guide.md`.

## 8) Execute ETL jobs from VS Code terminal

```powershell
python .\src\etl_pipeline.py
python .\src\report.py
```

## 9) Verify ingestion and transformations

- Confirm `output/parquet/fact_orders` exists after ETL.
- Confirm `output/parquet/category_metrics` exists.
- Confirm `output/reports/summary_report.txt` is created.

## 10) Common debug steps

- Check `JAVA_HOME` and `python --version`
- Activate the virtual environment before installing or running
- If Spark errors occur, install a matching Java JDK version
- If JSON load fails, check for valid JSON lines in `datasets/*.json`
