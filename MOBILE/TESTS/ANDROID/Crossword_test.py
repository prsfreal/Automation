import pytest
import time
from appium.webdriver.common.touch_action import TouchAction
from MOBILE.HELPERS.BasicClassConfig import Basic

class Test_Crossword(Basic):
    # Added this step to get type hinting from conftest for self.driver
    #Initialize TouchAction
    @pytest.fixture
    def additionalSetup(self, setupandteardown):
        self.driver = setupandteardown
        self.action = TouchAction(self.driver)


    def test_enter_letter(self, additionalSetup):
        time.sleep(25)
        self.action.tap(None, 716, 2357, 1).perform()

        time.sleep(7)
        self.action.tap(None, 727, 2553, 1).perform()

        time.sleep(7)
        self.action.tap(None, 734, 2571, 1).perform()

        time.sleep(15)
        self.action.press(None, 1000, 2500, 1).move_to(x=400, y=2500).move_to(x=720, y=2000).release().perform()
        time.sleep(2)
        self.action.press(None, 1000, 2500, 1).move_to(x=720, y=2000).move_to(x=400, y=2500).release().perform()
        time.sleep(2)
        self.action.press(None, 400, 2500, 1).move_to(x=1000, y=2500).move_to(x=720, y=2000).release().perform()
        time.sleep(2)
        self.action.press(None, 400, 2500, 1).move_to(x=720, y=2000).move_to(x=1000, y=2500).release().perform()
        time.sleep(2)
        self.action.press(None, 720, 2000, 1).move_to(x=1000, y=2500).move_to(x=400, y=2500).release().perform()
        time.sleep(2)
        self.action.press(None, 720, 2000, 1).move_to(x=400, y=2500).move_to(x=1000, y=2500).release().perform()
        time.sleep(2)






