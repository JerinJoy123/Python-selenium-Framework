from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    location = (By.LINK_TEXT, "India")
    checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    success_Button = (By.CSS_SELECTOR, "input[class*=' btn-success']")
    message = (By.CLASS_NAME, "alert-success")

    def getLocation(self):
        return self.driver.find_element(*ConfirmPage.location)

    def findCheckBox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def tapSuccessButton(self):
        return self.driver.find_element(*ConfirmPage.success_Button)

    def getMessage(self):
        return self.driver.find_element(*ConfirmPage.message)
