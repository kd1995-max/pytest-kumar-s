from pytest_topics.utils.myconfigparser import *
from pytest_topics.utils.configFileParser import ConfigFileParser

config = ConfigFileParser('prod.ini')

def test_getgmailurl():
	print(getGmailUrl())

def test_getoutlookurl():
	print(config.getOutlookUrl())
