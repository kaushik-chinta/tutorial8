import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

class ChromeSearch(unittest.TestCase):
    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.headless = True
        self.driver = webdriver.Firefox(options=options)
    
    def test_python_results(self):  
        self.driver.get("https://www.python.org")
        elem = self.driver.find_element("name", "q")
        elem.send_keys("unittest")
        elem.send_keys(Keys.RETURN)
        WebDriverWait(self.driver, 10).until(lambda x: "Results" in self.driver.page_source)
        assert "No results found." not in self.driver.page_source

    def test_python_no_results(self):
        self.driver.get("https://www.python.org")
        elem = self.driver.find_element("name", "q")
        elem.send_keys("tohranis")
        elem.send_keys(Keys.RETURN)
        WebDriverWait(self.driver, 10).until(lambda x: "No results found" in self.driver.page_source)
    
    def tearDown(self):
        self.driver.close()

unittest.main()