from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class MmaRait:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/fighting/mma/ufc/2024/ratings/men/')
        sleep(6)

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//div[@class='sp-sport-page__title']")

    def boets(self,count):
        boets = self.browser.find_elements(By.XPATH,"//td[@class='se-advanced-table-cell']")
        assert len(boets) == count

    def boet(self):
        boet = self.browser.find_element(By.XPATH,"//a[contains(text(),'Тацуро Тайра')]")
        boet.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/tag/tacuro-tayra-26076/', "No boets"
        self.browser.back()

    def champion(self):
        champion = self.browser.find_element(By.XPATH,"//div[@class='se-fighter-champion-panel__inner']")

    def women(self):
        women = self.browser.find_element(By.XPATH,"//div[@class='se-buttons-toggle-item']")
        women.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/fighting/mma/ufc/2024/ratings/women/', "No women"

    def player(self):
        player = self.browser.find_element(By.XPATH,"//a[contains(text(),'Манон Фиро')]")
        player.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/tag/manon-firo-25322/', "No Player"



