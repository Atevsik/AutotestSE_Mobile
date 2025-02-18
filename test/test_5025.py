from selenium.webdriver.common.by import By
import time

from pages.autor import Autor





def test_autor(browser):
    autor = Autor(browser)
    autor.open()
    autor.h1()
    autor.safin()
    autor.h2()
    autor.olen()
    autor.proverka(16)
    autor.next()






