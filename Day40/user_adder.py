# This is run on a replit instance 
import  requests


print("Welcome to Kevin's Flight Club." +
    "We find the best deals, and email you.")
name = input("What's your first name?\n")
email1 = input("What's your email?\n")
email2 = input("Can you please repeat your email?\n")
price = input("Is there a price you'd like to get alerts for flights below? (only destination currently is Sydney)")

while email1 != email2:
    print("it looks like there's an issue with your emails. Can you please input again?")

    email1 = input("What's your email?\n")
    email2 = input("Can you please repeat your email?\n")

url = 'https://api.sheety.co/7578b074a021d96b936b9161968196fb/flightUserDatabase/sheet1'
body = {
    "sheet1":{
        'userName' : name,
        'email':email1,
        'preferredPrice':price
    }
}
response = requests.post(url = url,json = body)

print(response.json())
print(response.text)
"""
  let url = 'https://api.sheety.co/7578b074a021d96b936b9161968196fb/flightUserDatabase/sheet1';
  let body = {
    sheet1: {
      ...
    }
  }
  fetch(url, {
    method: 'POST',
    body: JSON.stringify(body)
  })
  .then((response) => response.json())
  .then(json => {
    // Do something with object
    console.log(json.sheet1);
  });"""

print("You're in the club")


