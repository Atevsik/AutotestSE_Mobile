from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class MatchHock:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/hockey/L/matchcenter/116730/')
        sleep(6)

    def header(self):
        header = self.browser.find_element(By.XPATH,"//div[@class='se-header-mob__inner-stripe']")

    def auto(self):
        auto = self.browser.find_element(By.XPATH,"//div[@class='sp-matchcenter-board-team-details__logo-inner']//img[@title='Автомобилист']")
        auto.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/tag/avtomobilist-ekaterinburg-272/',"Не правильный команда 1"
        self.browser.back()

    def metal(self):
        metal = self.browser.find_element(By.XPATH,"//div[@class='sp-matchcenter-board-team-details__logo-inner']//img[@title='Металлург Мг']")
        metal.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/tag/metallurg-mg-hokkey-270/'
        self.browser.back()

    def seria(self):
        seria = self.browser.find_element(By.XPATH,"//div[@class='sp-mc-playoff-stage']//div[@class='se-titled-block se-titled-block--bg-white se-titled-block--align-center']")

    def seria_click(self):
        seria_click = self.browser.find_element(By.XPATH,"//tbody/tr/td[6]/a[1]/div[1]/div[1]/div[1]")
        seria_click.click()
        sleep(11111)
        assert self.browser.current_url == 'https://m.sport-express.ru/hockey/L/matchcenter/116731/', "Не правильная серия"
        self.browser.back()

    def vstr(self):
        vstr = self.browser.find_element(By.XPATH,"//a[3]//div[1]//div[3]//div[2]")
        vstr.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/hockey/L/matchcenter/116724/',"Не правильная встреча"
        self.browser.back()

    def eshe(self):
        eshe = self.browser.find_element(By.XPATH,"//div[@class='sp-matchcenter-face-to-face-matches__more']//div[@class='se-button se-button--white se-button--size-middle'][contains(text(),'Показать еще')]")
        eshe.click()

    def proverka(self,count):
        proverka = self.browser.find_elements(By.XPATH,"//div[@class='sp-matchcenter-face-to-face-matches__item-info']")
        assert len(proverka) == count

    def li4ka(self):
        li4ka = self.browser.find_element(By.XPATH,"//div[@class='sp-mc-faceToface-stats']//div[@class='se-titled-block se-titled-block--bg-white se-titled-block--align-center']")

    def sost(self):
        sost = self.browser.find_element(By.XPATH,"//div[contains(text(),'Текущее состояние команд')]")

    def leaders(self):
        leaders = self.browser.find_element(By.XPATH,"//div[@class='se-stack']//div[3]//div[2]//div[1]//div[1]//div[1]//div[1]//a[1]//div[1]//img[1]")
        leaders.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/tag/stefan-da-kosta-12657/', "Не правильный лидер"
        self.browser.back()

    def last_game(self):
        last_game = self.browser.find_element(By.XPATH,"//div[@class='sp-mc-last-team-matches']//a[3]//div[3]//div[1]")
        last_game.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/hockey/L/matchcenter/116724/',"Не правильная последняя игра"
        self.browser.back()

    def poloj(self):
        poloj = self.browser.find_element(By.XPATH,"//div[@class='sp-playoff-table']//div[4]//div[2]//div[1]//div[1]//div[1]//span[2]")
        poloj.click()

    def poloj2(self):
        poloj2 = self.browser.find_element(By.XPATH,"//div[contains(text(),'Положение команд')]")


    def scroll(self):
        scroll = self.browser.find_element(By.XPATH,"//footer[@class='se-footer']")
        scroll = self.browser.execute_script("arguments[0].scrollIntoView();", scroll)
        sleep(5)

    def smi2(self):
        smi2 = self.browser.find_element(By.XPATH,"//div[@id='adfox_159523826122331374']")

    def protokol(self):
        protokol = self.browser.find_element(By.XPATH,"//a[contains(text(),'Протокол')]")
        protokol.click()
        sleep(4)
        assert self.browser.current_url == 'https://m.sport-express.ru/hockey/L/matchcenter/116730/protocol/', "Не правильный протокол"

    def sobitia(self):
        sobitia = self.browser.find_element(By.XPATH,"//div[contains(text(),'События матча')]")

    def statist(self):
        statist = self.browser.find_element(By.XPATH,"//a[contains(text(),'Статистика игроков')]")
        statist.click()
        sleep(4)
        assert self.browser.current_url == 'https://m.sport-express.ru/hockey/L/matchcenter/116730/stats/', "Не правильная статистика"

    def igrok(self):
        ihrok = self.browser.find_element(By.XPATH,"//a[contains(text(),'С. Зборовский')]")
        ihrok.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/tag/sergey-zborovskiy-13668/', "не правильно"
        self.browser.back()

    def live(self):
        live = self.browser.find_element(By.XPATH,"//a[normalize-space()='Live']")
        live.click()
        sleep(4)
        assert self.browser.current_url == 'https://m.sport-express.ru/hockey/L/matchcenter/116730/live/',"Лайв"

    def time(self):
        time = self.browser.find_element(By.XPATH,"//div[@class='sp-matchcenter-live-translation-event__time sp-matchcenter-live-translation-event__time--goal']")

    def comment(self):
        comment = self.browser.find_element(By.XPATH,"//a[contains(text(),'Комментарии')]")
        comment.click()
        sleep(4)
        assert self.browser.current_url == 'https://m.sport-express.ru/hockey/L/matchcenter/116730/comments/', "Комент"

    def video(self):
        video = self.browser.find_element(By.XPATH,"//div[@class='se-page-menu-item']//a[contains(text(),'Видео')]")
        video.click()
        sleep(4)
        assert self.browser.current_url == 'https://m.sport-express.ru/hockey/L/matchcenter/116730/video/', "Видео"
















