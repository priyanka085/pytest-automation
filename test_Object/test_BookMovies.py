import time
import pytest
from selenium.webdriver.common.by import By

from pageObject.HomePage import HomePage


class TestBookMovies:

    @pytest.mark.usefixtures("setupBookMovies")
    def test_BookMovies(self):

        homepage = HomePage(self.driver)
        homepage.setlocation("Kolkata")

        self.driver.find_element(By.XPATH, "//a [text()='Movies']").click()
        time.sleep(2)
        homepage.getMovies("Hindi")

        languages = self.driver.find_elements(By.CSS_SELECTOR, "div [class ='sc-ije77g-2 evAbck']")
        for language in languages:
            zonre = language.find_element(By.CSS_SELECTOR, "div").text

            if zonre == 'Hindi':
                language.find_element(By.CSS_SELECTOR, "div").click()
                print(zonre)
                break

        time.sleep(4)



