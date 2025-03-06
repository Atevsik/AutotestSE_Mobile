
from itertools import count
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select

class GandballEuro:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/handball/europe/')

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'Чемпионат Европы по гандболу')]")

    def dop_menu(self):
        dop_menu = self.browser.find_element(By.XPATH,"//div[@class='se-subpopup-menu__button']")

    def news(self):
        news = self.browser.find_element(By.XPATH,"//div[@class='se-newsline']//section[@class='se-titled-block']")

    def reviews(self):
        reviews = self.browser.find_element(By.XPATH,"//div[@class='se-articles-block']//div[@class='se-titled-block__content']")






