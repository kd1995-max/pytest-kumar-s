import pytest

@pytest.fixture()
def setup_list():
    print('\n in fixtures \n')
    city = ['New York', 'London', 'Riyadh', 'Singapore', 'Mumbai']
    return city

def test_getitem(setup_list):
    print(setup_list[1:3])
    assert setup_list[0] == 'New York'
    assert setup_list[::2] == ['New York', 'Riyadh', 'Mumbai']

def myreverse(lst):
    lst.reverse()
    return lst

def test_reverselist(setup_list):
    assert setup_list[::-2] == ["Mumbai", 'Riyadh', 'New York']
    assert setup_list[::-1] == myreverse(setup_list)


@pytest.mark.xfail(reason="known issue: usefixtures cannot use the fixtures return value")
@pytest.mark.usefixtures("setup_list")
def test_usefixturedemo(setup_list):
    assert  1==1
    assert (setup_list[0])