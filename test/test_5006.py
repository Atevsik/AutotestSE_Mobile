from selenium.webdriver.common.by import By
import time

from pages.detalvideo import DetalVideo


def test_detal_video(browser):
    detal_video = DetalVideo(browser)
    detal_video.open()
    detal_video.header()
    detal_video.podelit()
    detal_video.podel_knop(5)
    detal_video.footer()
    detal_video.scroll()
    detal_video.reklama()
    detal_video.like()
