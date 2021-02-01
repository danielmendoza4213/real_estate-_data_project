from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import json

from time import sleep
from time import time
from typing import Tuple


class ImmoScraper:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.immoweb.be')
        self.handle_privacy_popup()
        self.set_links = set()
        self.failed_HTML = []

    def handle_privacy_popup(self):
        """
        Function that handles the popup when opening the website for the first time.
        """
        popup = True
        total_sleeping_time = 8
        sleep_per_iter = 0.5
        while popup:
            try:
                self.click_xpath('// *[ @ id = "uc-btn-accept-banner"]')
                popup = False
            except NoSuchElementException:
                sleep(sleep_per_iter)
                total_sleeping_time -= sleep_per_iter
                if total_sleeping_time < 0:
                    print('Did not find the button.')
                    popup = False

    def choose_transaction_type(self, tran_type: str):
        if tran_type.lower() == 'buy':
            xpath = '//*[@id="main-content"]/div/div/form/div[1]/div/div/section[1]/div/div/div/div[1]/label'
        else:
            xpath = '//*[@id="main-content"]/div/div/form/div[1]/div/div/section[1]/div/div/div/div[2]/label'
        btn = self.driver.find_element_by_xpath(xpath)
        btn.click()

    def choose_property_type(self, prop_type: str):
        """
        Method that chooses a property type on the advanced search page.
        :param prop_type: The property type to choose
        """
        btn = self.driver.find_element_by_xpath('//*[@id="propertyTypes"]/span')
        btn.click()
        prop_type = prop_type.lower()
        if prop_type == 'house':
            self.click_xpath('//*[@id="propertyTypes-item-0"]')
        elif prop_type == 'apartment':
            self.click_xpath('//*[@id="propertyTypes-item-1"]')
        elif prop_type == 'nre_house':
            self.click_xpath('//*[@id="propertyTypes-item-3"]')
        elif prop_type == 'nre_apartment':
            self.click_xpath('//*[@id="propertyTypes-item-4"]')

    def send_price_range(self, price_range: Tuple[int]):
        """
        Method that fills in the correct price range.
        The max search results for any given search is 10000. If the is reached then we should increase
        the number or range and decrease the size of the range.
        :param price_range: The range for the prices that we look for.
        """
        mini, maxi = price_range
        min_field = self.driver.find_element_by_xpath('//*[@id="minPrice"]')
        min_field.send_keys(mini)
        min_field = self.driver.find_element_by_xpath('//*[@id="maxPrice"]')
        min_field.send_keys(maxi)

    def click_xpath(self, xpath: str):
        """
        Method that finds an xpath and clicks on the element.
        :param xpath: Xpath we want to click
        """
        btn = self.driver.find_element_by_xpath(xpath)
        btn.click()

    def start_scraping(self):
        """
        Method that starts the scraping of immoweb.com. It goes to the advanced search page and changes between search
        parameters so every house/apartment ends up in our results. It automatically goes through all pages and collects
        all the links for the different results.
        """
        min_prices = [50000 * i for i in range(8)]
        max_prices = [50000 * i for i in range(1, 8)]
        max_prices.append(1000000000)
        price_range = zip(min_prices, max_prices)

        for prop_type in ['nre_house', 'nre_apartment', 'house', 'apartment']:
            for mini, maxi in zip(min_prices, max_prices):
                print(f'Searching for property type "{prop_type}" and price range "{(mini, maxi)}"')
                self.advanced_search(prop_type=prop_type, price_range=(mini, maxi))

    def advanced_search(self, prop_type: str, price_range: Tuple[int]) -> dict:
        """
        Method that does the advanced search. It goes to the advanced search page, chooses options that are given and
        clicks the search button.
        :param prop_type: The type of property we want to search for.
        :param price_range: The prince range we want to look for.
        """
        self.driver.get(
            'https://www.immoweb.be/en/advanced-search/house/for-sale?countries=BE&page=1&orderBy=relevance')
        self.choose_property_type(prop_type)
        self.send_price_range(price_range)
        self.click_xpath('//*[@id="stickySubmitFooter"]/button[2]')
        next_page = True

        while next_page:
            lst = self.driver.find_element_by_id("main-content")
            items = lst.find_elements_by_tag_name("li")

            for item in items:
                try:
                    inner_html = item.get_attribute('innerHTML')
                    if 'href="' in inner_html:
                        link = inner_html.split('href="')[1].split('" ')[0]
                        self.set_links.add(link)
                except:
                    self.failed_HTML.append({"items": items, "item": item})

            try:
                btn = self.driver.find_element_by_xpath("//span[contains(@class, 'sr-only') and text()='Next page']")
                btn = btn.find_element_by_xpath('..')
                btn.click()
            except NoSuchElementException:
                print('Could not find the  next page button')
                next_page = False

    def save_set(self):
        """
        Safe links to a json file.
        """
        json_str = json.dumps(list(self.set_links))
        loc = f'./links_{int(time())}.json'
        with open(loc, 'w') as outfile:
            json.dump(json_str, outfile)


if __name__ == '__main__':
    scraper = ImmoScraper()
    scraper.start_scraping()
    scraper.save_set()