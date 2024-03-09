#GUI----------------------------------------------------------------------------
import tkinter as tk
root=tk.Tk()
root.title("DataBase GUI")

top=[1,2,3,4]
for i in range(4): a=tk.Frame(root); a.pack(side="top"); top[i] = a; 

tk.Label(top[0],text=" USER: ",font=("Times New Roman",30)).pack(side="left")
user_entry=tk.Entry(top[0],font=("Times New Roman",30))
user_entry.pack(side="left")

tk.Label(top[1],text=" PASS: ",font=("Times New Roman",30)).pack(side="left")
pass_entry=tk.Entry(top[1],font=("Times New Roman",30))
pass_entry.pack(side="left")

tk.Label(top[2],text=" MAIL: ",font=("Times New Roman",30)).pack(side="left")
mail_entry=tk.Entry(top[2],font=("Times New Roman",30))
mail_entry.pack(side="left")

tk.Button(top[3],text="Create",font=("Times New Roman",30),border=5,command=lambda:create()).pack(side="left")
tk.Button(top[3],text="Read",font=("Times New Roman",30),border=5,command=lambda:read()).pack(side="left")
tk.Button(top[3],text="Update",font=("Times New Roman",30),border=5,command=lambda:update()).pack(side="left")
tk.Button(top[3],text="Delete",font=("Times New Roman",30),border=5,command=lambda:delete()).pack(side="left")

#Data-Base-------------------------------------------------------------------------

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="myuser",
    password="mypass")
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS loginDB")

mydb = mysql.connector.connect(
    host="localhost",
    user="myuser",
    password="mypass",
    database="loginDB")
mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS AllUser (user VARCHAR(255),pass VARCHAR(255),mail VARCHAR(255))")

def create():
    sql="INSERT INTO AllUser (user,pass,mail) VALUES (%s,%s,%s)"
    val=(user_entry.get(),pass_entry.get(),mail_entry.get())
    mycursor.execute(sql,val)
    mydb.commit()
    print("new user added")

def read():
    mycursor.execute("SELECT * FROM AllUser")
    result=mycursor.fetchall()
    print("(user:, pass:, mail:)")
    for i in result:
        print(i)

def update():
    u=user_entry.get()
    m=mail_entry.get()
    mycursor.execute(f"UPDATE AllUser SET mail = '{m}' WHERE user = '{u}'")
    mydb.commit()
    print(f"user {u} updated")

def delete():
    u=user_entry.get()
    mycursor.execute(f"DELETE FROM Alluser WHERE user = '{u}'")
    mydb.commit()
    print(f"user {u} deleted")
    #mycursor.execute("DROP TABLE AllUser")
    #mycursor.execute("DROP DATABASE loginDB")

root.mainloop()