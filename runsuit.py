# -*- coding: utf-8 -*-
import os,sys
import unittest
import time
# import HtmlTestRunner
import  HtmlTestRunner

import config

#os_path = config.get_os_path();
os_path = os.getcwd()
casesPath = os_path + "\\test_case"
reportPath = os_path + "\\Reports\\"
#templatePath = os_path + "/template/report_template.html"

'''如果HtmlTestRunner 报错请执行pip install html-testRunner '''

def CreatSuite():
    suite=unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(casesPath, pattern='test_scroll.py', top_level_dir=None)
    for test_case in discover:
        suite.addTests(test_case)
    return suite

if __name__ == "__main__":
    all_test_cases = CreatSuite()
    currentTime = str(int(time.time()))
    if not os.path.exists(reportPath):
        os.makedirs(reportPath)
    reportName = 'EPT_TestReport_' + currentTime + '.html'
    reportName = reportPath + reportName
    testRunner = HtmlTestRunner.HTMLTestRunner(output=reportPath)
    testRunner.run(all_test_cases)
