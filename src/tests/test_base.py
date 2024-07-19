

def test_base(set_up_browser):
    driver = set_up_browser
    driver.get("https://skillbox.ru/")
    assert "Skillbox" == driver.title
    driver.quit()