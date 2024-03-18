#FINAL PRODUCTION LEVEL TO BE CALLED 

#import all the neccessary librarys
import kiteapp as kt
import datetime
import time


#all the code required to authentication of kotak neo and kite api should be done here

enc = "cDgt17d1ENTb2renX2kE13mtRuALDqqfSB4E9vSQrDgLFVl/HeP5Wjl6syBapi/glnH5lCzjmS0da5/tFGBYm293HGDn9Oy1Dx/WeVnxR5YfA94Te2QuJw==" #login into kite goto ->inspect->networks->full->enctoken
kite = kt.KiteApp("avinash","PQW807",enc)#this block will authenticate the user using enc token in kite(zerodha)

#below you can write code for the authentication of kotakapi (which will be used for order placing purpose)



while True:
  print(kite.ltp("WIPRO"))
