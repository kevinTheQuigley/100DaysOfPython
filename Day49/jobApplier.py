from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import random as rd
import time
from arsewards import arsewards_dict

options = ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

#chrome_options = Options()
#chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
#driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3947031289&distance=25&geoId=102837144&keywords=python%20developer&origin=JOBS_HOME_KEYWORD_HISTORY&refresh=true")
nav_button = driver.find_element(By.CSS_SELECTOR, ".nav__button-secondary")
nav_button.click()

#Next page
email_input = driver.find_element(By.CSS_SELECTOR, "#username")
email_input.send_keys(arsewards_dict["kevinsHiddenEmail"])

pass_input = driver.find_element(By.CSS_SELECTOR, "#password")
pass_input.send_keys(arsewards_dict["lin"],Keys.ENTER)

def abort_application():
    # Click Close Button
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    time.sleep(2)
    # Click Discard Button
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()



print("looking for jobs list")
time.sleep(1.5)
job_list = driver.find_elements(By.CSS_SELECTOR,".job-card-container--clickable")
print("Found jobs list with " + str(len(job_list)) + " jobs")
for i in range(len(job_list)):
    print(i)
    time.sleep(1.5)
    print("Selecting Job")
    job_list[i].click()
    time.sleep(1.5)
    print("Applying")
    try:
        #apply_button =  driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button")
        apply_button =  driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
        apply_button.click()
        time.sleep(2)
        phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if phone.text == "":
            phone.send_keys(arsewards_dict["blank_number"],Keys.ENTER)
        next_button=  driver.find_element(By.CSS_SELECTOR, ".justify-flex-end button")
        next_button.click()
        time.sleep(2)
        next_button=  driver.find_element(By.CSS_SELECTOR, ".artdeco-button--primary")
        next_button.click()
        time.sleep(2)
        

    except NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        continue


