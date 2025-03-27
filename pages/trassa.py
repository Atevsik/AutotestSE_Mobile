
from itertools import count
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select

class FormulaTrassa:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/autosport/formula1/drivers/hemilton-lyuis-275/')
        sleep(6)

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//span[contains(text(),'Льюис Хэмилтон')]")

    def text(self):
        text = self.browser.find_element(By.XPATH,"//p[3]")

    def dop_menu(self):
        dop_menu = self.browser.find_element(By.XPATH,"//div[@class='se-subpopup-menu__button']")
        dop_menu.click()

    def obsh(self):
        obsh = self.browser.find_element(By.XPATH,"//a[contains(text(),'Трассы')]")
        obsh.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/autosport/formula1/circuits/', "No reviews"

    def fera(self):
        fera = self.browser.find_element(By.XPATH,"//a[normalize-space()='Autodromo Enzo e Dino Ferrari']")
        fera.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/autosport/formula1/circuits/autodromo-enzo-e-dino-ferrari-9/', "no fera"















