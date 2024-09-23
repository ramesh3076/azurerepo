# src/common.py

from pyspark.sql import DataFrame
from pyspark.sql.functions import col, regexp_replace

def remove_extra_spaces(df: DataFrame, column_name: str) -> DataFrame:
    print("testing started")
    return df.withColumn(column_name, regexp_replace(col(column_name), "\\s+", " "))

def filter_senior_citizen(df: DataFrame, age_column: str) -> DataFrame:
    print("testing started")
    return df.filter(col(age_column) >= 60)
