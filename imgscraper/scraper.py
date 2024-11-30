"""Web scraping for imgscraper"""

import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager


class ImgScraper:
    """Web scraper class for imgscraper"""
    def __init__(self, url, output_path, headless=False):
        self.url = url
        self.output_path = output_path
        self.headless = headless
        self.firefox_options = self._set_headless()
        self.driver = self._get_firefox_driver()
        self.img_urls = self._scrape_img_urls()
        self.driver.quit()

    def _set_headless(self):
        """Configure Firefox to open headless"""
        options = Options()
        if self.headless:
            options.add_argument("--headless")
        return options

    def _get_firefox_driver(self):
        """Return Firefox webdriver"""
        gdm = GeckoDriverManager().install()
        firefox_service = Service(gdm)
        return webdriver.Firefox(
            service=firefox_service,
            options=self.firefox_options
        )

    def _scrape_img_urls(self):
        """Get a list of image URLs for all the images at URL"""
        self.driver.get(self.url)
        imgs = self.driver.find_elements(By.TAG_NAME, 'img')
        return [img.get_attribute('src') for img in imgs]

    def download_images(self):
        """Download images"""
        for i, img_url in enumerate(self.img_urls):
            response = requests.get(img_url)
            if response.status_code != 200:
                continue
            filename = f'{self.output_path.name}_{i+1:03}'
            with open(self.output_path/filename, 'wb') as file:
                file.write(response.content)
