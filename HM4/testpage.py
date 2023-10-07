from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from BaseApp import BasePage
import logging, yaml
import requests, json

class TestSearchLocators:
    
    ids = dict()
    with open("./locators.yaml") as f:
        locators = yaml.safe_load(f)
        
    for locator in locators['xpath'].keys():
        ids[locator]= (By.XPATH, locators['xpath'][locator])
        
    for locator in locators['css'].keys():
        ids[locator]= (By.CSS_SELECTOR, locators['css'][locator])
    
    
    
class OperationsHelper(BasePage):
              
    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name= locator
        logging.debug(f'Send {word} to element {element_name}')
        field = self.find_element(locator)[0]
        if not field:
            logging.error(f'Element {locator} not found')
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f'Exceprion while operation with {locator}')
            return False
        return True
    
    
    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name= locator
        button = self.find_element(locator)[0]
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception('Exceprion with click')
            return False
        logging.debug(f'Clicked {element_name} button')
        return True
    
    
    
    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name= locator
        field = self.find_element(locator, time=3)[0]
        if not field:
            return None
        try:
            text = field.text 
        except:
            logging.exception(f'Exception while get test from {element_name}')
            return None
        logging.debug(f'We find text {text} in field {element_name}')
        return text
    
    #ENTER TEXT
    def enter_login(self,word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_LOGIN_FIELD'], word, description='login')
      
        
    def enter_pass(self,word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_PASS_FIELD'], word, description='pass')        
    
        
    def enter_title(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_TITLE'], word, description='title')
        
        
    def enter_description(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_DESCRIPTION'], word , description='description')
        
        
    def enter_content(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_CONTENT'], word, description='content')       
        
         
         
    def enter_contact_name(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_CONTACT_NAME'], word , description='name')
        
        
        
    def enter_contact_mail(self, word):
       self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_CONTACT_MAIL'], word, description='mail')
        
        
    def enter_contact_content(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_CONTACT_CONTENT'], word, description='content')   
        
    
    #GET
    
    def get_alert_text(self):
        try:
            WebDriverWait(self.driver, 3).until(EC.alert_is_present(),
                                        'Timed out waiting for PA creation ' +
                                        'confirmation popup to appear.')

            alert = self.driver.switch_to.alert
            logging.info(alert.text)
            text = alert.text
            alert.accept()
            logging.info("alert accepted")
            return text
        except Exception:
            logging.error("no alert")
            return False
         
    def get_alert(self):
        logging.info("Get alert text")
        text = self.get_alert_text()
        logging.info(text)
        return text
    
    def check_res_lbl(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_RES_LBL'], description='result')
        
        
    #CLICK
    
    def click_loggin_button(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_BTN_FIELD'], description='login')
        
    def click_new_post_button(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_NEW_POST_BTN'], description='new post')
        
    def click_save_button(self):
         self.click_button(TestSearchLocators.ids['LOCATOR_SAVE_BTN'], description='save')
            
    def click_contact_send_btn(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_CONTACT_SEND'], description='send')  
        
    def click_contact_link(self):
         self.click_button(TestSearchLocators.ids['LOCATOR_CONTACT_BTN'], description='contact')   
         
         
         
      
         
#REST API         
         
with open('config.yaml', 'r') as f:
    conf =  yaml.safe_load(f)

def get_token():
    response = requests.post(url=conf['url'], data={'username': conf['username'], 'password': conf['password']})
    return response.json()['token']

def get(token: str, params: dict):
    response = requests.get(conf['url_post'], headers={'X-Auth-Token': token}, params=params)
    return response.json()

def post(token: str, data: dict):
    response = requests.post(conf['url_post'], headers={'X-Auth-Token': token}, data=data)
    return response.json()


if __name__ == '__main__':
    temp = get_token()
    print(get(temp))