from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class MmaCalend:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/fighting/mma/ufc/2024/calendar/')
        sleep(6)

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//div[@class='sp-sport-page__title']")

    def filters(self):
        filters = self.browser.find_element(By.XPATH,"//div[@class='se-page-filters']")

    def book(self):
        book = self.browser.find_element(By.XPATH,"//div[@class='sp-calendar-fighting__bookie']")

    def match(self):
        match = self.browser.find_element(By.XPATH,"//div[@class='sp-calendar-fighting__events']//div[1]//div[2]//div[1]//div[2]//div[1]//div[1]//a[1]//div[3]//div[1]//div[2]//div[1]//div[2]//div[1]//div[1]//div[1]")
        match.click()
        sleep(4)
        assert self.browser.current_url == 'https://m.sport-express.ru/live/mma/ufc/event-16432/', "NO match"
        self.browser.back()

    def select(self):
        select = self.browser.find_element(By.XPATH,"//div[@class='se-sport-navigator__competition-name']")
        select.click()

    def aca(self):
        aca = self.browser.find_element(By.XPATH,"//div[@id='react-select-competitions-option-0-4']")
        aca.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/fighting/mma/aca/2025/calendar/', "No ACA"








