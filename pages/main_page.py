from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):
    def go_to_elements_page(self):
        elements_link = self.browser.find_element(*MainPageLocators.ELEMENT_LINK)
        elements_link.click()

    def should_be_main_page_url(self):
        url = self.browser.current_url
        assert "https://demoqa.com/" == url
