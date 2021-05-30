from pymongo import MongoClient, collection

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

def edit_theatre():
    print("Press A for add and R for remove")
    s=input("Enter:")
    if s=="A":
        n=input("Enter theatre name:")
        a = collection4.find()
        tid = a[collection4.count_documents({})-1]['_id']+1
        data={"_id":tid,"name":n}
        collection4.insert_one(data)
        print(n,"Theatre Added to the theatre list")
    elif s=="R":
        print("List of theatres")
        r3=collection4.find()
        for k in r3:
            print(k['_id'],"-",k['name'])
        print()
        rid=int(input("Enter theatre id:"))
        collection4.delete_one({"_id":rid})
        print("Theatre removed from list!")

def edit_movies():
    print("Press A for add and R for remove")
    s = input("Enter:").strip()
    if s == "A":
        a = collection2.find()
        mid = a[collection2.count_documents({})-1]['_id']+1

        movie = input("Enter movie name:")
        lang = input("Enter movie language:")
        price = int(input("Enter ticket rate:"))
        tid=int(input("Enter theatre:"))
        data={"_id":mid,"movie":movie,"language":lang,"Price":price,"t_id":tid}
        collection2.insert_one(data)
        print(movie,"Added to the movie list")
    elif s=="R":
        tt=int(input("Enter theatre id:"))
        print("List of movies")
        r3=collection2.find({'t_id':tt})
        for k in r3:
            print(k['_id'],"-",k['movie'])
        print()
        rid=int(input("Enter movie id:"))
        collection2.delete_one({"_id":rid})
        print("Movie removed from list!")


def edit_food():
    print("Press A for add and R for remove")
    s=input("Enter:")
    if s=="A":
        a = collection6.find()
        c = int(a[collection6.count_documents({})-1]['_id'][2])+1
        cid = "FC"+str(c)
        fname=input("Enter combo name:")
        fp=int(input("Enter combo price:"))
        foods={"_id":cid,"name":fname,"Price":fp}
        r5=collection6.insert_one(foods)
        print("Combo added to list")
    elif s=="R":
        r5=collection6.find()
        for j in r5:
            print(j['_id'],"-",j['name'],"-",j['Price'])
        fid=input("Enter food_combo id:")
        collection6.delete_one({'_id':fid})
        
def admin():
    
    while True:
        
        choice=int(input("Add/remove theatre: 1\nAdd/remove movies: 2\nAdd/remove combos: 3\nView collection: 4\nExit :5\nEnter: "))
        if choice==1:
            edit_theatre()
        elif choice==2:
            edit_movies()
        elif choice==3:
            edit_food()
        elif choice==4:
            from dashboard import dashboard_details
            dashboard_details()
        elif choice==5:
            exit()
        else:
            print("Invalid choice")

def admin_login():
    print("Welcome to Movieflix admin portal\n")
    admin_id=input("Adminname : ")
    pwd=input("Password : ")
    r1 = collection3.find()
    c = 0
    for i in r1:
      if i['name'] == admin_id:
        if i['password'] == pwd:
          c+=1
    if(c==1):
      print("Welcome back",admin_id,"!\n")
      admin()
    else:
        print("Invalid admin credentials")


#admin_login()

    

    
        
                            







        
