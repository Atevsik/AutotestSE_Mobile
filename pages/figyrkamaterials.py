
from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class FigyrkaNews:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/figure-skating/ice-age/')

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'Ледниковый период')]")

    def dop_menu(self):
        dop_menu = self.browser.find_element(By.XPATH,"//div[@class='se-subpopup-menu__button']")
        dop_menu.click()

    def obsh(self):
        obsh = self.browser.find_element(By.XPATH,"//a[@href='https://m.sport-express.ru/figure-skating/ice-age/materials/']")
        obsh.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/figure-skating/ice-age/materials/', "No materials"

    def knp1(self):
        knp1 = self.browser.find_element(By.XPATH,"//a[contains(text(),'Главные')]")
        knp1.click()
        sleep(10)
        assert self.browser.current_url == 'https://m.sport-express.ru/figure-skating/ice-age/materials/?isEditorialChoice=1'



