from pymongo import MongoClient
import random

client = MongoClient('mongodb+srv://dbuser1:1234@eshop.m8tu7.mongodb.net/test')

db = client['moviebook']
c5 = 'booked'
collection5=db[c5]

def cancel():
  Bid = input("Booking Id: ")
  name = input("Username: ")
  r1 = collection5.find()
  c = 0
  for i in r1:
    if i['bid'] == Bid:
      if i['name'] == name:
        c+=1
  if(c==1):
    otp=random.randrange(11111,99999)
    print('Generating OTP....')
    import smtplib, ssl

    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "nandhaa403@gmail.com"  # Enter your address
    receiver_email = "nandhabalanmarimuthu15@gmail.com"  # Enter receiver address
    password = 'nandhaaku'
    message = '\nYour otp is '+str(otp)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
      server.login(sender_email, password)
      server.sendmail(sender_email, receiver_email, message)
    o=int(input('Enter the OTP: '))
    if o == otp:
      collection5.delete_one({"bid":Bid})
      print('Your Booking is cancelled\nBill will be refunded soon')
    else:
      print('Invalid Otp')
  else:
    print('Invalid Usename or Booking Id')

cancel()