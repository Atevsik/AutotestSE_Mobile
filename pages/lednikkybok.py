
from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class FigyrkaKybok:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/biathlon/kubok-mira/')
        sleep(6)

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'Кубок мира по биатлону')]")

    def dop_menu(self):
        dop_menu = self.browser.find_element(By.XPATH,"//div[@class='se-subpopup-menu__button']")
        dop_menu.click()

    def obsh(self):
        obsh = self.browser.find_element(By.XPATH,"//a[contains(text(),'Общий зачет')]")
        obsh.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/winter/biathlon/kubok-mira/2024-2025/standing/men/', "No kubok"

    def be(self):
        be = self.browser.find_element(By.XPATH,"//a[contains(text(),'Йоханнес Бе')]")
        be.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/tag/yohannes-be-11383/', "No be"
        self.browser.back()

    def li4ka(self):
        li4ka = self.browser.find_element(By.XPATH,"//div[@class='se-select__value-container'][contains(text(),'Личный зачет')]")
        li4ka.click()

    def kubok(self):
        kubok = self.browser.find_element(By.XPATH,"//div[@class='se-page-filter']//div[@class='se-select__items']//div[3]")
        kubok.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/winter/biathlon/kubok-mira/2024-2025/nationscup/men/', "No kubok"

    def ukr(self):
        ukr = self.browser.find_element(By.XPATH,"//a[contains(text(),'Украина')]")
        ukr.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/tag/sbornaya-ukrainy-biatlon-15629/', "No ukr"
        self.browser.back()

    def wom(self):
        wom = self.browser.find_element(By.XPATH,"//a[@class='se-buttons-toggle-item']")
        wom.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/winter/biathlon/kubok-mira/2024-2025/nationscup/women/', "No women"

    def fra(self):
        fra = self.browser.find_element(By.XPATH,"//a[@class='se-router-link'][contains(text(),'Франция')]")
        fra.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/tag/sbornaya-francii-biatlon-14320/', "No fra"






