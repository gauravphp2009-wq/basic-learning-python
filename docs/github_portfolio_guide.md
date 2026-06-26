# GitHub Portfolio Guidance

## Repository structure

A clean repo should include:
- `README.md` with the project overview and setup steps
- `datasets/` with sample data used for the pipeline
- `src/` with ETL scripts and notebook examples
- `sql/` with query examples
- `docs/` with learning guides, roadmap, and setup instructions
- `tests/` with automated checks
- `.gitignore` to avoid committing generated output

## README template

Use this structure:
1. project title and summary
2. business problem solved
3. technologies used
4. project structure
5. setup and run commands
6. testing commands
7. Databricks transition notes
8. what you learned

## Screenshots to capture

Capture:
- the project folder structure in VS Code
- Spark application logs in the terminal
- Visual output of the Databricks notebook run
- contents of `output/reports/summary_report.txt`
- SQL query results and chart screenshots (optional)

## How to present the project

### LinkedIn
- publish a short post describing the project goal
- emphasize the transition from PHP backend to Data Engineering
- mention real skills: PySpark, ETL, SQL, Databricks, data quality
- link to your GitHub repo

### Resume
- include a single bullet under "Projects" such as:
  "Built an end-to-end PySpark ETL pipeline for eCommerce sales analytics, including data ingestion, cleaning, aggregation, SQL analysis, and Databricks notebook workflows."
- list technologies: Python, PySpark, Apache Spark, SQL, Databricks, Parquet, Git

## Best practices

- keep code modular and commented
- include both sample data and clear instructions
- use `tests/` to show automation
- name files and folders consistently
- document Windows-specific setup when your audience may use Windows
