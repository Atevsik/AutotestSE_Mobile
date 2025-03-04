from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class Brend:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/brend-centr/?showforever')
        sleep(6)

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[@class='se-sub-header__title']")

    def knp(self,count):
        knp = self.browser.find_elements(By.XPATH,"//a[@class='se19-button pv_10 ph_0 t_center']")
        assert len(knp) == count

    def h2(self):
        h2 = self.browser.find_element(By.XPATH,"//h2[contains(text(),'АЛЬТЕРНАТИВНЫЙ ЗНАК')]")










