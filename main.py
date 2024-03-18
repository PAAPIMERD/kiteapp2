#FINAL PRODUCTION LEVEL TO BE CALLED 

#import all the neccessary librarys
import kiteapp as kt
import datetime
import time


#all the code required to authentication of kotak neo and kite api should be done here

enc = "Oiz8IpBuSFK27ck6NRORetnCKbwmSM7RRdIJNd6RrMFwz0PJrqDL52O95HnO4CfhTZc9z+0DEwny5Jfzgc3/CT6IMZGYBLLhEc/smJdq6WnaOGy/HDATeg==" #login into kite goto ->inspect->networks->full->enctoken
kite = kt.KiteApp("avinash","PQW807",enc)#this block will authenticate the user using enc token in kite(zerodha)

#below you can write code for the authentication of kotakapi (which will be used for order placing purpose)



while True:
  print(kite.ltp("WIPRO"))
