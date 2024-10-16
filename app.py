import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import mysql.connector
import time


title=st.title('Red Bus')
subtitle=st.markdown('Online Bus Ticket Booking Site')

andhra=[]
df=pd.read_csv("all_data_ap.csv")
for i,r in df.iterrows(): 
    andhra.append(r['Route_name'])

kerala=[]
df=pd.read_csv("all_data_k.csv")
for i,r in df.iterrows():
    kerala.append(r['Route_name'])

telungana=[]
df=pd.read_csv("all_data_t.csv")
for i,r in df.iterrows():
    telungana.append(r['Route_name'])

kadamba=[]
df=pd.read_csv("all_data_kad.csv")
for i,r in df.iterrows():
    kadamba.append(r['Route_name'])

rajasthan=[]
df=pd.read_csv("all_data_r.csv")
for i,r in df.iterrows():
    rajasthan.append(r['Route_name'])

southbengal=[]
df=pd.read_csv("all_data_sb.csv")
for i,r in df.iterrows():
    southbengal.append(r['Route_name'])

hp=[]
df=pd.read_csv("all_data_hp.csv")
for i,r in df.iterrows():
    hp.append(r["Route_name"])

assam=[]
df=pd.read_csv("all_data_a.csv")
for i,r in df.iterrows():
    assam.append(r['Route_name'])

up=[]
df=pd.read_csv("all_data_up.csv")
for i,r in df.iterrows():
    up.append(r["Route_name"])

bihar=[]
df=pd.read_csv("all_data_b.csv")
for i,r in df.iterrows():
    bihar.append(r['Route_name'])


web=option_menu(menu_title="Online Bus",
                options=["Home","States and Routes"],
                icons=["House","Info_circle"],
                orientation="horizontal"
                )  

if web=="Home":
    st.title("Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit")
    
if web=="States and Routes":
    states=st.selectbox("Lists of States",['Andhra Pradesh','Kerala','Telungana','Kadamba','Rajasthan','South Bengal','Himachal Pradesh','Assam','Uttar Pradesh','Bihar'])
    fare=st.radio("Choose bus fare range",['50-1000','1000-2000','2000 and 4000'])

#Andhra state
if states=="Andhra Pradesh":
    A=st.selectbox("List of Routes",andhra)
    if fare=='50-1000':
        mydb = mysql.connector.connect(host="localhost",user="root",port="3306",database="redbus",password="181506")
        mycursor = mydb.cursor()
        qurey=f'''select * from redbusdetails
                    where Price Between 50 and 1000 and Route_name="{A}"
                    order by Price desc'''
        mycursor.execute(qurey)
        out=mycursor.fetchall()
        df=pd.DataFrame(out,columns=["ID","Route_name","Route_link","Bus_name","Bus_type","Departing_time","Duration","Reaching_time","Star_rating","Price","Seat_availability"])
        st.write(df)
    if fare=='1000-2000':
        mydb = mysql.connector.connect(host="localhost",user="root",port="3306",database="redbus",password="181506")
        mycursor = mydb.cursor()
        qurey=f'''select * from redbusdetails
                    where Price Between 1000 and 2000 and Route_name="{A}"
                    order by Price desc'''
        mycursor.execute(qurey)
        out=mycursor.fetchall()
        df=pd.DataFrame(out,columns=["ID","Route_name","Route_link","Bus_name","Bus_type","Departing_time","Duration","Reaching_time","Star_rating","Price","Seat_availability"])
        st.write(df)
    if fare=='2000 and 4000':
        mydb = mysql.connector.connect(host="localhost",user="root",port="3306",database="redbus",password="181506")
        mycursor = mydb.cursor()
        qurey=f'''select * from redbusdetails
                    where Price Between 2000 and 4000 and Route_name="{A}"
                    order by Price desc'''
        mycursor.execute(qurey)
        out=mycursor.fetchall()
        df=pd.DataFrame(out,columns=["ID","Route_name","Route_link","Bus_name","Bus_type","Departing_time","Duration","Reaching_time","Star_rating","Price","Seat_availability"])
        st.write(df)
#Kerala
if states=="Kerala":
    K=st.selectbox("List of Routes",kerala)
    if fare=='50-1000':
        mydb = mysql.connector.connect(host="localhost",user="root",port="3306",database="redbus",password="181506")
        mycursor = mydb.cursor()
        qurey=f'''select * from redbusdetails
                    where Price Between 50 and 1000 and Route_name="{K}"
                    order by Price desc'''
        mycursor.execute(qurey)
        out=mycursor.fetchall()
        df=pd.DataFrame(out,columns=["ID","Route_name","Route_link","Bus_name","Bus_type","Departing_time","Duration","Reaching_time","Star_rating","Price","Seat_availability"])
        st.write(df)
    if fare=='1000-2000':
        mydb = mysql.connector.connect(host="localhost",user="root",port="3306",database="redbus",password="181506")
        mycursor = mydb.cursor()
        qurey=f'''select * from redbusdetails
                    where Price Between 1000 and 2000 and Route_name="{K}"
                    order by Price desc'''
        mycursor.execute(qurey)
        out=mycursor.fetchall()
        df=pd.DataFrame(out,columns=["ID","Route_name","Route_link","Bus_name","Bus_type","Departing_time","Duration","Reaching_time","Star_rating","Price","Seat_availability"])
        st.write(df)
    if fare=='2000 and 4000':
        mydb = mysql.connector.connect(host="localhost",user="root",port="3306",database="redbus",password="181506")
        mycursor = mydb.cursor()
        qurey=f'''select * from redbusdetails
                    where Price Between 2000 and 4000 and Route_name="{K}"
                    order by Price desc'''
        mycursor.execute(qurey)
        out=mycursor.fetchall()
        df=pd.DataFrame(out,columns=["ID","Route_name","Route_link","Bus_name","Bus_type","Departing_time","Duration","Reaching_time","Star_rating","Price","Seat_availability"])
        st.write(df)
#Telungana
if states=="Telungana":
    T=st.selectbox("List of Routes",telungana)
    if fare=='50-1000':
        mydb = mysql.connector.connect(host="localhost",user="root",port="3306",database="redbus",password="181506")
        mycursor = mydb.cursor()
        qurey=f'''select * from redbusdetails
                    where Price Between 50 and 1000 and Route_name="{T}"
                    order by Price desc'''
        mycursor.execute(qurey)
        out=mycursor.fetchall()
        df=pd.DataFrame(out,columns=["ID","Route_name","Route_link","Bus_name","Bus_type","Departing_time","Duration","Reaching_time","Star_rating","Price","Seat_availability"])
        st.write(df)
    if fare=='1000-2000':
        mydb = mysql.connector.connect(host="localhost",user="root",port="3306",database="redbus",password="181506")
        mycursor = mydb.cursor()
        qurey=f'''select * from redbusdetails
                    where Price Between 1000 and 2000 and Route_name="{T}"
                    order by Price desc'''
        mycursor.execute(qurey)
        out=mycursor.fetchall()
        df=pd.DataFrame(out,columns=["ID","Route_name","Route_link","Bus_name","Bus_type","Departing_time","Duration","Reaching_time","Star_rating","Price","Seat_availability"])
        st.write(df)
    if fare=='2000 and 4000':
        mydb = mysql.connector.connect(host="localhost",user="root",port="3306",database="redbus",password="181506")
        mycursor = mydb.cursor()
        qurey=f'''select * from redbusdetails
                    where Price Between 2000 and 4000 and Route_name="{T}"
                    order by Price desc'''
        mycursor.execute(qurey)
        out=mycursor.fetchall()
        df=pd.DataFrame(out,columns=["ID","Route_name","Route_link","Bus_name","Bus_type","Departing_time","Duration","Reaching_time","Star_rating","Price","Seat_availability"])
        st.write(df)
#Kadamba
if states=="Kadamba":
    Ka=st.selectbox("List of Routes",kadamba)
    if fare=='50-1000':
        mydb = mysql.connector.connect(host="localhost",user="root",port="3306",database="redbus",password="181506")
        mycursor = mydb.cursor()
        qurey=f'''select * from redbusdetails
                    where Price Between 50 and 1000 and Route_name="{Ka}"
                    order by Price desc'''
        mycursor.execute(qurey)
        out=mycursor.fetchall()
        df=pd.DataFrame(out,columns=["ID","Route_name","Route_link","Bus_name","Bus_type","Departing_time","Duration","Reaching_time","Star_rating","Price","Seat_availability"])
        st.write(df)
    if fare=='1000-2000':
        mydb = mysql.connector.connect(host="localhost",user="root",port="3306",database="redbus",password="181506")
        mycursor = mydb.cursor()
        qurey=f'''select * from redbusdetails
                    where Price Between 1000 and 2000 and Route_name="{Ka}"
                    order by Price desc'''
        mycursor.execute(qurey)
        out=mycursor.fetchall()
        df=pd.DataFrame(out,columns=["ID","Route_name","Route_link","Bus_name","Bus_type","Departing_time","Duration","Reaching_time","Star_rating","Price","Seat_availability"])
        st.write(df)
    if fare=='2000 and 4000':
        mydb = mysql.connector.connect(host="localhost",user="root",port="3306",database="redbus",password="181506")
        mycursor = mydb.cursor()
        qurey=f'''select * from redbusdetails
                    where Price Between 2000 and 4000 and Route_name="{Ka}"
                    order by Price desc'''
        mycursor.execute(qurey)
        out=mycursor.fetchall()
        df=pd.DataFrame(out,columns=["ID","Route_name","Route_link","Bus_name","Bus_type","Departing_time","Duration","Reaching_time","Star_rating","Price","Seat_availability"])
        st.write(df)
#Rajasthan
if states=="Rajasthan":
    R=st.selectbox("List of Routes",rajasthan)
    if fare=='50-1000':
        mydb = mysql.connector.connect(host="localhost",user="root",port="3306",database="redbus",password="181506")
        mycursor = mydb.cursor()
        qurey=f'''select * from redbusdetails
                    where Price Between 50 and 1000 and Route_name="{R}"
                    order by Price desc'''
        mycursor.execute(qurey)
        out=mycursor.fetchall()
        df=pd.DataFrame(out,columns=["ID","Route_name","Route_link","Bus_name","Bus_type","Departing_time","Duration","Reaching_time","Star_rating","Price","Seat_availability"])
        st.write(df)
    if fare=='1000-2000':
        mydb = mysql.connector.connect(host="localhost",user="root",port="3306",database="redbus",password="181506")
        mycursor = mydb.cursor()
        qurey=f'''select * from redbusdetails
                    where Price Between 1000 and 2000 and Route_name="{R}"
                    order by Price desc'''
        mycursor.execute(qurey)
        out=mycursor.fetchall()
        df=pd.DataFrame(out,columns=["ID","Route_name","Route_link","Bus_name","Bus_type","Departing_time","Duration","Reaching_time","Star_rating","Price","Seat_availability"])
        st.write(df)
    if fare=='2000 and 4000':
        mydb = mysql.connector.connect(host="localhost",user="root",port="3306",database="redbus",password="181506")
        mycursor = mydb.cursor()
        qurey=f'''select * from redbusdetails
                    where Price Between 2000 and 4000 and Route_name="{R}"
                    order by Price desc'''
        mycursor.execute(qurey)
        out=mycursor.fetchall()
        df=pd.DataFrame(out,columns=["ID","Route_name","Route_link","Bus_name","Bus_type","Departing_time","Duration","Reaching_time","Star_rating","Price","Seat_availability"])
        st.write(df)
#SouthBengal
if states=="South Bengal":
    S=st.selectbox("List of Routes",southbengal)
    if fare=='50-1000':
        mydb = mysql.connector.connect(host="localhost",user="root",port="3306",database="redbus",password="181506")
        mycursor = mydb.cursor()
        qurey=f'''select * from redbusdetails
                    where Price Between 50 and 1000 and Route_name="{S}"
                    order by Price desc'''
        mycursor.execute(qurey)
        out=mycursor.fetchall()
        df=pd.DataFrame(out,columns=["ID","Route_name","Route_link","Bus_name","Bus_type","Departing_time","Duration","Reaching_time","Star_rating","Price","Seat_availability"])
        st.write(df)
    if fare=='1000-2000':
        mydb = mysql.connector.connect(host="localhost",user="root",port="3306",database="redbus",password="181506")
        mycursor = mydb.cursor()
        qurey=f'''select * from redbusdetails
                    where Price Between 1000 and 2000 and Route_name="{S}"
                    order by Price desc'''
        mycursor.execute(qurey)
        out=mycursor.fetchall()
        df=pd.DataFrame(out,columns=["ID","Route_name","Route_link","Bus_name","Bus_type","Departing_time","Duration","Reaching_time","Star_rating","Price","Seat_availability"])
        st.write(df)
    if fare=='2000 and 4000':
        mydb = mysql.connector.connect(host="localhost",user="root",port="3306",database="redbus",password="181506")
        mycursor = mydb.cursor()
        qurey=f'''select * from redbusdetails
                    where Price Between 2000 and 4000 and Route_name="{S}"
                    order by Price desc'''
        mycursor.execute(qurey)
        out=mycursor.fetchall()
        df=pd.DataFrame(out,columns=["ID","Route_name","Route_link","Bus_name","Bus_type","Departing_time","Duration","Reaching_time","Star_rating","Price","Seat_availability"])
        st.write(df)
#Himachal pradesh
if states=="Himachal Pradesh":
    H=st.selectbox("List of Routes",hp)
    if fare=='50-1000':
        mydb = mysql.connector.connect(host="localhost",user="root",port="3306",database="redbus",password="181506")
        mycursor = mydb.cursor()
        qurey=f'''select * from redbusdetails
                    where Price Between 50 and 1000 and Route_name="{H}"
                    order by Price desc'''
        mycursor.execute(qurey)
        out=mycursor.fetchall()
        df=pd.DataFrame(out,columns=["ID","Route_name","Route_link","Bus_name","Bus_type","Departing_time","Duration","Reaching_time","Star_rating","Price","Seat_availability"])
        st.write(df)
    if fare=='1000-2000':
        mydb = mysql.connector.connect(host="localhost",user="root",port="3306",database="redbus",password="181506")
        mycursor = mydb.cursor()
        qurey=f'''select * from redbusdetails
                    where Price Between 1000 and 2000 and Route_name="{H}"
                    order by Price desc'''
        mycursor.execute(qurey)
        out=mycursor.fetchall()
        df=pd.DataFrame(out,columns=["ID","Route_name","Route_link","Bus_name","Bus_type","Departing_time","Duration","Reaching_time","Star_rating","Price","Seat_availability"])
        st.write(df)
    if fare=='2000 and 4000':
        mydb = mysql.connector.connect(host="localhost",user="root",port="3306",database="redbus",password="181506")
        mycursor = mydb.cursor()
        qurey=f'''select * from redbusdetails
                    where Price Between 2000 and 4000 and Route_name="{H}"
                    order by Price desc'''
        mycursor.execute(qurey)
        out=mycursor.fetchall()
        df=pd.DataFrame(out,columns=["ID","Route_name","Route_link","Bus_name","Bus_type","Departing_time","Duration","Reaching_time","Star_rating","Price","Seat_availability"])
        st.write(df)
#Assam
if states=="Assam":
    As=st.selectbox("List of Routes",assam)
    if fare=='50-1000':
        mydb = mysql.connector.connect(host="localhost",user="root",port="3306",database="redbus",password="181506")
        mycursor = mydb.cursor()
        qurey=f'''select * from redbusdetails
                    where Price Between 50 and 1000 and Route_name="{As}"
                    order by Price desc'''
        mycursor.execute(qurey)
        out=mycursor.fetchall()
        df=pd.DataFrame(out,columns=["ID","Route_name","Route_link","Bus_name","Bus_type","Departing_time","Duration","Reaching_time","Star_rating","Price","Seat_availability"])
        st.write(df)
    if fare=='1000-2000':
        mydb = mysql.connector.connect(host="localhost",user="root",port="3306",database="redbus",password="181506")
        mycursor = mydb.cursor()
        qurey=f'''select * from redbusdetails
                    where Price Between 1000 and 2000 and Route_name="{As}"
                    order by Price desc'''
        mycursor.execute(qurey)
        out=mycursor.fetchall()
        df=pd.DataFrame(out,columns=["ID","Route_name","Route_link","Bus_name","Bus_type","Departing_time","Duration","Reaching_time","Star_rating","Price","Seat_availability"])
        st.write(df)
    if fare=='2000 and 4000':
        mydb = mysql.connector.connect(host="localhost",user="root",port="3306",database="redbus",password="181506")
        mycursor = mydb.cursor()
        qurey=f'''select * from redbusdetails
                    where Price Between 2000 and 4000 and Route_name="{As}"
                    order by Price desc'''
        mycursor.execute(qurey)
        out=mycursor.fetchall()
        df=pd.DataFrame(out,columns=["ID","Route_name","Route_link","Bus_name","Bus_type","Departing_time","Duration","Reaching_time","Star_rating","Price","Seat_availability"])
        st.write(df)
#Uttar Pradesh
if states=="Uttar Pradesh":
    UP=st.selectbox("List of Routes",up)
    if fare=='50-1000':
        mydb = mysql.connector.connect(host="localhost",user="root",port="3306",database="redbus",password="181506")
        mycursor = mydb.cursor()
        qurey=f'''select * from redbusdetails
                    where Price Between 50 and 1000 and Route_name="{UP}"
                    order by Price desc'''
        mycursor.execute(qurey)
        out=mycursor.fetchall()
        df=pd.DataFrame(out,columns=["ID","Route_name","Route_link","Bus_name","Bus_type","Departing_time","Duration","Reaching_time","Star_rating","Price","Seat_availability"])
        st.write(df)
    if fare=='1000-2000':
        mydb = mysql.connector.connect(host="localhost",user="root",port="3306",database="redbus",password="181506")
        mycursor = mydb.cursor()
        qurey=f'''select * from redbusdetails
                    where Price Between 1000 and 2000 and Route_name="{UP}"
                    order by Price desc'''
        mycursor.execute(qurey)
        out=mycursor.fetchall()
        df=pd.DataFrame(out,columns=["ID","Route_name","Route_link","Bus_name","Bus_type","Departing_time","Duration","Reaching_time","Star_rating","Price","Seat_availability"])
        st.write(df)
    if fare=='2000 and 4000':
        mydb = mysql.connector.connect(host="localhost",user="root",port="3306",database="redbus",password="181506")
        mycursor = mydb.cursor()
        qurey=f'''select * from redbusdetails
                    where Price Between 2000 and 4000 and Route_name="{UP}"
                    order by Price desc'''
        mycursor.execute(qurey)
        out=mycursor.fetchall()
        df=pd.DataFrame(out,columns=["ID","Route_name","Route_link","Bus_name","Bus_type","Departing_time","Duration","Reaching_time","Star_rating","Price","Seat_availability"])
        st.write(df)
#Bihar
if states=="Bihar":
    B=st.selectbox("List of Routes",bihar)
    if fare=='50-1000':
        mydb = mysql.connector.connect(host="localhost",user="root",port="3306",database="redbus",password="181506")
        mycursor = mydb.cursor()
        qurey=f'''select * from redbusdetails
                    where Price Between 50 and 1000 and Route_name="{B}"
                    order by Price desc'''
        mycursor.execute(qurey)
        out=mycursor.fetchall()
        df=pd.DataFrame(out,columns=["ID","Route_name","Route_link","Bus_name","Bus_type","Departing_time","Duration","Reaching_time","Star_rating","Price","Seat_availability"])
        st.write(df)
    if fare=='1000-2000':
        mydb = mysql.connector.connect(host="localhost",user="root",port="3306",database="redbus",password="181506")
        mycursor = mydb.cursor()
        qurey=f'''select * from redbusdetails
                    where Price Between 1000 and 2000 and Route_name="{B}"
                    order by Price desc'''
        mycursor.execute(qurey)
        out=mycursor.fetchall()
        df=pd.DataFrame(out,columns=["ID","Route_name","Route_link","Bus_name","Bus_type","Departing_time","Duration","Reaching_time","Star_rating","Price","Seat_availability"])
        st.write(df)
    if fare=='2000 and 4000':
        mydb = mysql.connector.connect(host="localhost",user="root",port="3306",database="redbus",password="181506")
        mycursor = mydb.cursor()
        qurey=f'''select * from redbusdetails
                    where Price Between 2000 and 4000 and Route_name="{B}"
                    order by Price desc'''
        mycursor.execute(qurey)
        out=mycursor.fetchall()
        df=pd.DataFrame(out,columns=["ID","Route_name","Route_link","Bus_name","Bus_type","Departing_time","Duration","Reaching_time","Star_rating","Price","Seat_availability"])
        st.write(df)




 


















        