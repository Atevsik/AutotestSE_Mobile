from itertools import count
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys


class Poisk:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/')
        sleep(6)

    def menu(self):
        menu = self.browser.find_element(By.XPATH, "//div[@class='se-header-mob__item se-header-mob__item--burger']")
        menu.click()

    def input(self):
        input = self.browser.find_element(By.XPATH, "//input[@id='menu-search']")
        input.clear()
        input.send_keys("Титов")
        input.send_keys(Keys.ENTER)
        sleep(4)
        assert self.browser.current_url == 'https://m.sport-express.ru/search/?sw=%D2%E8%F2%EE%E2', "Не правильный титов"

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h2[contains(text(),'Егор Титов')]")

    def text(self,count):
        text = self.browser.find_elements(By.XPATH,"//p[@class='se19-search__text']")
        assert len(text) == count

    def next_page(self):
        next_page = self.browser.find_element(By.XPATH,"//a[contains(text(),'Далее')]")
        next_page.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/search/page2/?sw=%D2%E8%F2%EE%E2', "Не правильная вторая страница"

    def scroll(self):
        scroll = self.browser.find_element(By.XPATH, "//footer[@class='se-footer']")
        scroll = self.browser.execute_script("arguments[0].scrollIntoView();", scroll)
        sleep(5)

    def smi2(self):
        smi2 = self.browser.find_element(By.XPATH,"//div[@id='adfox_159072868052985816']")



















