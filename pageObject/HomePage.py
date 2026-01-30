import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:
    def __init__(self,driver):
        self.driver = driver

    shop = (By.XPATH, "//a [text()='Shop']")
    #Amazon parameters
    search = (By.XPATH, "//input [@id = 'twotabsearchtextbox']")
    searchitem = (By.XPATH, "// span [text() = ' western wear']")

    #BookMyShow parameters
    location = (By.XPATH, "//input [@class = 'bwc__sc-1iyhybo-6 ilhhay']")


    def getshop(self):
        return self.driver.find_element(*self.shop)
    def searchItem(self, item):
        self.driver.find_element(*self.search).send_keys(item)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, "// span [text() = ' western wear']")))
        self.driver.find_element(*self.searchitem).click()

    def searchdress(self, dresstype):

        self.driver.find_element(By.XPATH, "//a [@id = 'nav-hamburger-menu']").click()
        wait = WebDriverWait(self.driver, 10)
        items = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "category-section")))
        print("Got the items")
        for item in items:
            catagory = item.find_element(By.CSS_SELECTOR, "div").text
            print(f"Catagory: {catagory}")
            if catagory == 'Shop by Category':
                nesteditems = item.find_elements(By.CSS_SELECTOR, "li")
                print(f"No of nested items : {len(nesteditems)}")

                for nesteditem in nesteditems:
                    fashion = nesteditem.find_element(By.CSS_SELECTOR, "div").text
                    if fashion == dresstype[0]:
                        print(f"Found {fashion}")
                        nesteditem.find_element(By.CSS_SELECTOR, "a").click()
                        try:
                            element = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Western Wear']")))
                            print(f"Found {element.text}")
                            self.driver.execute_script("arguments[0].click();", element)
                        except Exception as e:
                            print(f"An error occurred {e}")
                        break
                break

    #BookMovies methods
    def setlocation(self, place):
        self.driver.find_element(*self.location).send_keys(place)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span [@class = 'bwc__sc-ttnkwg-14 flGQbT']")))
        self.driver.find_element(By.XPATH, "//span [@class = 'bwc__sc-ttnkwg-14 flGQbT']").click()

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.invisibility_of_element((By.XPATH, "//div [@class = 'bwc__sc-1ihur1g-5 gznHHe in-animation']")))

    def getMovies(self, movielanguage):
        pass

