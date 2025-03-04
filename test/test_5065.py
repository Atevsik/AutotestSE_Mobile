from selenium.webdriver.common.by import By
import time


from pages.figyrkasports import FigyrkaSportsmn


def test_figyrka_sportsmn(browser):
    fig_sportsmn = FigyrkaSportsmn(browser)
    fig_sportsmn.open()
    fig_sportsmn.h1()
    fig_sportsmn.dop_menu()
    fig_sportsmn.obsh()
    fig_sportsmn.h2()
    fig_sportsmn.uki()
    fig_sportsmn.m()
    fig_sportsmn.j()
    fig_sportsmn.p()
    fig_sportsmn.t()











