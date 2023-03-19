from time import sleep
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
        caps["appium:deviceName"] = "localhost:55029"
        caps["appium:app"] = "C:\\Users\\vdi-student\\Downloads\\ApiDemos-debug.apk"
        caps["appium:ensureWebviewsHavePages"] = True
        caps["appium:nativeWebScreenshot"] = True
        caps["appium:newCommandTimeout"] = 3600
        caps["appium:connectHardwareKeyboard"] = True

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

    def tearDown(self):
        self.driver.quit()

    # def test_api_demos_1(self):
    #     el1 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="App")
    #     el1.click()
    #     el2 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Menu")
    #     el2.click()
    #     el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Inflate from XML")
    #     # el3.click()
    #     # if el3.text == "Inflate from XML":
    #     #     print("SUCCESS")
    #     self.assertEqual(el3.text, "Inflate from XML")
    #
    # def test_api_demos_2(self):
    #     el1 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="App")
    #     el1.click()
    #     el2 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Menu")
    #     el2.click()
    #     el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Inflate from XML")
    #     el3.click()
    #     title_inflate_from_xml = self.driver.find_element(
    #         by=AppiumBy.XPATH,
    #         value="/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.TextView"
    #     )
    #     self.assertEqual(title_inflate_from_xml.text, "App/Menu/Inflate from XML")

    def test_api_demos_3_drag_and_drop(self):
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(
            self.driver,
            mouse=PointerInput(interaction.POINTER_TOUCH, "touch")
        )
        actions.w3c_actions.pointer_action.move_to_location(332, 925)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(339, 454)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

        el1 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Views")
        el1.click()
        el2 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Drag and Drop")
        el2.click()

        sleep(3)

        # Drag and drop
        dot_1 = self.driver.find_element(by=AppiumBy.ID, value="io.appium.android.apis:id/drag_dot_1")
        dot_2 = self.driver.find_element(by=AppiumBy.ID, value="io.appium.android.apis:id/drag_dot_2")

        # TODO: Nalezy zmodyfikowac ponizszy kod w celu obslugi przesuniecia z dot_1 do dot_2
        actions_dnd = ActionChains(self.driver, duration=2000)
        # actions_dnd.move_to_element(dot_1)
        # actions_dnd.click_and_hold()
        # actions_dnd.pause(2)
        # actions_dnd.move_to_element(dot_2)
        # actions_dnd.pause(2)
        # actions_dnd.release()
        actions_dnd.drag_and_drop(dot_1, dot_2)
        actions_dnd.perform()

        self.driver.save_screenshot("C:\\Users\\vdi-student\\screenshot.png")

        sleep(5)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestApiDemos)
    unittest.TextTestRunner(verbosity=2).run(suite)
