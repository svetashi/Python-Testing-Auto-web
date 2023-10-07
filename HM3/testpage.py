from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from BaseApp import BasePage
import logging

class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, '//*[@id="login"]/div[1]/label/input[1]')
    LOCATOR_PASS_FIELD = (By.XPATH, '//*[@id="login"]/div[2]/label/input[1]')
    LOCATOR_BTN_FIELD = (By.CSS_SELECTOR, 'button')
 
    
class OperationsHelper(BasePage):
    def enter_login(self,word):
        logging.info(f'Send {word} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}')
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field[0].clear()
        login_field[0].send_keys(word)
        
    def enter_pass(self,word):
        logging.info(f'Send {word} to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}')
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        login_field[0].clear()
        login_field[0].send_keys(word)
        
        
    def click_loggin_button(self):
        logging.info('Click login button')
        self.find_element(TestSearchLocators.LOCATOR_BTN_FIELD)[0].click()
        
        

        