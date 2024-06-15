from selenium.webdriver.common.by import By

from pageObjects.ConfimPage import ConfirmPage


class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.XPATH, "//div[@class='card h-100']")
    cardFooter = (By.CSS_SELECTOR, "button[class='btn btn-info']")
    btn_Primary = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    checkOut = (By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitle(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_element(*CheckOutPage.cardFooter)

    def getBtn_Primary(self):
        return self.driver.find_element(*CheckOutPage.btn_Primary)

    def checkOutItems(self):
        self.driver.find_element(*CheckOutPage.checkOut).click()
        last_page = ConfirmPage(self.driver)
        return last_page
