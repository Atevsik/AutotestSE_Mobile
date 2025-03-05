from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class DetalStory:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/obshchestvo/stories/rossiya-sankcii-na-olimpiade-i-chm-sorevnovaniya-v-rossii-i-vystuplenie-sbornoy-i-sportsmenov-dopingovyy-krizis-i-sudy-protiv-mok-i-vada-852911/')

    def header(self):
        header = self.browser.find_element(By.XPATH, "//div[@class='se-header-mob__inner-stripe']")

    def paris(self):
        paris = self.browser.find_element(By.XPATH,"//p[@class='se-material-page__rubric']//a[contains(text(),'Париж-2024')]")
        paris.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/olympics/summer/', "Не правильный париж"
        self.browser.back()

    def footer(self):
        footer = self.browser.find_element(By.XPATH,"//footer[@class='se-footer']")

    def scroll(self):
        scroll = self.browser.find_element(By.XPATH, "//footer[@class='se-footer']")
        scroll = self.browser.execute_script("arguments[0].scrollIntoView();", scroll)
        sleep(5)

    def reklama(self):
        reklama = self.browser.find_element(By.XPATH,"//div[@Id='adfox_150116181456951773']")

    def smi2(self):
        smi2 = self.browser.find_element(By.XPATH, "//div[@id='adfox_159072868052985816']")

    def podelit(self):
        podelit = self.browser.find_element(By.XPATH,"//div[@class='se-shareblock__icon']//*[name()='svg']")
        podelit.click()

    def podel_knop(self,count):
        podel_knop = self.browser.find_elements(By.XPATH,"//button[@class='react-share__ShareButton']")
        assert len(podel_knop) == count

    def like(self):
        like = self.browser.find_element(By.XPATH, "//div[@class='se-material-page__footer-socials']")

    def teg(self):
        teg = self.browser.find_element(By.XPATH,"//span[contains(text(),'Олимпиада')]")
        teg.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/olympics/', "Не правильная олимпиада"
        self.browser.back()