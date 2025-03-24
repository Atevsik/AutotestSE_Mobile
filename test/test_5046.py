from selenium.webdriver.common.by import By
import time


from pages.worldhockey import World


def test_world(browser):
    world = World(browser)
    world.open()
    world.h1()
    world.dop_menu()
    world.stat()
    world.h2()
    world.dop_menu2() #В новой версии, обратить внимание на этот шаг, сделать его лучше, (убрать гет)
    world.info(472)
    #world.tag()
    world.li4ka()
    world.player()
    world.vratar()
    #world.player2()
    world.zash()
    #world.player3()
    world.nap()
    #world.player4()
    world.comand()
    world.tablet(16)
    world.usa()
    world.scroll()
    world.smi2()










