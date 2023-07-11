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

# Using [allure](https://docs.qameta.io/allure/#_manual_installation) to generate test reports

## Setup
1. Download the latest allure package zip file from the [allure framework GitHub](https://github.com/allure-framework/allure2/releases)
   1. Unzip the downloaded zip file
   2. Copy the path until bin file (including bin)
   3. Add it to path environment variable

2. Install [allure-pytest](https://docs.qameta.io/allure/#_pytest) adaptor using pip

```
pip install allure-pytest
```

## Generating reports:
Generate a folder(_automatically named **allure-report**_) to save allure reports using the following command:
```
allure generate
```

1. Run the tests using the following command:
```
pytest --alluredir=allure-report <test_file.py>
```
2. View the allure report previously generated
```
allure serve allure-report
```

### Generate allure-report into one html file
After generating allure-report, when we need to save everything into one html file (to share it); install an external package which builds allure generated folder into one html file:

Requirements: Python 3.6+

```
pip install allure-combine
```

allure-combine [package implementation and documentation](https://github.com/MihanEntalpo/allure-single-html-file)

Then each time after running test, when want to save allure-report in one sharable HTML file:
```
allure generate -c allure-report -o allure-results-html
```
```
allure-combine ./allure-results-html
```

### Pytest useful

Parametrizing test functions using [pytest.fixture()](https://docs.pytest.org/en/7.4.x/how-to/parametrize.html)