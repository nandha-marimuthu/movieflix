from pymongo import MongoClient, collection
import datetime
import random
import string  
import secrets  
client = MongoClient('mongodb+srv://dbuser1:1234@eshop.m8tu7.mongodb.net/test')

db = client['moviebook']
c1 = 'cus_details'
c2 = 'movie'
c3 = 'staff'
c4 = 'theatre_id'
c5 = 'booked'
c6 = 'food'
tcount=50
collection4=db[c4]
collection5=db[c5]
collection2=db[c2]
collection1=db[c1]
collection3=db[c3]
collection6=db[c6]
data={}
cus_details={}
print("Welcome to TheatreZone")
print()
booking_id=random.randint(1000,10000)
ticket_id=random.randint(10,100)
result1 = collection4.find()
print()
print("Theatre list")
for i in result1:
  print(i['_id'],i['name'])
  tt=i['_id']
screen=int(input("Enter theatre:"))
result2 = collection2.find({'t_id':screen})
for j in result2:
  print("Movie id - ",j['_id'])
  print("Movie name - ",j['movie'])
  print("Language - ",j['language'])
  print("Price  - ",j['Price'])
  print()
movie=int(input("Enter movie id:"))
print("Your selection")
r3=collection2.find({'_id':movie})
for j in r3:
  print(j['movie'],j['language'],j['Price'])
  m=j['movie']
  a=j['Price']
t=int(input("Enter ticket count:"))
if t<tcount:
  rate=t*a;
  #print(rate)
  tcount=tcount-t;
  #print(tcount);
val=rate
mydate=datetime.date.today()
#d= Date()
#print(d)
#print(mydate)
data['_id']=booking_id
data['customer']=cname
data['movie']=m
#data['date']=mydate
data['theatre_id']=screen
data['ticket_id']=ticket_id
#print(data)
print("Do you want to enjoy your show with snacks ? (y/n)")
f=input("Enter your choice:")
if f=="y":
  food(data)




  

print()
print("Your booking!!")
r4=collection5.insert_one(data)
for key,val in data.items():
print (key,"-",val)

