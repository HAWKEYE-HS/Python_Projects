import selenium
from selenium import webdriver
import time
from bs4 import BeautifulSoup as bs
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


def login(username, password):
    time.sleep(2)
    user = driver.find_element_by_name('username')
    user.send_keys(username)
    time.sleep(3)
    pwd = driver.find_element_by_name('password')
    pwd.send_keys(password)
    path = "//*[@type='submit']"
    time.sleep(3)
    login_but = driver.find_element_by_xpath(path)
    login_but.click()
    time.sleep(30)


def search(text):
    term = driver.find_element_by_class_name("XTCLo x3qfX ")
    term.send_keys(text)
    term.send_keys(Keys.ENTER)
    time.sleep(3)


def first_pic():
    pic = driver.find_element_by_class_name("eLAPa")
    pic.click()


def like_post():
    time.sleep(6)
    path = "//*[@class='fr66n']"
    like = driver.find_element_by_xpath(path)
    soup = bs(like.get_attribute('innerHTML'), 'html.parser')
    if (soup.find('svg')['aria-label'] == 'Like'):
        like.click()
    else:
        pass


def next_post():
    time.sleep(2)
    try:
        path = "//*[@style='display: inline-block; transform: rotate(90deg);']"
        nex = driver.find_element_by_xpath(path)
        soup = bs(nex.get_attribute('innerHTML'), 'html.parser')
        if (soup.find('svg')['aria-label'] == 'Next'):
            nex.click()
        time.sleep(1)
        return nex
    except selenium.common.exceptions.NoSuchElementException:
        return 0


def continue_liking():
    while (True):
        next_pic = next_post()
        if next_pic:
            next_pic.click()
            time.sleep(5)

            like_post()
            time.sleep(5)
        else:
            print("end")
            break


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("https://www.instagram.com/accounts/login/")
    login("ABC", "XYZ")
    time.sleep(10)
    first_pic()
    like_post()
    next_post()
    continue_liking()
