
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Basic:

    def waitAndsee(self, elem, find='ID', time=5):
        if find == 'XPATH':
            WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located((By.XPATH, elem))
            )

        elif find == 'ID':
            WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located((By.ID, elem))
            )

        else:
            WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located((By.XPATH, elem))
            )
