from seleniumwire import webdriver

# Create a new instance of the Chrome web driver
driver = webdriver.Chrome()

# Perform a GET request to a webpage
driver.get(
    "https://www.google.com/search?q=lambda+test&tbm=isch&ved=2ahUKEwj5yoy0raL_AhWNF7cAHSfBCoYQ2-cCegQIABAA&oq=lambda+test&gs_lcp=CgNpbWcQAzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBggAEAUQHjIGCAAQCBAeMgYIABAIEB4yBggAEAgQHjIGCAAQCBAeMgYIABAIEB46BAgjECc6BwgAEIoFEEM6BwgjEOoCECc6CAgAEIAEELEDUABYgihgpyxoAXAAeASAAbcBiAGnEpIBBDAuMTaYAQCgAQGqAQtnd3Mtd2l6LWltZ7ABA8ABAQ&sclient=img&ei=6bR4ZLmyK42v3LUPp4KrsAg&bih=746&biw=1536&rlz=1C1CHBF_enIN893IN893#imgrc=5gZQH7pNd8B6lM"
)

# Access the requests made by the browser
for request in driver.requests:
    if request.response:
        print(request.url, request.response.status_code)
