import time
import pytest
from selenium.webdriver.common.by import By

from pageObject.HomePage import HomePage


class TestBigBasket:
    @pytest.mark.usefixtures("setupBigB")
    def test_BigB(self):
        homepage = HomePage(self.driver)
        try:
            element = self.driver.find_element(By.CSS_SELECTOR, "[class = 'a-button-text']")
            if element.is_displayed():
                print("Element found")
                element.click()
        except Exception as e:
            print(f"An error occurred {e}")

        dresstype = ["Women's Fashion", "Western Wear", "Dresses and Jumpsuits", "VRVastra"]
        homepage.searchdress(dresstype)
        #homepage.searchItem("Women's clothing")

        time.sleep(2)

