import selenium
from selenium.webdriver import Firefox
from selenium.webdriver import Chrome
import requests
from channel_page import ChannelPage
from video_page import VideoPage
import csv
import time
import sys


args = sys.argv
url = ''
if len(args) <= 1:
    while not url:
        url = input("Please enter url for the channel...")
else:
    url = args[1]



jquery_cdn = "https://code.jquery.com/jquery-3.6.0.js"
options = selenium.webdriver.ChromeOptions()
options.add_argument("--mute-audio")
driver = Chrome(options=options)
driver.get(url)
jq = requests.get(jquery_cdn).text
driver.execute_script(jq)
videos_btn_element = driver.find_elements_by_xpath('//div[@id="tabsContainer"]/div[@id="tabsContent"]/tp-yt-paper-tab[@role="tab"]')[1].click()
channel_name = driver.find_element_by_xpath(
    '//div[contains(@id, "inner-header-container")]/div/ytd-channel-name[@id="channel-name"]/div/div/yt-formatted-string[@id="text" and contains(@class, "ytd-channel-name")]').text

cp = ChannelPage(driver)
while not cp.near_bottom():
    cp.scroll_down()
    time.sleep(0.6)

urls = list(cp.get_urls())
with open(f'{channel_name}.csv', 'w', newline='') as f:
    csv_writer = csv.writer(f)
    for url in (urls):
        try:
            driver.get(url)
            vp = VideoPage(driver)
            title = vp.get_title()
            vp.click_press_more()
            description = vp.get_description()
            print("\n", "-"*25, title, "-"*25, "\n", description, "\n")
            csv_writer.writerow([title, description, url])
        except Exception as e:
            print(f"\033[91m{e}\033[0m")

driver.quit()
