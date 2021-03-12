import pytest
from appium import webdriver


# Add option to pytest CLI
def pytest_addoption(parser):
    parser.addoption("--app")

# Retrieve custom CLI input
@pytest.fixture()
def app(request):
    return request.config.getoption('--app')

# Select which app/device combo you want to use for testing
@pytest.fixture()
def setupandteardown(app):
    host_url = 'http://localhost:4723/wd/hub'

    #ANDROID Emulator
    if app == 'emu':
        desired_capabilities = {
            "automationName": "UiAutomator2",
            "platformName": "ANDROID",
            "deviceName": "ANDROID Emulator",
            "app": "/Users/philiprealini/Desktop/Stuff/Python/AppiumAutomation/APPS/twitter.apk",
            "appWaitPackage": "com.twitter.android",
            "appWaitActivity": "com.twitter.android.onboarding.common.CtaSubtaskActivity"
        }
        driver = webdriver.Remote(host_url, desired_capabilities)


    elif app == 'emu2':
        desired_capabilities = {
            "platformName": "ANDROID",
            "deviceName": "ANDROID Emulator",
            "app": "/Users/philiprealini/Desktop/Stuff/Python/AppiumAutomation/APPS/all.in.one.calculator_2.1.4-214_minAPI21(nodpi)_apkmirror.com.apk",
            "appWaitPackage": "all.in.one.calculator",
            "appWaitActivity": "app.calculator.ui.activities.feed.FeedActivity"
        }
        driver = webdriver.Remote(host_url, desired_capabilities)

    elif app == 'emu3':
        desired_capabilities = {
            "platformName": "ANDROID",
            "deviceName": "ANDROID Emulator",
            "app": "/Users/philiprealini/Desktop/Stuff/Python/AutomationFramework/MOBILE/APPS/com.fugo.wow_2.6.0-3219546_minAPI21(arm64-v8a,armeabi-v7a)(nodpi)_apkmirror.com.apk",
            "appWaitPackage": "com.fugo.wow",
            "appWaitActivity": "com.unity3d.player.UnityPlayerActivity"
        }
        driver = webdriver.Remote(host_url, desired_capabilities)

    #ANDROID Device
    elif app == 'droid':
        desired_capabilities = {
            "platformName": "ANDROID",
            "deviceName": "8ADX0R4E2",
            "app": "/Users/philiprealini/Desktop/Stuff/Python/AppiumAutomation/APPS/twitter.apk",
            "automationName": "UiAutomator2"
        }
        driver = webdriver.Remote(host_url, desired_capabilities)

    #iPhone Emulator
    elif app == 'imu':
        desired_capabilities = {
            'app': '/Users/philiprealini/Library/Developer/Xcode/DerivedData/AppiumTest-bvpfmexqkirgvqgwckkcefxkssyi/Build/Products/Debug-iphonesimulator/AppiumTest.app',
            'platformName': 'iOS',
            'platformVersion': '14.2',
            'deviceName': 'iPhone 11',
            'automationName': 'XCUITest'
        }
        driver = webdriver.Remote(host_url, desired_capabilities)

    #iPhone Device
    elif app == 'iphone':
        desired_capabilities = {
            # Do not have iOS device
            'app': '/Users/philiprealini/Library/Developer/Xcode/DerivedData/AppiumTest-bvpfmexqkirgvqgwckkcefxkssyi/Build/Products/Debug-iphonesimulator/AppiumTest.app',
            'platformName': 'iOS',
            'platformVersion': '14.2',
            'deviceName': 'iPhone 11',
            'automationName': 'XCUITest'
        }
        driver = webdriver.Remote(host_url, desired_capabilities)


    yield driver

    driver.close_app()
