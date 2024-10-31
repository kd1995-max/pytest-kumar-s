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

