from selenium.webdriver.common.by import By
import time

from pages.tagcomand import TagComand



def test_tag_comand(browser):
    tc = TagComand(browser)
    tc.open()
    tc.info()
    tc.info1()
    tc.football()
    tc.spotrsmen()
    tc.read_next()
    tc.text()
    tc.material(30)
