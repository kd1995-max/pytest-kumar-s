import pytest

@pytest.mark.skipit
def test_case_01():
    assert 'hello' in 'hello world'

def test_case_02():
    assert 'world' in 'hello world'

@pytest.mark.skipit
@pytest.mark.skiptest
def test_case_03():
    assert 'world234' in 'hello world'