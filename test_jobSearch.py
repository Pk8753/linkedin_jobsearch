import HtmlTestRunner
import unittest
from selenium import webdriver
from Utilities.utilites import JobUtilites

class test_jobSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # #HeadlessBrowser
        # cls.options = webdriver.ChromeOptions()
        # cls.options.headless = True
        # cls.driver = webdriver.Chrome(executable_path="Driver/chromedriver", options= cls.options)

        #withBrowswer
        cls.driver = webdriver.Chrome(executable_path="Driver/chromedriver")
        cls.url = "https://www.linkedin.com/jobs/search?position=1&pageNum=0"
        cls.driver.get(cls.url)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def test_01_JobSearch(self):
        driver = self.driver
        jobUtility = JobUtilites(driver)
        jobUtility.jobScrapper()

    def test_02_xlLoad(self):
        driver = self.driver
        loadUtility = JobUtilites(driver)
        loadUtility.loadJobIntoExcel()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Reports'))



