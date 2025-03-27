from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class MmaMatch:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/tag/hoakin-bakli-25917/')
        sleep(6)

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//div[@class='sp-profile-name__name']")

    def info(self):
        info = self.browser.find_element(By.XPATH,"//div[@class='sp-tag-page-layout-info']//div[5]//div[1]//div[2]")

    def last_boi(self):
        last_boi = self.browser.find_element(By.XPATH,"//tbody/tr[2]/td[1]/div[1]/div[2]")
        last_boi.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/live/mma/ufc/event-16432/#',"No last boi"
        self.browser.back()

    def allnews(self):
        allnews = self.browser.find_element(By.XPATH,"//a[@class='se-button se-button--size-big se-last-materials__all']")
        allnews.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/tag/hoakin-bakli-25917/news/', "No News"
        self.browser.back()

    def allresult(self):
        allresult = self.browser.find_element(By.XPATH,"//a[contains(text(),'Все результаты')]")
        allresult.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/tag/hoakin-bakli-25917/results/', "No result"

    def proverka(self,count):
        proverka = self.browser.find_elements(By.XPATH,"//td[@class='se-advanced-table-cell se-advanced-table-cell--sorted']")
        assert len(proverka) == count






