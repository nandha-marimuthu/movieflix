from pymongo import MongoClient, collection

client = MongoClient('mongodb+srv://dbuser1:1234@eshop.m8tu7.mongodb.net/test')

db = client['moviebook']
c1 = 'cus_details'
c2 = 'movie'
c3 = 'staff'
c4 = 'theatre_id'
c5 = 'booked'

collection4=db[c4]
collection5=db[c5]
collection2=db[c2]
collection1=db[c1]
collection3=db[c3]


def dashboard_details():
    print("1. movie-wise collection\n2.date-wise collection in each theatre")
    d=int(input("Enter:"))
    if d==1:
        moviename=input("Movie name:")
        date=input("Enter date(dd-mm-yyyy):")
        r1=collection5.find({'movie':moviename,'date':date})
        b=0
        c=0
        for i in r1:
            b+=i['bill']
            c+=i['qty']

        print("Collection: Rs.",b,"/-\n","Tickets sold:",c)
    elif d==2:
        a=0
        dd=0
        theatreid=int(input("Enter theatre id:"))
        r2=collection4.find({'_id':theatreid})
        for i in r2:
            print(i['name'])
            tn=i['name']
        r3=collection2.find({'t_id':theatreid})
        date1=input("Enter date(dd-mm-yyyy):")
        r4=collection5.find({'date':date1,'theatre':tn})
        for k in r4:
            a+=k['bill']
            dd+=k['qty']
        print("Collection in",tn,"on",date1,": Rs.",a,"/-")
        print("Tickets sold in",tn,"on",date1,":",dd)            

#dashboard_details()
#theatre wise booking in descending order


