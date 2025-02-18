from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class TagComand:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/tag/spartak-futbol-514/')

    def info(self):
        info = self.browser.find_element(By.XPATH,"//td[normalize-space()='1922']")

    def info1(self):
        info1 = self.browser.find_element(By.XPATH,"//td[contains(text(),'Вид спорта:')]")

    def football(self):
        football = self.browser.find_element(By.XPATH,"//u[contains(text(),'Футбол')]")
        football.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/football/', "Не правильный футбол"
        self.browser.back()

    def spotrsmen(self):
        sportsmen = self.browser.find_element(By.XPATH,"//a[contains(text(),'Все о клубе')]")
        sportsmen.click()
        assert self.browser.current_url == 'https://www.sport-express.ru/football/L/command/1/', "Не правильный спортсмен"
        self.browser.back()

    def read_next(self):
        read_next = self.browser.find_element(By.XPATH,"//button[contains(text(),'Читать полностью')]")
        read_next.click()

    def text(self):
        text = self.browser.find_element(By.XPATH,"//p[contains(text(),'«Спартак» - 12-кратный чемпион СССР и 10-кратный ч')]")

    def material(self,count):
        material = self.browser.find_elements(By.XPATH,"//div[@class='se19-news-feed__item']")
        assert len(material) == count

