import selenium
from selenium.webdriver import Firefox
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Sequence, Union, List
import utils


class VideoPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 3)

    def get_title(self) -> str:
        xpath = '//h1[contains(@class, "title")]'
        title_elements: List[WebElement] = self.wait.until(
            EC.visibility_of_any_elements_located((By.XPATH, xpath)))
        for title_element in title_elements:
            title = title_element.text
            if isinstance(title, str) and title:
                return title

    def get_description(self) -> str:
        base_xpath = '//*[@id="description"]/yt-formatted-string'
        text_subxpath = './/span[contains(@class, "style-scope")]'
        url_subxpath = './/a[@href]'
        xpath = '//div[@id="description"]//span[contains(@class,"style-scope")]'
        self.wait.until(
            EC.visibility_of_any_elements_located((By.XPATH, xpath)))
        full_description = ''
        base_element: WebElement = self.driver.find_element_by_xpath(base_xpath)
        for child_element in base_element.find_elements_by_xpath("./*"):
            child_element: WebElement
            tag_name: str = child_element.tag_name
            if tag_name == "span":
                full_description += child_element.text
            if tag_name == "a":
                if r"hashtag/" not in child_element.get_attribute("href"):
                    url = child_element.get_attribute("href")
                    url = utils.redirected_url(url)
                    full_description += url
        return full_description