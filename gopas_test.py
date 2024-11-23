import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options


@pytest.fixture(scope="function")
def driver():
    options = Options()
    driver = webdriver.Firefox(service=FirefoxService(executable_path="C:/Python39/Scripts/geckodriver.exe"), options=options)
    yield driver
    driver.quit()


def test_search_course(driver):
    driver.get("https://www.gopas.cz/")
    time.sleep(3)
    search_box = driver.find_element(By.CSS_SELECTOR, "#advanced-search input")
    search_box.send_keys("Data Science and Machine Learning with Python")
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)
    course_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Data Science and Machine Learning with Python")
    course_link.click()
    time.sleep(3)
    assert "Data Science and Machine Learning with Python" in driver.title
