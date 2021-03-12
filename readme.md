API
PRE-Requisites = NONE

From Project Root DIR
-Run all tests
pytest API/TESTS

-Run one test file
pytest tests/{filename}

-run one test function from file
pytest tests/{filename} -k '{methodname}'

-run one parameter from the test function
pytest tests/{filename} -k '{methodname}' --ss {index position of the test from the parameter list}


MOBILE
PRE-Requisites = Appium, XCODE, Android Development Studio

discover appPackage and appActivity (MAC)
adb shell dumpsys window | grep -E 'mCurrentFocus'

(PC)
adb shell dumpsys window | find "mCurrentFocus"


Android Emulator tests sequence:
Start Appium server
Use Andriod Studio AVD to launch a emulator with no APK set to the device type you want to test
pytest [PATH_TO_TESTFILE] -k ['METHOD_IN_FILE'] --app [emu, droid, imu, iphone]

WEB
PRE-Requisites = Browser Drivers

pytest -n={MAX IS 3} {PATH TO FILE} -k '{FUNCTION NAME}' --browser {BROWSER FROM CONFTEST.py SETUP()} --html={PATH TO FILE} --self-contained-html



.ENV file not included
LOGS generated automatically
