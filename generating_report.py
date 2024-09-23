# Databricks notebook source
import shutil
import os

# Define paths
report_path = '/Workspace/Repos/ramesh.sadineni@gmail.com/azurerepo/report.html'
local_dbfs_path = '/dbfs/tmp/report.html'

# Check if the report file exists
if os.path.exists(report_path):
    # Copy the file to DBFS
    shutil.copyfile(report_path, local_dbfs_path)
    print("File copied to DBFS.")

    # Confirm the file is in DBFS
    print(dbutils.fs.ls("dbfs:/tmp/"))  # List files in /tmp directory

    # Generate a download link
    displayHTML("<a href='/files/tmp/report.html' target='_blank'>Click here to download the report</a>")
else:
    print("Report file not found.")

