
from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class Shlem :

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/tennis/grand-slam/')


    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[normalize-space()='Australian Open 2025']")

    def dop_menu(self):
        dop_menu = self.browser.find_element(By.XPATH,"//div[@class='se-subpopup-menu__button']")
        dop_menu.click()

    def obsh(self):
        obsh = self.browser.find_element(By.XPATH,"//a[normalize-space()='Australian Open']")
        obsh.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/tennis/L/big/ausopen/', "No reviews"












