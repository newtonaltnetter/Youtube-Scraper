import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service("path/to/chromedriver.exe"))


def searchVideo(x):
    driver.get("https://www.youtube.com/results?search_query=" + x)
    time.sleep(2)
    video = driver.find_element(By.XPATH, '//*[@id="video-title"]')
    videoEmb = video.get_attribute("href")
    titleVideo = video.get_attribute("title")
    midias = {
        "title": titleVideo,
        "video": videoEmb,
    }
    return midias


print("Aguarde, os dados estão sendo coletados...")

args = ["house", "camping", "etc..", "etc.."]
for x in args:
    midia = searchVideo(x)
    print(midia)
