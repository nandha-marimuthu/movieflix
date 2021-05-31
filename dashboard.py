from pymongo import MongoClient

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



def movie_bookings():
    b =  collection5.find()
    x,y= [],[]

    for i in b:
        c = collection5.find({'movie':i['movie']})
        a = 0
        for j in c:
            a+=j['qty']
        if i['movie'] not in x:
            x.append(i['movie'])
            y.append(a)
    for i in range(len(x)):
        print(x[i],' - ',y[i])

def theatre_bookings():
    b =  collection5.find()
    x,y= [],[]

    for i in b:
        c = collection5.find({'theatre':i['theatre']})
        a = 0
        for j in c:
            a+=j['qty']
        if i['theatre'] not in x:
            x.append(i['theatre'])
            y.append(a)
    for i in range(len(x)):
        print(x[i],' - ',y[i])


def dashboard_details():
    print("1. movie-wise collection\n2.theatre-wise collection\n3. Moviewise Bookings\n4.Theatrewise Bookings")
    d=int(input("Enter:"))
    if d==1:
        r = collection5.find()
        x=[]
        for i in r:
            if i['movie'] not in x:
                x.append(i['movie'])
                print(i['movie'])
        moviename=input("Movie name:")
        r1=collection5.find({'movie':moviename})
        b=0
        c=0
        for i in r1:
            b+=i['bill']
            c+=i['qty']

        print("Collection: Rs.",b,"/-\n","Tickets sold:",c)
    elif d==2:
        rr = collection5.find()
        xx=[]
        for i in rr:
            if i['theatre'] not in xx:
                xx.append(i['theatre'])
                print(i['theatre'])
        theatrename=input("Theatre name:")
        r1=collection5.find({'theatre':theatrename})
        bb=0
        cc=0
        for i in r1:
            bb+=i['bill']
            cc+=i['qty']

        print("Collection: Rs.",bb,"/-\n","Tickets sold:",cc)
        
    elif (d == 3):
        movie_bookings()
    elif(d==4):
        theatre_bookings()       







