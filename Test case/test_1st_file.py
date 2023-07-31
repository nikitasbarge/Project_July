import pytest
from selenium import webdriver


class Test_my001:

    def test_sum_001(self):
        a=5
        b=10
        sum= a+b
        print("Sum of a nd b :", sum)
        if sum== 15:
            assert True
        else:
            assert False

    @pytest.mark.xfail
    def test_credURL_002(self):
        driver = webdriver.Chrome()
        driver.get("https://credence.in/")
        if driver.title == "Credence" :
            print("U R at credence site")
            assert True
            driver.close()
        else:
            print("U R at wrong site")
            driver.close()
            assert False

    def test_sub_003(self):
        a= 10
        b= 5
        sub= a-b
        print("Sub of a and b :", sub)
        if sub == 5:
            assert True
        else:
            assert False



