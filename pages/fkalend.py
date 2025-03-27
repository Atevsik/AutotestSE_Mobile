
from itertools import count
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select

class FormulaCalend:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/autosport/formula1/calendar/')
        sleep(6)

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//span[contains(text(),'Календарь гонок')]")

    def dop_menu(self):
        dop_menu = self.browser.find_element(By.XPATH,"//div[@class='se-subpopup-menu__button']")
        dop_menu.click()

    def obsh(self):
        obsh = self.browser.find_element(By.XPATH,"//a[contains(text(),'Кубок конструкторов')]")
        obsh.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/autosport/formula1/results/constructor/', "No reviews"

    def vibor(self):
        vibor = self.browser.find_element(By.XPATH, "(//select)[1]")
        vibor.click()
        select = Select(vibor)
        select.select_by_index(1)
        sleep(5)
        assert self.browser.current_url == 'https://m.sport-express.ru/autosport/formula1/results/constructor/?season=2024', "Не правильный урл"

    def reklama(self):
        reklama = self.browser.find_element(By.XPATH,"//div[@id='adfox_159072868052985816']")

    def redbull(self):
        redbull = self.browser.find_element(By.XPATH,"//div[@title='Red Bull']")
        redbull.click()

    def serxio(self):
        serxio = self.browser.find_element(By.XPATH,"//a[contains(text(),'Серхио Перес')]")
        serxio.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/autosport/formula1/drivers/peres-serhio-619/', "no serxio"















