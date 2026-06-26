"""Report generation for PythonSparks analytics pipeline."""

import os
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from pyspark.sql import SparkSession


def load_parquet(spark: SparkSession, path: str):
    return spark.read.parquet(path)


def render_summary(df, output_path: str) -> None:
    """Generate a text summary report from aggregated metrics."""
    rows = df.collect()
    with open(output_path, "w", encoding="utf-8") as summary_file:
        summary_file.write("PythonSparks eCommerce Analytics Report\n")
        summary_file.write("====================================\n\n")
        summary_file.write("Revenue by Category:\n")
        for row in rows:
            summary_file.write(
                f"- {row['category']}: revenue={row['total_revenue']:.2f}, units={row['total_units']}, margin={row['total_margin']:.2f}\n"
            )

        summary_file.write("\nReport generated with PySpark and local parquet output.\n")


def generate_report(output_dir: str = "output") -> None:
    spark = SparkSession.builder.appName("PythonSparks Report").getOrCreate()
    try:
        metrics_df = load_parquet(spark, os.path.join(output_dir, "parquet", "category_metrics"))
        report_path = os.path.join(output_dir, "reports", "summary_report.txt")
        render_summary(metrics_df, report_path)
        print(f"Report saved to: {report_path}")
    finally:
        spark.stop()


if __name__ == "__main__":
    generate_report()
