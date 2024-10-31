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

For further reference, explore the [Pytest cache documentation](https://docs.pytest.org/en/latest/cache.html).
