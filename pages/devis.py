
from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class Devis:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/tennis/davis-cup/')
        sleep(6)


    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'Теннис Кубок Дэвиса 2024')]")

    def dop_menu(self):
        dop_menu = self.browser.find_element(By.XPATH,"//div[@class='se-subpopup-menu__button']")
        dop_menu.click()

    def obsh(self):
        obsh = self.browser.find_element(By.XPATH,"//a[contains(text(),'Результаты')]")
        obsh.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/tennis/L/davis/', "No reviews"










