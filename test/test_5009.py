from selenium.webdriver.common.by import By
import time

from pages.detalpoll import DetalPoll




def test_detal_poll(browser):
    detal_poll = DetalPoll(browser)
    detal_poll.open()
    detal_poll.header()
    detal_poll.reklama()
    detal_poll.detal_menu()
