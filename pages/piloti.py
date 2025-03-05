
from itertools import count
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select

class FormulaPilot:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/autosport/formula1/teams/')

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//span[contains(text(),'Команды')]")

    def dop_menu(self):
        dop_menu = self.browser.find_element(By.XPATH,"//div[@class='se-subpopup-menu__button']")
        dop_menu.click()

    def obsh(self):
        obsh = self.browser.find_element(By.XPATH,"//div[@class='se-element-popupmenu__item se-subpopup-menu-popup__item']//a[contains(text(),'Пилоты')]")
        obsh.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/autosport/formula1/drivers/', "No reviews"

    def alex(self):
        alex = self.browser.find_element(By.XPATH,"//a[contains(text(),'Александр Албон')]")
        alex.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/autosport/formula1/drivers/albon-aleksandr-779/', "No alex"
        self.browser.back()

    def fera(self):
        fera = self.browser.find_element(By.XPATH,"//div[8]//div[4]//div[1]//div[1]//a[1]//p[1]")
        fera.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/autosport/formula1/teams/ferrari-19/?season=2025', "no fera"














