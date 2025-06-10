# get_books.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import json
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920x1080')

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")
time.sleep(3) 

book_cards = driver.find_elements(By.CSS_SELECTOR, 'li.row.cp-search-result-item')
print("Books found:", len(book_cards))

results = []

for card in book_cards:
    try:
        title_element = card.find_element(By.CLASS_NAME, 'title-content')
        title = title_element.text.strip()
    except:
        title = "N/A"

    try:
        author_elements = card.find_elements(By.CLASS_NAME, 'author-link')
        authors = [a.text.strip() for a in author_elements if a.text.strip()]
        author = "; ".join(authors) if authors else "N/A"
    except:
        author = "N/A"

    try:
        format_element = card.find_element(By.CLASS_NAME, 'display-info-primary')
        format_year = format_element.text.strip()
    except:
        format_year = "N/A"

    results.append({
        "Title": title,
        "Author": author,
        "Format-Year": format_year
    })

driver.quit()
df = pd.DataFrame(results)
print(df)

# TASK 4
df.to_csv("get_books.csv", index=False)
with open("get_books.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=4, ensure_ascii=False)

