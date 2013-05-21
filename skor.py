
import socket
import datetime
import time
import os

import urllib
import urllib2
#import requests



ssil='http://clck.yandex.ru/redir/dtype=stred/pid=2787/cid=1849/path=soft/*https://download.yandex.ru/element/opera/YandexElement.exe'
period=10 #min
filename='C:\test_skorost\test.zip'

numb=1
pr=''
f=open('log.txt','a')

dt = datetime.datetime.now() 
tm=dt.strftime(' %H:%M:%S %d-%m-%Y')
 
#f.write('start at '+tm+'\n')
print ('start')

while 1:
    while (1):
        dt = datetime.datetime.now() 
        tm=dt.strftime('%M')
        if pr!=tm and int(tm)%period==0:
            pr=tm
            break
        time.sleep(60*period/12)

    
    dt = datetime.datetime.now() 
    tm=dt.strftime(' %H:%M:%S %d-%m-%Y')
    f.write('test number; '+str(numb) +';'+tm+':')
   # print ('start test number: ', numb,tm)
    
 #   print ('start test number: ', numb,tm,'')    
  
    nach=time.time()
    try:
        
        urllib.urlretrieve(ssil, "test.zip")
    #download
 #       time.sleep(1)
    except:
        kon=time.time()
        f.write(str(kon-nach)+'error \n')
        print ('end test ', kon-nach,'error','bit/sec')
    else:
        kon=time.time()
    #    print (os.stat("test.zip").st_size)
    #    print(len(open("test.zip").read()))
     #   folder_size=len(open("test.zip").read())
        folder_size=os.stat("test.zip").st_size
        dt = datetime.datetime.now() 
        tm=dt.strftime(' %H:%M:%S %d-%m-%Y')
        f.write(tm+';'+str(8*folder_size/(kon-nach)/1024/1024)+';Mbit/sec\n')
        f.flush()
        print (tm, 8*folder_size/(kon-nach)/1024/1024,'Mbit/sec')
    numb+=1


f.close()
print ('end')


