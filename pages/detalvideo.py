from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class DetalVideo:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/video/den-s-alekseem-shevchenko/videoreports/sibir-vse-dalshe-ot-pley-off-u-salavata-yulaeva-zablokirovali-scheta-den-s-alekseem-shevchenko-31-yanvarya-2024-2174072/')
        sleep(6)

    def header(self):
        header = self.browser.find_element(By.XPATH, "//div[@class='se-header-mob__inner-stripe']")

    def footer(self):
        footer = self.browser.find_element(By.XPATH,"//footer[@class='se-footer']")

    def scroll(self):
        scroll = self.browser.find_element(By.XPATH, "//footer[@class='se-footer']")
        scroll = self.browser.execute_script("arguments[0].scrollIntoView();", scroll)
        sleep(5)

    def reklama(self):
        reklama = self.browser.find_element(By.XPATH, "//div[@id='adfox_159072868052985816']")

    def podelit(self):
        podelit = self.browser.find_element(By.XPATH,"//div[@class='se-shareblock__icon']//*[name()='svg']")
        podelit.click()

    def podel_knop(self,count):
        podel_knop = self.browser.find_elements(By.XPATH,"//button[@class='react-share__ShareButton']")
        assert len(podel_knop) == count

    def like(self):
        like = self.browser.find_element(By.XPATH, "//div[@class='se-material-page__footer-socials']")