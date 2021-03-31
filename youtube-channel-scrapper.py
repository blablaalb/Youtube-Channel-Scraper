import selenium
from selenium.webdriver import Firefox
from selenium.webdriver import Chrome
import time
import requests


url = "https://www.youtube.com/c/OldSchoolCombat/videos"

driver = Chrome()
driver.get(url)

jquery_cdn = "https://code.jquery.com/jquery-3.6.0.js"
jq = requests.get(jquery_cdn).text
driver.execute_script(jq)


def scroll_down():
    script = """ 
        function getelement(){
            let selector = "ytd-two-column-browse-results-renderer.style-scope";
            return document.querySelector(selector);
        }

        window.scrollTo(0,getelement().scrollHeight);
    """
    driver.execute_script(script)

def near_bottom():
    script = """
    return $(window).scrollTop() + $(window).height() > $(document).height() - 10;
    """
    response = driver.execute_script(script)
    return response

def get_urls():
    xpath = '//a[@id="video-title" and @href]'
    urls = driver.find_elements_by_xpath(xpath)
    for url in urls:
        yield url.get_attribute("href")

def print_titles():
    xpath = '//*[@id="video-title"]'
    titles = driver.find_elements_by_xpath(xpath)
    for title in titles:
        print(title.text)

def make_url_abs(url: str) -> str:
    return "https://www.youtube.com" + url

while not near_bottom():
    scroll_down()
    print("--- scrolling! ---")
    time.sleep(0.5)
    

print_titles()
for url in get_urls():
    print(url)



# driver.quit()
