# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput


class TestApiDemos(unittest.TestCase):
    def setUp(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["appium:platformVersion"] = "9"
        caps["appium:deviceName"] = "localhost:50078"
        caps["appium:app"] = "C:\\Users\\vdi-student\\Downloads\\ApiDemos-debug.apk"
        caps["appium:ensureWebviewsHavePages"] = True
        caps["appium:nativeWebScreenshot"] = True
        caps["appium:newCommandTimeout"] = 3600
        caps["appium:connectHardwareKeyboard"] = True

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

    def tearDown(self):
        self.driver.quit()

    def test_api_demos(self):

        el1 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="App")
        el1.click()
        el2 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Menu")
        el2.click()
        el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Inflate from XML")
        # el3.click()
        # if el3.text == "Inflate from XML":
        #     print("SUCCESS")
        self.assertEqual(el3.text, "Inflate from XML")


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestApiDemos)
    unittest.TextTestRunner(verbosity=2).run(suite)