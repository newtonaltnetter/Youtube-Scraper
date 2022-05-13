#https://github.com/newtonaltnetter

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# we set the chromedriver path here
driver = webdriver.Chrome(service=Service("path/to/chromedriver.exe"))


# function to scrape video url
def searchVideo(x):
    driver.get("https://www.youtube.com/results?search_query=" + x)
    
    # sleep for 2 seconds
    time.sleep(2)
    
    # here the driver takes the first video
    video = driver.find_element(By.XPATH, '//*[@id="video-title"]')
    videoEmb = video.get_attribute("href")
    titleVideo = video.get_attribute("title")
    midias = {
        "title": titleVideo,
        "video": videoEmb,
    }
    return midias


print("Please wait, data is being collected...")

# these are the words you want to search for
args = ["house", "camping", "etc..", "etc.."]
for x in args:
    # call the function
    midia = searchVideo(x)
    print(midia)
