import os


# Capture the command line input for super specific (ss) parameter to pass to UTILITIES.PassParameters
def pytest_addoption(parser):
    parser.addoption("--ss", action="store")


def pytest_configure(config):
    if config.getoption('ss'):
        os.environ["ss"] = config.getoption('ss')


