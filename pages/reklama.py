from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class Reklama:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/advert/www/')
        sleep(6)

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'Реклама на ресурсах «Спорт-Экспресс»')]")

    def ever(self):
        ever = self.browser.find_element(By.XPATH,"//a[contains(text(),'ЭВЕРЕСТ')]")
        ever.click()
        assert self.browser.current_url == 'https://www.everest-sales.ru/', "Не правильный эверест"
        self.browser.back()

    def name1(self):
        name1 = self.browser.find_element(By.XPATH,"//b[contains(text(),'Алёна Ширяева')]")

    def tell1(self):
        tell1 = self.browser.find_element(By.XPATH,"//a[normalize-space()='Eshiryaeva@eve.rest']")

    def name2(self):
        name2 = self.browser.find_element(By.XPATH,"//b[contains(text(),'Олег Лукьянов')]")

    def tel2(self):
        tel2 = self.browser.find_element(By.XPATH,"//a[normalize-space()='o.lukyanov@sport-express.ru']")

    def name3(self):
        name3 = self.browser.find_element(By.XPATH,"//b[contains(text(),'Мария Маркова')]")

    def tel3(self):
        tel3 = self.browser.find_element(By.XPATH,"//a[normalize-space()='m.markova@sport-express.ru']")
