from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class FootballOlimp:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/olympics/summer/football/2016/calendar/')

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'Календарь')]")

    def fot(self):
        fot = self.browser.find_element(By.XPATH,"//div[4]//div[2]//div[2]//div[2]//a[1]//div[1]//div[1]//div[1]//div[2]")
        fot.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/olympics/rio2016/football/fbl_match-shveciya-olimp-yuar-olimp-244164/', "Foot"
        self.browser.back()

    def men(self):
        men = self.browser.find_element(By.XPATH,"//body/section[@id='pageone']/div[contains(@class,'se-olympic-page')]/div[contains(@class,'se-olympic-page__content')]/div[@id='olympic_calendar_details']/div[contains(@class,'sport_day_stage_time')]/div[contains(@class,'b-result__sport')]/div[9]/div[3]/div[1]/span[1]")























