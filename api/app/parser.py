from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def parse_animes(url: str):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(url)

    wait = WebDriverWait(driver, 10)

    try:
        no_hover = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "no-hover")))
        total_cnt_of_pages = int(no_hover.find_element(By.CLASS_NAME, "link-total").text)
        print('Количество страниц:', total_cnt_of_pages)
    except Exception as e:
        print("Ошибка при получении количества страниц:", e)
        driver.quit()
        return []

    all_animes = []

    for page in range(2):
        try:
            time.sleep(2)
            entries_div = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cc-entries")))
            articles = entries_div.find_elements(By.TAG_NAME, "article")

            for article in articles:
                try:
                    title_name_ru = article.find_element(By.CLASS_NAME, "name-ru").text
                    misc_div = article.find_element(By.CLASS_NAME, "misc")
                    spans = misc_div.find_elements(By.TAG_NAME, "span")
                    img = article.find_element(By.TAG_NAME, "img")

                    data = {
                        "russianname": title_name_ru,
                        "animetype": spans[0].text if len(spans) > 0 else "Unknown",
                        "releaseyear": spans[1].text if len(spans) > 1 else "Unknown",
                        "cover": img.get_attribute("src")
                    }
                    all_animes.append(data)

                except Exception as e:
                    print("Ошибка при парсинге аниме:", e)

            forward_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "link-next")))
            forward_button.click()

        except Exception as e:
            print("Ошибка на странице:", e)
            break

    driver.quit()
    return all_animes