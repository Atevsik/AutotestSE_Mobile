
from itertools import count
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select

class LifeStyleFilm:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/zozh/movies/')
        sleep(6)

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//div[@class='se-photogallery-swipe__image']//img")

    def topnews(self):
        topnews = self.browser.find_element(By.XPATH,"//div[@class='ls-mainpage__block ls-mainpage__block--topnews']")

    def reviews(self):
        reviews = self.browser.find_element(By.XPATH,"//div[@class='ls-main-articles']")

    def qa(self):
        qa = self.browser.find_element(By.XPATH,"//div[@class='ls-qa']")

    def hotnews(self):
        hotnews = self.browser.find_element(By.XPATH,"//div[@class='ls-best-materials-main-page']")

    def expert(self):
        expert = self.browser.find_element(By.XPATH,"//div[@class='ls-experts']")

    def recept(self):
        recept = self.browser.find_element(By.XPATH,"//div[@class='ls-mainpage__rubrics ls-mainpage__rubrics--top']//div//a[@class='ls-rubric-menu-item ls-rubric-menu-item--sub'][contains(text(),'Фильмы')]")
        recept.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/tag/kino-9843/'

    def h2(self):
        h2 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'Фильмы')]")

    def h3(self):
        h3 = self.browser.find_element(By.XPATH,"//h2[contains(text(),'Все материалы')]")




