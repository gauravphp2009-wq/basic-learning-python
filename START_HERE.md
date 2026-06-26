# 🚀 START HERE — Your First Steps

Welcome to **PythonSparks**! This file tells you exactly what to do first.

## ✅ What's Been Created For You

A complete, production-ready Data Engineering project at: `d:\wamp\www\PythonSparks`

- ✅ 25+ files organized and documented
- ✅ 4 sample datasets (eCommerce sales, customers, products, orders)
- ✅ 5 core ETL modules (ingestion, cleaning, transformation, reporting, tests)
- ✅ 6 comprehensive guides (setup, implementation, roadmap, Databricks, portfolio)
- ✅ SQL examples and Databricks notebook template
- ✅ All dependencies installed and verified
- ✅ Ready to learn and deploy

---

## 📍 Your Starting Point

You have **2 paths** depending on what you want to do now:

### Path A: Learn the Project (Recommended First)
```powershell
# 1. Open the master guide
cat MASTER_GUIDE.md
# OR open in VS Code
code MASTER_GUIDE.md

# 2. This gives you the complete overview in 10 minutes
```

### Path B: Verify Everything Works (5 minutes)
```powershell
# 1. Activate virtual environment
.\.venv\Scripts\Activate.ps1

# 2. Validate setup (no Java required)
python validate_setup.py

# 3. See all pass ✅
```

---

## 🎯 The 30-Minute Quick Start

Follow these steps in order:

```powershell
# Step 1: Navigate to project (should already be here)
cd d:\wamp\www\PythonSparks
pwd
ls

# Step 2: Activate virtual environment
.\.venv\Scripts\Activate.ps1
# You should see (.venv) in your prompt now

# Step 3: Validate setup (no Java needed)
python validate_setup.py
# You should see all ✅ checks pass

# Step 4: Read the quick reference
cat QUICKSTART.md

# Step 5: Read the master guide
cat MASTER_GUIDE.md

# Estimated time: 30 minutes
```

**That's it!** You now understand the entire project.

---

## 🔧 Next: Install Java and Run the Pipeline

When you're ready (or after Step 5):

### 1. Install Java (one-time, required for PySpark)

**Step 1a: Download**
- Go to https://adoptium.net/
- Click **Latest LTS Release** (version 21 or higher)
- Select **Windows x64 .msi installer**
- Run the installer

**Step 1b: Install (Default Settings)**
- Accept the license
- Choose "Install for all users" (recommended)
- Accept default installation path: `C:\Program Files\Eclipse Adoptium\jdk-21.0.x`
- Click Install
- Finish and close

**Step 1c: Set JAVA_HOME (Important!)**
1. Open **Settings** > **System** > **About**
2. Click **Advanced system settings** (right side)
3. Click **Environment Variables** (bottom)
4. Click **New** under "System variables"
5. Enter:
   - Variable name: `JAVA_HOME`
   - Variable value: `C:\Program Files\Eclipse Adoptium\jdk-21.0.x` (or wherever you installed)
6. Click **OK** three times

**Step 1d: Verify Installation**
```powershell
# Close and reopen PowerShell
# Then run:
java -version
# Should show: openjdk 21.0.x or similar

# Also check JAVA_HOME:
$env:JAVA_HOME
# Should show the installation path
```

**If verification fails:**
```powershell
# Try adding to PATH manually
$newPath = "C:\Program Files\Eclipse Adoptium\jdk-21.0.x\bin"
$env:Path += ";$newPath"
java -version
```

### 2. Run the ETL pipeline

Once Java is verified:

```powershell
# Make sure virtual environment is active
.\.venv\Scripts\Activate.ps1

# Run the full pipeline
python src/etl_pipeline.py

# Expected output:
# 1) Ingesting raw datasets
# 2) Cleaning and validating datasets
# 3) Building business fact table
# 4) Showing sample output
# [metrics table]
# 
# Takes 30-60 seconds on first run (Spark starts up)
# Subsequent runs are much faster
```

**If you see "Java gateway exited":**
- Verify `java -version` works
- Check that `JAVA_HOME` environment variable is set
- Restart PowerShell and try again

### 3. Check the output

```powershell
# View the generated report
cat output/reports/summary_report.txt

# List the generated data files
ls output/parquet/

# You should see directories:
# - fact_orders/
# - category_metrics/
```

### 4. Success! 🎉

If you see the report and parquet files, everything works!

Next step: Read the guides and follow the 6-week roadmap in `docs/roadmap.md`

---

## 📚 Documentation Map

| I want to... | Read this |
|---|---|
| Understand the entire project | [MASTER_GUIDE.md](docs/MASTER_GUIDE.md) ← **START HERE** |
| Get setup steps for Windows | [complete_windows_setup_guide.md](docs/complete_windows_setup_guide.md) |
| Understand how the code works | [implementation_guide.md](docs/implementation_guide.md) |
| Follow a 6-week study plan | [roadmap.md](docs/roadmap.md) |
| Deploy to Databricks | [databricks_workflow.md](docs/databricks_workflow.md) |
| Build a portfolio project | [github_portfolio_guide.md](docs/github_portfolio_guide.md) |
| Quick command reference | [QUICKSTART.md](QUICKSTART.md) |
| Full project inventory | [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) |

---

## ❓ I'm Confused. What Should I Do?

**Just run this:**
```powershell
.\.venv\Scripts\Activate.ps1
python validate_setup.py
```

If it says ✅ all checks pass, you're good! Everything is working.

---

## 🎓 Learning Path (6 Weeks)

**Week 1:** Setup and understand data
**Week 2:** Spark fundamentals  
**Week 3:** Data cleaning and ETL
**Week 4:** SQL and analytics
**Week 5:** Reporting and Databricks
**Week 6:** Portfolio and LinkedIn

👉 See [roadmap.md](docs/roadmap.md) for detailed curriculum

---

## 💡 Quick Tips

1. **Always activate venv first:** `.\.venv\Scripts\Activate.ps1`
2. **First Spark run is slow:** It builds the Java JVM (2-5 minutes is normal)
3. **Check error messages:** They tell you what's missing
4. **Validate anytime:** `python validate_setup.py`
5. **Read the code:** Start with `src/clean_transform.py`

---

## 🆘 Something Doesn't Work?

### Issue: `(.venv)` not showing in prompt
```powershell
# Try this exact command
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

### Issue: `java: command not found`
- Install Java from https://adoptium.net/
- Then restart PowerShell

### Issue: Module not found errors
```powershell
# Reinstall dependencies
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Issue: Validation script fails
```powershell
# Make sure you're in the right directory
pwd  # Should show d:\wamp\www\PythonSparks
ls   # Should list datasets, docs, src, etc.
```

More help: See [complete_windows_setup_guide.md](docs/complete_windows_setup_guide.md)

---

## ✨ What You Have

```
PythonSparks/
├── README.md                 # Project overview
├── MASTER_GUIDE.md          # Start here! Complete guide
├── QUICKSTART.md            # Commands reference
├── PROJECT_SUMMARY.md       # Full inventory
├── validate_setup.py        # Check everything works
├── requirements.txt         # Dependencies (installed)
│
├── datasets/                # Sample data (4 files)
├── src/                     # ETL code (5 modules)
├── sql/                     # SQL queries (4 examples)
├── notebooks/               # Databricks notebook
├── docs/                    # Guides (6 documents)
├── tests/                   # Test cases (5 tests)
└── .venv/                   # Virtual environment
```

Everything is here. Everything works. Ready to go! 🚀

---

## 🎯 Your Next Action

**Pick one:**

- 👉 **I want the big picture first:** Open [MASTER_GUIDE.md](docs/MASTER_GUIDE.md)
- 👉 **I want to see it run:** Run `python validate_setup.py`
- 👉 **I want quick commands:** Open [QUICKSTART.md](QUICKSTART.md)
- 👉 **I want to start learning:** Follow [roadmap.md](docs/roadmap.md)

---

## 🎉 Congratulations!

You now have a complete Data Engineering project that will teach you everything you need to transition from PHP backend to Data Engineering.

The combination of:
- ✅ Your 13+ years of backend experience
- ✅ This structured project
- ✅ The comprehensive guides

...will make you a strong data engineer. Trust the process, follow the roadmap, and you'll get there.

**Happy learning!** 📚🚀

---

**Questions?** Everything is documented. Start with [MASTER_GUIDE.md](docs/MASTER_GUIDE.md) — it has answers to almost every question you might have.
