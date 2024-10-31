# Pytest Automation Setup

This guide will help you set up a Pytest-based testing environment and run your tests efficiently.

## Prerequisites

Ensure you have Python installed on your system. You can check this by running:

```bash
python --version
```

## Installation Steps

1. **Install Pytest**  
   Install the latest version of Pytest with the command:
   ```bash
   pip install pytest
   ```
   Or, specify a version:
   ```bash
   pip install pytest==5.4.3
   ```

2. **List Installed Packages**  
   To see all installed packages in your Python environment:
   ```bash
   pip list
   ```

3. **Freeze Requirements**  
   Save the current list of packages in `requirements.txt`:
   ```bash
   pip freeze > requirements.txt
   ```

## Naming Conventions for Tests

- **Test Modules (Files)**: Name test files as `test_<name>.py` or `<name>_test.py`.
- **Test Functions**: Use `test_<name>` for naming functions.
- **Test Classes**: Use `Test<Name>` for naming classes.

Group related tests within test classes and package them appropriately by including an `__init__.py` file in each directory.

## Running Tests

To run tests, use the `pytest` command followed by the directory or file name:

```bash
pytest <folder-name>
pytest <file-name>
```

> **Note**: Enable your virtual environment if running from the command line.

### Common Pytest Options

- `-v` (Verbose Mode): Increases verbosity for detailed outputs.
- `--lf` or `--last-failed`: Only reruns tests that failed last time.
- `--ff` or `--failed-first`: Runs the failed tests first, then the rest.


## Writing and Validating Tests

### Assertions

Assertions are essential for validating the outcomes of tests. Here are some guidelines:

- Use operators like `==`, `!=`, `<=`, and `>=` for comparisons in assertions.
- Assert a condition to be `True` with `assert 1` or `False` with `assert 0` (fails the test).
- Use `assert in` to check if a value exists within a list, tuple, or string.
- **Best Practice**: Aim to use only one `assert` per test for clarity.

### Test Discovery

Pytest automatically discovers tests:

- Running `pytest` without arguments searches in the current directory and subdirectories.
- Specifying files or directories (e.g., `pytest <filename>`) restricts discovery to those locations.
- Ensure directories are recognized as Python packages by including an `__init__.py` file.

### Handling Expected Exceptions

For tests expected to raise exceptions, use `pytest.raises`:

```python
import pytest

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        1 / 0
```

In this case, the test will pass if the specified exception (`ZeroDivisionError`) is raised, which is useful for negative test cases.


## Managing Test Execution

### Skipping Tests

Skip tests that are not applicable or need conditional execution.

- **Simple skip**: Skip a test unconditionally:
  ```python
  @pytest.mark.skip()
  ```
- **Conditional skip**: Skip based on a condition:
  ```python
  @pytest.mark.skipif(condition)
  ```
- **Skip entire module**: Skip all tests in a module with:
  ```python
  pytestmark = pytest.mark.skipif(condition)
  ```

### Markers for Test Grouping

Use markers to categorize and selectively run tests. Common examples:

- Mark a test with a specific label, like `sanity` or `uitest`:
  ```python
  @pytest.mark.sanity
  ```
- To run only tests marked as `sanity`:
  ```bash
  pytest -m sanity
  ```

Markers also support logical operators like `and`, `or`, and `not` for complex test selection:
```bash
pytest -m "sanity and uitest"
```

> **Note**: Define all custom markers in `pytest.ini` to avoid warnings.

### Expecting Failures (`xfail`)

Mark tests expected to fail, useful for known issues or unimplemented features:

- Basic usage:
  ```python
  @pytest.mark.xfail
  ```
- Expect a failure based on a condition:
  ```python
  @pytest.mark.xfail(condition)
  ```
- Use `raises` for specific exceptions:
  ```python
  @pytest.mark.xfail(raises=IndexError)
  ```

When a test passes unexpectedly, `pytest` will show an `XPASS` result, otherwise `XFAIL` for expected failures.

### Running Tests by Name

Run tests based on partial or full name matching with the `-k` option:
```bash
pytest -k "test_name_part"
```
You can use `and`, `or`, and `not` in the expression for refined selection.

### Common Command-Line Options

Use `pytest --help` to view all available options. Some useful ones include:

- `-m MARKEXPR`: Run tests matching a mark expression.
- `-x` or `--exitfirst`: Stop after the first failure.
- `--maxfail=num`: Stop after a specific number of failures.
- `-q` or `--quiet`: Decrease verbosity.
- `--tb=no`: Suppress traceback for errors.
- `--collect-only`: Only collect tests without executing them.

### Test Outcomes

- `PASSED` (.): Test passed.
- `FAILED` (F): Test failed.
- `SKIPPED` (s): Test was skipped.
- `XFAIL` (x): Expected failure, test ran and failed.
- `XPASS` (X): Unexpectedly passed.
- `ERROR` (E): An error occurred outside the test function.

## Advanced Testing Techniques

### Parameterized Tests

Parameterized tests allow you to run the same test multiple times with different input values, which is ideal for data-driven testing.

Example:
```python
import pytest

@pytest.mark.parametrize("test_input, expected", [("5+5", 10), ("5-5", 0), ("7*8", 56)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected
```

### Fixtures

Fixtures provide a setup for tests by preparing the necessary data or state before each test. Common uses include setting up a database connection or initializing a web driver.

- **Creating a fixture**:
  ```python
  import pytest

  @pytest.fixture()
  def sample_data():
      return {"key": "value"}
  ```

- **Using a fixture**: Add it as a parameter to your test function:
  ```python
  def test_data(sample_data):
      assert sample_data["key"] == "value"
  ```

- **Defining shared fixtures**: Place them in `conftest.py` to make them accessible across multiple test files without imports.

### Setup and Teardown with Fixtures

Use `yield` in fixtures to define teardown code, which runs after the test:
```python
@pytest.fixture()
def resource_setup_teardown():
    setup_resource = "resource setup"
    yield setup_resource  # Teardown code runs after yield
    print("Teardown resource")
```

### Fixture Scopes

Fixture scope determines its lifespan:
- **Function**: Default, runs once per test function.
- **Class**: Runs once per test class.
- **Module**: Runs once per module.
- **Session**: Runs once per test session.

### Parameterizing Fixtures

You can parameterize fixtures to run tests with multiple sets of data:
```python
@pytest.fixture(params=[1, 2, 3])
def number(request):
    return request.param
```

### Tracing Fixtures

To view fixture setup, run Pytest with `--setup-show`:
```bash
pytest --setup-show
```

## Advanced Testing Techniques

### 1. Parameterized Tests

Parameterized tests allow you to reuse the same test with different data inputs, which is great for data-driven testing.

**Example**:
```python
import pytest

@pytest.mark.parametrize("number, expected", [(2, 4), (3, 9), (4, 16)])
def test_square(number, expected):
    assert number ** 2 == expected
```

### 2. Fixtures

Fixtures set up any required resources before a test and clean them up afterward. They make tests more modular and reusable.

**Basic Fixture Example**:
```python
import pytest

@pytest.fixture
def sample_data():
    return {"name": "Alice", "age": 30}

def test_sample_data(sample_data):
    assert sample_data["name"] == "Alice"
    assert sample_data["age"] == 30
```

**Fixture with Teardown**:
Using `yield` in a fixture allows you to specify teardown steps to be run after the test completes.
```python
@pytest.fixture
def db_connection():
    conn = "Database Connection Established"
    yield conn
    print("Closing Database Connection")

def test_db(db_connection):
    assert db_connection == "Database Connection Established"
```

### 3. Fixture Scope

Fixture scope determines how often a fixture is run:
- **Function**: Runs once per test.
- **Class**: Runs once per test class.
- **Module**: Runs once per module.
- **Session**: Runs once per test session.

**Example with Class Scope**:
```python
@pytest.fixture(scope="class")
def setup_once():
    return "Setup done once per class"

class TestExample:
    def test_first(self, setup_once):
        assert setup_once == "Setup done once per class"
        
    def test_second(self, setup_once):
        assert setup_once == "Setup done once per class"
```

### 4. Passing Configuration Files from Command Line

Pytest allows you to specify a configuration file path via command-line options, which can be accessed within fixtures for customized test setups. 

#### Step 1: Add Command-Line Option in `conftest.py`

Define a command-line option to specify the configuration file path, allowing flexibility to use different files in various environments (e.g., dev, prod).

```python
# conftest.py
import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--config", 
        action="store", 
        default="config.json", 
        help="Path to the configuration file"
    )
```

Here, the `--config` option lets you set a configuration file path, with a default of `config.json`.

#### Step 2: Create a Fixture to Load Configurations

Create a fixture that reads the specified configuration file. Here, we’ll use JSON format, but this could be adapted for other file types (e.g., YAML, INI).

```python
# conftest.py
import pytest
import json

@pytest.fixture
def config(pytestconfig):
    config_path = pytestconfig.getoption("config")
    with open(config_path, "r") as f:
        config_data = json.load(f)
    return config_data
```

This fixture:
- Retrieves the config file path using `pytestconfig.getoption("config")`.
- Opens and loads the JSON configuration as a dictionary.

#### Step 3: Use the Configuration in Tests

Now, any test that includes `config` as a parameter will receive the loaded configuration data.

```python
def test_api_url(config):
    assert "api_url" in config
    assert config["api_url"] == "https://example.com/api"
```

Run this test with:
```bash
pytest --config=config_prod.json
```

### 5. Customizing Test Runs with Command-Line Options

You can customize test runs by passing arguments through the command line or configuring options in `pytest.ini`.

**Example: Passing Arguments**:
Define options in `conftest.py` using `pytest_addoption`:
```python
# conftest.py
def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev")

@pytest.fixture
def env(pytestconfig):
    return pytestconfig.getoption("env")

def test_env(env):
    assert env in ["dev", "prod", "qa"]
```
Run with:
```bash
pytest --env=prod
```

**Example: pytest.ini Configuration**:
You can add default options in `pytest.ini`:
```ini
# pytest.ini
[pytest]
addopts = --maxfail=3 -rf
```

This configuration limits the test run to three failures and provides failure reports.

### 6. Using External Data with `@pytest.mark.parametrize`

Load data from a file (e.g., JSON, CSV) to parameterize tests dynamically.

**Example with JSON**:
```python
import pytest
import json

def get_test_data():
    with open("data.json") as f:
        return json.load(f)

@pytest.mark.parametrize("username, password", get_test_data())
def test_login(username, password):
    assert username and password  # Example login test
```
