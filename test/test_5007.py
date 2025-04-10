from selenium.webdriver.common.by import By
import time

from pages.detalstory import DetalStory



def test_detal_story(browser):
    detal_story = DetalStory(browser)
    detal_story.open()
    detal_story.header()
    detal_story.paris()
    detal_story.reklama()
    detal_story.podelit()
    detal_story.podel_knop(5)
    detal_story.footer()
    detal_story.scroll()
    detal_story.smi2()
    #detal_story.teg()
    detal_story.like()
