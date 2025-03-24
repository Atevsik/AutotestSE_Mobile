from selenium.webdriver.common.by import By
import time

from pages.nhltable import NhlTable


def test_nhl_table(browser):
    nhltable = NhlTable(browser)
    nhltable.open()
    #nhltable.dop_menu()
    #nhltable.table()
    #nhltable.h2()
    #nhltable.regulr()
    #nhltable.vas()
    #nhltable.konferen()
    #nhltable.vost() -=- ---- Все переписать
    #nhltable.zap()
    #nhltable.scroll()
    #nhltable.smi2()
    #nhltable.deviz()
    #nhltable.konf1()
    #nhltable.konf2()
    #nhltable.so4()
















