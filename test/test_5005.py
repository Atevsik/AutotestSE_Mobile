from selenium.webdriver.common.by import By
import time

from pages.detalphoto import DetalPhoto


def test_detal_photo(browser):
    detal_photo = DetalPhoto(browser)
    detal_photo.open()
    detal_photo.header()
    detal_photo.karysel()
    detal_photo.podelit()
    detal_photo.podel_knop(5)
    detal_photo.footer()
    detal_photo.scroll()
    detal_photo.reklama()
    detal_photo.like()
