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
