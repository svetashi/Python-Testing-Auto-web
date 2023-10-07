import logging, yaml
from testpage import OperationsHelper
import pytest
from BaseApp import BasePage
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.basicConfig(filename="log.txt", level=logging.INFO)


with open('./config.yaml') as f:
    testdata = yaml.safe_load(f)
    
name = testdata['login']
passwd = testdata['password']


def test_step1(browser):
    logging.info('Test 1 starting')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    sleep(2)
    testpage.enter_login(name)
    testpage.enter_pass(passwd)
    testpage.click_loggin_button()
    sleep(2)
    redirected = testpage.wait_for_redirect('https://test-stand.gb.ru/')
    if redirected:
        logging.info("SUCCESS")
    else:
        logging.error("FAIL")
    assert redirected
   
   
def test_step2(browser):
    logging.info('Test 2 starting')
    testpage = OperationsHelper(browser)
    testpage.click_new_post_button()
    sleep(2)
    redirected = testpage.wait_for_redirect('https://test-stand.gb.ru/posts/create')
    if redirected:
        logging.info("SUCCESS")
    else:
        logging.error("FAIL")
    assert redirected
    
    
def test_step3(browser):
    logging.info('Test 3 starting')
    testpage = OperationsHelper(browser)
    testpage.enter_title('test #3')
    testpage.enter_description('check working')
    testpage.enter_content('tommytommy')
    testpage.click_save_button()
    sleep(2)
    assert testpage.check_res_lbl()
          
     
def test_step4(browser):
    logging.info('Test 4 starting')
    testpage = OperationsHelper(browser)
    testpage.click_contact_link()
    sleep(1)
    testpage.enter_contact_name('sveta')
    testpage.enter_contact_mail('meow@gmail.com')
    testpage.enter_contact_content('paws paws')
    testpage.click_contact_send_btn()
    sleep(2)
    assert testpage.get_alert()
              

if __name__ == '__main__':
    pytest.main(['-svv'])