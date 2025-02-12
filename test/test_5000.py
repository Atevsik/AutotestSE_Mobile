from selenium.webdriver.common.by import By
import time

from pages.spiso4gazeta import Spiso4Gazeta


def test_gazeta_spiso4(browser):
    gazeta = Spiso4Gazeta(browser)
    gazeta.open()
    gazeta.knopki(2)
    gazeta.detal_knp()
    gazeta.polosa()
    gazeta.podval()
    gazeta.scroll()
    gazeta.smi2()








