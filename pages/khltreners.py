from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class Treners:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/hockey/L/khl/2023-2024/trainers/')
        sleep(6)

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'FONBET Чемпионат КХЛ. Тренеры')]")

    def text(self):
        text = self.browser.find_element(By.XPATH,"//div[@class='sp-page__title']//h1[contains(text(),'Тренеры')]")

    def mixa(self):
        mixa = self.browser.find_element(By.XPATH,"//img[@title='Кравец Михаил']")
        mixa.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/hockey/L/trainer/206/', "Не правильный тренер"
        self.browser.back()

    def spisok(self,count):
        spisok = self.browser.find_elements(By.XPATH,"//td[@class='se-advanced-table-cell se-advanced-table-cell-fix-left se-advanced-table-cell-fix-left-last']")
        assert len(spisok) == count

    def knop(self):
        knop = self.browser.find_element(By.XPATH,"//div[@class='se-button']")
        knop.click()

    def scroll(self):
        scroll = self.browser.find_element(By.XPATH,"//footer[@class='se-footer']")
        scroll = self.browser.execute_script("arguments[0].scrollIntoView();", scroll)
        sleep(5)

    def smi2(self):
        smi2 = self.browser.find_element(By.XPATH,"//div[@id='adfox_159523826122331374']")




