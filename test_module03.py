import pytest

def test_case_01():
    # with pytest.raises(Exception):
    assert (1/0)

def test_case_02():
    with pytest.raises(Exception):
        assert (1/0)

def func():
    raise ValueError("Index Error func1 raised")

def test_case_03():
    with pytest.raises(Exception) as excinfo:
        # assert 3 > 3
        func()

    print(str(excinfo))
    assert (str(excinfo.value) == "Index Error func1 raised")