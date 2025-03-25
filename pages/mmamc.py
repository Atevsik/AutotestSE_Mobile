from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class MmaMC:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/live/mma/ufc/')

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//div[@class='sp-sport-page__title']")

    def select(self):
        select = self.browser.find_element(By.XPATH,"//div[@class='se-sport-navigator__competition-name']")
        select.click()

    def bella(self):
        bella = self.browser.find_element(By.XPATH,"//div[@id='react-select-competitions-option-0-2']")
        bella.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/live/mma/bellator/'

    def last(self):
        last = self.browser.find_element(By.XPATH,"//a[contains(text(),'Прошедшие')]")
        last.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/live/mma/bellator/14-09-2024/', "No data"

    def match(self):
        match = self.browser.find_element(By.XPATH,"//body/section[@id='pageone']/div[@class='se-matchcenter-page']/div[@class='sp-sport-page']/div[@class='sp-sport-page__content']/div[@class='se-matchcenter-sports-list']/div[@class='sp-mobile-indent-content']/div[@class='sp-mobile-indent-content-collapsed']/div[@class='se-matchcenter-sports-list__competitions se-matchcenter-sports-list__competitions--active']/div[@class='se-matchcenter-sports-list__competition']/div[@class='se-competition-titled-block']/div[@class='se-competition-titled-block__content']/div[@class='se-matchcenter-sports-list__competition-matches']/div[@class='se-matchcenter-matches se-matchcenter-fighting-matches']/a[2]/div[1]/div[2]/div[1]/div[2]/div[1]")
        match.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/live/mma/bellator/event-16147/', "No match"





