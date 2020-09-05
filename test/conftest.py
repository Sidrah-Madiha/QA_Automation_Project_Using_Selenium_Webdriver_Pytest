"""
This module contain shared fixtures
"""

import pytest
import selenium.webdriver
import json

@pytest.fixture
def config(scope="session"):
    with open("config.json") as config_file:
        config =json.load(config_file)
    assert config['browser'] in ['Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0
    return  config

@pytest.fixture
def browser(config):
    #set up webdriver instance
    if config['browser'] == 'Chrome':
        b = selenium.webdriver.Chrome()
    elif config['browser'] == 'Headless Chrome':
        opt = selenium.webdriver.ChromeOptions()
        opt.add_argument('headless')
        b = selenium.webdriver.Chrome(options=opt)
    else:
        raise Exception('Browser "{}" is not supported!'.format(config['browser']))

    #add implicit waits
    b.implicitly_wait(config['implicit_wait'])

    #return the webdriver instance from setup
    yield b

    # clean up webdriver instance
    b.quit()

