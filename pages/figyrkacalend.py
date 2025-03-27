
from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class FigyrkaCalend:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/figure-skating/chempionat-rossii/')
        sleep(6)
        sleep(5)

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'Чемпионат России по фигурному катанию 2024')]")

    def dop_menu(self):
        dop_menu = self.browser.find_element(By.XPATH,"//div[@class='se-subpopup-menu__button']")
        dop_menu.click()

    def obsh(self):
        obsh = self.browser.find_element(By.XPATH,"//a[@href='https://m.sport-express.ru/winter/figure-skating/chempionat-rossii/calendar/']")
        obsh.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/winter/figure-skating/chempionat-rossii/2024-2025/calendar/', "No obsh"

    def h2(self):
        h2 = self.browser.find_element(By.XPATH,"//div[@class='sp-sport-page__title']")

    def book(self):
        book = self.browser.find_element(By.XPATH,"//div[@class='se-bookie-badge-with-adv']")

    def event(self):
        event = self.browser.find_element(By.XPATH,"//div[contains(text(),'Танцы, ритм-танец')]")
        event.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/live/figure-skating/chempionat-rossii/event-16437/', "No event"
        self.browser.back()













