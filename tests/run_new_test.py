#%pip install pytest
import pytest
import os
import sys
import shutil

# 1. Ensure pytest cache is fully cleared
os.system('pytest --cache-clear')

# 2. Delete all .pyc files to avoid conflicts from previous runs
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.pyc'):
            os.remove(os.path.join(root, file))

# 3. Skip writing .pyc files on a readonly filesystem
sys.dont_write_bytecode = True

# 4. Change the working directory to the repo root
repo_root = '/Workspace/Repos/ramesh.sadineni@gmail.com/azurerepo'  # Adjust the path if needed
os.chdir(repo_root)

# 5. Remove the previous HTML report if it exists
if os.path.exists('report.html'):
    os.remove('report.html')

# 6. Optionally remove the cached test results
if os.path.exists('.pytest_cache'):
    shutil.rmtree('.pytest_cache')

# 7. Define pytest options
pytest_options = ["--cache-clear", "-v", "-s", "--lf"]
#pytest_options = ["--cache-clear", "-v", "-s", "--ff"] first run failed tests and after again will run remaining tests
# 8. Run pytest with the specified options and ensure fresh results
retcode = pytest.main(pytest_options)

# 9. Print retcode for debugging
print(f"Return code: {retcode}")

# 10. Fail the script if any test failures occur
assert retcode == 0, 'The pytest invocation failed. See the log above for details.'

# # 11. Define the path to the new HTML report and DBFS location
# local_report_path = 'report.html'  # The new report path
# dbfs_report_path = '/dbfs/tmp/report.html'  # DBFS location

# # 12. Copy the fresh report to DBFS for download
# shutil.copyfile(local_report_path, dbfs_report_path)

# # 13. Provide a new download link for the report
# displayHTML("<a href='/files/tmp/report.html' target='_blank'>Click here to download the latest report</a>")
