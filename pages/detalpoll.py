from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class DetalPoll:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/football/rfpl/poll/manfred-ugalde-chto-pokazhet-novyy-forvard-v-spartake-2174067/')

    def tablo(self):
        tablo = self.browser.find_element(By.XPATH,"//div[@class='se-translation-scoreboard__events']")

    def knopki(self):
        knopki = self.browser.find_element(By.XPATH,"//div[@class='se-translation-scoreboard__buttons-intervals']")

    def reklama(self):
        reklama = self.browser.find_element(By.XPATH,"//div[@id='adfox_150116181456951773']")

    def detal_menu(self):
        detal_menu = self.browser.find_element(By.XPATH,"//div[@class='se-subpopup-menu__button']")

    def header(self):
        header = self.browser.find_element(By.XPATH,"//div[@class='se-header-mob__inner-stripe']")




