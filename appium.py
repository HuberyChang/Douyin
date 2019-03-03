import time, random
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC


def main():
    server = 'http://localhost:4723/wd/hub'
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'STF_AL00',
        'appPackage': 'com.ss.android.ugc.aweme',
        'appActivity': '.main.MainActivity',
        # 关闭手机软键盘
        'unicodeKeyboard': True,
        'resetKeyboard': True
    }
    driver = webdriver.Remote(server, desired_caps)
    wait = WebDriverWait(driver, 60)
    button1 = wait.until(EC.presence_of_element_located((By.ID, 'com.ss.android.ugc.aweme:id/q6')))
    button1.click()
    button2 = wait.until(EC.presence_of_element_located((By.ID, 'com.android.packageinstaller:id/permission_deny_button')))
    button2.click()
    button3 = wait.until(EC.presence_of_element_located((By.ID, 'com.android.packageinstaller:id/permission_deny_button')))
    button3.click()
    time.sleep(2)
    TouchAction(driver).press(x=515, y=1200).move_to(x=515, y=1000).release().preform()
    time.sleep(20)
    TouchAction(driver).press(x=950,y=800).release().preform()
    button4 = wait.until(EC.presence_of_element_located((By.ID, 'com.ss.android.ugc.aweme:id/afg')))

