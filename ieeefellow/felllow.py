from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import os

def save_item(name, region, clazz, category, first_category, second_category, citation):
    path = "H:\\fellow.txt"
    if not os.path.exists(path):
        with open(path, "a+") as f:
            f.write("name#region#class#Category(prior to 2024 class)#1st. Contribution#2nd. Contribution Category#citation\n")
    with open(path, "a+") as f:
        f.write(f"{name}#{region}#{clazz}#{category}#{first_category}#{second_category}#{citation}\n")


driver_path = "chromedriver.exe"
user_agent = "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
url = "https://services27.ieee.org/fellowsdirectory/keywordsearch.html"
options = Options()
# options.headless = True
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument(user_agent)

service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=options)
driver.get(url)
driver.implicitly_wait(10)

page_num = 1
while True:
    print("Current Page：", page_num)
    page_num = page_num + 1
    search_box = driver.find_element(By.CLASS_NAME, "tbody")
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
        save_item(name, region, clazz, category, first_category, second_category, citation)
        print(author.text)
    button = driver.find_element(By.ID, "pagination")
    button = button.find_element(By.CLASS_NAME, "center-block")
    button = button.find_element(By.CLASS_NAME, "right")
    button = button.find_element(By.TAG_NAME, "a")
    try:
        button.click()
        time.sleep(3)
    except Exception as e:
        print(e)
        break
driver.quit()
