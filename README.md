# PythonSparks: Data Engineering Portfolio Project

A complete, beginner-friendly **end-to-end Data Engineering project** for PHP/Laravel developers transitioning to data engineering using **Python, PySpark, SQL, and Databricks**.

## 🎯 What is This?

PythonSparks is a realistic eCommerce analytics pipeline that teaches you:
- **Data Ingestion:** Loading CSV and JSON datasets with PySpark
- **Data Cleaning:** Type casting, null handling, deduplication
- **Data Transformation:** Multi-table joins and computed columns
- **Data Aggregation:** GROUP BY, SUM, and business metrics
- **SQL Analytics:** Real-world queries for insights
- **ETL Orchestration:** Building end-to-end workflows
- **Reporting:** Generating business-ready reports
- **Databricks Deployment:** Moving to cloud infrastructure

## 🚀 Quick Start

```powershell
# 1. Navigate to project
cd d:\wamp\www\PythonSparks

# 2. Create and activate virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 3. Install dependencies
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# 4. Validate setup (no Java required)
python validate_setup.py

# 5. Run the ETL pipeline (requires Java/JAVA_HOME set)
python src/etl_pipeline.py

# 6. Generate report
python src/report.py

# 7. Run tests
pytest tests/ -v
```

## 📚 Documentation

| Document | Purpose |
|----------|---------|
| **[MASTER_GUIDE.md](docs/MASTER_GUIDE.md)** | 👈 **Start here!** Overview, learning path, all concepts |
| **[QUICKSTART.md](QUICKSTART.md)** | Command reference for Windows 11 |
| **[complete_windows_setup_guide.md](docs/complete_windows_setup_guide.md)** | Detailed Windows setup with troubleshooting |
| **[implementation_guide.md](docs/implementation_guide.md)** | Detailed explanation of each code module |
| **[roadmap.md](docs/roadmap.md)** | 6-week learning plan with weekly goals |
| **[databricks_workflow.md](docs/databricks_workflow.md)** | Deploying to Databricks Community Edition |
| **[github_portfolio_guide.md](docs/github_portfolio_guide.md)** | GitHub, resume, and LinkedIn tips |

## 📁 Project Structure

```
PythonSparks/
├── MASTER_GUIDE.md              # Start here!
├── QUICKSTART.md                # Command reference
├── validate_setup.py            # Setup verification (no Java needed)
├── requirements.txt             # Python dependencies
├── README.md                    # This file
│
├── datasets/                    # Sample data (CSV, JSON)
├── src/                         # ETL code (ingestion, cleaning, transformation)
├── sql/                         # SQL query examples
├── notebooks/                   # Databricks notebook template
├── docs/                        # Setup, learning, deployment guides
├── tests/                       # Automated tests (pytest)
└── output/                      # Generated parquet and reports
```

## 💡 What You'll Learn

### Concepts
- Apache Spark and distributed computing fundamentals
- PySpark DataFrames and SQL
- ETL pipeline design and implementation
- Data quality validation and testing
- Parquet format and columnar storage
- Databricks platform and cloud workflows

### Skills
- Writing production-quality ETL code
- Debugging data pipelines
- Testing with pytest
- Using Git and GitHub for portfolio projects
- Presenting technical projects professionally

## ⚙️ System Requirements

- **Python 3.11+**
- **Java 17+** (required for running Spark, optional for setup validation)
- **Windows 11** (or any Windows version with PowerShell)
- ~5GB free disk space (for PySpark and dependencies)

## 🏗️ Project Highlights

### Realistic Business Problem
Model an eCommerce company's sales pipeline: ingest orders, join customer and product data, validate data quality, compute revenue metrics.

### Complete Data Pipeline
- **Ingestion:** Read CSV sales and products, JSON customers and orders
- **Cleaning:** Type casting, normalization, filtering invalid rows
- **Transformation:** Multi-table joins, computed columns (gross_margin)
- **Aggregation:** Revenue by category, top customers, trends
- **Output:** Parquet format for efficient analytics

### Production-Ready Code
- Modular design with separate ingestion, cleaning, transformation modules
- Comprehensive error handling
- Well-commented and documented
- Automated tests with pytest

### Multiple Deployment Options
- Run locally on Windows with PySpark
- Deploy to Databricks with notebooks and jobs
- Scalable to real data volumes

## 🎓 Learning Path

**Week 1-2:** Python, virtual environments, Spark basics
**Week 3-4:** Data cleaning, ETL design, SQL analytics
**Week 5-6:** Databricks, reporting, portfolio preparation

See [roadmap.md](docs/roadmap.md) for detailed weekly curriculum.

## ⚠️ WAMP Server Note

WAMP is **not required** for this project. PySpark and Python run independently from your Apache/MySQL/PHP stack. You can safely keep this project in `d:\wamp\www\PythonSparks` alongside your PHP projects—they don't interfere with each other.

## 🆘 Having Issues?

1. **Setup validation:** Run `python validate_setup.py` (no Java needed)
2. **Java installation:** Check [complete_windows_setup_guide.md](docs/complete_windows_setup_guide.md#1-verify-python-and-java)
3. **Commands not working:** See [QUICKSTART.md](QUICKSTART.md#fixing-common-issues)
4. **Code questions:** Read [implementation_guide.md](docs/implementation_guide.md)
5. **Stuck?** Check [MASTER_GUIDE.md](docs/MASTER_GUIDE.md#h-debugging-common-issues)

## 📊 Next Steps After Setup

1. ✅ Validate setup: `python validate_setup.py`
2. ✅ Run pipeline: `python src/etl_pipeline.py`
3. ✅ Read code: Review `src/clean_transform.py`
4. ✅ Follow roadmap: 6-week learning plan in `docs/roadmap.md`
5. ✅ Deploy to Databricks: See `docs/databricks_workflow.md`
6. ✅ Share on GitHub: See `docs/github_portfolio_guide.md`

## 📈 Portfolio & Career

This project demonstrates:
- ✅ End-to-end ETL pipeline design
- ✅ PySpark and SQL proficiency
- ✅ Data validation and quality
- ✅ Production code practices
- ✅ Cloud platform knowledge (Databricks)
- ✅ Professional documentation and presentation

Perfect for your portfolio and resume. See [github_portfolio_guide.md](docs/github_portfolio_guide.md) for tips.

## 🤝 Contributing & Feedback

Suggestions for improvements? Create an issue or pull request. Feedback helps make this project better for others!

## 📝 License

This project is open-source and free to use for learning purposes.

---

**Ready?** Start with [MASTER_GUIDE.md](docs/MASTER_GUIDE.md) 👈
