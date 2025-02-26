from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class Hock24:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/hockey/world-u20/')

    def h1(self):
        self.browser.find_element(By.XPATH,"//h1[contains(text(),'Молодежный чемпионат мира по хоккею 2025')]")

    def dop_menu(self):
        dop_menu = self.browser.find_element(By.XPATH,"//div[@class='se-subpopup-menu__button']")
        dop_menu.click()

    def comand(self):
        comand = self.browser.find_element(By.XPATH,"//div[@class='se-element-popupmenu__item se-subpopup-menu-popup__item']//a[contains(text(),'Команды')]")
        comand.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/hockey/L/world-u20/2023-2024/teams/', "Не правильные команды"

    def h2(self):
        h2 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'Молодежный чемпионат мира. Команды')]")

    def spisok(self,count):
        spisok = self.browser.find_elements(By.XPATH,"//div[@class='sp-competition-teams-item sp-competition-teams-item--wide']")
        assert len(spisok) == count

    def sostav(self):
        sostav = self.browser.find_element(By.XPATH,"//div[@class='sp-competition-teams']//div[1]//div[1]//div[2]//div[2]//a[1]")
        sostav.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/hockey/L/team/106/players/', "Не правильный состав"
        self.browser.back()

    def calend(self):
        calend = self.browser.find_element(By.XPATH,"//div[4]//div[1]//div[2]//div[2]//a[2]")
        calend.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/hockey/L/world-u20/2023-2024/calendar/?team=111', "Не правильный календарь"
        self.browser.back()

    def stat(self):
        stat = self.browser.find_element(By.XPATH,"//div[8]//div[1]//div[2]//div[2]//a[3]")
        stat.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/hockey/L/team/156/players-stats/', "Не правильная стистика"














