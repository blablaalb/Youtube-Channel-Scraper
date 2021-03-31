import selenium
from selenium.webdriver import Firefox
from selenium.webdriver import Chrome
import requests
from channel_page import ChannelPage
from video_page import VideoPage

url = "https://www.youtube.com/c/OldSchoolCombat/videos"
jquery_cdn = "https://code.jquery.com/jquery-3.6.0.js"

options  = selenium.webdriver.ChromeOptions()
options.add_argument("--mute-audio")
driver = Chrome(options=options)
driver.get(url)
jq = requests.get(jquery_cdn).text
driver.execute_script(jq)

cp = ChannelPage(driver)
urls = list(cp.get_urls())

for url in (urls):
    driver.get(url)
    vp = VideoPage(driver)
    title = vp.get_title()
    description = vp.get_description()
    print(f"{title}\n{description}")
    input("Press any key to continue...")
