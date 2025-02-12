from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class DetalOnline:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/football/england/online/liverpul-chelsi-smotret-besplatno-match-22-tura-apl-v-pryamom-efire-onlayn-tekstovaya-translyaciya-i-rezultat-31-yanvarya-2024-2173894/')

    def header(self):
        header = self.browser.find_element(By.XPATH, "//div[@class='se-header-mob__inner-stripe']")


    def footer(self):
        footer = self.browser.find_element(By.XPATH,"//footer[@class='se-footer']")

    def podelit(self):
        podelit = self.browser.find_element(By.XPATH,"//div[@class='se-shareblock__icon']//*[name()='svg']")
        podelit.click()

    def podel_knop(self,count):
        podel_knop = self.browser.find_elements(By.XPATH,"//button[@class='react-share__ShareButton']")
        assert len(podel_knop) == count

    def teg(self):
        teg = self.browser.find_element(By.XPATH,"//p[@class='se-material-online-page__live']")

    def date_online(self):
        date_online = self.browser.find_element(By.XPATH,"//div[contains(text(),'1 февраля, 01:20')]")
