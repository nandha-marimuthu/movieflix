from pymongo import MongoClient
from admin import admin_login

client = MongoClient('mongodb+srv://dbuser1:1234@eshop.m8tu7.mongodb.net/test')

db = client['moviebook']
c1 = 'cus_details'
c2 = 'movie'
c3 = 'staff'
c4 = 'theatre_id'
c5 = 'booked'
c6 = 'food'
c7 = 'promo'
collection7=db[c7]
collection4=db[c4]
collection5=db[c5]
collection2=db[c2]
collection1=db[c1]
collection3=db[c3]
collection6=db[c6]

def register():
  uname = input("Name : ")
  email = input("Email : ")
  password = input("Password : ")
  place = input("Region : ")
  collection1.insert_one({"name":uname,"email":email,"password":password,"place":place})
  print('Your Id is registered sucessfully ! ')
  from booking import booking
  booking(uname)

def user_login():
    print("Welcome to Movieflix\n")
    name=input("Username : ")
    pwd=input("Password : ")
    r1 = collection1.find()
    c = 0
    for i in r1:
      if i['name'] == name:
        if i['password'] == pwd:
          c+=1
    if(c==1):
      print("Welcome back",name,"!\n")
      print("B for booking C for cancel")
      bc=input("Enter:")
      if bc=="B":     
        from booking import booking
        booking(name)
      elif bc=="C":
        from cancel import cancel
        cancel()
      else:
        print("Invalid")
        user_login()
    else:
        print("Invalid login credentials")
        reg = input("Do you want to register(y/n) : ")
        if reg == 'y':
          register()

def starthere():
  print("User: 1\nAdmin: 2\n")
  v=int(input("Enter:"))
  if v==1:
    user_login()
  elif v==2:
    from admin import admin_login
    admin_login()
  else:
    print("Invalid choice")

starthere()
