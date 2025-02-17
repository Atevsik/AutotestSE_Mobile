from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class MC:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/live/')

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//div[@class='sp-sport-page__title']")

    def dopmenu(self):
        dopmenu = self.browser.find_element(By.XPATH,"//div[@class='se-subpopup-menu__button']")

    def reklama(self):
        reklama = self.browser.find_element(By.XPATH,"//div[@id='adfox_150116232399767734']")

    def header(self):
        header = self.browser.find_element(By.XPATH,"//div[@class='se-header-mob__inner-stripe']")

    def knopi(self):
        knopi = self.browser.find_element(By.XPATH,"//div[@data-component='matchcenter-filter']")

    def h2(self):
        h2 = self.browser.find_element(By.XPATH,"//div[@class='sp-sport-page__title']")

    def sport_navigator(self):
        sport_navigator = self.browser.find_element(By.XPATH,"//div[@class='se-sport-navigator__sport']")

    def scroll(self):
        scroll = self.browser.find_element(By.XPATH,"//footer[@class='se-footer']")
        scroll = self.browser.execute_script("arguments[0].scrollIntoView();", scroll)
        sleep(5)

    def smi2(self):
        smi2 = self.browser.find_element(By.XPATH,"//div[@id='adfox_159072868052985816']")


