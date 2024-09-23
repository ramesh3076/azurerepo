# tests/conftest.py

import sys

# Prevent Python from writing .pyc files
sys.dont_write_bytecode = True

import pytest
from pyspark.sql import SparkSession

@pytest.fixture(scope="session")
def spark_session():
    spark = SparkSession \
        .builder \
        .appName("Spark Unit Test") \
        .master("local[*]") \
        .getOrCreate()

    return spark



