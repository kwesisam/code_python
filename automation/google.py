from selenium import webdriver

#it
from selenium.webdriver.common.by import By
from selenium.webdriver
#adding options to stop the browser clsoing by it self
option = webdriver.option()
option.add_experimental_options("datach", True)

#this works but it will close after some time 
#connecting to a browser
driver = webdriver.chrome(options = option)

# accessing the google by it url
driver.get('https//google.com/')

#finding html elment of web page


#for this example search field is the search by for google
search_field = driver.find_element(By.CLASS_NAME, 'the class name')

#clearing the search field
search_field.clear()
# this will inputed in the search by and it will submit by it self
search_field.send_keys("the search term")

