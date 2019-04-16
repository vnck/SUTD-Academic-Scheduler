import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Scheduler(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_coord_login(self):
        driver = self.driver
        driver.get("http://localhost:3000/login")
        assert "SUTD Academic Scheduler" in driver.title
        user = driver.find_element_by_name("user")
        user.send_keys("coord1")
        user.send_keys(Keys.RETURN)
        pw = driver.find_element_by_name("password")
        pw.send_keys("12345")
        pw.send_keys(Keys.RETURN)
        buttons = driver.find_elements_by_xpath(
            "//*[contains(text(), 'Submit')]")
        buttons[0].click()
        time.sleep(2)
        print(driver.current_url)
        assert driver.current_url == "http://localhost:3000/coordinator-home"

    def test_user_login(self):
        driver = self.driver
        driver.get("http://localhost:3000/login")
        assert "SUTD Academic Scheduler" in driver.title
        user = driver.find_element_by_name("user")
        user.send_keys("user3")
        user.send_keys(Keys.RETURN)
        pw = driver.find_element_by_name("password")
        pw.send_keys("12345")
        pw.send_keys(Keys.RETURN)
        buttons = driver.find_elements_by_xpath(
            "//*[contains(text(), 'Submit')]")
        buttons[0].click()
        time.sleep(2)
        print(driver.current_url)
        assert driver.current_url == "http://localhost:3000/instructor-home"

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
