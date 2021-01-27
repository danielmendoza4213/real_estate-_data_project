from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from time import sleep


class ImmoScraper:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def first_contact(self):
        self.driver.get('https://www.immoweb.be/nl')
        # sleep(3)

    def handle_privacy_popup(self):
        popup = True
        total_sleeping_time = 5
        sleep_per_iter = 0.5
        while popup:
            try:
                btn_verder_surfen = self.driver.find_element_by_xpath('// *[ @ id = "uc-btn-accept-banner"]')
                popup = False
            except NoSuchElementException:
                sleep(sleep_per_iter)
                total_sleeping_time -= sleep_per_iter
                if total_sleeping_time < 0:
                    print('Did not find the button.')
                    break
        btn_verder_surfen.click()

    def choose_type(self):
        btn = self.driver.find_element_by_xpath('//*[@id="propertyTypesDesktop"]')
        btn.send_keys('Appartement')


if __name__ == '__main__':
    scraper = ImmoScraper()
    scraper.first_contact()
    scraper.handle_privacy_popup()
    scraper.choose_type()

#self.driver.switch_to.window(self.driver.window_handles[1])
#selenium.common.exceptions.NoSuchElementException