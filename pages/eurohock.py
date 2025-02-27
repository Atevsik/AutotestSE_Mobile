from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class EuroHock:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/hockey/L/europe/2023-2024/calendar/')

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'Еврохоккейтур. Календарь/Результаты')]")

    def book(self):
        book = self.browser.find_element(By.XPATH,"//div[@class='sp-competition-calendar__extra']")

    def scroll(self):
        scroll = self.browser.find_element(By.XPATH, "//footer[@class='se-footer']")
        scroll = self.browser.execute_script("arguments[0].scrollIntoView();", scroll)
        sleep(5)

    def smi2(self):
        smi2 = self.browser.find_element(By.XPATH, "//div[@id='adfox_159523826122331374']")















