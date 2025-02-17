from selenium.webdriver.common.by import By
import time
from pages.mchok import MChock


def test_mc_hook(browser):
    mc_hoc = MChock(browser)
    mc_hoc.open()
    mc_hoc.h1()
    mc_hoc.dopmenu()
    mc_hoc.reklama()
    mc_hoc.header()
    mc_hoc.knopi()
    mc_hoc.h2()
    mc_hoc.sport_navigator()
    mc_hoc.scroll()
    mc_hoc.smi2()
    mc_hoc.selector()
    mc_hoc.olimp()
    mc_hoc.read_news()
    mc_hoc.last_match()
    mc_hoc.match()