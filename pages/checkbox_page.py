from .base_page import BasePage
from .locators import CheckBoxPageLocators

class CheckboxPage(BasePage):
    def open_home_directory(self):
        home_directory = self.browser.find_element(*CheckBoxPageLocators.HOME_ARROW_LINK)
        home_directory.click()

    def open_download_directory(self):
        download_directory = self.browser.find_element(*CheckBoxPageLocators.DOWNLOAD_ARROW_LINK)
        download_directory.click()

    def select_word_file(self):
        word_file = self.browser.find_element(*CheckBoxPageLocators.WORD_FILE_LINK)
        word_file.click()

    def should_be_message(self):
        assert self.is_element_present(*CheckBoxPageLocators.MESSAGE), "Success message is not presented"

    def should_be_right_success_text(self):
        result_message = self.browser.find_element(*CheckBoxPageLocators.TEXT_SUCCESS).text
        assert result_message == "wordFile"

    def should_be_checkbox_page_url(self):
        url = self.browser.current_url
        assert "checkbox" in url

    def should_be_open_home_directory(self):
        assert self.is_element_present(*CheckBoxPageLocators.HOME_DIRECTORY),"Home directory is not open"

    def should_be_open_download_directory(self):
        assert self.is_element_present(*CheckBoxPageLocators.DOWNLOAD_DIRECTORY), "Download directory is not open"