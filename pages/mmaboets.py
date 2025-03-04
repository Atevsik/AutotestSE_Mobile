from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class MmaBoets:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/fighting/mma/ufc/2024/fighters/')
        sleep(6)

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//div[@class='se-competition-titled-block__title']")

    def player(self):
        player = self.browser.find_element(By.XPATH,"//a[contains(text(),'Дастин Джейкоби')]")
        player.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/tag/dastin-dzheykobi-25695/', "No Player"
        self.browser.back()

    def women(self):
        women = self.browser.find_element(By.XPATH,"//div[@class='se-buttons-toggle-item']")
        women.click()




