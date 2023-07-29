import smtplib
import random
import datetime as dt
with open('quotes.txt','r') as data_file:
    quotes_data=data_file.readlines()
    todays_quote = random.choice(quotes_data)

with smtplib.SMTP('') as connection:
    connection.starttls()
    connection.login('mymail@mail.com','password')
    connection.sendmail(from_addr='mymail@mail.com',
                        to_addrs='mymail@mail.com',
                        msg=f'Subject:Todays quote\n\n {todays_quote}')