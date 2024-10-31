import pytest

#--------------------------------------------------------------------------------------------------------
#| Fixtures are created when first requested by a test, and are destroyed based on their scope:		|
#--------------------------------------------------------------------------------------------------------
#| 1.function: the default scope, the fixture is destroyed at the end of the test.			|
#| 2.class: the fixture is destroyed during teardown of the last test in the class.			|
#| 3.module: the fixture is destroyed during teardown of the last test in the module.			|
#| 4.package: the fixture is destroyed during teardown of the last test in the package.			|
#| 5.session: the fixture is destroyed at the end of the test session.					|
#| Ref: https://docs.pytest.org/en/stable/fixture.html							|
#--------------------------------------------------------------------------------------------------------

def pytest_configure():
	pytest.weekdays1 = ['mon', 'tue', 'wed']
	pytest.weekdays2 = ['fri', 'sat', 'sun']

@pytest.fixture(scope="module")
def setup01():
	wk1 = pytest.weekdays1.copy()
	wk1.append('thur')
	yield wk1
	print("\n after yield in setup01 Fixtures")
	wk1.pop()

@pytest.fixture(scope="session")
def setup02():
	wk2 = pytest.weekdays2.copy()
	wk2.insert(0, 'thur')
	yield wk2

@pytest.fixture()
def setup04(request):
	mon = getattr(request.module, "months")
	print('\n in fixture setup 04 \n')
	print('\n Fixture Scope: ' + str(request.scope))
	print('\n calling function: ' + str(request.function.__name__))
	print('\n calling module \n' + str(request.module.__name__))
	mon.append('April')
	yield mon

@pytest.fixture()
def setup05():
	def get_structure(name):
		if name == 'list':
			return [1, 2, 3]
		elif name == 'tuple':
			return (1, 2, 3)

	return get_structure

