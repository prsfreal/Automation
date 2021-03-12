from selenium.webdriver.common.action_chains import ActionChains
import time


class ArticleArchivePage:

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)

    article1 = '//*[@id="post-3520"]/div/div/div/div/section[2]/div/div/div/div/div/div[2]/div/div/article[1]/div/a'
    article2 = '//*[@id="post-3520"]/div/div/div/div/section[2]/div/div/div/div/div/div[2]/div/div/article[2]/div/a'
    article3 = '//*[@id="post-3520"]/div/div/div/div/section[2]/div/div/div/div/div/div[2]/div/div/article[3]/div/a'
    article4 = '//*[@id="post-3520"]/div/div/div/div/section[2]/div/div/div/div/div/div[2]/div/div/article[4]/div/a'

    def navigateToArticle1(self):
        self.action.move_to_element(self.driver.find_element_by_xpath(self.article1))
        self.action.click(self.driver.find_element_by_xpath(self.article1))
        self.action.perform()
        time.sleep(1)




