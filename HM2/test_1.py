import yaml
from module import Site
import pytest
import time

with open('config.yaml') as f:
    config = yaml.safe_load(f)

if __name__ != '__main__':
    site = Site(config['adress'])

def test_step1():
    x_selector1 ='//*[@id="login"]/div[1]/label/input'
    input1 = site.find_element('xpath', x_selector1)
    input1.send_keys('Mihger')
    x_selector2 ='//*[@id="login"]/div[2]/label/input'
    input2 = site.find_element('xpath', x_selector2)
    input2.send_keys('583510e7ba')
    btn_selector = 'button'
    btn= site.find_element('css' , btn_selector)
    btn.click()
    assert site.wait_for_redirect('https://test-stand.gb.ru/')
    
def test_step2():
    btn_create_post= '//*[@id="create-btn"]'
    btn = site.find_element('xpath' , btn_create_post)
    btn.click()
    
    title = '//*[@id="create-item"]/div/div/div[1]/div/label/input'
    input_title = site.find_element('xpath', title)
    input_title.send_keys('sveta')
    
    description = '//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea'
    input_description = site.find_element('xpath', description)
    input_description.send_keys('kakleta')
    
    content = '//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea'
    input_content = site.find_element('xpath', content)
    input_content.send_keys('tasty')
    
    btn_save= '//*[@id="create-item"]/div/div/div[7]/div/button/span'
    btn_s = site.find_element('xpath' , btn_save)
    btn_s.click()
    
    time.sleep(2)
    
    post_title_selector = '//*[@id="app"]/main/div/div[1]/h1'
    post_title = site.find_element('xpath', post_title_selector)
    assert 'sveta' in post_title.text
          

if __name__ == '__main__':
    pytest.main(['-svv'])