from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class Spiso4Gazeta:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/newspaper/')

    def knopki(self,count):
        knopki = self.browser.find_elements(By.XPATH,"//div[@class='se19-rubricator__group']")
        assert len(knopki) == count

    def detal_knp(self):
        detal_knp = self.browser.find_element(By.XPATH,"//div[@class='se-subpopup-menu__button']")

    def polosa(self):
        polosa = self.browser.find_element(By.XPATH,"//div[contains(text(),'Полоса 1')]")

    def podval(self):
        podval = self.browser.find_element(By.XPATH,"//footer[@class='se-footer']")

    def scroll(self):
        scroll = self.browser.find_element(By.XPATH,"//footer[@class='se-footer']")
        scroll = self.browser.execute_script("arguments[0].scrollIntoView();", scroll)
        sleep(5)

    def smi2(self):
        smi2 = self.browser.find_element(By.XPATH,"//div[@id='adfox_159072868052985816']")







