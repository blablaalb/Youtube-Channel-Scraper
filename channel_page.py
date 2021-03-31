import selenium
from selenium.webdriver import Firefox
from selenium.webdriver import Chrome
from typing import Sequence


class ChannelPage:

    def __init__(self, driver):
        self.driver = driver

    def scroll_down(self):
        script = """ 
            function getelement(){
                let selector = "ytd-two-column-browse-results-renderer.style-scope";
                return document.querySelector(selector);
            }

            window.scrollTo(0,getelement().scrollHeight);
        """
        self.driver.execute_script(script)

    def near_bottom(self):
        script = """
        return $(window).scrollTop() + $(window).height() > $(document).height() - 10;
        """
        response = self.driver.execute_script(script)
        return response

    def get_urls(self) -> Sequence[str]:
        xpath = '//a[@id="video-title" and @href]'
        urls = self.driver.find_elements_by_xpath(xpath)
        for url in urls:
            yield url.get_attribute("href")

    def get_titles(self) -> Sequence[str]:
        xpath = '//*[@id="video-title"]'
        titles = self.driver.find_elements_by_xpath(xpath)
        for title in titles:
            yield title.text
