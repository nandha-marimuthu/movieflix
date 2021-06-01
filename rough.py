# from pandas.core.frame import DataFrame
# import streamlit as st
# # To make things easier later, we're also importing numpy and pandas for
# # working with sample data.
# import numpy as np
# import pandas as pd

# from pymongo import MongoClient

# client = MongoClient('mongodb+srv://dbuser1:1234@eshop.m8tu7.mongodb.net/test')

# db = client['moviebook']
# c1 = 'cus_details'
# c2 = 'movie'
# c3 = 'staff'
# c4 = 'theatre_id'
# c5 = 'booked'

# collection4=db[c4]
# collection5=db[c5]
# collection2=db[c2]
# collection1=db[c1]
# collection3=db[c3]



# def theatre():
#     st.title('Theatre wise collection')
#     b =  collection5.find()
#     x,y,z= [],[],[]
#     for i in b:
#         c = collection5.find({'theatre':i['theatre']})
#         a = 0
#         b = 0
#         for j in c:
#             a+=j['qty']
#             b+=j['bill']
#         if i['theatre'] not in x:
#             x.append(i['theatre'])
#             y.append(a)
#             z.append(b)
#     df = pd.DataFrame({
#   'Theatre': x,
#   'Bookings': y,
#   'Collection':z
# })
#     df
#     a = st.line_chart({"data": y,'theatre':z})
    





# def movie():
  
#     st.title('Movie wise collection')
#     b1 =  collection5.find()
#     x1,y1,z1= [],[],[]
#     for i in b1:
#         c1 = collection5.find({'movie':i['movie']})
#         a1 = 0
#         b1 = 0
#         for j in c1:
#           a1+=j['qty']
#           b1+=j['bill']
#         if i['movie'] not in x1:
#           x1.append(i['movie'])
#           y1.append(a1)
#           z1.append(b1)
#     df = pd.DataFrame({
#   'Movie': x1,
#   'Bookings': y1,
#   'Collection':z1
# })
#     df


# def dashboard():
#     if st.checkbox('Show Moviewise collection'):
#         movie()
#     if st.checkbox('Show Theatrewise collection'):
#         theatre()




# def select():
#     r = collection2.find()
#     x=[]
#     for i in r:
#         x.append(i['movie'])
    
   

#     moviename = st.selectbox(
#     'Which movie do you like to book?',
#      x)
     
#     'You selected: ', moviename
#     text = st.text_input("Date")

#     text2 = st.text_input("Quantity")
#     if st.checkbox('Do you want snacks'):
#       text,text2

    
# def booking():

#     # left_column, right_column = st.beta_columns(2)
#     # pressed = left_column.button('Show movies')
#     # if pressed:
#     #     right_column.write("Woohoo!")
#     select()






# option = st.sidebar.selectbox('Menu',['Home','booking','dashboard'])

# if option == 'booking':
#   q = st.sidebar.text_input('Username')
#   w = st.sidebar.text_input('passowrd')
#   if q=='hello' and w=='hello':
#     booking()
# if option == 'dashboard':
#   q = st.sidebar.text_input('Adminname')
#   w = st.sidebar.text_input('passowrd')
#   if q=='hlo' and w=='hlo':
#     dashboard()  
  

