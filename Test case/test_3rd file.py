import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Test_my003:
    def test_mul001(self):
        a= 3
        b= 6
        mul= a*b
        if mul == 18:
            print("Mul of a nd b :", mul)
            assert True
        else:
            assert False

    def test_checkout002(self):
        driver = webdriver.Chrome()

        driver.get("https://automation.credence.in/login")

        driver.find_element(By.ID, "email").send_keys("nikitasbarge@gmail.com")
        driver.find_element(By.CSS_SELECTOR, "#password").send_keys("nikita123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        # playstation
        driver.find_element(By.XPATH, "//body/div[@class='container']/div[2]/div[1]/div[1]/div[1]/a[1]/img[1]").click()
        driver.find_element(By.CSS_SELECTOR, "input[value='Add to Cart']").click()

        driver.find_element(By.XPATH, "//a[@class='btn btn-primary btn-lg']").click()

        # macbook
        driver.find_element(By.XPATH, "//h3[normalize-space()='Apple Macbook Pro']").click()
        driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()

        driver.find_element(By.XPATH, "//a[@class='btn btn-primary btn-lg']").click()

        # electric guitar
        driver.find_element(By.XPATH, "//h3[normalize-space()='Electric Guitar']").click()
        driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()

        # proceed to checkout
        driver.find_element(By.XPATH, "//a[@class='btn btn-success btn-lg']").click()
        # name
        driver.find_element(By.XPATH, "//input[@id='first_name']").send_keys("nikita")
        # lastname
        driver.find_element(By.XPATH, "//input[@id='last_name']").send_keys("barge")
        # phone
        driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("8888390852")
        # add
        driver.find_element(By.XPATH, "//textarea[@id='address']").send_keys("ajinkya colony satara")
        # zip_code
        driver.find_element(By.XPATH, "//input[@id='zip']").send_keys("415501")
        # state_click
        state_name = Select(driver.find_element(By.XPATH, "//select[@id='state']"))
        state_name.select_by_visible_text("Pune")
        # owner
        driver.find_element(By.XPATH, "//input[@id='owner']").send_keys("nikita")
        # cvv
        driver.find_element(By.XPATH, "//input[@id='cvv']").send_keys("257")
        # cardNo
        driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("4716")
        driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("1089")
        driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("9971")
        driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("6531")
        # ExpDate
        # year
        Ex_Date = Select(driver.find_element(By.XPATH, "//select[@id='exp_year']"))
        Ex_Date.select_by_visible_text("2024")
        # month
        Ex_month = Select(driver.find_element(By.XPATH, "//select[@id='exp_month']"))
        Ex_month.select_by_visible_text("May")
        # mastercard
        driver.find_element(By.XPATH, "//img[@id='mastercard']").click()
        # checkout
        driver.find_element(By.XPATH, "//button[@id='confirm-purchase']").click()

        time.sleep(10)