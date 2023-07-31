import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Test_my_002:

    def test_crekart_login_001(self):

        driver = webdriver.Chrome()
        driver.maximize_window()

        driver.get("https://automation.credence.in/login")

        driver.find_element(By.XPATH, "//input[@id='email']").send_keys("nikitasbarge@gmail.com")

        driver.find_element(By.XPATH, "//input[@id='password']").send_keys("nikita123")

        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        try:
            driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
            print("login pass")
            assert True
        except:
            print("login failed")
            assert False

    @pytest.mark.skip
    def test_credkart_orderAmtVer_002(self):

        chrome_options = webdriver.ChromeOptions()

        chrome_options.add_argument("headless")

        driver = webdriver.Chrome(options=chrome_options)

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

        time.sleep(2)
        product_quantity = Select(driver.find_element(By.XPATH, "//tbody/tr[1]/td[3]/select"))
        product_quantity.select_by_index(2)

        time.sleep(1)
        product_quantity1 = Select(driver.find_element(By.XPATH, "//tbody/tr[2]/td[3]/select"))
        product_quantity1.select_by_index(3)

        time.sleep(2)
        product_quantity2 = Select(driver.find_element(By.XPATH, "//tbody/tr[3]/td[3]/select"))
        product_quantity2.select_by_index(2)

        time.sleep(1)
        l = len(driver.find_elements(By.XPATH, "//tbody/tr/td[4]"))
        print(l)

        product_price_list = []

        for r in range(1, l - 2):
            var1 = driver.find_element(By.XPATH, "//tbody/tr[" + str(r) + "]/td[4]").text
            print(var1)
            product_price = (var1[1:])  ###slicing to remove $
            product_price_list.append(float(product_price))

        Exp_Subtotal = round((sum(product_price_list)), 2)

        print("Exp_Subtotal = " + str(Exp_Subtotal))
        # Exp_Subtotal=13,099.9
        # System_Subtotal=13099.9
        print(product_price_list)

        System_Value = []

        for r in range(l - 2, l + 1):
            var2 = driver.find_element(By.XPATH, "//tbody/tr[" + str(r) + "]/td[4]").text
            var3 = var2.replace(",", "")
            system_price = (var3[1:])
            System_Value.append(float(system_price))

        print(System_Value)

        # Subtotal
        print("Exp_subtotal =", Exp_Subtotal)
        print("system_subtotal = ", System_Value[0])

        if Exp_Subtotal == System_Value[0]:
            print("Subtotal total matched")
            assert True
        else:
            print("Subtotal is not matched")
            assert False

        # Tax
        Exp_tax = round(Exp_Subtotal * 0.13, 2)
        print("Exp_tax =", Exp_tax)
        print("system_tax =", System_Value[1])

        if Exp_tax == System_Value[1]:
            print("tax is matched")
            assert True
        else:
            print("Tax is not matched")
            assert False

        # overall_total
        Exp_Overall_total = round((System_Value[0] + System_Value[1]), 2)
        print("Exp_Overall_total =", Exp_Overall_total)
        print("System_Overall_total =", System_Value[2])

        if Exp_Overall_total == System_Value[2]:
            print("Overall total is matched")
            assert True
        else:
            print("Overall total is not matched")
            assert False

        time.sleep(2)