# Setup pytest sample project using virtual env

1. Install [python](https://www.python.org/downloads/)
2. Install [pip](https://pip.pypa.io/en/stable/installation/#get-pip-py)
3. Create and activate virtual env (using Powershell cmd)
```
python -m venv venv
```

```
.\venv\Scripts\activate
```
4. Install [pytest](https://docs.pytest.org/en/7.4.x/getting-started.html) using pip (having virtual env activated)
```
python -m pip install pytest
```

5. Install [AltTester](https://pypi.org/project/AltTester-Driver/) package using pip

```
pip install AltTester-Driver
```

# Run tests from cmd

In order for pytest to be able to identify test classes, used prefix `test_` for filenames and test functions.
```
pytest
```

Use `-s` in order to see printed output:
```
pytest -s <specific_file.py>
```

In order to run tests which use `unittest` [unit testing framework](https://docs.python.org/3/library/unittest.html)
```
python -m unittest test_recorder.py
```