import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from parameterized import parameterized


class TestApiDemos(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps["platformName"] = "Android"
        desired_caps["appium:platformVersion"] = "9"
        desired_caps["appium:deviceName"] = "127.0.0.1:5555"
        desired_caps["appium:appPackage"] = "com.android.calculator2"
        desired_caps["appium:appActivity"] = "com.android.calculator2.Calculator"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

    @parameterized.expand([
        [1, "1"],
        [2, "2"],
        [3, "3"],
        [4, "4"],
        [5, "5"],
    ])
    def test_button_click_value(self, digit, expected_value):
        button = self.driver.find_element(
            by=AppiumBy.ID,
            value=f"com.android.calculator2:id/digit_{digit}"
        )
        button.click()
        formula = self.driver.find_element(by=AppiumBy.ID, value="com.android.calculator2:id/formula")
        self.assertEqual(formula.text, expected_value)

    @parameterized.expand([
        [1, 2, 3],
        [2, 4, 6],
        [3, 7, 10],
    ])
    def test_add_two_numbers(self, a, b, expected_result):
        button_a = self.driver.find_element(
            by=AppiumBy.ID,
            value=f"com.android.calculator2:id/digit_{a}"
        )
        button_a.click()
        button_add = self.driver.find_element(by=AppiumBy.ID, value=f"com.android.calculator2:id/op_add")
        button_add.click()
        button_b = self.driver.find_element(
            by=AppiumBy.ID,
            value=f"com.android.calculator2:id/digit_{b}"
        )
        button_b.click()
        button_eq = self.driver.find_element(by=AppiumBy.ID, value=f"com.android.calculator2:id/eq")
        button_eq.click()
        result = self.driver.find_element(by=AppiumBy.ID, value="com.android.calculator2:id/result")
        self.assertEqual(result.text, str(expected_result))


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestApiDemos)
    unittest.TextTestRunner(verbosity=2).run(suite)
