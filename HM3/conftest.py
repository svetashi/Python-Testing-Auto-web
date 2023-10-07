import yaml, pytest
from selenium import webdriver 

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


with open('config.yaml') as f:
    config = yaml.safe_load(f)
    browser_type = config['browser']
    

driver = None

@pytest.fixture(scope='session')
def browser(): 
    global driver
    if driver:
        yield driver
    else:
        if browser_type == 'chrome':
            service = Service(executable_path=ChromeDriverManager().install())
            options = webdriver.ChromeOptions()       
            driver = webdriver.Chrome(service=service, options=options)
        yield driver
    # driver.quit()
    
   

     