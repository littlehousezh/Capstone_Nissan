import time
import csv
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

data = []
youtube_video_url = "https://www.youtube.com/watch?v=wJmUTfZCvhU"

with Chrome() as driver:

    wait = WebDriverWait(driver, 15)

    driver.get(youtube_video_url)

    video_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1.title yt-formatted-string"))).text

    for item in range(200):
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
        time.sleep(15)

    for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#content"))):
        data.append([video_title, comment.text])

with open("youtube_comments.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Video Title", "Comment"])
    writer.writerows(data)
