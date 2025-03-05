from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class NHL3:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/hockey/nhl/nashi-v-nhl-pervaya-trojka/')

    def header(self):
        header = self.browser.find_element(By.XPATH,"//div[@class='se-header-mob__inner-stripe']")

    def tablo(self):
        tablo = self.browser.find_element(By.XPATH,"//div[@class='se-translation-scoreboard__events']")

    def knopki(self):
        knopki = self.browser.find_element(By.XPATH,"//div[@class='se-translation-scoreboard__buttons-intervals']")

    def top_material(self):
        top_material = self.browser.find_element(By.XPATH, "//div[@class='se-top-materials']")

    def knopka_all_news(self):
        knopka_all_news = self.browser.find_element(By.XPATH, "//a[@class='se-button se-button--size-middle']")
        knopka_all_news.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/hockey/nhl/nashi-v-nhl-pervaya-trojka/news/', "Не правильные главные новости"
        self.browser.back()

    def podval(self):
        podval = self.browser.find_element(By.XPATH, "//footer[@class='se-footer']")

    def knoka_podval1(self):
        knopka_podval1 = self.browser.find_element(By.XPATH, "//a[contains(text(),'Редакция')]")
        knopka_podval1.click()
        sleep(4)
        assert self.browser.current_url == 'https://m.sport-express.ru/editorial/', "Не правильная редакция"
        self.browser.back()

    def knoka_podval2(self):
        knopka_podval2 = self.browser.find_element(By.XPATH, "//a[contains(text(),'Подписка на газету')]")
        knopka_podval2.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/subscribe/', "Не правильная газета"
        self.browser.back()

    def knoka_podval3(self):
        knopka_podval3 = self.browser.find_element(By.XPATH, "//a[contains(text(),'Отдел рекламы')]")
        knopka_podval3.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/advert/www/', "Не правильная реклама"
        self.browser.back()

    def knoka_podval4(self):
        knopka_podval4 = self.browser.find_element(By.XPATH, "//a[contains(text(),'Вход / регистрация')]")
        knopka_podval4.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/profile/', "Не правильный вход"
        self.browser.back()

    def knoka_podval5(self):
        knopka_podval5 = self.browser.find_element(By.XPATH, "//a[contains(text(),'Написать в редакцию')]")

    def knoka_podval6(self):
        knopka_podval6 = self.browser.find_element(By.XPATH, "//a[contains(text(),'Правовая информация')]")
        knopka_podval6.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/company/usematerial/', "Не правильное инфо"
        self.browser.back()

    def knoka_podval7(self):
        knopka_podval7 = self.browser.find_element(By.XPATH, "//a[contains(text(),'Проверка фактов')]")
        knopka_podval7.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/company/checkfacts/', "Не правильные факты"
        self.browser.back()

    def knoka_podval8(self):
        knopka_podval8 = self.browser.find_element(By.XPATH, "//a[contains(text(),'Контакты')]")
        knopka_podval8.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/company/contacts/', "Не правильные контакты"
