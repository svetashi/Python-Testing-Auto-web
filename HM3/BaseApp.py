import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://test-stand.gb.ru'
        
        
    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator), message=f'Can`t find element by locator {locator}')
    
    def get_element_property(self, locator, property):
        element = self.find_element(locator)
        return element.value_of_css_property(property)
    
    def wait_for_redirect(self, expected_url):
        wait = WebDriverWait(self.driver, 10)
        try:
            wait.until(EC.url_to_be(expected_url))
            return True
        except Exception as exc:
            logging.error("Timeout")
            return False
        
    def go_to_site(self):
        return self.driver.get(self.base_url)
    
    def get_alert_text(self):
        try:
            alert = self.browser.switch_to.alert
            return alert.text
        except:
            logging.exception('Exception with alert')
            return None
    