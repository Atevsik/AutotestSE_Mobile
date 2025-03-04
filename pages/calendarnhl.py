from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class CalendNhl:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/hockey/nhl/')
        sleep(6)

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'НХЛ 2024 - 2025')]")

    def dop_menu(self):
        dop_menu = self.browser.find_element(By.XPATH,"//div[@class='se-subpopup-menu__button']")
        dop_menu.click()

    def calend(self):
        calend = self.browser.find_element(By.XPATH,"//div[@class='se-element-popupmenu__item se-subpopup-menu-popup__item']//a[contains(text(),'Календарь')]")
        calend.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/hockey/L/nhl/2024-2025/calendar/', "Не правильный календарь"

    def h2(self):
        h2 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'НХЛ. Календарь/Результаты')]")

    def date(self):
        date = self.browser.find_element(By.XPATH,"//h2[@class='sp-competition-calendar__day-title']")

    def book(self):
        book = self.browser.find_element(By.XPATH,"//div[@class='sp-competition-calendar__bookie']")

    def scroll(self):
        scroll = self.browser.find_element(By.XPATH, "//footer[@class='se-footer']")
        scroll = self.browser.execute_script("arguments[0].scrollIntoView();", scroll)
        sleep(5)

    def smi2(self):
        smi2 = self.browser.find_element(By.XPATH,"//div[@id='adfox_159523826122331374']")





