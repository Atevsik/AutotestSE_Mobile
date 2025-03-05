
from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class LijiNews:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/skiing/chempionat-mira/')

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'ЧМ по лыжным видам спорта')]")

    def dop_menu(self):
        dop_menu = self.browser.find_element(By.XPATH,"//div[@class='se-subpopup-menu__button']")
        dop_menu.click()

    def obsh(self):
        obsh = self.browser.find_element(By.XPATH,"//a[@href='https://m.sport-express.ru/skiing/news/']")
        obsh.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/skiing/news/', "No news"










