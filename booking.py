from pymongo import MongoClient, collection
import datetime
import random
import secrets
import string
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

def offer(bill):
  offer = ['FIRST10','MOVIE5']
  of = input('Did you have any Offer Code(y/n) :')
  if of == 'y':
    o = input('OfferCode: ')
    if o in offer:
      bill = bill-(bill/10)
      return bill
    else:
      print('Invalid Code')
      return bill
  else:
    return bill
  



def booking(name):
  result1 = collection4.find()
  print("Theatre list")
  for i in result1:
    print(i['_id'],i['name'])
    tt=i['_id']
  screen=int(input("Enter theatre:"))
  result2 = collection2.find({'t_id':screen})
  for j in result2:
    print("\nMovie id - ",j['_id'],"\nMovie name - ",j['movie'],"\nLanguage - ",j['language'],"\nPrice  - ",j['Price'])
  movie=int(input("Enter movie id:"))

  r3=collection2.find({'_id':movie})
  for j in r3:
    print('You have choosen',j['movie'],j['language'],'price -',j['Price'])
    movie = j['movie']
    bill = j['Price']
    date = datetime.date.today()
    qty = int(input("Enter the No of tickets: "))
    bill = bill*qty
    print(bill)
  data = {'name':name,'movie':movie,'qty':qty,'date':date}

  f = input('Do you want to enjoy the movie with snaks(y/n): ')
  if f == 'y':
    food = collection6.find()
    for i in food:
      print('id: ',i['_id'],'\nName: ',i['name'],'\nprice: ',i['Price'])

    fid = input('Combo Id: ')
    fqty = int(input('Quantity: '))
    f1 = collection6.find({'_id':fid})
    for i in f1:
      print('you have Ordered ',i['name'])
      fbill = i['Price']*fqty
      print(type(fbill))
      bill+=fbill
    data['fid'] = fid
    data ['fqty'] = fqty
  else:
    data['fid'] = 'None'
    data ['fqty'] = 'None'
  offer = ['FIRST10','MOVIE5']
  of = input('Did you have any Offer Code(y/n) :')
  if of == 'y':
    o = input('OfferCode: ')
    if o in offer:
      bill = bill-(bill/10)
    else:
      print('Invalid Code')
  data['bill'] = bill
  num = 4
  bid = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(num))  
  print("Booking Id is :",bid)  
  data['bid'] = bid
  print(data)

booking('nandha')



    
