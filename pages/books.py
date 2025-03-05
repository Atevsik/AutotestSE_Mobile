from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class Books:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/rating-bookmakerov/news/reyting-bukmekerov-1989757/')

    def h1(self):
        h1 = self.browser.find_element(By.XPATH,"//h1[contains(text(),'Рейтинг букмекеров')]")

    def filtr(self):
        filtr = self.browser.find_element(By.XPATH,"//div[@class='se-bookies-ratings__filter']")

    def obzor(self):
        obzor = self.browser.find_element(By.XPATH,"//div[contains(@class,'se-bookies-ratings__table-wrapper')]//div[contains(@class,'se-bookies-ratings__table')]//div[1]//div[5]//a[1]")
        obzor.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/rating-bookmakerov/news/fonbet-1989751/', "Не правильный фонбет"
        self.browser.back()

    def pari(self):
        pari = self.browser.find_element(By.XPATH,"//div[contains(@class,'se-bookies-ratings__table-row se-bookies-ratings__table-row--pari')]//div[contains(@class,'se-bookies-ratings__table-td se-bookies-ratings__table-td--col-company')]//img")
        pari.click()
        assert self.browser.current_url == "https://m.sport-express.ru/rating-bookmakerov/news/pari-1989749/", 'не правильный пари'
        self.browser.back()


    def span(self):
        span = self.browser.find_element(By.XPATH,"//span[contains(text(),'«СЭ» оценивает букмекерские компании по нескольким')]")

    def scroll(self):
        scroll = self.browser.find_element(By.XPATH, "//footer[@class='se-footer']")
        scroll = self.browser.execute_script("arguments[0].scrollIntoView();", scroll)
        sleep(5)

    def smi2(self):
        smi2 = self.browser.find_element(By.XPATH, "//div[@id='adfox_159072868052985816']")

    def comment(self):
        comment = self.browser.find_element(By.XPATH,"//div[@class='se19-comments-item']")
















