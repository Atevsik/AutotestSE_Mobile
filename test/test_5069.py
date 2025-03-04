from selenium.webdriver.common.by import By
import time

from pages.figyrkaitogi import FigyrkaItogi



def test_fig_itogi(browser):
    fig_itog = FigyrkaItogi(browser)
    fig_itog.open()
    fig_itog.h1()
    fig_itog.top3()
    fig_itog.book()
    fig_itog.sport()
    fig_itog.result()
    fig_itog.footer()
















