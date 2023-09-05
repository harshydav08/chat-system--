import requests


def getData(jwt):
  data = []
  d = requests.get(f"https://flask-internship.iamkunal9.repl.co/getdata/{jwt}").json()
  if len(d) > 0:
    for j in data:
      print(f"From: {j['from']}\nMessage: {j['message']}")
  else:
    print("No message found")


def postData(jwt):
  to = input("Enter username whom you want to send message: ")
  message = input("Enter Message: ")
  data = {'from': jwt, 'to': to, 'message': message}
  resp = requests.post("https://flask-internship.iamkunal9.repl.co/postdata",
                       json=data).json()
  if resp['success'] == "ok":
    print("Data sent successfully")
  else:
    print("Error while sending")

def login(username, password):
  resp = requests.post("https://flask-internship.iamkunal9.repl.co/login",json={"username":username,"password":password}).json()
  return resp  
  
jwt = None

while True:
  uname = input("Enter UserName")
  passwd = input("Enter Password") 
  rsp = login(uname,passwd)
  if rsp['success']:
    jwt = rsp['jwt']
    break
while True:
  inpt = input(
    "Enter 1 to fetch new chat\nEnter 2 to send message\Enter 3 to exit\n")
  match inpt:
    case "1":
      getData(jwt)
    case "2":
      postData(jwt)
    case "3":
      exit()
    case default:
      print("Invalid Input")