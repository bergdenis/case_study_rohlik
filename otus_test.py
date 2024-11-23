import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options


@pytest.fixture
def driver():
    options = Options()
    driver = webdriver.Firefox(service=FirefoxService(executable_path="C:/Python39/Scripts/geckodriver.exe"), options=options)
    driver.implicitly_wait(3)
    yield driver
    driver.quit()


def test_find_and_open_course(driver):
    course_name = "Python QA Engineer"
    driver.get("https://otus.ru/")
    nav_element = driver.find_element(By.XPATH, "//*[@class='sc-k2vhmo-1 cYMYSf']")
    nav_element.click()
    search_input = driver.find_element(By.XPATH, "//input[@placeholder='Поиск по курсам']")
    search_input.send_keys(course_name)
    course_element = driver.find_element(By.XPATH, "//p[text()='Python QA Engineer']")
    course_element.click()
    driver.find_element(By.XPATH, "//h1[text()='Python QA Engineer']")
