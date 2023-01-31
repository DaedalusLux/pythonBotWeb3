

from DbInj import *
import requests



TOKEN = "" #insert token of your bot
YourId = "" #insert your id
message = "I ran the script, check if everything is ok"

def sendMex():

 url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={YourId}&text={message}"
 print(requests.get(url).json())

# dbUsage.createCsv() # Create the csv
users = []
f = open("data.csv", "r", newline='')
reader = csv.reader(f, delimiter = ",", lineterminator= "\n")
next(reader, None)

for n in reader: 
   user={}
   user["address"] = n[0]
   user["balance"] = n[1]
   users.append(user)



nonce = None
for n in range(len(users)):
    userss = users[n]
    print(userss['address'])
    nonce = Web3Function.sendTnx(addressRecipient=userss["address"], amount="0.01", Oldnonce=nonce)
      
      
sendMex()

    








