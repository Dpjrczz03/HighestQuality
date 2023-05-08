from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
global t
t=int(input())
def timel():

    opt=Options()
    opt.add_experimental_option("debuggerAddress","localhost:2407")
    driver = webdriver.Chrome(options=opt)
    # try:
    c=0

    a=driver.current_window_handle
    for i in reversed(range(len(driver.window_handles))):
        driver.switch_to.window(driver.window_handles[i])
        if "youtube" in driver.current_url:
            ri=i
            c+=1
            driver.switch_to.window(a)
            if c==1:
                time.sleep(t)
            driver.switch_to.window(driver.window_handles[ri])
            driver.close()
            driver.switch_to.window(a)

    # except:
    #     print("lodu")
    #     pass
if __name__=='__main__':
    while True:
        a=time.time()
        timel()
        b=time.time()
        # if(b-a>5):
        #     time.sleep(t+4)

        time.sleep(10)


