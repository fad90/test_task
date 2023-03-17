from .base_page import BasePage
from .locators import ElementsPageLocators

class ElementsPage(BasePage):
    def go_to_checkbox_page(self):
        checkbox_link = self.browser.find_element(*ElementsPageLocators.CHECKBOX_LINK)
        checkbox_link.click()

    def should_be_elements_page_url(self):
        url = self.browser.current_url
        assert "elements" in url