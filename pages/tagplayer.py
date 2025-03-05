from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class TagPlayer:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/tag/valeriy-karpin-135/')

    def info(self):
        info = self.browser.find_element(By.XPATH,"//td[contains(text(),'2 февраля 1969')]")

    def info1(self):
        info1 = self.browser.find_element(By.XPATH,"//td[contains(text(),'Вид спорта:')]")

    def football(self):
        football = self.browser.find_element(By.XPATH,"//u[contains(text(),'Футбол')]")
        football.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/football/', "Не правильный футбол"
        self.browser.back()

    def spotrsmen(self):
        sportsmen = self.browser.find_element(By.XPATH,"//a[contains(text(),'Все о спортсмене')]")
        sportsmen.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/football/L/player/9477/seasons/2002/', "Не правильный спортсмен"
        self.browser.back()

    def bio(self):
        bio = self.browser.find_element(By.XPATH,"//a[contains(text(),'Биография')]")
        bio.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/football/rusteam/reviews/biografiya-valeriya-karpina-sportivnaya-karera-i-lichnaya-zhizn-byvshego-rossiyskogo-futbolista-i-nyneshnego-trenera-rostova-i-sbornoy-rossii-1831504/', "Не правильная био"
        self.browser.back()

    def read_next(self):
        read_next = self.browser.find_element(By.XPATH,"//button[contains(text(),'Читать полностью')]")
        read_next.click()

    def text(self):
        text = self.browser.find_element(By.XPATH,"//font[contains(text(),'Тренировал «Спартак», «Мальорку» и армавирское «То')]")

    def material(self,count):
        material = self.browser.find_elements(By.XPATH,"//div[@class='se19-news-feed__item']")
        assert len(material) == count

    def next(self):
        next = self.browser.find_element(By.XPATH,"//a[contains(text(),'Далее')]")
        next.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/tag/valeriy-karpin-135/page2/', "Не правлиьная вторая страница"

