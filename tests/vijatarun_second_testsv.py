# tests/run_second_tests.py
%pip install pytest
import pytest
import os
import sys


# Delete all .pyc files
#os.system('find . -name "*.pyc" -delete')

# Run all tests in the repository root.
notebook_path = dbutils.notebook.entry_point.getDbutils().notebook().getContext().notebookPath().get()
repo_root = os.path.dirname(os.path.dirname(notebook_path))
os.chdir(f'/Workspace/{repo_root}')

# Skip writing pyc files on a readonly filesystem.
sys.dont_write_bytecode = True

# Run pytest with verbose output
retcode = pytest.main(["-v"])


# Fail the cell execution if we have any test failures.
assert retcode == 0, 'The pytest invocation failed. See the log above for details.'
