from selenium.webdriver.common.by import By
import time

from pages.matchpagehockey import MatchHock


def test_match_hock(browser):
    mh = MatchHock(browser)
    mh.open()
    mh.header()
    mh.auto()
    mh.metal()
    mh.seria()
    mh.seria_click()
    mh.vstr()
    mh.eshe()
    mh.proverka(10)
    mh.li4ka()
    mh.sost()
    mh.leaders()
    mh.last_game()
    mh.poloj()
    mh.poloj2()
    mh.scroll()
    mh.smi2()
    mh.protokol()
    mh.sobitia()
    mh.statist()
    mh.igrok()
    mh.live()
    mh.time()
    mh.comment()
    mh.video()


















