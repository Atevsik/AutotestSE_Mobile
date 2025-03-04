from selenium.webdriver.common.by import By
import time

from pages.figyrkacomand import FigyrkaComand



def test_figyrka_comand(browser):
    fig_comand = FigyrkaComand(browser)
    fig_comand.open()
    fig_comand.h1()
    fig_comand.dop_menu()
    fig_comand.obsh()
    fig_comand.h2()
    fig_comand.italy()
    fig_comand.sostav()











