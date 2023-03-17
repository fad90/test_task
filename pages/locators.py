from selenium.webdriver.common.by import By

class MainPageLocators():
    ELEMENT_LINK = (By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div[1]")

class ElementsPageLocators():
    CHECKBOX_LINK = (By.ID, "item-1")

class CheckBoxPageLocators():
    HOME_ARROW_LINK = (By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/ol/li/span/button")
    DOWNLOAD_ARROW_LINK = (By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/ol/li/ol/li[3]/span/button")
    WORD_FILE_LINK = (By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[1]/ol/li/ol/li[3]/ol/li[1]/span/label")
    MESSAGE = (By.ID, "result")
    TEXT_SUCCESS = (By.CLASS_NAME, "text-success")
    HOME_DIRECTORY = (By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/ol/li/ol")
    DOWNLOAD_DIRECTORY = (By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div/ol/li/ol/li[3]/ol")