from pages.checkbox_page import CheckboxPage
from pages.main_page import MainPage
from pages.elements_page import ElementsPage

def test_guest_can_select_word_file(browser):
    link = "https://demoqa.com/"
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.should_be_main_page_url()
    main_page.go_to_elements_page()
    elements_page = ElementsPage(browser, browser.current_url)
    elements_page.should_be_elements_page_url()
    elements_page.go_to_checkbox_page()
    checkbox_page = CheckboxPage(browser, browser.current_url)
    checkbox_page.should_be_checkbox_page_url()
    checkbox_page.open_home_directory()
    checkbox_page.should_be_open_home_directory()
    checkbox_page.open_download_directory()
    checkbox_page.should_be_open_download_directory()
    checkbox_page.select_word_file()
    checkbox_page.should_be_message()
    checkbox_page.should_be_right_success_text()