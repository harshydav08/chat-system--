
#from flask import Flask,request
from http import HTTPStatus
import requests


users={1:{
    "username":"iamkunal9",
    "password":"whoami",
  },
  2:{
    "username":"harshyadav",
    "password":"kuchbhi",
  },
  3:{
    "username":"muskaann.29",
    "password":"Sotu@123",
  },
  4:{
    "username":"ishajain",
    "password":"isha12",
},
  5:{
    "username":"kalika123",
    "password":"kalika2",
  },
  6:{
    "username":"kritig20",
    "password":"kayy2",
  },  
  7:{
    "username":"RituRAjs12",
    "password":"kyundu",
  },
  8:{'username':'Aditya@2',
     'password':'A2',
    }}

ids=None 
while ids==None:
    uname=input("enter username:") 
    passd=input("enter password:")
    for i in range(1,4):
        if uname == users[i]["username"] and passd == users[i]["password"]:
                ids = i
                break
print(f"hey{users[ids]['username']}") 

def send_message(sender_id, recipient_id, message):

    print(f"Message sent from {users[sender_id]['name']} to {users[recipient_id]['name']}: {message}")

def check_messages(user_id):
    
    print(f"Checking messages for {users[user_id]['name']}:{message}")

while True:
    print("Options:")
    print("1: Send a message")
    print("2: Check messages")
    print("3: Log out or exit")
    
    choice = input("enter your choice: ")
    
    if choice == "1":
        recipient_id = int(input("enter recipient's ID: "))
        message = input("enter your message: ")
        show=requests.post("https://flask-internship.iamkunal9.repl.co/postdata").json()
        print(show.content)
        send_message(ids, recipient_id, message)
        
    elif choice == "2":
        check_messages(ids,message)
        
    elif choice == "3":
        print("log out")
        break
        
    else:
        print("invalid choice. please choose again.")

     
   




