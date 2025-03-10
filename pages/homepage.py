from itertools import count
from selenium.webdriver.common.by import By
from time import sleep

class HomePage:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://m.sport-express.ru/')

    def knopki_menu(self):
        knopki_menu = self.browser.find_element(By.XPATH,"//div[@class='se-header-mob__right']")

    def tablo(self):
        tablo = self.browser.find_element(By.XPATH,"//div[@class='se-translation-scoreboard__events']")

    def knopki(self):
        knopki = self.browser.find_element(By.XPATH,"//div[@class='se-translation-scoreboard__buttons-intervals']")

    def top_material(self):
        top_material = self.browser.find_element(By.XPATH, "//div[@class='se-top-materials']")

    def spisok_news(self,count):
        spisok_news = self.browser.find_elements(By.XPATH,"//li[@class='mse-mainnews__item']")
        assert len(spisok_news) == count

    def spisok_reviews(self,count):
        spisok_reviews = self.browser.find_elements(By.XPATH,"//div[@class='se-articles-block__item' and not(@data-component='hidden-block')]")
        assert len(spisok_reviews) == count

    def knopka_all_news(self):
        knopka_all_news = self.browser.find_element(By.XPATH,"//a[contains(text(),'Все главные новости')]")
        knopka_all_news.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/news/?isEditorialChoice=1', "Не правильные главные новости"
        self.browser.back()

    def video(self):
        video = self.browser.find_element(By.XPATH,"//div[@class='se-video-block']")

    def knopka_all_reviews(self):
        knopka_all_reviews = self.browser.find_element(By.XPATH,"//a[contains(text(),'Больше статей')]")
        knopka_all_reviews.click()

    def photo(self):
        photo = self.browser.find_element(By.XPATH,"//div[@class='se-photo-reports']")

    def photo_click(self):
        photo_click = self.browser.find_element(By.XPATH,"//a[@class='se-button se-photo-reports__button-more se-button--size-big']")
        photo_click.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/photoreports/', "Не правильное фото"
        self.browser.back()

    def gazeta(self):
        gazeta = self.browser.find_element(By.XPATH,"//section[@class='se-titled-block mb_20']")

    def scroll(self):
            scroll = self.browser.find_element(By.XPATH, "//footer[@class='se-footer']")
            scroll = self.browser.execute_script("arguments[0].scrollIntoView();", scroll)
            sleep(5)

    def podpiska(self):
        podpiska = self.browser.find_element(By.XPATH,"//div[@class='swiper-slide swiper-slide-active']//a[@class='se-button se-newspaper-widget__button-subscription se-button--size-big'][contains(text(),'Подписка 2025')]")
        podpiska.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/subscribe/', "Не правильная подписка"
        self.browser.back()

    def opros_teg(self,count):
        opros_teg = self.browser.find_elements(By.XPATH,"//section[@class='se-titled-block mb_30']")
        assert len(opros_teg) == count

    def podval(self):
        podval = self.browser.find_element(By.XPATH,"//footer[@class='se-footer']")

    def knoka_podval1(self):
        knopka_podval1 = self.browser.find_element(By.XPATH,"//a[contains(text(),'Редакция')]")
        knopka_podval1.click()
        sleep(5)
        assert self.browser.current_url == 'https://m.sport-express.ru/editorial/',"Не правильная редакция"
        self.browser.back()

    def knoka_podval2(self):
        knopka_podval2 = self.browser.find_element(By.XPATH, "//a[contains(text(),'Подписка на газету')]")
        knopka_podval2.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/subscribe/', "Не правильная газета"
        self.browser.back()

    def knoka_podval3(self):
        knopka_podval3 = self.browser.find_element(By.XPATH, "//a[contains(text(),'Отдел рекламы')]")
        knopka_podval3.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/advert/www/', "Не правильная реклама"
        self.browser.back()

    def knoka_podval4(self):
        knopka_podval4 = self.browser.find_element(By.XPATH, "//a[contains(text(),'Вход / регистрация')]")
        knopka_podval4.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/profile/', "Не правильный вход"
        self.browser.back()

    def knoka_podval5(self):
        knopka_podval5 = self.browser.find_element(By.XPATH, "//a[contains(text(),'Написать в редакцию')]")

    def knoka_podval6(self):
        knopka_podval6 = self.browser.find_element(By.XPATH, "//a[contains(text(),'Правовая информация')]")
        knopka_podval6.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/company/usematerial/', "Не правильное инфо"
        self.browser.back()

    def knoka_podval7(self):
        knopka_podval7 = self.browser.find_element(By.XPATH, "//a[contains(text(),'Проверка фактов')]")
        knopka_podval7.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/company/checkfacts/', "Не правильные факты"
        self.browser.back()

    def knoka_podval8(self):
        knopka_podval8 = self.browser.find_element(By.XPATH, "//a[contains(text(),'Контакты')]")
        knopka_podval8.click()
        assert self.browser.current_url == 'https://m.sport-express.ru/company/contacts/', "Не правильные контакты"