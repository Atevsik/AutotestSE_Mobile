from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class Stadions:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/hockey/L/khl/2023-2024/stadiums/')
        sleep(6)

    def dopmenu(self):
        dopmenu = self.browser.find_element(By.XPATH, "//div[@class='se-subpopup-menu__button']")

    def header(self):
        header = self.browser.find_element(By.XPATH, "//div[@class='se-header-mob__inner-stripe']")

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'FONBET Чемпионат КХЛ. Стадионы')]")

    def h1v1(self):
        h1v1 = self.browser.find_element(By.XPATH,"//div[@class='sp-page__title']//h1[contains(text(),'Стадионы')]")

    def stadion(self):
        stadion = self.browser.find_element(By.XPATH,"//a[contains(text(),'ВТБ Арена')]")
        stadion.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/hockey/L/stadium/452/', "Не правильный стадион"
        self.browser.back()

    def comand(self):
        comand = self.browser.find_element(By.XPATH,"//a[contains(text(),'МХК Спартак')]")
        comand.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/tag/mhk-spartak-11491/', "Не правильная команда"
        self.browser.back()

    def scroll(self):
        scroll = self.browser.find_element(By.XPATH, "//footer[@class='se-footer']")
        scroll = self.browser.execute_script("arguments[0].scrollIntoView();", scroll)
        sleep(5)

    def smi2(self):
        smi2 = self.browser.find_element(By.XPATH, "//div[@id='adfox_159523826122331374']")

