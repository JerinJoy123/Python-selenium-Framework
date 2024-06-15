from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest

from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.ConfimPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utlities.baseClass import BaseClass


# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):
    def test_e2e(self):
        homePage = HomePage(self.driver)
        checkOutPage = homePage.shopItems()
        products = checkOutPage.getCardTitle()

        for product in products:
            product_name = product.find_element(By.XPATH, "div/h4/a").text
            if product_name == "Blackberry":
                checkOutPage.getCardFooter().click()

        checkOutPage.getBtn_Primary().click()
        last_page = checkOutPage.checkOutItems()

        self.driver.find_element(By.ID, "country").send_keys("ind")
        self.verifyLinkPresence("India")
        last_page.getLocation().click()
        last_page.findCheckBox().click()
        last_page.tapSuccessButton().click()
        successText = last_page.getMessage().text
        assert "Success" in successText
