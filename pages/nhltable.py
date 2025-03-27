from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class NhlTable:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/hockey/nhl/')
        sleep(6)

    def dop_menu(self):
        dop_menu = self.browser.find_element(By.XPATH,"//div[@class='se-subpopup-menu__button']")
        dop_menu.click()

    def table(self):
        table = self.browser.find_element(By.XPATH,"//a[contains(text(),'Таблицы')]")
        table.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/hockey/L/nhl/2024-2025/?type=conference', "Не правильный таблица"

    def h2(self):
        h2 = self.browser.find_element(By.XPATH, "//h1[contains(text(),'НХЛ. Турнирная таблица')]")

    def konf1(self):
        konf1 = self.browser.find_element(By.XPATH, "//h2[contains(text(),'Западная конференция')]")

    def konf2(self):
        konf2 = self.browser.find_element(By.XPATH, "//h2[contains(text(),'Восточная конференция')]")

    def so4(self):
        so4 = self.browser.find_element(By.XPATH, "//img[@title='Торонто']")
        so4.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/tag/toronto-meypl-livz-1932/', "Не правильный торонто"


    def konferen(self):
        konferen = self.browser.find_element(By.XPATH, "//a[contains(text(),'Конференции')]")
        konferen.click()
        sleep(5)
        assert self.browser.current_url == 'https://m.sport-express.ru/hockey/L/nhl/2024-2025/?type=conference', "Не правильная конференция"

    def vost(self):
        vost = self.browser.find_element(By.XPATH, "//div[contains(text(),'Восточная конференция')]")

    def zap(self):
        zap = self.browser.find_element(By.XPATH, "//div[contains(text(),'Западная конференция')]")

    def scroll(self):
        scroll = self.browser.find_element(By.XPATH, "//footer[@class='se-footer']")
        scroll = self.browser.execute_script("arguments[0].scrollIntoView();", scroll)
        sleep(5)

    def smi2(self):
        smi2 = self.browser.find_element(By.XPATH, "//div[@id='adfox_159523826122331374']")

    def obsh(self):
        obsh = self.browser.find_element(By.XPATH, "//a[contains(text(),'Общая')]")
        obsh.click()
        sleep(5)
        assert self.browser.current_url == 'https://m.sport-express.ru/hockey/L/khl/2024-2025/?type=tour', "Не правильная общая"

    def regulr(self):
        regulr = self.browser.find_element(By.XPATH, "//th[@class='se-advanced-table-cell']//div[contains(text(),'Регулярный чемпионат')]")

    def vas(self):
        vas = self.browser.find_element(By.XPATH, "//img[@title='Вашингтон']")
        vas.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/tag/vashington-kepitalz-1163/', "Не правильный вашингтон"
        self.browser.back()

    def deviz(self):
        deviz = self.browser.find_element(By.XPATH,"//a[contains(text(),'Дивизионы')]")
        deviz.click()
        sleep(5)
        assert self.browser.current_url == 'https://m.sport-express.ru/hockey/L/nhl/2024-2025/?type=division'





