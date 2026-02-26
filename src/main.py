from pyspark.sql import SparkSession
import os
from pyspark.sql.functions import col

def main():
    spark = SparkSession.builder.getOrCreate()

    catalog = os.getenv("catalog")
    schema = os.getenv("schema")

    spark.sql(f"USE CATALOG {catalog}")
    spark.sql(f"USE SCHEMA {schema}")

    spark.sql("""
        CREATE TABLE IF NOT EXISTS sample_table (
            id INT,
            name STRING
        )
    """)