from selenium.webdriver.common.by import By

class ShopPage:
    def __init__(self,driver):
        self.driver = driver

    items = (By.CSS_SELECTOR, "div [class = 'card h-100']")
    cart = (By.XPATH, "//a [@class = 'nav-link btn btn-primary']")
    quantity = (By.XPATH, "//input[ @class = 'form-control']")
    checkoutitem = (By.XPATH, "//button[ @class ='btn btn-success']")

    def getItems(self):
        return self.driver.find_elements(*self.items)
    def viewCart(self):
        self.driver.find_element(*self.cart).click()
    def setQuantity(self,number):
        self.driver.find_element(*self.quantity).clear()
        self.driver.find_element(*self.quantity).send_keys(number)
    def checkoutProduct(self):
        self.driver.find_element(*self.checkoutitem).click()


