import csv
import mysql.connector
from web3 import Web3




class dbUsage:
 global data


 def addressQuery():
  db = mysql.connector.connect(
    host = "localhost",                                # insert your host
    user = "root",                                     # insert your user
    password = "",                                     # insert your passwd
    database = "testaddress")                          # choose your DB

  cursor = db.cursor()
  sql = "SELECT addr, balance  FROM ADDRESS"           # Query
  cursor.execute(sql)
  result = cursor.fetchall()
  return result

 
 data = addressQuery()
 def createCsv():
  fields = ['address', 'balance']
  file = open("data.csv", "w")
  with file:   
    write = csv.writer(file, delimiter= ",", lineterminator= "\n")
    write.writerow(fields)
    write.writerows(data)
    file.close()



class Web3Function():
    
 global web3 
 web3 = Web3(Web3.HTTPProvider("https://rinkeby.infura.io/v3/"))

 def sendTnx(addressSend = '' ,
             privateKey = "", 
             addressRecipient = "",
             amount = "0.1",
             Oldnonce = None
             
  ):
#   web3 = Web3(Web3.HTTPProvider("https://rinkeby.infura.io/v3/"))
  check1 = web3.isConnected() # Trigger the function only if the connection is estabilished

  
  account_1 = addressSend     
  private_key1 = privateKey    
  nonce = web3.eth.getTransactionCount(account_1)
  gas = 2000000
  while Oldnonce == nonce:
    nonce = web3.eth.getTransactionCount(account_1)
   

  tx= {
      'nonce': nonce,
      'to': addressRecipient,
      'value': web3.toWei(amount, 'ether'),
       'gas': gas,
       'gasPrice': web3.toWei('50', 'gwei')
  }

  if check1:
         signed_tx = web3.eth.account.sign_transaction(tx, private_key1)
         tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
         print(web3.toHex(tx_hash))
  else:
         print("unable to create the connection to web3")
  return nonce 

     
    










