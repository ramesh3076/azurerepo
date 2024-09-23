# Databricks notebook source
from pyspark.sql import DataFrame
from pyspark.sql.functions import col, regexp_replace

def remove_extra_spaces(df: DataFrame, column_name: str):
    print("remove_extra_spaces started")
    return df.withColumn(column_name, regexp_replace(col(column_name), "\\s+", " "))

def filter_senior_citizen(df: DataFrame, age_column: str):
    print("filter_senior_citize started")
    return df.filter(col(age_column) >= 60)

# COMMAND ----------

# Import the required class
from pyspark.sql import SparkSession

def test_senior_citizen_count_negative(spark_session):
    sample_data = [{"name": "John D.", "age": 60},
                   {"name": "Alice G.", "age": 25},
                   {"name": "Bob T.", "age": 65},
                   {"name": "Eve A.", "age": 66}]

    # Create a Spark DataFrame
    original_df = spark_session.createDataFrame(sample_data)

    # Apply the filter function from before
    filtered_df = filter_senior_citizen(original_df, "age")
    display(filtered_df.count())

    expected_data = [{"name": "John D.", "age": 60},
                     {"name": "Bob T.", "age": 65},
                     {"name": "Eve A.", "age": 66}]

    expected_df = spark_session.createDataFrame(expected_data)
    print(expected_df.count())

    filtered_df.count() == expected_df.count()

# Create a SparkSession
spark_session = SparkSession.builder.getOrCreate()

# Call the test_single_space function and pass the spark_session variable
test_senior_citizen_count_negative(spark_session)

# COMMAND ----------

from pyspark.sql import DataFrame
from pyspark.sql.functions import col, regexp_replace

def remove_extra_spaces1(df, column_name):
    print("remove_extra_spaces started")

    df1 = df.withColumn(column_name, regexp_replace(col(column_name), "\\s+", " "))

    return df1



# COMMAND ----------

# Import the required class
from pyspark.sql import SparkSession

# Test Case 1 - Remove Single Space
def test_single_space(spark_session):
    sample_data = [{"name": "John    D.", "age": 30},
                   {"name": "Alice   G.", "age": 25},
                   {"name": "Bob  T.", "age": 35},
                   {"name": "Eve   A.", "age": 28}]

    # Create a Spark DataFrame
    original_df = spark_session.createDataFrame(sample_data)
    
    # Show the DataFrame to verify its creation
    #display(original_df)

    # Apply the transformation function from before
    transformed_df = remove_extra_spaces1(original_df, "name")
    #display(transformed_df)
    

    expected_data = [{"name": "John D.", "age": 30},
                     {"name": "Alice G.", "age": 25},
                     {"name": "Bob T.", "age": 35},
                     {"name": "Eve A.", "age": 28}]

    expected_df = spark_session.createDataFrame(expected_data)
    #display(expected_df)

    transformed_df.collect() == expected_df.collect()
 

# Create a SparkSession
spark_session = SparkSession.builder.getOrCreate()

# Call the test_single_space function and pass the spark_session variable
test_single_space(spark_session)

# COMMAND ----------

# Test Case 1 - Remove Single Space
def test_single_space(spark_session):
    sample_data = [{"name": "John    D.", "age": 30},
                   {"name": "Alice   G.", "age": 25},
                   {"name": "Bob  T.", "age": 35},
                   {"name": "Eve   A.", "age": 28}]

    # Create a Spark DataFrame
    original_df = spark_session.createDataFrame(sample_data)

    # Apply the transformation function from before
    transformed_df = remove_extra_spaces(original_df, "name")

    expected_data = [{"name": "John D.", "age": 30},
                     {"name": "Alice G.", "age": 25},
                     {"name": "Bob T.", "age": 35},
                     {"name": "Eve A.", "age": 28}]

    expected_df = spark_session.createDataFrame(expected_data)

    transformed_df.collect() == expected_df.collect()
    
# Test Case 2 - Row count    
def test_row_count(spark_session):
    sample_data = [{"name": "John    D.", "age": 30},
                   {"name": "Alice   G.", "age": 25},
                   {"name": "Bob  T.", "age": 35},
                   {"name": "Eve   A.", "age": 28}]

    # Create a Spark DataFrame
    original_df = spark_session.createDataFrame(sample_data)

    # Apply the transformation function from before
    transformed_df = remove_extra_spaces(original_df, "name")

    expected_data = [{"name": "John D.", "age": 30},
                     {"name": "Alice G.", "age": 25},
                     {"name": "Bob T.", "age": 35},
                     {"name": "Eve A.", "age": 28}]

    expected_df = spark_session.createDataFrame(expected_data)
    print(expected_df.count())

    transformed_df.count() == expected_df.count()
    
# Test Case 3 - Senior Citizen count   
def test_senior_citizen_count(spark_session):
    sample_data = [{"name": "John D.", "age": 60},
                   {"name": "Alice G.", "age": 25},
                   {"name": "Bob T.", "age": 65},
                   {"name": "Eve A.", "age": 28}]

    # Create a Spark DataFrame
    original_df = spark_session.createDataFrame(sample_data)

    # Apply the filter function from before
    filtered_df = filter_senior_citizen(original_df, "age")

    expected_data = [{"name": "John D.", "age": 60},
                     {"name": "Bob T.", "age": 65}]

    expected_df = spark_session.createDataFrame(expected_data)
    print(expected_df.count())

    filtered_df.count() == expected_df.count()

# Test Case 4 - Senior Citizen count Negative case  
def test_senior_citizen_count_negative(spark_session):
    sample_data = [{"name": "John D.", "age": 60},
                   {"name": "Alice G.", "age": 25},
                   {"name": "Bob T.", "age": 65},
                   {"name": "Eve A.", "age": 66}]

    # Create a Spark DataFrame
    original_df = spark_session.createDataFrame(sample_data)

    # Apply the filter function from before
    filtered_df = filter_senior_citizen(original_df, "age")

    expected_data = [{"name": "John D.", "age": 60},
                     {"name": "Bob T.", "age": 65}]

    expected_df = spark_session.createDataFrame(expected_data)
    print(expected_df.count())

    print(filtered_df.count() == expected_df.count())
