
import time
from DbInj import *

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
#    Web3Function.sendTnx(addressRecipient=user["address"], amount="0.01")


nonce = None
for n in range(len(users)):
    userss = users[n]
    print(userss['address'])
    nonce = Web3Function.sendTnx(addressRecipient=userss["address"], amount="0.01", Oldnonce=nonce)

    








