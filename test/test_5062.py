from selenium.webdriver.common.by import By
import time

from pages.figyrkagranpri import FigyrkaGranPri



def test_figyrka_gran_pri(browser):
    fig = FigyrkaGranPri(browser)
    fig.open()
    fig.h1()
    fig.dop_menu()
    fig.obsh()
    fig.h2()
    fig.gleb()
    fig.dance()
    fig.sofia()
    fig.jen()
    fig.anna()
    fig.pari()












