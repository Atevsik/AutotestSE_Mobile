
from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class MmaMatchPage:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/live/mma/ufc/event-14640/')
        sleep(6)
        sleep(5)

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'. UFC 299.')]")

    def books(self):
        books = self.browser.find_element(By.XPATH,"//div[@class='sp-matchcenter-event-page__bookies']")

    def vs(self):
        vs = self.browser.find_element(By.XPATH,"//div[@class='sp-matchcenter-event-fights-facetoface__right']")
        vs.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/live/mma/ufc/event-5130/#', "No VS"
        self.browser.back()

    def shon(self):
        shon = self.browser.find_element(By.XPATH,"//div[@class='se-matchcenter-event-summary-fighter-details']//div[@class='se-matchcenter-event-summary-fighter-details__photo']//img")
        shon.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/tag/shon-o-melli-18323/', "No Shon"
        self.browser.back()

    def vera(self):
        vera = self.browser.find_element(By.XPATH,"//div[@class='se-matchcenter-event-summary-fighter-details se-matchcenter-event-summary-fighter-details--reverse']//div[@class='se-matchcenter-event-summary-fighter-details__photo']//img")
        vera.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/tag/marlon-vera-25201/', "No Vera"
        self.browser.back()

    def stat(self):
        stat = self.browser.find_element(By.XPATH,"//div[@class='se-matchcenter-event-comparative-statistic-params__title']")









