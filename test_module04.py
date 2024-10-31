import pytest
import sys
# skipping the whole module
pytestmark = pytest.mark.skipif(sys.platform != "linux", reason="This test case works only for linux")

const = 9/5
def cent_to_feh(cent = 0):
    fah = (cent * const) + 32
    return fah

@pytest.mark.skip(reason="skipping for no reason")
def test_01():
    assert cent_to_feh() == 32

@pytest.mark.skipif(sys.version_info > (3 , 6), reason="doesn't work on py version above 3.6")
def test_02():
    assert type(cent_to_feh()) == float

def test_03():
    print(sys.platform)
    assert cent_to_feh(38) == 100.4