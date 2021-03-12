import pytest
import time
from appium.webdriver.common.touch_action import TouchAction
from decouple import config
from MOBILE.HELPERS.BasicClassConfig import Basic

class Test_Twitter(Basic):
    # Added this step to get type hinting from conftest for self.driver
    #Initialize TouchAction
    id = config('twitterID')
    password = config('twitterPass')

    idfield = 'com.twitter.android:id/login_identifier'
    passwordfield = 'com.twitter.android:id/login_password'
    loginbutton = 'com.twitter.android:id/login_login'
    tweetbutton = 'com.twitter.android:id/composer_write'
    tweetfield = 'com.twitter.android:id/tweet_text'
    whocansee = '//android.view.ViewGroup[@content-desc="Sets to people you follow or mention can reply"]'
    convocontrol = 'com.twitter.android:id/conversation_controls_view'
    hamburger = '//android.widget.ImageButton[@content-desc="Show navigation drawer"]'
    settingsandprivacy = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[6]'
    accounts = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[1]'
    username = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.RelativeLayout'
    logout = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout'

    @pytest.fixture
    def additionalSetup(self, setupandteardown):
        self.driver = setupandteardown
        self.action = TouchAction(self.driver)

    def test_Login(self, additionalSetup):

        self.action.tap(None, 867, 2600, 1).perform()

        self.waitAndsee(self.idfield)
        self.driver.find_element_by_id(self.idfield).send_keys(self.id)
        self.driver.find_element_by_id(self.passwordfield).send_keys(self.password)
        self.driver.find_element_by_id(self.loginbutton).click()

        self.waitAndsee(self.tweetbutton)
        self.driver.find_element_by_id(self.tweetbutton).click()

        self.waitAndsee(self.tweetfield)
        self.driver.find_element_by_id(self.tweetfield).send_keys('This is a tweet')
        self.driver.find_element_by_id(self.convocontrol).click()

        self.waitAndsee(elem=self.whocansee, find='XPATH')
        self.driver.find_element_by_xpath(self.whocansee).click()

        #Don't tweet
        #self.driver.find_element_by_id('com.twitter.android:id/button_tweet').click()

        self.driver.find_element_by_xpath(self.hamburger).click()

        self.waitAndsee(elem=self.settingsandprivacy, find='XPATH')
        self.driver.find_element_by_xpath(self.settingsandprivacy).click()

        self.waitAndsee(elem=self.accounts, find='XPATH')
        self.driver.find_element_by_xpath(self.accounts).click()

        self.waitAndsee(elem=self.username, find='XPATH')
        self.action.press(x=772, y=1308).move_to(x=749, y=553).release().perform()
        self.driver.find_element_by_xpath(self.logout).click()

        time.sleep(20)



