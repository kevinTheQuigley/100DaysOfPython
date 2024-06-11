from hugchat import hugchat
from selenium.webdriver.common.by import By
from hugchat.login import Login
from arsewards import arsewards_dict

# Log in to huggingface and grant authorization to huggingchat
EMAIL = arsewards_dict["kevinsHiddenEmail"]
PASSWD = arsewards_dict["hugit"]
cookie_path_dir = "./cookies/" # NOTE: trailing slash (/) is required to avoid errors
sign = Login(EMAIL, PASSWD)
cookies = sign.login(cookie_dir_path=cookie_path_dir, save_cookies=True)
# Create your ChatBot
chatbot = hugchat.ChatBot(cookies=cookies.get_dict())  # or cookie_path="usercookies/<email>.json"
''''
message_result = chatbot.chat("You are applying for a job, and this is your resume:-"+arsewards_dict["resumeShort"]) # note: message_result is a generator, the method will return immediately.
# Non stream
message_str: str = message_result.wait_until_done() # you can also print(message_result) directly. 
print (message_str)


message_result = chatbot.chat("How many years of experience do you have?") # note: message_result is a generator, the method will return immediately.
# Non stream
message_str: str = message_result.wait_until_done() # you can also print(message_result) directly. 
print (message_str)

# importing the modules
 
# using chrome driver
driver=webdriver.Chrome()
 
# web page url
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
 
# find id of option
x = driver.find_element(By.CSS_SELECTOR,"#RESULT_RadioButton-9")
drop=Select(x)
option_list =drop.options
qString = ""
for option in option_list[1:]:
    qString +=","+option.text
    
question = "Can you select one word from these options: " + qString



'''
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

# Initialize the Chrome driver with options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--log-level=3")  # Suppress warnings and errors
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the web page
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

# Wait to ensure the page is fully loaded (you might use WebDriverWait for a better approach)
time.sleep(3)

# Find the dropdown element by its CSS selector
x = driver.find_element(By.CSS_SELECTOR, "#RESULT_RadioButton-9")

# Initialize the Select class with the dropdown element
drop = Select(x)

# Retrieve all options in the dropdown
option_list = drop.options

# Build the question string from the options, skipping the first one
qString = ",".join([option.text for option in option_list[1:]])
question = "Can you select one word from these options and respond with a single word: " + qString 
print(question)




message_result = chatbot.chat(question)
message_str: str = message_result.wait_until_done() # you can also print(message_result) directly. 
print(message_str)
# select by visible text
drop.select_by_visible_text(message_str)
time.sleep(4)

driver.close()