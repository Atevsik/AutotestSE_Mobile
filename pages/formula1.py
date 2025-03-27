
from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class Formula1:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/autosport/formula1/results/')
        sleep(6)

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//span[contains(text(),'Результаты')]")

    def dop_menu(self):
        dop_menu = self.browser.find_element(By.XPATH,"//div[@class='se-subpopup-menu__button']")
        dop_menu.click()

    def obsh(self):
        obsh = self.browser.find_element(By.XPATH,"//a[contains(text(),'Календарь гонок')]")
        obsh.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/autosport/formula1/calendar/', "No reviews"

    def usa(self):
        usa = self.browser.find_element(By.XPATH,"//span[contains(text(),'Гран-при Майами')]")
        usa.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/autosport/formula1/calendar/gran-pri-maiami_2025-1146/'












