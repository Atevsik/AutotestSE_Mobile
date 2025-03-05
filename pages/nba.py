
from itertools import count
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select

class Nba:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/basketball/nba/')

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'НБА')]")

    def dop_menu(self):
        dop_menu = self.browser.find_element(By.XPATH,"//div[@class='se-subpopup-menu__button']")
        dop_menu.click()

    def obsh(self):
        obsh = self.browser.find_element(By.XPATH,"//a[contains(text(),'Календарь / результаты')]")
        obsh.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/basketball/L/men/nba/2024-2025/calendar/', "No reviews"

















