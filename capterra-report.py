import shutil
import selenium
import time
from selenium import webdriver
import os
import capterra_config
# to make sure we are in the right directory
os.chdir(r'C:\Users\leven\Desktop\Marketing DB')

#Show selenium where the chromedriver is located.
chromedriver = 'c:/Users/leven/Desktop/Marketing DB/chromedriver.exe'
driver = webdriver.Chrome(chromedriver)

#Capterra credentials
username = your username here
password = your password here

#Open capterra as a new tab in chrome
driver.get("https://capterra.com/vp")

#enter the username & password
form_username = driver.find_element_by_id('login_username')
form_username.send_keys(username)

form_password = driver.find_element_by_id('login_password')
form_password.send_keys(password)


#Click the submit button
driver.find_element_by_name('commit').click()

# By now we are in!

#Find the reports link and click.
driver.get("https://www.capterra.com/vp/clicks")

# Filling the form for report filters. By default the report end date is the most recently available one.
# For now, I'm only going to set the report begin date and that will be January 1 2018.
start_date_form = driver.find_element_by_id('start_date')

# We need to clear the default value first.
driver.find_element_by_id('start_date').clear()

# Pass the start date value
start_date = "01-01-2018"
start_date_form.send_keys(start_date)
    #trying to click the selected date which should close the calendar overlay
day = driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[1]/td[2]/a')
day.click()

#click "get report"
submit_element = driver.find_element_by_class_name("submit")
submit_element.click()

#finding and clicking the download link
download = driver.find_element_by_link_text("Download Daily Activity")
download.click()

#to make the script wait until the download is complete
time.sleep(4000)

#to find and manipulate the downloaded files.

# getting to the downloads folder & finding the downloaded file.
path = r'C:\Users\leven\Downloads'
os.chdir(path)
files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
    #print ("All by modified oldest to newest:"), files

#rename & move the downloaded file as levo-query in the marketing db folder.
os.rename(files[-1], 'capterra')
shutil.move(r'C:\Users\leven\Downloads\capterra',r'C:\Users\leven\Desktop\Marketing DB\Data\capterra.csv')

# logging out
logout = driver.find_element_by_link_text("Logout")
logout.click()

print("Successfully downloaded the report as capterra.csv")

#changing the directory back to marketing db
os.chdir(r'C:\Users\leven\Desktop\Marketing DB')
