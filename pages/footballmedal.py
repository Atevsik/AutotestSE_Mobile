from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class FootballOlimpMedal:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/olympics/summer/football/2016/medals/')
        sleep(6)

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'Медальный зачет')]")

    def comand(self,count):
        comand = self.browser.find_elements(By.XPATH,"//td[@class='se-olympic-medals-short__table-col--country']")
        assert len(comand) == count

    def sved(self):
        sved = self.browser.find_element(By.XPATH,"//td[@class='se-olympic-medals-short__table-col--country']//a[contains(text(),'Швеция')]")
        sved.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/olympics/summer/2016/medals/swe/', "Sved"
        self.browser.back()

    def h2(self):
        h2 = self.browser.find_element(By.XPATH,"//h2[contains(text(),'Призёры и медали')]")


























