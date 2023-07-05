from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#chrome driver
# service_Obj = Service("D:\RobotAutomation\ChromeDriver\chromedriver.exe") # Setting path for chrome driver
#
# options = webdriver.ChromeOptions() # Keep browser tab open
# options.add_experimental_option("detach", True) # Keep browser tab open
#
#
# driver = webdriver.Chrome(options=options, service=service_Obj) # Initializing the driver for chrome
driver = webdriver.Chrome(executable_path="D:\RobotAutomation\ChromeDriver\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.saucedemo.com/") # Hitting the Url
print("Navigated to the URL")

print(driver.title) #tab title
print(driver.current_url)

driver.find_element(By.ID,"user-name").send_keys("standard_user") # Enter Username
driver.find_element(By.ID,"password").send_keys("secret_sauce") # Enter Password

print("Successfully Logged In")

# //tagName[@attribute='value']
driver.find_element(By.XPATH,"//input[@data-test='login-button']").click()  # Click log in button
url = driver.current_url
print(url)
assert "https://www.saucedemo.com/inventory.html" in url  # Check the new url

item1 = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/a/div").text
item2 = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div/div/div[5]/div[2]/div[1]/a/div").text
driver.find_element(By.XPATH,"//*[@id='add-to-cart-sauce-labs-bike-light']").click() # Click Bike light item 1
driver.find_element(By.XPATH,"//*[@id='add-to-cart-sauce-labs-onesie']").click() #Click Onesie item 2


number = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[1]/div[1]/div[3]/a/span").text # Verifying number of products selected
print("Number of products selected is "+str(number))
driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[1]/div[1]/div[3]/a/span").click() # Clicking the Cart icon

print("Navigated to Cart Section")
print(driver.current_url)
assert item1 in driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div[2]/a/div").text #Check the selected product match in cart page
assert item2 in driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div[1]/div[4]/div[2]/a/div").text #Check the selected product match in cart page


driver.find_element(By.ID,"checkout").click() #Clicked Checkout
driver.find_element(By.ID,"first-name").send_keys("Test") #Enter First Name
driver.find_element(By.ID,"last-name").send_keys("Purchase") #Enter Last Name
driver.find_element(By.ID,"postal-code").send_keys("123456") #Enter Zip Code
driver.find_element(By.ID,"continue").click() #Click Continue button
driver.find_element(By.ID,"finish").click() #Click Finish Button

message = driver.find_element(By.XPATH,"//*[@id='checkout_complete_container']/h2").text #Append successful message
assert "Thank" in message
print("Pass")
print("Testing Git Workflow")
print("Hellow World")
print("Test1")
print("Test2")


