from hugchat import hugchat
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
message_result = chatbot.chat("You are applying for a job, and this is your resume:-"+arsewards_dict["resumeShort"]) # note: message_result is a generator, the method will return immediately.
# Non stream
message_str: str = message_result.wait_until_done() # you can also print(message_result) directly. 

message_result = chatbot.chat("How many years of experience do you have?") # note: message_result is a generator, the method will return immediately.
# Non stream
message_str: str = message_result.wait_until_done() # you can also print(message_result) directly. 
print (message_str)