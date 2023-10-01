import yaml
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with open('config.yaml') as f:
    config = yaml.safe_load(f)
    browser = config['browser']
    
class Site:
    def __init__(self, adress):
        if browser == 'chrome':
            service = Service(executable_path=ChromeDriverManager().install())
            options = webdriver.ChromeOptions()
            self.driver = webdriver.Chrome(service=service, options=options) 
            self.driver.get(adress)
            self.driver.maximize_window()
            time.sleep(config['sleep_time'])       
        
    def find_element(self, mode, path):
        if mode == 'css':
            element = self.driver.find_element(By.CSS_SELECTOR, path)
        elif mode == 'xpath':
            element = self.driver.find_element(By.XPATH, path)
        else:
            element = None
        return element
    
    def get_element_property(self, mode, path, property):
        element = self.find_element(mode, path)
        return element.value_of_css_property(property)
    
    def wait_for_redirect(self, expected_url):
        wait = WebDriverWait(self.driver, 10)
        try:
            wait.until(EC.url_to_be(expected_url))
            return True
        except Exception as exc:
            print("timeout")
            return False

    def close(self):
        self.driver.close()