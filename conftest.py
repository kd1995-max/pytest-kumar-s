import pytest

QA_config = 'qa.prop'
prod_config = 'prod.prop'

def pytest_addoption(parser):
	parser.addoption("--cmdopt", default='QA')

@pytest.fixture()
def cmdopt(pytestconfig):
	opt = pytestconfig.getoption("cmdopt")

	if opt == 'Prod':
		f = open(prod_config, 'r')
	else:
		f = open(QA_config, 'r')

	yield f
