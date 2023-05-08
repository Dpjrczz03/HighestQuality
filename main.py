from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
c=0
opt=Options()
opt.add_experimental_option("debuggerAddress","localhost:2407")
driver = webdriver.Chrome(options=opt)

def highestquality():


    if 'youtube' in driver.current_url and 'watch' in driver.current_url:
        driver.refresh()
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR,'.ytp-settings-button').click()
        time.sleep(0.1)
        driver.find_element(By.CSS_SELECTOR,".ytp-settings-menu .ytp-menuitem:last-child").click()
        time.sleep(0.1)
        driver.find_element(By.CSS_SELECTOR,".ytp-quality-menu .ytp-menuitem:first-child").click()
        global a
        a=driver.current_url


if __name__=='__main__':
    while True:
        if c==0:
            highestquality()
            time.sleep(1)
            a=driver.current_url
            c+=1
        else:
            if a!=driver.current_url:
                highestquality()
                time.sleep(1)