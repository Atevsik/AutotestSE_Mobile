
from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class LijiMir:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/skiing/kubok-mira/')
        sleep(6)

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'Кубок мира по лыжным гонкам')]")

    def dop_menu(self):
        dop_menu = self.browser.find_element(By.XPATH,"//div[@class='se-subpopup-menu__button']")
        dop_menu.click()

    def obsh(self):
        obsh = self.browser.find_element(By.XPATH,"//div[@class='se-element-popupmenu__item se-subpopup-menu-popup__item']//a[contains(text(),'Календарь')]")
        obsh.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/winter/skiing/kubok-mira/2024-2025/calendar/', "No kubok"

    def reklama(self):
        reklama = self.browser.find_element(By.XPATH,"//div[@id='adfox_150116181456951773']")

    def book(self):
        book = self.browser.find_element(By.XPATH,"//div[@class='se-bookie-badge-with-adv']")

    def gonka(self):
        gonka = self.browser.find_element(By.XPATH,"//div[contains(text(),'Гонка преследования, 15 км, мужчины')]")
        gonka.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/live/skiing/kubok-mira/event-16285/', "no game"
        self.browser.back()










