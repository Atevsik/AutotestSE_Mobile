from selenium.webdriver.common.by import By
import time

from pages.figyrkamedal import FigyrkaMeadal


def test_figyrka_medal(browser):
    fig_medal = FigyrkaMeadal(browser)
    fig_medal.open()
    fig_medal.h1()
    fig_medal.dop_menu()
    fig_medal.obsh()
    fig_medal.h2()
    fig_medal.god()
    fig_medal.v2024()
    fig_medal.italy()
    fig_medal.m()
    fig_medal.j()
    fig_medal.p()
    fig_medal.t()











