# Databricks notebook source
import shutil
import os

# Define the path to the report file and the DBFS location
report_path = '/Workspace/Repos/ramesh.sadineni@gmail.com/azurerepo/report.html'
local_dbfs_path = '/dbfs/tmp/report.html'

# Verify if the file exists
if os.path.exists(report_path):
    # Copy the file to DBFS local file system
    shutil.copyfile(report_path, local_dbfs_path)

    # Read the file content
    with open(local_dbfs_path, 'r') as file:
        file_content = file.read()

    # Write the file content to DBFS
    dbutils.fs.put("dbfs:/tmp/report.html", file_content, overwrite=True)

    # Generate a download link
    displayHTML(f"<a href='/files/tmp/report.html' target='_blank'>Click here to download the report</a>")
else:
    print("File not found at the specified path.")

# COMMAND ----------

dbutils.fs.cp("dbfs:/tmp/report.html", "dbfs:/FileStore/tmp/report.html")

# COMMAND ----------

displayHTML("<a href='/files/tmp/report.html' target='_blank'>Click here to download the report</a>")


# COMMAND ----------



# COMMAND ----------



# COMMAND ----------

# Display a link to download the report
displayHTML("<a href='/tmp/report.html' target='_blank'>Click here to download the report</a>")

# COMMAND ----------

# List files in the tmp directory to verify the report.html file is there
dbutils.fs.ls("dbfs:/tmp/")

# COMMAND ----------

# Display a link to download the report
displayHTML("<a href='/files/tmp/report.html' target='_blank'>Click here to download the report</a>")

