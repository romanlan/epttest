# -*- coding: utf-8 -*-
import time
import UrlList
from test_login import test_login
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re ,logging


class test_Dong(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    # 类中需执行的用例以test_开头
    def test_dongdong(self):
        # logurl = 'https://passport.joybuy.com/new/facade.html'
        # url = ['https://www.joybuy.com/600256740.html', 'https://sale.joybuy.com/pc/Bbs6QhqwtZ.html']

        url = UrlList.en_url
        driver = self.driver
        driver.maximize_window()
        # driver.get(logurl)
        # test_login.test_log_in(self)  # 已登录
        for i in url:
            time.sleep(3)
            driver.get(i)
            try:
                driver.find_element_by_link_text("Help").click()
                driver.find_element_by_link_text("Chat").click()
                num = driver.window_handles
                driver.switch_to.window(num[num.__len__()-1])

                self.assertEqual(driver.current_url, "https://support.joybuy.com/support/index?source=3")
            except Exception as e:
                print(i+'不一致')
                logging.exception(e)

        # driver.close()


    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()


