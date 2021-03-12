#Contains attributes of the TestSuiteClasses that get created for each new file in ./TESTS
#These attributes may or not be called for each test method.

import inspect
from UTILITIES.WebCustomLogger import LogGen
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class basic:
    logger = LogGen.loggen()
    defName = (inspect.stack()[0][3])

    def waitAndsee(self, elem, find='XPATH', time=5):
        if find == 'XPATH':
            try:
                WebDriverWait(self.driver, time).until(
                    EC.presence_of_element_located((By.XPATH, elem))
                )
            except:
                self.logger.info(f'Could not find element = {elem}')

        elif find == 'ID':
            try:
                WebDriverWait(self.driver, time).until(
                    EC.presence_of_element_located((By.ID, elem))
                )
            except:
                self.logger.info(f'Could not find element = {elem}')

        else:
            try:
                WebDriverWait(self.driver, time).until(
                    EC.presence_of_element_located((By.XPATH, elem))
                )
            except:
                self.logger.info(f'Could not find element = {elem}')
