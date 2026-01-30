from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class CheckOutPage:
    def __init__(self,driver):
        self.driver = driver

    location = (By.XPATH, "//input [@id = 'country']")
    checkbox = (By.XPATH, "//div[@class = 'checkbox checkbox-primary']")
    purchase = (By.XPATH, "//input [@type = 'submit']")
    mssg = (By.XPATH, "//div[@class = 'alert alert-success alert-dismissible']")
    def setLocation(self, country):
        self.driver.find_element(*self.location).send_keys(country)
        wait = WebDriverWait(self.driver,10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, country)))
        self.driver.find_element(By.LINK_TEXT, country).click()

    def checkCheckBox(self):
        self.driver.find_element(*self.checkbox).click()

    def purchaseItems(self):
        self.driver.find_element(*self.purchase).click()

    def getConfirmation(self):
        return self.driver.find_element(*self.mssg).text