from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class Podpis:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/subscribe/')
        sleep(6)

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h2[contains(text(),'-')]")

    def gazeta1(self):
        gazeta1 = self.browser.find_element(By.XPATH,"//section[@id='pageone']//section[1]")

    def oformit(self):
        oformit = self.browser.find_element(By.XPATH,"(//a[contains(text(),'Оформить подписку')])[1]")

    def knp(self):
        knp = self.browser.find_element(By.XPATH,"//a[contains(text(),'Подробнее')]")
        knp.click()
        assert self.browser.current_url == 'https://www.ural-press.ru/'













