from selenium.webdriver.common.by import By

class LoginPage:

    username=(By.NAME,"username")
    password=(By.NAME,"password")
    login_btn=(By.XPATH,"//button[@type='submit']")

    def login(self,driver,user,pwd):

        driver.find_element(*self.username).send_keys(user)
        driver.find_element(*self.password).send_keys(pwd)
        driver.find_element(*self.login_btn).click()
