from selenium.webdriver.common.by import By
import time



from pages.lednikkybok import FigyrkaKybok


def test_mma_lij_kybok(browser):
    lij_kubok = FigyrkaKybok(browser)
    lij_kubok.open()
    lij_kubok.h1()
    lij_kubok.dop_menu()
    lij_kubok.obsh()
    lij_kubok.be()
    lij_kubok.li4ka()
    lij_kubok.kubok()
    lij_kubok.ukr()
    lij_kubok.wom()
    lij_kubok.fra()














