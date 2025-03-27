
from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class BiatlonMir:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/biathlon/chempionat-mira/')
        sleep(6)

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'Чемпионат мира по биатлону')]")

    def dop_menu(self):
        dop_menu = self.browser.find_element(By.XPATH,"//div[@class='se-subpopup-menu__button']")
        dop_menu.click()

    def obsh(self):
        obsh = self.browser.find_element(By.XPATH,"//a[@href='https://m.sport-express.ru/winter/biathlon/chempionat-mira/medals/teams/all/']")
        obsh.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/winter/biathlon/chempionat-mira/2024-2025/medals/teams/all/', "No OBSH"

    def usa(self):
        usa = self.browser.find_element(By.XPATH,"//div[contains(text(),'США')]")
        usa.click()

    def m(self):
        m = self.browser.find_element(By.XPATH,"//a[@class='se-buttons-toggle-item'][contains(text(),'М')]")
        m.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/winter/biathlon/chempionat-mira/2024-2025/medals/teams/men/',"No men"

    def j(self):
        j = self.browser.find_element(By.XPATH, "//a[@class='se-buttons-toggle-item'][contains(text(),'Ж')]")
        j.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/winter/biathlon/chempionat-mira/2024-2025/medals/teams/women/', "No W"

    def s(self):
        s = self.browser.find_element(By.XPATH, "//a[@class='se-buttons-toggle-item'][contains(text(),'С')]")
        s.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/winter/biathlon/chempionat-mira/2024-2025/medals/teams/mixed/', "No mix"







