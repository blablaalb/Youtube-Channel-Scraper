import selenium
from selenium.webdriver import Firefox
from selenium.webdriver import Chrome
import requests
from channel_page import ChannelPage
from video_page import VideoPage
import csv
import time

url = "https://www.youtube.com/c/OldSchoolCombat/videos"
jquery_cdn = "https://code.jquery.com/jquery-3.6.0.js"

options  = selenium.webdriver.ChromeOptions()
options.add_argument("--mute-audio")
driver = Chrome(options=options)
driver.get(url)
jq = requests.get(jquery_cdn).text
driver.execute_script(jq)

cp = ChannelPage(driver)
while not cp.near_bottom():
    cp.scroll_down()
    time.sleep(0.6)

urls = list(cp.get_urls())
with open('channel.csv', 'w', newline='') as f:
    csv_writer  = csv.writer(f)
    for url in (urls):
        driver.get(url)
        vp = VideoPage(driver)
        title = vp.get_title()
        vp.click_press_more()
        description = vp.get_description()
        print(f"{title}\n{description}")
        csv_writer.writerow([title, description, url])

driver.quit()
