from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class World:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/hockey/world/')

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'Чемпионат мира по хоккею 2024')]")

    def dop_menu(self):
        dop_menu = self.browser.find_element(By.XPATH,"//div[@class='se-subpopup-menu__button']")
        dop_menu.click()

    def stat(self):
        stat = self.browser.find_element(By.XPATH,"//a[contains(text(),'Статистика')]")
        stat.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/hockey/L/world/2025/statistic/'

    def h2(self):
        h2 = self.browser.find_element(By.XPATH,"//h1[@class='se-sub-header__title']")

    def dop_menu2(self):
        dop_menu2 = self.browser.find_element(By.XPATH,"//div[@class='se-page-filters__button']//span//*[name()='svg']")
        dop_menu2.click()
        self.browser.get('https://m.sport-express.ru/hockey/L/world/2024/statistic/')

    def info(self,count):
        info = self.browser.find_elements(By.XPATH,"//td[@class='se-advanced-table-cell']")
        assert len(info) == count

    def tag(self):
        tag = self.browser.find_element(By.XPATH,"//body[1]/section[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[4]/a[1]")
        tag.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/hockey/L/player/12994/',"Не правильный тег"
        self.browser.back()

    def li4ka(self):
        li4ka = self.browser.find_element(By.XPATH,"//a[contains(text(),'Личная')]")
        li4ka.click()
        sleep(4)
        assert self.browser.current_url == 'https://m.sport-express.ru/hockey/L/world/2024/statistic/players/', "Не правильная личка"

    def player(self):
        player = self.browser.find_element(By.XPATH,"//img[@title='Червенка Роман']")
        player.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/tag/roman-chervenka-1694/', "Не правильный игрок"
        self.browser.back()

    def vratar(self):
        vratar = self.browser.find_element(By.XPATH,"//a[contains(text(),'Вратари')]")
        vratar.click()
        sleep(4)
        assert self.browser.current_url == 'https://m.sport-express.ru/hockey/L/world/2024/statistic/players/?role=goalkeepers', "Не правильный вратарь"

    def player2(self):
        player2 = self.browser.find_element(By.XPATH,"//img[@title='Достал Лукаш']")
        player2.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/hockey/L/player/16657/', "Не правильный игрок2"
        self.browser.back()

    def zash(self):
        zash = self.browser.find_element(By.XPATH,"//a[contains(text(),'Защитники')]")
        zash.click()
        sleep(4)
        assert self.browser.current_url == 'https://m.sport-express.ru/hockey/L/world/2024/statistic/players/?role=defenses', "Не правильный защитник"

    def player3(self):
        player3 = self.browser.find_element(By.XPATH, "//img[@title='Овитю Йоанн']")
        player3.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/tag/yoann-ovityu-14153/', "Не правильный игрок3"
        self.browser.back()

    def nap(self):
        nap = self.browser.find_element(By.XPATH,"//a[contains(text(),'Нападающие')]")
        nap.click()
        sleep(4)
        assert self.browser.current_url == 'https://m.sport-express.ru/hockey/L/world/2024/statistic/players/?role=forwards', "Не правильный напдающий"

    def player4(self):
        player4 = self.browser.find_element(By.XPATH, "//img[@title='Годро Джонни']")
        player4.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/tag/dzhonni-godro-12941/', "Не правильный игрок4"
        self.browser.back()
        sleep(4)

    def comand(self):
        comand = self.browser.find_element(By.XPATH,"//a[contains(text(),'Командная')]")
        comand.click()
        sleep(4)
        assert self.browser.current_url == 'https://m.sport-express.ru/hockey/L/world/2024/statistic/teams/',"Не правильная команда"

    def tablet(self,count):
        tablet = self.browser.find_elements(By.XPATH,"//div[@class='sp-team-image-with-name sp-competition-stats-teams__team']")
        assert len(tablet) == count

    def usa(self):
        usa = self.browser.find_element(By.XPATH,"//a[contains(text(),'США')]")
        usa.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/tag/sbornaya-ssha-hokkey-10639/',"Не правильная США"
        self.browser.back()

    def scroll(self):
        scroll = self.browser.find_element(By.XPATH, "//footer[@class='se-footer']")
        scroll = self.browser.execute_script("arguments[0].scrollIntoView();", scroll)
        sleep(5)

    def smi2(self):
        smi2 = self.browser.find_element(By.XPATH,"//div[@id='adfox_159523826122331374']")









