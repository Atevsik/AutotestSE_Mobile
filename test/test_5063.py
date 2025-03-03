from selenium.webdriver.common.by import By
import time

from pages.figyrkacalend import FigyrkaCalend




def test_mma_figyrka_calend(browser):
    fig_calend = FigyrkaCalend(browser)
    fig_calend.open()
    fig_calend.h1()
    fig_calend.dop_menu()
    fig_calend.obsh()
    fig_calend.h2()
    fig_calend.book()
    fig_calend.event()











