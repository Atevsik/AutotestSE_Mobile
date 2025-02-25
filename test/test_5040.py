from selenium.webdriver.common.by import By
import time

from pages.games import Games




def test_games(browser):
    game = Games(browser)
    game.open()
    game.logo()
    game.h1()
    game.h2()












