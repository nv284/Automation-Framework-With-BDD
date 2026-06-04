from pages.login_page import LoginPage

def test_login(setup):

    driver = setup

    driver.get("https://opensource-demo.orangehrmlive.com/")

    page = LoginPage()

    page.login(
        driver,
        "Admin",
        "admin123"
    )

    assert "OrangeHRM" in driver.title
