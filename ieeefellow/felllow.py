import argparse

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import os


def save_item(name, region, clazz, category, first_category, second_category, citation, path):
    if not os.path.exists(path):
        with open(path, "a+", encoding="utf-8") as f:
            f.write("name#region#class#Category(prior to 2024 class)#1st. Contribution#2nd. Contribution Category#citation\n")
    with open(path, "a+", encoding="utf-8") as f:
        f.write(f"{name}#{region}#{clazz}#{category}#{first_category}#{second_category}#{citation}\n")


def next_page(driver):
    button = driver.find_element(By.ID, "pagination")
    button = button.find_element(By.CLASS_NAME, "center-block")
    button = button.find_element(By.CLASS_NAME, "right")
    button = button.find_element(By.TAG_NAME, "a")
    if button.get_attribute("href") == "":
        return False
    try:
        button.click()
        time.sleep(5)
        return True
    except Exception as e:
        print(e)
        return False


if __name__ == '__main__':
    # fellow_path = "H:\\fellow.txt"
    # chrome_driver_path = E:\\Environments\\chromedriver-win64\\chromedriver.exe
    parser = argparse.ArgumentParser(description='Scrape Fellow List')
    parser.add_argument('--fellow_path', type=str,
                        help='Path to save the Fellow list', default="H:\\fellow3.txt")
    parser.add_argument('--chrome_driver_path', type=str,
                        help='Path to the ChromeDriver executable',
                        default="E:\\Environments\\chromedriver-win64\\chromedriver.exe")
    parser.add_argument('--start_page', type=int, help='URL of the start page to scrape', default=1)
    args = parser.parse_args()

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/91.0.4472.124 Safari/537.36")
    service = Service(args.chrome_driver_path)
    chrome_driver = webdriver.Chrome(service=service, options=options)
    chrome_driver.get("https://services27.ieee.org/fellowsdirectory/keywordsearch.html")
    chrome_driver.implicitly_wait(10)

    start_page = args.start_page
    page_num = 0

    while True:
        page_num = page_num + 1
        print("Current Page：", page_num)
        if page_num < start_page:
            next_page(chrome_driver)
            continue
        search_box = chrome_driver.find_element(By.CLASS_NAME, "tbody")
        authors = search_box.find_elements(By.CLASS_NAME, "tr")
        for author in authors:
            name = author.find_element(By.CLASS_NAME, "name").text
            region = author.find_element(By.CLASS_NAME, "region").text
            clazz = author.find_element(By.CLASS_NAME, "class").text
            categories = author.find_elements(By.CLASS_NAME, "category")
            category = categories[0].text
            first_category = categories[1].text
            second_category = categories[2].text
            citation = author.find_element(By.CLASS_NAME, "citation").text
            save_item(name, region, clazz, category, first_category, second_category, citation, args.fellow_path)
            print(author.text)
        if not next_page(chrome_driver):
            break
    chrome_driver.quit()

