from selenium.webdriver.common.by import By
import time

from pages.mcfoot import MCfoot



def test_mc_football(browser):
    mc_foot = MCfoot(browser)
    mc_foot.open()
    mc_foot.h1()
    mc_foot.dopmenu()
    mc_foot.reklama()
    mc_foot.header()
    mc_foot.knopi()
    mc_foot.h2()
    mc_foot.sport_navigator()
    mc_foot.scroll()
    mc_foot.smi2()
    mc_foot.selector()
    mc_foot.olimp()
    mc_foot.read_news()