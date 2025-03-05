from itertools import count
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

class zpKHL:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/hockey/khl/money/2023-2024/')

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[@class='se-player-salaries-main-page__title']")

    def filti(self):
        filtri = self.browser.find_element(By.XPATH,"//div[@class='se-filters-salaries']")

    def input(self):
        input = self.browser.find_element(By.XPATH, "//input[@placeholder='Игрок']")
        input.clear()
        input.send_keys("Шалунов")
        input.send_keys(Keys.ENTER)

    def proverka(self):
        proverka = self.browser.find_elements(By.XPATH,"//div[@class='se-players-salaries__player']")

    def player1(self):
        player1 = self.browser.find_element(By.XPATH,"//div[@class='se-players-salaries__player-profile_name']")
        player1.click()
        sleep(4)

    def player2(self):
        player2 = self.browser.find_element(By.XPATH,"//a[contains(text(),'Перейти в профиль')]")
        player2.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/tag/maksim-shalunov-12961/', "Не правильный игрок"
        self.browser.back()

    def select1(self):
        select1 = self.browser.find_element(By.XPATH,"//body/div[@class='se-player-salaries-layout']/main[@class='se-player-salaries-layout__content']/div[@class='se-player-salaries-main-page']/div[@class='se-player-salaries-main-page__inner']/div[@class='se-player-salaries-main-page__content']/div[@class='se-player-salaries-main-page__filters']/div[@class='se-filters-salaries']/div[2]/div[2]/div[1]/div[1]/div[1]")
        select1.click()

    def select2(self):
        select2 = self.browser.find_element(By.XPATH,"//div[@class='se-select__item'][contains(text(),'Авангард')]")
        select2.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/hockey/khl/money/2023-2024/avangard-omsk-275/', "не паврльная команда"






