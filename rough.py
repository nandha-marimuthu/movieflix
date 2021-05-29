from pymongo import MongoClient
import datetime

client = MongoClient('mongodb+srv://dbuser1:1234@eshop.m8tu7.mongodb.net/test')

db = client['moviebook']
collection1 = db['theatre_id']

data = [
  {"name":"nandha","password":"admin1"},
  {"name":"keerthana","password":"admin2"},{"name":"jagdeesh","password":"admin3"},{"name":"malavika","password":"admin4"}
]


import random
import string  
import secrets 
num = 4
bid = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(num))  
print("Booking Id is :",bid)  




# c1 = 'cus_details'
# c2 = 
# c3 = 'staff'
# c4 = 'theatre_id'
# c5 = 'booked'
# c6 = 'food'

# collection1=db[c1]
# collection2=db[c2]
# collection3=db[c3]
# collection4=db[c4]
# collection5=db[c5]
# collection6=db[c6]


# ids = input(': ')
# pwd = input(': ')

# r1=collection3.find({'_id':ids})
# for i in r1:
#   a = i

# if (a['password'] == pwd):
#   print('sucess')
# else:
#   print('failure')