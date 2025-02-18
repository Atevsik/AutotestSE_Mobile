from selenium.webdriver.common.by import By
import time

from pages.tagplayer import TagPlayer


def test_tag_player(browser):
    tp = TagPlayer(browser)
    tp.open()
    tp.info()
    tp.info1()
    tp.football()
    tp.spotrsmen()
    tp.bio()
    tp.read_next()
    tp.text()
    tp.material(30)
    tp.next()
    tp.material(30)
