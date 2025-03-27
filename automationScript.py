import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Variable Declaration
Wait_Time = 3
Password = "17/CsC/028@"
E_mail = "nsibietimeh@gmail.com"
first_Name = "Kingsley"
last_Name = "Martins"
city = "Lagos"
state_Of_Origin = "AK"
URL = "https://automationplayground.com/crm/login.html"

# Browser Initialization
driver = webdriver.Chrome()
driver.get(URL)
driver.maximize_window()
time.sleep(Wait_Time)

# Fill Login details
Email_Address = driver.find_element(By.ID, "email-id" )
Email_Address.send_keys(E_mail)

PassWord = driver.find_element(By.ID, "password" )
PassWord.send_keys(Password)
time.sleep(Wait_Time)

Remember_me = driver.find_element(By.ID, "remember")
Remember_me.click()

Submit = driver.find_element(By.ID, "submit-id")
Submit.click()
time.sleep(Wait_Time)

# Navigate to dashboard and click on add customer to fill in customer details
Add_New = driver.find_element(By.ID, "new-customer" )
Add_New.click()


Email_Address = driver.find_element(By.ID, "EmailAddress" )
Email_Address.send_keys(E_mail)

First_Name = driver.find_element(By.ID, "FirstName" )
First_Name.send_keys(first_Name)

Last_Name = driver.find_element(By.ID, "LastName" )
Last_Name.send_keys(last_Name)

City = driver.find_element(By.ID, "City" )
City.send_keys(city)

State_Dropdown = Select(driver.find_element(By.ID, "StateOrRegion"))
State_Dropdown.select_by_visible_text("Alaska")

Gender = driver.find_element(By.NAME, "gender")
Gender.click()

Check = driver.find_element(By.NAME, "promos-name" )
Check.click()
time.sleep(Wait_Time)

submit = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
submit.click()
time.sleep(Wait_Time)

# LoginOut
sign_out = driver.find_element(By.LINK_TEXT, "Sign Out")
sign_out.click()
time.sleep(Wait_Time)









