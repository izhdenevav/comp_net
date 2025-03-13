from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

df = pd.DataFrame(columns=["RussianName", "AnimeType", "ReleaseYear", "Cover"])

data = {"RussianName": "RussianName", "AnimeType": "AnimeType", "ReleaseYear": "ReleaseYear", "Cover": "Cover"}
df = pd.DataFrame([data])
df.to_csv("animes_data.csv", mode='a', index=False, header=False)

driver = webdriver.Chrome()

driver.get("https://shikimori.one/animes")

# контейнер, из которого я хочу достать количество страниц
no_hover = driver.find_element(By.CLASS_NAME, "no-hover") 
# текст из спана с количеством страниц
total_cnt_of_pages = no_hover.find_element(By.CLASS_NAME, "link-total").text
print('Количество страниц: ', total_cnt_of_pages)
forward_button = driver.find_element(By.CLASS_NAME, "link-next")

for _ in range(int(total_cnt_of_pages)):
    time.sleep(2)
    entries_div = driver.find_element(By.CLASS_NAME, "cc-entries")
    articles = entries_div.find_elements(By.TAG_NAME, "article")
    for article in articles:
        title_name_ru = article.find_element(By.CLASS_NAME, "name-ru").text
        # title_name_en = article.find_element(By.CLASS_NAME, "name-en")
        misc_div = article.find_element(By.CLASS_NAME, "misc")
        spans = misc_div.find_elements(By.TAG_NAME, "span")
        img = article.find_element(By.TAG_NAME, "img")
        
        data = {
            "RussianName": title_name_ru,
            "AnimeType": spans[0].text,
            "ReleaseYear": spans[1].text,
            "Cover": img.get_attribute("src")
            }

        df = pd.DataFrame([data])
        df.to_csv("animes_data.csv", mode='a', index=False, header=False)


    forward_button.click()