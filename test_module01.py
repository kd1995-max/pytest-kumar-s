# there should be only one assert in one function definition
def test_a1():
    print("This is my first test")
    assert 5 + 5 == 10
    assert 5 - 5 == 0
    assert 5 * 5 == 25
    assert 5 / 5 == 1

def test_a2():
    assert 5*5 == 0, "failed test intentionally"

def test_a3():
    assert 5//2 == 2 # integer truncating division

def test_a4():
    assert 1 # same as true

def test_a5():
    assert 123 # same as true

def test_a6():
    assert 0 # same as false

def test_a7():
    assert 4 in divmod(9,2) # divmod() returns a remainder and quotient as tupple also "not in can be used similarly"

def test_a8():
    assert [1,2] < [1, 2 , 4 , 5] # checking for subsets

def test_a9():
    assert [1,2] == [1, 2 ] # checking for subsets