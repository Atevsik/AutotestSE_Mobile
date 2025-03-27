
from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class FigyrkaSportsmn:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/winter/figure-skating/grand-pri/2022-2023/calendar/')
        sleep(6)

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//div[@class='sp-sport-page__title']")

    def dop_menu(self):
        dop_menu = self.browser.find_element(By.XPATH,"//div[@class='se-subpopup-menu__button']")
        dop_menu.click()

    def obsh(self):
        obsh = self.browser.find_element(By.XPATH,"//div[@class='se-element-popupmenu__item se-subpopup-menu-popup__item']//a[contains(text(),'Спортсмены')]")
        obsh.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/winter/figure-skating/grand-pri/2023-2024/players/', "No sportsmn"

    def h2(self):
        h2 = self.browser.find_element(By.XPATH,"//div[@class='sp-sport-page__title']")

    def uki(self):
        uki = self.browser.find_element(By.XPATH,"//a[contains(text(),'Юна Аоки')]")
        uki.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/tag/yuna-aoki-29194/', "No uki"
        self.browser.back()

    def m(self):
        m = self.browser.find_element(By.XPATH,"//div[@class='se-buttons-toggle-item'][contains(text(),'М')]")
        m.click()


    def j(self):
        j = self.browser.find_element(By.XPATH, "//div[contains(text(),'Ж')]")
        j.click()


    def p(self):
        p = self.browser.find_element(By.XPATH, "//div[@class='se-buttons-toggle-item'][contains(text(),'П')]")
        p.click()


    def t(self):
        t = self.browser.find_element(By.XPATH, "//div[@class='se-buttons-toggle-item'][contains(text(),'Т')]")
        t.click()


















