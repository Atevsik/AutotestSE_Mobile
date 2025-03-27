
from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class FigyrkaItogi:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/live/figure-skating/chempionat-rossii/event-16113/')
        sleep(6)

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//div[@class='sp-sport-page__title']")

    def top3(self):
        top3 = self.browser.find_element(By.XPATH,"//h2[contains(text(),'Елизавета Худайбердиева / Егор Базин')]")
        top3.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/tag/elizaveta-hudayberdyeva-egor-bazin-20784/', "No top3"
        self.browser.back()

    def book(self):
        book = self.browser.find_element(By.XPATH,"//div[@class='se-bookie-badge-with-adv']")

    def sport(self):
        sport = self.browser.find_element(By.XPATH,"//div[contains(text(),'София Качушкина / Марк Волков')]")

    def result(self):
        result = self.browser.find_element(By.XPATH,"//td[normalize-space()='76.79']")

    def footer(self):
        footer = self.browser.find_element(By.XPATH,"//footer[@class='se-footer']")
