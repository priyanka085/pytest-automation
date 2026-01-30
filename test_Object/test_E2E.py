import time
import pytest
from selenium.webdriver.common.by import By

from pageObject.HomePage import HomePage
from pageObject.ShopPage import ShopPage
from pageObject.CheckOutPage import CheckOutPage


class TestE2E:
    @pytest.mark.usefixtures("setup")
    def test_demo(self):

        homepage = HomePage(self.driver)
        shoppage = ShopPage(self.driver)
        checkoutpage = CheckOutPage(self.driver)
        homepage.getshop().click()


        items = shoppage.getItems()
        for item in items:
            itemName = item.find_element(By.CSS_SELECTOR, "h4 a").text
            if itemName == "iphone X":
                item.find_element(By.CSS_SELECTOR,"button[class = 'btn btn-info']").click()
                break
        shoppage.viewCart()
        shoppage.setQuantity(2)
        shoppage.checkoutProduct()
        checkoutpage.setLocation("India")
        checkoutpage.checkCheckBox()
        checkoutpage.purchaseItems()
        mssg = checkoutpage.getConfirmation()
        assert "Success" in mssg
        time.sleep(1)


