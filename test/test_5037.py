from selenium.webdriver.common.by import By
import time

from pages.books import Books



def test_it(browser):
   books = Books(browser)
   books.open()
   books.h1()
   books.filtr()
   books.obzor()
   books.pari()
   books.span()
   books.scroll()
   books.smi2()
   books.comment()











