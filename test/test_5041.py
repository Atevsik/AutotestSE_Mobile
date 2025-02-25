from selenium.webdriver.common.by import By
import time
from pages.talkfrieday import Talk


def test_friday(browser):
    frieday = Talk(browser)
    frieday.open()
    frieday.h1()
    frieday.knopka()
    frieday.knopki1()
    frieday.knopki2()
    frieday.knopki3()
    frieday.vid_sport()
    frieday.gazeta()
    frieday.proverka(10)






