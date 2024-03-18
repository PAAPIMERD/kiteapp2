#FINAL PRODUCTION LEVEL TO BE CALLED 

#import all the neccessary librarys
import kiteapp as kt
import datetime
import time


#all the code required to authentication of kotak neo and kite api should be done here

enc = "nbGuq+7aqzqph05toD7xvOnsf5xPnHIQpPXegCMV2rJSESis5BmlDy0Y325TRJkn3r+2N3Uro1YTTsTomjUVyvJ3UJytpmJo87wEHY+R293hpeczuGQdUg==" #login into kite goto ->inspect->networks->full->enctoken
kite = kt.KiteApp("avinash","PQW807",enc)#this block will authenticate the user using enc token in kite(zerodha)

#below you can write code for the authentication of kotakapi (which will be used for order placing purpose)



while True:
  print(kite.ltp("WIPRO"))
