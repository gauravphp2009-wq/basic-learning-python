#!/usr/bin/env python
"""
Setup validation script for PythonSparks.

Verifies that all Python packages are installed and project structure is correct.
Doesn't require Java/Spark to start (can be run on any system for import testing).
"""

import sys
import os
from pathlib import Path


def check_python_version():
    """Verify Python 3.11 or later is installed."""
    if sys.version_info < (3, 11):
        print(f"❌ Python 3.11+ required. You have {sys.version_info.major}.{sys.version_info.minor}")
        return False
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} installed")
    return True


def check_project_structure():
    """Verify all required directories and files exist."""
    required_dirs = ["datasets", "src", "tests", "sql", "docs", "notebooks"]
    required_files = ["README.md", "requirements.txt", ".gitignore"]
    
    all_good = True
    
    for dir_name in required_dirs:
        if os.path.isdir(dir_name):
            print(f"✅ {dir_name}/ exists")
        else:
            print(f"❌ {dir_name}/ missing")
            all_good = False
    
    for file_name in required_files:
        if os.path.isfile(file_name):
            print(f"✅ {file_name} exists")
        else:
            print(f"❌ {file_name} missing")
            all_good = False
    
    return all_good


def check_data_files():
    """Verify sample datasets are available."""
    required_data = [
        "datasets/sales.csv",
        "datasets/customers.json",
        "datasets/products.csv",
        "datasets/orders.json",
    ]
    
    all_good = True
    for data_file in required_data:
        if os.path.isfile(data_file):
            size = os.path.getsize(data_file)
            print(f"✅ {data_file} ({size} bytes)")
        else:
            print(f"❌ {data_file} missing")
            all_good = False
    
    return all_good


def check_python_packages():
    """Verify required Python packages are installed."""
    packages = ["pyspark", "pandas", "pytest"]
    all_good = True
    
    for package in packages:
        try:
            __import__(package)
            print(f"✅ {package} installed")
        except ImportError:
            print(f"❌ {package} not installed")
            all_good = False
    
    return all_good


def check_source_code():
    """Verify main source modules can be imported."""
    try:
        from src.ingest import create_spark_session, read_csv_data
        print("✅ src.ingest imports successfully")
    except ImportError as e:
        print(f"❌ src.ingest import failed: {e}")
        return False
    
    try:
        from src.clean_transform import clean_sales, build_business_facts
        print("✅ src.clean_transform imports successfully")
    except ImportError as e:
        print(f"❌ src.clean_transform import failed: {e}")
        return False
    
    return True


def main():
    """Run all validation checks."""
    print("\n" + "=" * 60)
    print("PythonSparks Setup Validation")
    print("=" * 60 + "\n")
    
    checks = [
        ("Python Version", check_python_version),
        ("Project Structure", check_project_structure),
        ("Data Files", check_data_files),
        ("Python Packages", check_python_packages),
        ("Source Code", check_source_code),
    ]
    
    results = []
    for check_name, check_func in checks:
        print(f"\n{check_name}:")
        print("-" * 60)
        try:
            result = check_func()
            results.append((check_name, result))
        except Exception as e:
            print(f"❌ Error during check: {e}")
            results.append((check_name, False))
    
    # Summary
    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)
    
    all_passed = all(result for _, result in results)
    
    for check_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status}: {check_name}")
    
    print()
    if all_passed:
        print("✅ All checks passed! Your project is ready.")
        print("\nNext steps:")
        print("1. Set JAVA_HOME environment variable if not done")
        print("2. Run: python src/etl_pipeline.py")
        print("3. Run: python src/report.py")
        print("4. Run: pytest tests/ -v")
        return 0
    else:
        print("❌ Some checks failed. Review the output above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
