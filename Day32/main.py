import datetime
import smtplib
from arsewards import arsewards_dict
import random
import pandas
#globals
my_email = "KevinsFancyTester12@gmail.com"
destination_email = arsewards_dict["kevinsHiddenEmail"]
password =   arsewards_dict[my_email]
gmPass = arsewards_dict["KevinsFancyGmAppPassword"]
gmail_link = "smtp.gmail.com"

now = datetime.datetime.now()
with open("./quotes.txt","r") as file1:
    quotes = file1.readlines()
#,delimiter = "-")

print(now.weekday())
if now.weekday() == 0:
    with  smtplib.SMTP(host = gmail_link) as connection:
        body = random.choice(quotes)
        connection.starttls()
        connection.login(user= my_email, password = gmPass)
        connection.sendmail(msg = f"Subject:Monday Motivation \n\n{body}", from_addr=my_email, to_addrs=destination_email)
        connection.close()
##################### Extra Hard Starting Project ######################
# Loading birthdays.csv


# 2. Check if today matches a birthday in the birthdays.csv
birthdaysDF = pandas.read_csv("birthdays.csv")
birthdaysDF['date'] = pandas.to_datetime(birthdaysDF[['year','month','day']],format = "YY-MM-DD")
birthdaysDF['date'] = birthdaysDF['date'].apply(lambda x: x.replace(year = now.year))
print(now.date())
print(birthdaysDF['date'])
print('break')
for index,birthday in birthdaysDF.iterrows():
    print(birthday['date'])
    if str(now.date()) == birthday["date"].strftime("%Y-%m-%d"): 
        num = random.randint(1,4)
        with open(f"letter_templates/letter_{num}.txt") as file1:
            lines = file1.readlines()
        body = "\n".join(lines)
        body = body.replace("[NAME]",birthday['name'])
        print(body)

        with  smtplib.SMTP(host = gmail_link) as connection:
        #    body = f"Happy birthday {birthday['name']} \n Hope you have a beautiful day and eat lots of cake"
            subject = f"Happy birthday {birthday['name']}"
            destination_email = birthday['email']
            connection.starttls()
            connection.login(user= my_email, password = gmPass)
            connection.sendmail(msg = f"Subject:{subject} \n\n{body}", from_addr=my_email, to_addrs=destination_email)
            connection.close() 



#if now.date == 

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




