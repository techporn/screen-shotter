from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options


class Driver(WebDriver):
    def __init__(self, browser: str, headless=True):
        options = Options()
        if headless:
            options.add_argument('--headless')
            
        if browser == "chrome":   
            webdriver.Chrome.__init__(self, options=options)
        elif browser == "firefox": webdriver.Firefox.__init__(self, options=options)
        elif browser == "edge":   webdriver.Edge.__init__(self, options=options)
        elif browser == "opera":  webdriver.Opera.__init__(self, options=options)
        elif browser == "ie":     webdriver.Ie.__init__(self, options=options)
        else: raise TypeError()


# driver = Driver("chrome")
# driver.set_window_size(width, height)
# driver.get('https://www.python.org')
# driver.save_screenshot('screenshot.png')
