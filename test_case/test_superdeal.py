
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, logging
from selenium.webdriver.common.action_chains import ActionChains
import UrlList


class test_Scroll(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_scroll(self):
        driver = self.driver
        driver.maximize_window()
        #url = UrlList.en_url
        # for i in range(0, 15):
        driver.get("https://www.joybuy.com/superdeals/detail.html")
        #driver.get(url[i])
        time.sleep(5)
            #  将滚动条移动到页面的顶部
        # js_top = "var navloaction = document.getElementById(\"top-rate\");" \
        #              "if (navloaction)" \
        #              "{var height=navloaction.offsetTop;" \
        #              "document.documentElement.scrollTop=height;}"
        # driver.execute_script(js_top)
        # time.sleep(1)
        js_top = "var navloaction = document.getElementById(\"flashTab\");" \
                  "if (navloaction)" \
                  "{var height=navloaction.offsetTop;" \
                  "document.documentElement.scrollTop=height;}"
        driver.execute_script(js_top)
        time.sleep(1)

        e = driver.find_elements_by_class_name("ct")
        e[1].click()
        time.sleep(5)

        js_top2 = "var navloaction = document.getElementsByClassName(\"categories w\");" \
                 "if (navloaction)" \
                 "{var height=navloaction[0].offsetTop;" \
                 "document.documentElement.scrollTop=height;}"
        driver.execute_script(js_top2)
        time.sleep(1)

        ele = driver.find_element_by_class_name("pics")
        ActionChains(driver).move_to_element(ele).perform()
        #driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Wide Watches Collections'])[1]/following::p[2]").click()
        time.sleep(5)
        js_lazy = "var timer=setInterval(function()" \
                      "{" \
                      "var scrollTop=document.documentElement.scrollTop||document.body.scrollTop;" \
                      "console.log(scrollTop);" \
                      "var ispeed=100;" \
                      "if(scrollTop>2500)" \
                      "{" \
                      "clearInterval(timer);" \
                      "}" \
                      "document.documentElement.scrollTop=document.body.scrollTop=scrollTop+ispeed;" \
                      "},1000)"
        driver.execute_script(js_lazy)
        time.sleep(20)
        driver.find_element_by_xpath("//a[@class='more goodsListBtn12']").click()
        js_lazy2 = "var timer=setInterval(function()" \
          "{" \
          "var scrollTop=document.documentElement.scrollTop||document.body.scrollTop;" \
          "console.log(scrollTop);" \
          "var ispeed=100;" \
          "if(scrollTop>4000)" \
          "{" \
          "clearInterval(timer);" \
          "}" \
          "document.documentElement.scrollTop=document.body.scrollTop=scrollTop+ispeed;" \
          "},1000)"
        driver.execute_script(js_lazy2)
        time.sleep(20)
        js_open = 'window.open("https://www.baidu.com");'
        driver.execute_script(js_open)
        num = driver.window_handles
        driver.switch_to.window(num[num.__len__()-1])


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
