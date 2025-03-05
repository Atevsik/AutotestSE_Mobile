
from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class FigyrkaComand:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/figure-skating/chempionat-evropy/')

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'ЧЕ по фигурному катанию')]")

    def dop_menu(self):
        dop_menu = self.browser.find_element(By.XPATH,"//div[@class='se-subpopup-menu__button']")
        dop_menu.click()

    def obsh(self):
        obsh = self.browser.find_element(By.XPATH,"//a[@href='https://m.sport-express.ru/winter/figure-skating/chempionat-evropy/teams/']")
        obsh.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/winter/figure-skating/chempionat-evropy/2024-2025/teams/', "No sportsmn"

    def h2(self):
        h2 = self.browser.find_element(By.XPATH,"//div[@class='sp-sport-page__title']")

    def italy(self):
        italy = self.browser.find_element(By.XPATH,"//div[contains(text(),'Италия')]")
        italy.click()

    def sostav(self):
        sostav = self.browser.find_element(By.XPATH,"//div[@class='sp-competition-command-list__popup sp-competition-command-list__popup--open']//a[@class='sp-competition-command-list__popup-compound'][contains(text(),'Состав')]")
        sostav.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/tag/sbornaya-italii-figure-skating-20320/composition/', "No sostav"

