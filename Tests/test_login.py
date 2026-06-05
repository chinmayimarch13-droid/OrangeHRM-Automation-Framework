from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com")

print(driver.title)

driver.quit()
