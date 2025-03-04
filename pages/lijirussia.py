
from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class LijiRussia:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/skiing/chempionat-rossii/')
        sleep(6)

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'Чемпионат России по лыжным гонкам 2024')]")

    def dop_menu(self):
        dop_menu = self.browser.find_element(By.XPATH,"//div[@class='se-subpopup-menu__button']")
        dop_menu.click()

    def obsh(self):
        obsh = self.browser.find_element(By.XPATH,"//a[@href='https://m.sport-express.ru/skiing/chempionat-rossii/reviews/']")
        obsh.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/skiing/chempionat-rossii/reviews/', "No reviews"










