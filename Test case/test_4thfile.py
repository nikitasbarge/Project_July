import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_my004:

    def test_orangeHrm_001(self):
        driver = webdriver.Chrome()
        ##Login
        # url
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.implicitly_wait(60)
        # username
        driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        # password
        driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        driver.implicitly_wait(60)
        # login
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        driver.implicitly_wait(120)

        ##Logout
        # click on dropdown
        driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']").click()
        # click on logout
        driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()

        try:
            driver.find_element(By.XPATH, "//img[@alt='company-branding']")
            print("Logout passed")
        except:
            print("Logout failed")

        time.sleep(5)

class Test_my005:
    @pytest.mark.nikita
    def test_div_001(self):
        a= 20
        b= 5
        div = a/b
        if div == 4:
            print("Div :", div)
            assert True
        else:
            assert False
