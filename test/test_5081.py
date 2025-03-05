from selenium.webdriver.common.by import By
import time

from pages.piloti import FormulaPilot


def test_f_pilot(browser):
    f_pilot = FormulaPilot(browser)
    f_pilot.open()
    f_pilot.h1()
    f_pilot.dop_menu()
    f_pilot.obsh()
    f_pilot.alex()
    f_pilot.fera()
















