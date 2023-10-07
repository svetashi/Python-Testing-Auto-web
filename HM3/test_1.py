import logging
from testpage import OperationsHelper
import pytest
from BaseApp import BasePage
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.basicConfig(filename="log.txt", level=logging.DEBUG)

def test_step1(browser):
    logging.info('Test starting')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login('Mihger')
    testpage.enter_pass('583510e7ba')
    testpage.click_loggin_button()
    redirected = testpage.wait_for_redirect('https://test-stand.gb.ru/')
    if redirected:
        logging.info("SUCCESS")
    else:
        logging.error("FAIL")
    assert redirected
    
def test_step2(browser):
    btn_contact= '//*[@id="app"]/main/nav/ul/li[2]/a' 
    btn = browser.find_element('xpath' , btn_contact)
    btn.click()
    
    sleep(1)
    
    your_name = '//*[@id="contact"]/div[1]/label/input'
    input_your_name = browser.find_element('xpath', your_name)
    input_your_name.send_keys('sveta')
    
    email = '//*[@id="contact"]/div[2]/label/input'
    input_email = browser.find_element('xpath', email)
    input_email.send_keys('kakleta@gmail.com')
    
    content = '//*[@id="contact"]/div[3]/label/span/textarea'
    input_content = browser.find_element('xpath', content)
    input_content.send_keys('questions')
    
    
    btn_save= '//*[@id="contact"]/div[4]/button/span'
    btn_s = browser.find_element('xpath' , btn_save)
    btn_s.click()
    
    try:
        WebDriverWait(browser, 3).until(EC.alert_is_present(),
                                    'Timed out waiting for PA creation ' +
                                    'confirmation popup to appear.')

        alert = browser.switch_to.alert
        logging.info(f'Alert text: {alert.text}')
        alert.accept()
        logging.info("alert accepted")
        assert True
    except Exception:
        logging.error("no alert")
        assert False
              

if __name__ == '__main__':
    pytest.main(['-svv'])