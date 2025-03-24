from selenium.webdriver.common.by import By
import time
from pages.spiso4story import Spiso4Story


def test_story_spiso4(browser):
   story = Spiso4Story(browser)
   story.open()
   story.h1()
   story.knopka()
   story.dop_news()
   story.gazeta()
   story.k_hockey()
   story.selector()
   story.mma()
   story.scroll()
   story.reklama()





