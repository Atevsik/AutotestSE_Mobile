
from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class FigyrkaGranPri:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/figure-skating/grand-pri-rossii/')
        sleep(6)
        sleep(5)

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'Гран-при России по фигурному катанию')]")

    def dop_menu(self):
        dop_menu = self.browser.find_element(By.XPATH,"//div[@class='se-subpopup-menu__button']")
        dop_menu.click()

    def obsh(self):
        obsh = self.browser.find_element(By.XPATH,"//a[contains(text(),'Общий зачет')]")
        obsh.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/winter/figure-skating/grand-pri-rossii/2024-2025/standing/men/', "No obsh"

    def h2(self):
        h2 = self.browser.find_element(By.XPATH,"//div[@class='sp-sport-page__title']")

    def gleb(self):
        gleb = self.browser.find_element(By.XPATH,"//a[contains(text(),'Глеб Лутфуллин')]")
        gleb.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/tag/gleb-lutfullin-23885/', "No gleb"
        self.browser.back()

    def dance(self):
        dance = self.browser.find_element(By.XPATH,"//a[contains(text(),'Танцы')]")
        dance.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/winter/figure-skating/grand-pri-rossii/2024-2025/standing/dance/', "No dance"

    def sofia(self):
        sofia = self.browser.find_element(By.XPATH,"//a[contains(text(),'София Леонтьева / Даниил Горелкин')]")
        sofia.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/tag/sofiya-leonteva-daniil-gorelkin-28971/', "No sofia"
        self.browser.back()

    def jen(self):
        jen = self.browser.find_element(By.XPATH,"//a[contains(text(),'Жен')]")
        jen.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/winter/figure-skating/grand-pri-rossii/2024-2025/standing/women/', "No women"

    def anna(self):
        anna = self.browser.find_element(By.XPATH, "//a[contains(text(),'Анна Фролова')]")
        anna.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/tag/anna-frolova-18660/', "No anna"
        self.browser.back()

    def pari(self):
        pari = self.browser.find_element(By.XPATH,"//a[contains(text(),'Пары')]")
        pari.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/winter/figure-skating/grand-pri-rossii/2024-2025/standing/pair/', "No pari"











