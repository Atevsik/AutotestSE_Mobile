from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class Autor:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/editorial/')

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'Редакция')]")

    def safin(self):
        safin = self.browser.find_element(By.XPATH,"//img[@alt='Марат Сафин']")
        safin.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/author/marat-safin/', "Не правильный сафин"
        self.browser.back()

    def h2(self):
        h2 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'Авторы')]")

    def olen(self):
        olen = self.browser.find_element(By.XPATH,"//img[@alt='Дмитрий Аленичев']")
        olen.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/author/dmitriy-alenichev/', "Не правильный олень"
        self.browser.back()

    def proverka(self,count):
        proverka = self.browser.find_elements(By.XPATH,"//div[@class='se-author-list__item']")
        assert len(proverka) == count

    def next(self):
        next = self.browser.find_element(By.XPATH,"//body/section[@id='pageone']/div[@class='se-center-wrapper']/div/div[@class='se-authors-page']/div[@class='se-authors-page']/div[@class='se-authors-page__group']/div[2]/div[1]/div[2]/div[1]")
        next.click()







