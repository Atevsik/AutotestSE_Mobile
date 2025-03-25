
from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class FigyrkaMeadal:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/figure-skating/chempionat-mira/')
        sleep(5)

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'ЧМ по фигурному катанию 2024')]")

    def dop_menu(self):
        dop_menu = self.browser.find_element(By.XPATH,"//div[@class='se-subpopup-menu__button']")
        dop_menu.click()

    def obsh(self):
        obsh = self.browser.find_element(By.XPATH,"//a[@href='https://m.sport-express.ru/winter/figure-skating/chempionat-mira/medals/teams/all/']")
        obsh.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/winter/figure-skating/chempionat-mira/2024-2025/medals/teams/all/', "No obsh"

    def h2(self):
        h2 = self.browser.find_element(By.XPATH,"//div[@class='sp-sport-page__title']")

    def god(self):
        god = self.browser.find_element(By.XPATH,"//div[@class='se-sport-navigator__season']")
        god.click()
        sleep(4)

    def v2024(self):
        v2024 = self.browser.find_element(By.XPATH,"//div[@id='react-select-seasons-option-0-1']")
        v2024.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/winter/figure-skating/chempionat-mira/2023-2024/medals/teams/all/', "No god"

    def italy(self):
        italy = self.browser.find_element(By.XPATH,"//div[contains(text(),'Италия')]")
        italy.click()

    def m(self):
        m = self.browser.find_element(By.XPATH,"//a[@class='se-buttons-toggle-item'][contains(text(),'М')]")
        m.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/winter/figure-skating/chempionat-mira/2023-2024/medals/teams/men/', "No men"

    def j(self):
        j = self.browser.find_element(By.XPATH, "//a[@class='se-buttons-toggle-item'][contains(text(),'Ж')]")
        j.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/winter/figure-skating/chempionat-mira/2023-2024/medals/teams/women/', "No w"

    def p(self):
        p = self.browser.find_element(By.XPATH, "//a[@class='se-buttons-toggle-item'][contains(text(),'П')]")
        p.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/winter/figure-skating/chempionat-mira/2023-2024/medals/teams/pairs/', "No p"

    def t(self):
        t = self.browser.find_element(By.XPATH, "//a[@class='se-buttons-toggle-item'][contains(text(),'Т')]")
        t.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/winter/figure-skating/chempionat-mira/2023-2024/medals/teams/dance/', "No t"


















