from selenium import webdriver
from bs4 import BeautifulSoup

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time

# ED URL

VIDEO_EXAMPLE = 'https://www.instagram.com/p/CAXWAc1gJHq/'
NORMAL_EXAMPLE = 'https://www.instagram.com/p/B7_5aG7J2EY/'


def main():
    txt_file = open('gucci-url.txt', errors='ignore', encoding='utf=8')
    urls = []  # all the urls (from base file)
    file_final = []

    for line in txt_file:
        urls.append(line.strip())

    for line in urls:
        data_of_a_single_post = []

        single_website = str(line)
        driver = webdriver.Chrome('/users/jaehee.ryu/Downloads/chromedriver')
        driver.implicitly_wait(3)

        driver.get(single_website)

        wait_loading(driver, "c-Yi7")

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        # collect dates
        dates = driver.find_element_by_class_name('c-Yi7').text
        print(dates)
        data_of_a_single_post.append(dates)

        # collect view (0, view) or likes (likes, view)
        video_or_not(driver, data_of_a_single_post)

        file_final.append(data_of_a_single_post)

        driver.close()

    import csv

    with open("datetime.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(file_final)


def wait_loading(driver, class_name):
    wait = WebDriverWait(driver, 10)
    element = wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, class_name)))

def video_or_not(driver, data_of_a_single_post):
    try:
        views = driver.find_element_by_class_name('vcOH2').text
        print(views)
        data_of_a_single_post.append('0')
        data_of_a_single_post.append(views)

    # cannot find the push view button
    # likes = driver.find_element_by_class_name('vJRqr').text
    # print(likes)
    # num_like.append(likes)
    except:
        likes = driver.find_element_by_class_name('Nm9Fw').text
        print(likes)
        data_of_a_single_post.append(likes)
        data_of_a_single_post.append('0')

    pass


# infinite scrolling - looks very nice when there's just "1" scroll bar
#
#    last_height = driver.execute_script("return document.body.scrollHeight")
#    while True:
#        # Scroll down to bottom
#        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#        # Wait to lode page
#        time.sleep(SCROLL_PAUSE_TIME)
#
#        # when going to the very end once, sometimes they don't load the page
#        driver.execute_script("window.scrollTo(0, document.body.scrollHeight-50);")
#        time.sleep(SCROLL_PAUSE_TIME)
#
#        # Calculate new scroll height and compare with last scroll height
#        new_height = driver.execute_script("return document.body.scrollHeight")
#        if new_height == last_height:
#            break
#        last_height = new_height


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
