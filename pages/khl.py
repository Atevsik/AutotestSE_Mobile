from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class KHL:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/hockey/khl/')
        sleep(6)

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'КХЛ 2024 - 2025')]")

    def dop_menu(self):
        dop_menu = self.browser.find_element(By.XPATH,"//div[@class='se-subpopup-menu__button']")
        dop_menu.click()

    def table(self):
        table = self.browser.find_element(By.XPATH,"//a[contains(text(),'Таблицы')]")
        table.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/hockey/L/khl/2024-2025/?type=division'

    def h2(self):
        h2 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'FONBET КХЛ. Турнирная таблица')]")

    def konf1(self):
        konf1 = self.browser.find_element(By.XPATH,"//h2[contains(text(),'Западная конференция')]")

    def konf2(self):
        konf2 = self.browser.find_element(By.XPATH,"//h2[contains(text(),'Восточная конференция')]")

    def so4(self):
        so4 = self.browser.find_element(By.XPATH,"//div[@class='sp-team-image-with-name__name']//a[contains(text(),'Сочи')]")
        so4.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/tag/sochi-hokkey-11503/',"Не правильный сочи"
        self.browser.back()

    def konferen(self):
        konferen = self.browser.find_element(By.XPATH,"//a[contains(text(),'Конференции')]")
        konferen.click()
        sleep(5)
        assert self.browser.current_url == 'https://m.sport-express.ru/hockey/L/khl/2024-2025/?type=conference', "Не правильная конференция"

    def vost(self):
        vost = self.browser.find_element(By.XPATH,"//div[contains(text(),'Восточная конференция')]")

    def zap(self):
        zap = self.browser.find_element(By.XPATH,"//div[contains(text(),'Западная конференция')]")

    def scroll(self):
        scroll = self.browser.find_element(By.XPATH, "//footer[@class='se-footer']")
        scroll = self.browser.execute_script("arguments[0].scrollIntoView();", scroll)
        sleep(5)

    def smi2(self):
        smi2 = self.browser.find_element(By.XPATH,"//div[@id='adfox_159523826122331374']")

    def obsh(self):
        obsh = self.browser.find_element(By.XPATH,"//a[contains(text(),'Общая')]")
        obsh.click()
        sleep(5)
        assert self.browser.current_url == 'https://m.sport-express.ru/hockey/L/khl/2024-2025/?type=tour', "Не правильная общая"

    def regulr(self):
        regulr = self.browser.find_element(By.XPATH,"//th[@class='se-advanced-table-cell']//div[contains(text(),'Регулярный чемпионат')]")

    def dinamo(self):
        dinamo = self.browser.find_element(By.XPATH,"//tbody/tr[10]/td[2]/div[1]/div[2]/a[1]")
        dinamo.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/tag/dinamo-moskva-hokkey-520/', "Не правильный динамо"








