from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class Golshak:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/golyshak-vspominaet/')

    def header(self):
        self.browser.find_element(By.XPATH,"//div[@class='se-header-mob__inner-stripe']")

    def reklama(self):
        reklama = self.browser.find_element(By.XPATH,"//div[@id='adfox_150116181456951773']")

    def materials(self,count):
        materials = self.browser.find_elements(By.XPATH,"//div[@class='se-articles-block__item' and not(@data-component='hidden-block')]")
        assert len(materials) == count

    def date(self):
        date = self.browser.find_element(By.XPATH,"//span[@class='se-material-preview-info__datetime ']")

    def scroll(self):
        scroll = self.browser.find_element(By.XPATH, "//footer[@class='se-footer']")
        scroll = self.browser.execute_script("arguments[0].scrollIntoView();", scroll)
        sleep(5)

    def smi2(self):
        smi2 = self.browser.find_element(By.XPATH,"//div[@id='adfox_159072868052985816']")


