#!/usr/bin/env python
# -*- coding: utf-8 -*-

#include shablon_html.py


#import http.server
#import socketserver
#from http.server import HTTPServer, SimpleHTTPRequestHandler
 
#from http.server import BaseHTTPRequestHandler, HTTPServer, \
 #    SimpleHTTPRequestHandler, CGIHTTPRequestHandler
#from http import server


#import server

import json

import os

from http.server import BaseHTTPRequestHandler, HTTPServer
 
 
from main_ui import Ui_MainWindow

import sys
from PyQt4 import QtGui, QtCore
import random
import math
from PyQt4.QtCore import * 
from PyQt4.QtGui import * 
#from PyQt4.QtOpenGL import *.
from PyQt4.QtCore import Qt
import datetime
import time

import threading
import struct

import socket
import sys
import time

probel='&nbsp;'
WIDTH_ZN=50
OKR=1

file_bd=''



mas_set=[]
p_asu=0
p_arm=0
p_osn=0
vivod=0

shablon_param='''<html>
<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
<head><body><h2>Oreol KONCENTRATOR     </h2><table>
<tr><td>Model name      </td><td>PyQt</td></tr>
<tr><td>Serial Number   </td><td>1             </td></tr>
<tr><td>Firmware version</td><td>0.1           </td></tr>
<tr><td>                </td><td>              </td></tr>
<tr><td>MAC address     </td><td>1.2.3.4.5     </td></tr>
<tr><td>IP address      </td><td>ADDRIP  </td></tr>
<tr><td>Gateway IP addr </td><td>192.168.1.1   </td></tr>
<tr><td>Subnet Mask     </td><td>255.255.255.0 </td></tr>
<tr><td>                </td><td>              </td></tr>
<tr><td>Ситуации    </td><td>SIT</td></tr>
<tr><td>Тех этап    </td><td>ETAP</td></tr>
<tr><td>Тех режим     </td><td>REZIM</td></tr>
<tr><td>                </td><td>              </td></tr>
<tr><td>Вес    </td><td>WES</td></tr>
<tr><td>Нагрузка    </td><td>NAGR</td></tr>
<tr><td>Тальблок    </td><td>TB</td></tr>
<tr><td>Давление    </td><td>DAV</td></tr>
<tr><td>Глубина забоя    </td><td>GL</td></tr>
<tr><td>Длина инструмента    </td><td>DL</td></tr>
</table></body></html>'''  

'''
<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">   <head><body><h2>Oreol KONCENTRATOR     </h2><table>
<tr><td>Model name      </td><td>PyQt</td></tr>
<tr><td>Serial Number   </td><td>1             </td></tr>
<tr><td>Firmware version</td><td>0.1           </td></tr>
<tr><td>                </td><td>              </td></tr>
'''

shablon_zag='''<html><br>
<tr><td>MAC address     </td><td>1.2.3.4.5     </td><td></td><td>  Текущее время : </td><td>TEKVR</td><td> </td><td></td><td>  Загрузка расч. :</td><td>ZAGRAS</td></tr>
<tr><td>IP address      </td><td>IPARRD  </td><td></td><td>  Состояние АРМ : </td><td>SOSTARM&nbsp;&nbsp;</td><td>  Пакетов АРМ : </td><td>PAKARM&nbsp;&nbsp;</td><td>  Загрузка АРМ : </td><td>ZAGARM</td></tr>
<tr><td>Gateway IP addr </td><td>192.168.1.1   </td><td></td><td>  Состояние АСУ : </td><td>SOSTASU&nbsp;&nbsp;</td><td>  Пакетов АСУ : </td><td>PAKASU&nbsp;&nbsp;</td><td>  Загрузка АСУ : </td><td>ZAGASU</td></tr>
<tr><td>Subnet Mask     </td><td>255.255.255.0 </td><td></td><td>  Состояние Сети: </td><td>SOSTSET&nbsp;&nbsp;</td><td>  Пакетов Сети : </td><td>PAKSET&nbsp;&nbsp;</td><td>  Загрузка Сети : </td><td>ZAGSET</td></tr>
</html>'''
 
 
shablon_zag1='''<html><br><TABLE>
<TR><td>MAC address     </td><td>1.2.3.4.5     </td><td></td><td>  Текущее время : </td><td>TEKVR</td><td> </td><td></td><td>  Загрузка расч. :</td><td>ZAGRAS</td></TR>

<TR><td>IP address      </td><td>IPARRD  </td><td></td><td>  Состояние АРМ : </td><td>SOSTARM&nbsp;&nbsp;</td><td>  Пакетов АРМ : </td><td>PAKARM&nbsp;&nbsp;</td><td>  Загрузка АРМ : </td><td>ZAGARM</td></TR>

<TR><td>Gateway IP addr </td><td>192.168.1.1   </td><td></td><td>  Состояние АСУ : </td><td>SOSTASU&nbsp;&nbsp;</td><td>  Пакетов АСУ : </td><td>PAKASU&nbsp;&nbsp;</td><td>  Загрузка АСУ : </td><td>ZAGASU</td></TR>

<TR><td>Subnet Mask     </td><td>255.255.255.0 </td><td></td><td>  Состояние Сети: </td><td>SOSTSET&nbsp;&nbsp;</td><td>  Пакетов Сети : </td><td>PAKSET&nbsp;&nbsp;</td><td>  Загрузка Сети : </td><td>ZAGSET</td></TR>

'''
shablon_ot= '''<tr><td>&nbsp;'''
shablon_ser= '''</td><td>&nbsp;'''
shablon_zak= '''</td></tr>&nbsp;'''

shablon_kon= '''</body></html>''' 



pr_sit=[]
sit=[]

nul=0
spo=1
burenie=2
pzr=3
narawivanie=4
prorabotka=5
promivka=6
pz=7
nadzaboim=8
pustoikruk=9

st_nul=         "не_определено "
st_spo=         "спо           "
st_burenie=     "бурение       "
st_pzr=         "пзр           "
st_narawivanie= "наращивание   "
st_prorabotka=  "проработка    "
st_promivka=    "промывка      "
st_pz=          "пз            "
st_nadzaboim=   "над_забоем    "
st_pustoikruk=  "пустой_крюк   "

	
name="вес двл тб ст_тб об бл_в и_пзр и_бур в_кл н_ин пгр_тб пр_зн нагр гл_заб дл_ин эт реж сит"

'''
param_name=[]
ind_asu_param_in=[]
ind_asu_param_out=[]
ind_arm_param_in=[]
ind_arm_param_out=[]
ind_set_param_in=[]
ind_set_param_out=[]
ind_rasch=[]
f_rasch=[]
'''

param_name=[
"Вес на крюке","Вес колонны","Нагрузка на долото","Давление на входе","Обороты ротора",
"Положение тальблока","Параметр 1","Параметр 1","Параметр 1","Параметр 1",
"кнопки асу","асу 1","асу 2","асу 3","асу 4","асу 5",
"асу 6","асу 7","асу 8","Параметр 1","Параметр 1",
"Положение тальблока","Параметр 1","Параметр 1","Параметр 1","Параметр 1",
"тех этап","тех режим","ситуации","глубина забоя","длина инструмента","вр СПО","вр бурения","вр Цирк","Параметр 1","Параметр 1",
"Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1",
"Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1",
"Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1",
"Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1",
"Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1",
"Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1",
"Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1",
"Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1",
"Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1",
"Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1","Параметр 1",
]

ind_asu_param_in=[10,11,12,13,14,15,16,17,18]
ind_asu_param_out=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49]
ind_arm_param_in=[20,21,22,23,24,25,26,27,28]
ind_arm_param_out=[30,31,32,33,34,35]
'''
ind_set_param_in=[[100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119],[50,51,52,53],[60,61,62,63]]
ind_set_param_out=[[70,71,72,73],[80,81,82,83],[90,91,92,93]]
'''

ind_set_param_in=[[100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119],[50,51,52,53],[60,61,62,63],[60,61,62,63],[60,61,62,63],[60,61,62,63],[60,61,62,63],[60,61,62,63],[60,61,62,63],[60,61,62,63]]
ind_set_param_out=[[70,71,72,73],[80,81,82,83],[90,91,92,93],[90,91,92,93],[90,91,92,93],[90,91,92,93],[90,91,92,93],[90,91,92,93],[90,91,92,93],[90,91,92,93]]

ind_rasch=[85,86,87,88,89]
f_rasch=['param[78]/2','param[79]/2','param[80]/2','param[81]/2','param[82]/2','param[83]/2','param[84]/2','param[85]/2','param[86]/2','param[86]+param[85]']


param=[]

# настройки
'''
asu_host = '10.0.0.219'
asu_port=5000
bait=200

arm_host = 'ya.ru'
arm_port=80
'''

PERIOD=0.10

start_en=0
finish_en=0





# датчики
wk=0	#	вес на крюке
pr=0 	#	давление на входе
dk=0	#	положение тальблока
sp=0	#	обороты ротора

# необходимые для рассчета параметры
bwk=2 	#	блокировочное значение веса на крюке
bpr=2	#	блокировочное значение давления
lp=50	#	интервал пзр
ld=10	#	интервал бурения
wi=20	#	вес инструмента - колонны
ni=10	#	номер инструмента
cp=0	#	погрешность талевого блока
pp=1	#	призабойная зона
st_dk=0
ves_sv=3
dl_sv=28
pr_tb=0
fl_n=0


# рассчетные параметры
teh_etap=nul	#	тех этапы:	0- �� ����������;	1 - ���;	2- �������; 3-���.
teh_rezim=nul	#	тех режим				0- �� ����������;	1 - ���;	2- �������; 3-���; 4- �����������; 5-����������; 6- ��������; 7 - ��.
situacii=0
wd=0	#	нагрузка на долото
cd=100	#	глубина забоя
dd=50 # 	длина инструмента

vr_spo=0
vr_burenie=0
vr_cirk=0





# программные константы и переменные
st_tek_situacii=''
st_tek_teh_rezim=''
st_tek_teh_etap=''
debug=0
d_tb=1

step=0
obw=0
timer=0
nach=0		
step=0
pr_vrem	=0	
pr_vrem1=0
kon=0

error=0
error_str=''



# индексы
ind_wk=1	#	вес на крюке
ind_pr=4 	#	давление на входе
ind_dk=6	#	положение тальблока
ind_sp=5	#	обороты ротора

# необходимые для рассчета параметры

ind_wi=2	#	вес инструмента - колонны

# рассчетные параметры
ind_teh_etap=27	#	тех этапы:	0- ﰰ楥즭1 - ҏλ	2- ⴰ殨廠3-ЇЮ
ind_teh_rezim=28	#	тех режим				0- ﰰ楥즭1 - ҏλ	2- ⴰ殨廠3-Їл 4- Ẩ㡭饻 5-౮𠡮򪠻 6- ౮󘠻 7 - Ї.
ind_situacii=29
ind_wd=3	#	нагрузка на долото
ind_cd=30	#	глубина забоя
ind_dd=31   # 	длина инструмента

ind_vr_spo=32
ind_vr_burenie=33
ind_vr_cirk=34

class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
        
def izm():

    global wk,pr,dk,sp,bwk,lp,ld,wi,ni,cp,pp,wd,cd,dd, teh_etap,teh_rezim,situacii,step,vr_burenie,vr_spo,bpr,vr_cirk,st_dk
        
    global d_tb, ves_sv, dl_sv, timer
        
    st_dk=dk
#   dk+=d_tb
    
        
    if timer==0:
        
        dk=30	

        
    if timer<=28:
        # бурение
        dk-=1
        wk=dd*10
        pr=100
        sp=10	
    #	print timer	, u'бурение'	
        
    if timer>28 and timer<=58:
        # вытаскивают квадрат
        dk+=1
        wk=dd*10
        pr=100
        sp=10	
    #	print timer	, u'вытаскиваем квадрат'	
        
    if timer>58 and timer<=60:
        # операции по смене квадрата на трубу
        dk-=1
        wk=0
        pr=0
        sp=0			
    #	print timer	, u'меняем квадрат на трубу'	

        
    if timer>60 and timer<=63:
        # операции по смене квадрата на трубу
        dk+=1
        wk=0
        pr=0
        sp=0	
    #	print timer	, u'меняем квадрат на трубу'	
        
    if timer>63 and timer<=66:
        # операции по смене квадрата на трубу
        dk-=1
        wk=0
        pr=0
        sp=0
    #	print timer	, u'меняем квадрат на трубу'	

    if timer>66 and timer<=94:
        # опускаем колонну
        dk-=1
        wk=dd*10
        pr=0
        sp=0
    #	print timer	, u'опускаем колону'	
        
    if timer>94 and timer<=124:
        # навинчиваем квадрат
        dk+=1
        wk=0
        pr=0
        sp=0
    #	print timer	, u'навинчиваем квадрат'	


    if timer>124 and timer<=125:
        timer=-1		
        
    timer+=1
    
    param[ind_wk-1]=wk	#	вес на крюке
    param[ind_pr-1]=pr 	#	давление на входе
    param[ind_dk-1]=dk	#	положение тальблока
    param[ind_sp-1]=sp	#	обороты ротора

        # необходимые для рассчета параметры

    param[ind_wi-1]=wi	#	вес инструмента - колонны

        # рассчетные параметры
    param[ind_teh_etap-1]=teh_etap	#	тех этапы:	0- ﰰ楥즭1 - ҏλ	2- ⴰ殨廠3-ЇЮ
    param[ind_teh_rezim-1]	=teh_rezim#	тех режим				0- ﰰ楥즭1 - ҏλ	2- ⴰ殨廠3-Їл 4- Ẩ㡭饻 5-౮𠡮򪠻 6- ౮󘠻 7 - Ї.
    param[ind_situacii-1]=situacii
    param[ind_wd-1]= wd  #	нагрузка на долото
    param[ind_cd-1]=cd	#	глубина забоя
    param[ind_dd-1] =dd  # 	длина инструмента

    param[ind_vr_spo-1]=vr_spo
    param[ind_vr_burenie-1]=vr_burenie
    param[ind_vr_cirk-1]  = vr_cirk
    
    


def raschet():    
        global wk,pr,dk,sp,bwk,lp,ld,wi,ni,cp,pp,wd,cd,dd, teh_etap,teh_rezim,situacii,step,vr_burenie,vr_spo,bpr,vr_cirk,st_tb
        
        global pr_tb, st_dk, fl_n
        
        global ind_wk,ind_pr,ind_dk,ind_sp,ind_wi,ind_teh_etap,ind_teh_rezim,ind_situacii,ind_wd,ind_cd,ind_dd,ind_vr_spo,ind_vr_burenie,ind_vr_cirk
        
  #     начало рассчетные параметры вычисляются
  
    # ind_rasch=[80,81,82,83,84,85,86,87,88,89]
    # f_rasch

        for i in range(len(ind_rasch)):
            param[ind_rasch[i]]=eval(f_rasch[i])
  
  
  #     конец рассчетные параметры вычисляются
                # индексы
                
        wk=param[ind_wk-1]	#	вес на крюке
        pr=param[ind_pr-1] 	#	давление на входе
        dk=param[ind_dk-1]	#	положение тальблока
        sp=param[ind_sp-1]	#	обороты ротора

            # необходимые для рассчета параметры

        wi=param[ind_wi-1]	#	вес инструмента - колонны

            # рассчетные параметры
        teh_etap=param[ind_teh_etap-1]	#	тех этапы:	0- ﰰ楥즭1 - ҏλ	2- ⴰ殨廠3-ЇЮ
        teh_rezim=param[ind_teh_rezim-1]	#	тех режим				0- ﰰ楥즭1 - ҏλ	2- ⴰ殨廠3-Їл 4- Ẩ㡭饻 5-౮𠡮򪠻 6- ౮󘠻 7 - Ї.
        situacii=param[ind_situacii-1]
        wd=param[ind_wd-1]#	нагрузка на долото
        cd=param[ind_cd-1]	#	глубина забоя
        dd=param[ind_dd-1]   # 	длина инструмента

        vr_spo=param[ind_vr_spo-1]
        vr_burenie=param[ind_vr_burenie-1]
        vr_cirk=param[ind_vr_cirk-1]  
    
        if wk>=bwk:		
            situacii=nadzaboim
            
            if dd<lp:
                teh_etap=pzr
                teh_rezim=pzr
            else:
                if dd<cd-ld:
                        teh_etap=spo
                        
                        if pr>bpr:
                            vr_cirk+=step
                            wd=wi-wk
                            if sp>0:
                                teh_rezim=prorabotka
                            else:
                                teh_rezim=promivka
                        
                        else:
                            teh_rezim=spo
                            
                else:
                    teh_etap=burenie
                    
                    if cd-dd<pp:
                        if pr>bpr:
                            vr_cirk+=step
                            wd=wi-wk
                            teh_rezim=burenie
                        else:
                            teh_rezim=narawivanie
                            
                    else:
                        if pr>bpr:
                            vr_cirk+=step
                            wd=wi-wk
                            if sp>0:
                                teh_rezim=prorabotka
                            else:
                                teh_rezim=promivka
                        else:
                            teh_rezim=narawivanie					
                        
                        
                    
            
            
            
        else:		
            situacii=pustoikruk
            if dd>lp:
                if dd<cd-lp:
                    
                    teh_etap=spo
                    teh_rezim=spo
                else:
                    
                    teh_etap=burenie
                    teh_rezim=narawivanie
            else:
                teh_etap=pzr
                teh_rezim=pz
                
   #     print ('dop')        
        wd=0
        if  teh_rezim==burenie:
            vr_burenie+=step
            if fl_n:
                wi=wk
                fl_n=0
            wd=wi-wk
        else:
            fl_n=1
            
            
            

        if  teh_rezim==spo:
            vr_spo+=step	

        if situacii==nadzaboim:
            dd+=pr_tb-dk # 	длина инструмента		

        if 	teh_rezim==burenie:
            if st_dk>dk:
                cd+=st_dk-dk	#	глубина забоя    
    
        pr_tb=dk
        
  #      print (situacii,teh_etap,teh_rezim)
        
          
        param[ind_wk-1]=wk	#	вес на крюке
        param[ind_pr-1]=pr 	#	давление на входе
        param[ind_dk-1]=dk	#	положение тальблока
        param[ind_sp-1]=sp	#	обороты ротора

            # необходимые для рассчета параметры

        param[ind_wi-1]=wi	#	вес инструмента - колонны

            # рассчетные параметры
        param[ind_teh_etap-1]=teh_etap	#	тех этапы:	0- ﰰ楥즭1 - ҏλ	2- ⴰ殨廠3-ЇЮ
        param[ind_teh_rezim-1]	=teh_rezim#	тех режим				0- ﰰ楥즭1 - ҏλ	2- ⴰ殨廠3-Їл 4- Ẩ㡭饻 5-౮𠡮򪠻 6- ౮󘠻 7 - Ї.
        param[ind_situacii-1]=situacii
        param[ind_wd-1]= wd  #	нагрузка на долото
        param[ind_cd-1]=cd	#	глубина забоя
        param[ind_dd-1] =dd  # 	длина инструмента

        param[ind_vr_spo-1]=vr_spo
        param[ind_vr_burenie-1]=vr_burenie
        param[ind_vr_cirk-1]  = vr_cirk
        
    
def vivod():
	global wk,pr,dk,sp,bwk,lp,ld,wi,ni,cp,pp,wd,cd,dd, teh_etap,teh_rezim,situacii,step,vr_burenie,vr_spo,bpr,vr_cirk,st_dk
	
	global pr_sit,sit,name
	
	global uw

	sit=[wk,pr,dk,st_dk,sp,bwk,lp,ld,wi,ni,cp,pp,wd,cd,dd,teh_etap,teh_rezim,situacii]
	
#	print sit
#	print pr_sit

	if pr_sit!=sit:
	
		if situacii==nadzaboim:
			print (st_nadzaboim,)
		elif situacii==pustoikruk:
				print (st_pustoikruk,)	
		else:	
			print (st_nul,)
			


		if	teh_etap==spo:
			print (st_spo,)
		elif	teh_etap==burenie:
			print (st_burenie,)
		elif	teh_etap==pzr:
			print (st_pzr,)
		else:
			print (st_nul,)

		if	teh_rezim==spo:
			print (st_spo)
		elif	teh_rezim==burenie:
			print (st_burenie)
		elif	teh_rezim==pzr:
			print (st_pzr)
		elif	teh_rezim==narawivanie:
			print (st_narawivanie)
		elif	teh_rezim==prorabotka:
			print (st_prorabotka)		
		elif	teh_rezim==promivka:
			print (st_promivka)
		elif	teh_rezim==pz:
			print (st_pz)
		else:
			print (st_nul)	

	#	print step
		'''
		print wd
		print vr_burenie,vr_spo, vr_cirk	
		'''
	#	uw.textBrowser_6.text+='вес нагр тб дав глуб длина_инстр '
	#	uw.textBrowser_6.insertHtml("в\n")
	#	uw.textBrowser_6.insertHtml("<font color=red>red text</font>\n");
		
	#	print name
	#	print sit
		print ("вес нагр тб дав глуб длина_инстр ")
		print (wk, wd, dk, pr, cd, dd)
		print()
		pr_sit=sit


	#	uw.emit(QtCore.SIGNAL("mysignal(QString)"),"html_parameters="+str(situacii)+" "+str(teh_etap)+" "+str(teh_rezim)+" "+str(wk)+" "+str(wd)+" "+str(dk)+" "+str(pr)+" "+str(cd)+" "+str(dd)+" <br>")

   
class asu(QtCore.QThread):    
    st_sost=''
    kol_pak=0
    zag_pot=0
    vr_rab=0
    vr_sleep=0
    host=''
    port=0
    
    def _init_(self,parent=None):
        QtCore.QThread._init_(self,parent)		
    def run(self):
#def asu():
        global start_en, finish_en
        global param,ind_asu_param_in, uw
        global  PERIOD
		
        print ('start asu')
        
        a= time.time()
        b= time.time()
        
        
        # этот код гарантированно не будет прерван каким либо другим потоком
        zapros='''GET http://ya.ru/ HTTP/1.0\r\n\r\n'''

 
        a1=time.time()
        zad=0
        b1=a1
        kol=0
        dl=0
        '''
        buf='00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19'
        zapros='\x01\x03\x00\x00\x00\x05\x85\xC9'

        nul='\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30'
        zapros='\x3A\x33\x34'
        zapros+=nul
        zapros+=nul
        zapros+=nul
        zapros+=nul
        zapros+=nul
        zapros+='\x30\x30\x30\x30\x30\x30\x30\x30'
        zapros+='\x33\x34\x00'
        
        
        otvet=b':4400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000044.'
        '''
        time.sleep(1)
        self.kol_pak=0
        '''
        while 1:
        
            bait=96
            asu_host=socket.gethostbyname(socket.gethostname())
            self.st_sost='starting at '+asu_host+' : '+str(asu_port)
            time.sleep(2)
                    
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((asu_host, asu_port))
            self.st_sost='listen at '+asu_host+' : '+str(asu_port)  
            s.listen(0)
              
            sock, addr = s.accept()                      
            s.close()                
            sock.settimeout(5) 
            print (sock, addr)
            self.st_sost='accept to '+str(addr) 

            while 1:
                self.kol_pak+=1
                data = bytes(otvet)
                
                     
                sock.send(data)            
                time.sleep(0.1)
            sock.close()
            
        '''
            
            
      

        kol=0
        start_en=0
    #    lock = Lock()
        while True:

            error=0
            succ=0
            b= time.time()
 
            try:
                a=time.time()
                time.sleep(1)
                b=time.time()
                
              #  bait=96                
                raz=0
                self.host=socket.gethostbyname(socket.gethostname())
                self.st_sost='starting at '+self.host+' : '+str(self.port)
        
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.bind((self.host, self.port))
                s.listen(0)
                self.st_sost='listen at '+self.host+' : '+str(self.port)                
                sock, addr = s.accept()                      
                s.close()       
                tmo=0.01
                
                sock.settimeout(tmo) 
                self.st_sost='accept to '+str(addr)

          #      self.emit(QtCore.SIGNAL("mysignal(QString)"),"textBrowser= conn est"+"<br>")

                
                error=0
                PERIOD1=self.period
                tm=2*PERIOD1/tmo
            #    print (tmo)
                
                tmr=10
 
                while 1:
                
                    if finish_en==1:
                        sock.close()
                        print ('finish asu')
                        finish_en=0
                        return 
                    
                    
               #     print zad,time.time()-ot
 
                    c=time.time()
                    if (c-a)!=0:
                        self.zag_pot=(c-b)/(c-a)
                    self.vr_rab+=c-b
                    self.vr_sleep+=c-a
                    a=time.time()
                    zad=PERIOD1-(c-b)-0.01
                #    print (zad,PERIOD1,c-b)
                    if zad>0:                    
                        time.sleep(zad)
                        

                    zap=[]
                    raz=0
                    while (len(zap)!=self.bait_in):
                        try:
                            raz+=1
                        #    vr=sock.recv(bait-len(zap))
                        #    print ('++++++++++++++')
                        #    print (type(vr),vr)
                            
                        #    zap+=bytes(vr) 
                        #    print (type(zap),zap)

                        #    zap+=bytes(sock.recv(bait-len(zap))) 
                            zap+=(sock.recv(self.bait_in-len(zap))) 
                       #     print ("LEN "+str(len(zap)))
                            if raz>tm:
                       #         print("BREAK")
                            #    raise
                                break
                                
                        except : #socket.timeout as err:
                            if raz>tm:                                
                       #         print("BREAK")
                                break         
                                
                    b=time.time()
                                     
                    if len(zap)==self.bait_in:
                        error=0
                        self.kol_pak+=1

                       
                     #   self.print (param_in)
                    #    param_out=otvet.split                       
                    #    data = bytes(otvet)
                    #    data = bytes('1234')
                   #     print (type(b'12345'),b'12345')
                    
                    #    print (zap)
                    #    print (ord('3'))
                    #    print (chr(48))
                        
                    #    print ()
                    #    print ('crc calculate')
                    #    print (zap)
                        crc=0x43
                        for i in range(26,92,2):
                       #     print (i,zap[i],hex(zap[i]),hex(zap[i])[2:])
                        #    print (i,end=',')
                        #    print (zap[i],end=',')
                        #    print (chr(zap[i]),end=',')
                           
                            sim=chr(zap[i+1])
                        #    print (sim,end=',')
                        #    print (crc)
                            if sim=='A':
                                crc1=160
                            elif sim=='B':
                                crc1=176
                            elif sim=='C':
                                crc1=192
                            elif sim=='D':
                                crc1=208
                            elif sim=='E':
                                crc1=224
                            elif sim=='F':
                                crc1=240
                            else:
                                crc1=int(sim)*16
 
                            sim=chr(zap[i])
                        #    print (sim,end=',')
                        #    print (crc)
                            if sim=='A':
                                crc1+=10
                            elif sim=='B':
                                crc1+=11
                            elif sim=='C':
                                crc1+=12
                            elif sim=='D':
                                crc1+=13
                            elif sim=='E':
                                crc1+=14
                            elif sim=='F':
                                crc1+=15
                            else:
                                crc1+=int(sim)
                            crc+=crc1
                     #       print (int(chr(zap[i])),crc)
                     #   print (crc, chr(zap[92]), chr(zap[93]),zap[94])
                     
                    #    print (str(hex(crc))[2:],str(chr(zap[92]))+str(chr(zap[93])).lower())
                       
                        if str(hex(crc))[-2:]==str(chr(zap[93]).lower())+str(chr(zap[92])).lower():
                        #    print (zap)
 
                            zap1=[]
                            '''
                            for ii in range(26,92):
                                try:
                                    zap1.append(chr(zap[ii]))
                                except:
                                    zap1.append('-1')
                            '''
                            
                            
                            

                            sim=chr(zap[27])

                            if sim=='A':
                                        crc1=160
                            elif sim=='B':
                                        crc1=176
                            elif sim=='C':
                                        crc1=192
                            elif sim=='D':
                                        crc1=208
                            elif sim=='E':
                                        crc1=224
                            elif sim=='F':
                                        crc1=240
                            else:
                                        crc1=int(sim)*16
         
                            sim=chr(zap[26])

                            if sim=='A':
                                        crc1+=10
                            elif sim=='B':
                                        crc1+=11
                            elif sim=='C':
                                        crc1+=12
                            elif sim=='D':
                                        crc1+=13
                            elif sim=='E':
                                        crc1+=14
                            elif sim=='F':
                                        crc1+=15
                            else:
                                        crc1+=int(sim)

                            st=chr(crc1)
                            s1=struct.unpack('<b',bytes(st, "latin-1"))
                        #    print (st,len(st),s1)
                            param[ind_asu_param_in[0]]=s1[0]
                                
                            for i in range(len(ind_asu_param_in)-1):
                                sd=8*i
 
                                st=''

                                for j in range(0,8,2):
                                    
                                    sim=chr(zap[29+sd+j])

                                    if sim=='A':
                                        crc1=160
                                    elif sim=='B':
                                        crc1=176
                                    elif sim=='C':
                                        crc1=192
                                    elif sim=='D':
                                        crc1=208
                                    elif sim=='E':
                                        crc1=224
                                    elif sim=='F':
                                        crc1=240
                                    else:
                                        crc1=int(sim)*16
         
                                    sim=chr(zap[28+sd+j])

                                    if sim=='A':
                                        crc1+=10
                                    elif sim=='B':
                                        crc1+=11
                                    elif sim=='C':
                                        crc1+=12
                                    elif sim=='D':
                                        crc1+=13
                                    elif sim=='E':
                                        crc1+=14
                                    elif sim=='F':
                                        crc1+=15
                                    else:
                                        crc1+=int(sim)
                                        
                                    c=crc1
                                 #   print (chr(zap[28+sd+j])+chr(zap[29+sd+j]))
                                 #   c=int(chr(zap[28+sd+j])+chr(zap[29+sd+j]))
                                #    print (sd+j,i,j,c,zap[28+sd+j],zap[29+sd+j],chr(zap[28+sd+j]),chr(zap[29+sd+j]))
                                    
                                    
                                    st+=chr(c)

                                s1=struct.unpack('<f',bytes(st, "latin-1"))

                                param[ind_asu_param_in[i+1]]=s1[0]
                                '''
                                v=struct.pack('<f', 6)
                                
                                v1=[]
                                for i in v:
                                    v1.append(i)
                               
                                print (bytes(st[::-1], "latin-1"),st,len(st),s1[0])
                                '''
                      
                            ot=':44'                 
                            crc=0x44                       
                            ot+='00'
                            crc+=0
                            f=1
                            
                            for i in range(50):
                                
                            #    byt = struct.unpack('>4c', struct.pack('>f', f))
                                byt=[]
                           
                            #    f=struct.pack('<f', i)
                            
                                f=struct.pack('<f', param[ind_asu_param_out[i]])
                                '''
                                if i==0:
                                    f=struct.pack('<f',5)
                                '''
                        
                                '''
                                for x in f:
                                    
                                    if i==0:
                                        byt.append(5)
                                    else:
                                        byt.append(x)
                                '''
                              
                           
                                for j in f:

                                    s=str(hex(j))[2:].zfill(2)   
  
                                    sim=s[0].lower()
                    
                                    if sim=='a':
                                        crc1=160
                                    elif sim=='b':
                                        crc1=176
                                    elif sim=='c':
                                        crc1=192
                                    elif sim=='d':
                                        crc1=208
                                    elif sim=='e':
                                        crc1=224
                                    elif sim=='f':
                                        crc1=240
                                    else:
                                        crc1=int(sim)*16
         
                                    sim=s[1].lower()

                                    if sim=='a':
                                        crc1+=10
                                    elif sim=='b':
                                        crc1+=11
                                    elif sim=='c':
                                        crc1+=12
                                    elif sim=='d':
                                        crc1+=13
                                    elif sim=='e':
                                        crc1+=14
                                    elif sim=='f':
                                        crc1+=15
                                    else:
                                        crc1+=int(sim)  

                                    crc+=crc1
                                    
                                    ot+=s[::-1]
                                                                
                        
                            ot+=hex(crc)[-2:].zfill(2)[::-1]+'.'
                      
                            sock.send(ot.encode('latin-1').upper())  
                       
                        else:
                
                            pass
                    else:
                        error+=1 
                        
                        if error>tmr:
                            print("RAISE")
                            raise

                   
                                          
            except:
                
                self.st_sost='..failed at '+self.host+' : '+str(self.port)
             #   sock.close()
  
 
               
class sohran(QtCore.QThread):    
    st_sost=''
    kol_pak=0
    zag_pot=0
    vr_rab=0
    vr_sleep=0

    id=0
    

    
    
    def _init_(self,parent=None):

        QtCore.QThread._init_(self,parent)				

        
    def run(self):	

        global start_en,finish_en
        global  PERIOD, param
        print ('start sohran ') 
        
        ot=time.time()
        a=time.time()
        b=time.time()
        
        dt = datetime.datetime.now() 
    #    print (dt.strftime('%d_%m_%Y'))
        fil=dt.strftime('%d_%m_%Y')+'.log'
    #    m=dt.strftime('%d_%m_%Y_%H_%M')+'.log'
        f=open(fil,'a')
        print ('open file ', fil)
    #    f=open(m,'a')
        
        
        PERIOD1=1
        mas_soh=[]
        kol=1
        start_en=0

        while 1:
                if finish_en==1:
                        f.close()
                        print ('finish sohran')
                        finish_en=0
                        return 
           
                try:    
                    zad=PERIOD1-(time.time()-ot)
          

                    c=time.time()
                    if (c-a)!=0:
                        self.zag_pot=(c-b)/(c-a)
                    self.vr_rab+=c-b
                    self.vr_sleep+=c-a
                    a=time.time()
                
                    if zad>0:
                    
                        time.sleep(zad)
                        
                    b=time.time()

                    ot=time.time()

                    dt = datetime.datetime.now() 
               
                    dt = datetime.datetime.now() 
    
                    fil1=dt.strftime('%d_%m_%Y')+'.log'
                #    m1=dt.strftime('%d_%m_%Y_%H_%M')+'.log'
                    tm=dt.strftime(' %H:%M:%S %d-%m-%Y')
               
                    if fil1!=fil:
                #    if m1!=m:
                        kol=1
                        for i in range(len(mas_soh)):
                    #        print ('write to ', fil)
                            f.write(str(mas_soh[i][0])+';')
                            f.write(mas_soh[i][1]+';')
                            for n in mas_soh[i][2]:
                                f.write(str(n)+';')
                            f.write('\n')
                            
                        f.flush()
                        mas_soh=[]
                        f.close()
                        fil=fil1
                        f=open(fil,'a')
                    #    m=m1
                    #    f=open(m,'a')
               
                    mas_soh.append([str(kol),tm,param])
                    
                    kol+=1
                
                    if kol==60:
                        kol=1
                        for i in range(len(mas_soh)):
                     
                            f.write(str(mas_soh[i][0])+';')
                            f.write(mas_soh[i][1]+';')
                            for n in mas_soh[i][2]:
                                f.write(str(n)+';')
                            f.write('\n')
                            
                        f.flush()
                        mas_soh=[]
                        
                except:
                    print ('error at sohran')
                    
                else:
                    pass
                    
                    
                    
                   
                
class sett(QtCore.QThread):    
    st_sost=''
    kol_pak=0
    zag_pot=0
    vr_rab=0
    vr_sleep=0
    host=''
    port=0
    kol_in_bait=0
    id=0
    PERIOD=0
    
    kod=[]                  #   текущий код ацп 
    mas_per_usr=[]          #  
    mas_sum=[]              #
    mas_t_per=[]            #
    mas=[]                  #   усредненный код ацп
    t_kal=[]                #   таблица калибровки
    
    
    def _init_(self,parent=None):

        QtCore.QThread._init_(self,parent)				

        
    def run(self):	
#def sett():
        global start_en, finish_en
       
        print ('start sett ')
    #    print ('start sett '+self.id)
        
        a=time.time()
        b=time.time()
             
        # этот код гарантированно не будет прерван каким либо другим потоком
        zapros='''GET http://ya.ru/ HTTP/1.0\r\n\r\n'''

        a1=time.time()
        zad=0
        b1=a1
        kol=0
        dl=0
        buf='00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19'
        zapros='\x01\x03\x00\x00\x00\x05\x85\xC9'

        nul='\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30'
        zapros='\x3A\x33\x34'
        zapros+=nul
        zapros+=nul
        zapros+=nul
        zapros+=nul
        zapros+=nul
        zapros+='\x30\x30\x30\x30\x30\x30\x30\x30'
        zapros+='\x33\x34\x00'

        kol=0
        start_en=0
    #    lock = Lock()
        while True:

            error=0
            succ=0
            b= time.time()
 
            try:
                c=time.time()
                self.vr_rab+=c-b
                self.vr_sleep+=c-a
                
                vr_t=0
                obw=0
                vr_pr=0
                vr_t=0
                ozid=0
                kol_p=0
                
                time.sleep(1)
                
                b=time.time()

           #     print (time.time(),' s,',self.id,' try ',self.host, self.port)
                self.st_sost=str(self.id)+' try '+self.host+' : '+str(self.port)
         
                if finish_en==1:
                       
                        s.close()
                        print ('finish set ',self.id)
                        finish_en=0
                        return                

           #     self.emit(QtCore.SIGNAL("mysignal(QString)"),"textBrowser_5= trying connect to "+host+" "+ str(port)+" <br>")
    
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(5000)   
                
                kol_neotv=0

                if finish_en==1:
                       
                        s.close()
                        print ('finish set ',self.id)
                        finish_en=0
                        return 

                    
                s.connect((self.host, self.port))               
                
                print (self.id,'con est')
                self.st_sost='con '+self.host+' : '+str(self.port)
				
            #    self.emit(QtCore.SIGNAL("mysignal(QString)"),"textBrowser_5= conn est"+"<br>")
 
				
                otpr=0
                succ=0
                error=0
              
                tm=0.01
                tmo=1
             
                s.settimeout(tm)
            
                vr_zap=0
                vr_wait=0
                
                ot=0
                otp=0
                prin=0
                
                    #pass
                while 1:
                    if finish_en==1:
                       
                        s.close()
                        print ('finish set ',self.id)
                        finish_en=0
                        return 
                    zad=self.PERIOD-(time.time()-ot)
               #     print zad,time.time()-ot

                    c=time.time()
                    if (c-a)!=0:
                        self.zag_pot=(c-b)/(c-a)
                    self.vr_rab+=c-b
                    self.vr_sleep+=c-a
                    a=time.time()
                    
                    if zad>0:                    
                        time.sleep(zad)
                        
                    b=time.time()

                    ot=time.time()

                    vr_zap-=time.time()
                                        
                    data = bytes('123456789', 'utf-8')
                    vr_ot=time.clock()
         #           if self.id==0:
         #               print ('send',len(data))
                    s.send(data)
                                     
                    otp=time.time()
                 
                    vr_zap+=time.time()
                    vr_wait-=time.time()
                    otpr+=1

                    pr=[]
                    raz=0  
                                                       
                    while (len(pr)!=self.kol_in_bait):
                        try:
                            raz+=1
                            pr+=s.recv(self.kol_in_bait-len(pr))
                            
                            if raz>tmo/tm:
                            #    if self.id!=0:
                                print (time.time(),self.id,'timepout') 
                                kol_neotv+=1
                                s.close()
                                print('close timeout')
                                break

                        except : #socket.timeout as err:
                            
                            if raz>tmo/tm:
                            #    if self.id!=0:
                                print (time.time(),self.id,'except timeout') 
                                s.close()
                                kol_neotv+=1
                                print('close timeout exept')
                                break

                    if kol_neotv>10:
                        kol_neotv+=0
                        s.close()
                        print ('close on kol_neotv')
                 #   if self.id==0:        
                 #       print (len(pr), time.time(),pr)
                    vr_wait+=time.time()
           #         if self.id!=0:
           #                         print (self.id,time.time(),len(pr),pr) 
                    '''
                    if self.id==0:
                        vr_t=time.time()
                        obw+=vr_t-vr_pr
                        vr_pr=vr_t
                        ozid+=time.clock()-vr_ot
                        kol_p+=1
                        if kol_p>1000:
                            print ('time on 1 paket ',obw,'ms, sr ozid ',ozid,' ms')
                            kol_p=0
                            obw=0
                            ozid=0
                    '''
                    if len(pr)==self.kol_in_bait:
                                succ+=1    
                                self.kol_pak+=1
  
#   ind_set_param_in=[[40,41,42,43],[50,51,52,53],[60,61,62,63]]
#   ind_set_param_out=[[70,71,72,73],[80,81,82,83],[90,91,92,93]]
                              

                                for i in range(0,len(ind_set_param_in[self.id])):
                                #    param[ind_set_param_in[self.id][i]]=pr[i*2]*256+pr[i*2+1]
                                
                                    self.kod[i]=pr[i*2]*256+pr[i*2+1]
                                    
                                    if self.mas_t_per[i]<self.mas_per_usr[i]:
                                        self.mas_t_per[i]+=1
                                        
                                        self.mas_sum[i]+=self.kod[i]  
                                        if  self.mas_t_per[i]==0:
                                            self.mas[i] =self.kod[i]
                                        else:                                    
                                            self.mas[i] = self.mas_sum[i]/self.mas_t_per[i]  
                                   #     print (self.mas_per_usr[i],self.mas_t_per[i],self.mas_sum[i],self.mas[i] )
                                    
                                    else:   
                                   #     print (self.id,i,self.mas_per_usr[i],self.mas_t_per[i],self.mas_sum[i],self.mas[i] )
                                     #   self.mas[i] =self.kod[i]
                                    
                                        
                                        self.mas_sum[i]-=self.mas[i]
                                        
                                        self.mas_sum[i]+=self.kod[i]       
                                        if  self.mas_t_per[i]==0:
                                            self.mas[i] =self.kod[i]
                                        else:
                                            self.mas[i] = self.mas_sum[i]/self.mas_t_per[i]                                         
                                           
                                 #   self.t_kal[i] = []
              
                                
                                for i in range(0,len(ind_set_param_in[self.id])):
                                
                                    
                                    if len(self.t_kal[i])==0 or len(self.t_kal[i])%2==1 :
                                        param[ind_set_param_in[self.id][i]]=self.mas[i]
                                    
                                    else:
                                        ind=-1
                                        for ind1 in range(0,len(self.t_kal[i])-1,2):
                                            
                                            if self.mas[i]<self.t_kal[i][ind1]:
                                                ind=ind1
                                                break
                                            
                                          #  pass
                                   #     print (ind,self.t_kal[i],self.mas[i])
                                        
                                        zn_kal=0
                                        
                                        if ind==0 :
                                            param[ind_set_param_in[self.id][i]]=self.t_kal[i][1]
                                        elif ind==-1:
                                            param[ind_set_param_in[self.id][i]]=self.t_kal[i][-1]
                                        elif ind-2<len(self.t_kal[i])-2:
                                        #    print (ind,self.t_kal[i],self.t_kal[i][ind+3]-self.t_kal[i][ind+1],self.mas[i]-self.t_kal[i][ind],self.t_kal[i][ind+2]-self.t_kal[i][ind],self.t_kal[i][ind+1])                 
                                            ind=ind-2                  
                                            zn_kal=(self.t_kal[i][ind+3]-self.t_kal[i][ind+1])*(self.mas[i]-self.t_kal[i][ind])/(self.t_kal[i][ind+2]-self.t_kal[i][ind])+self.t_kal[i][ind+1]
                                        #    print (self.mas[i],zn_kal)
                                            
                                            
                                            param[ind_set_param_in[self.id][i]]=zn_kal
                                            param[ind_set_param_in[self.id][i]]=self.kod[i]
                                        
                                           
                           #     print ('\nreceive: ',self.kol_in_bait, len(pr),pr)

                    else:
                                error+=1   
                                            
                    prin=time.time()
                    
                    

                    '''
                    if a-b>1:
                        print  ('send',otpr,'receive',succ,'errors',error,'temp',otpr//(a-b),'zap',10000.*vr_zap/otpr,'wait',1000.0*vr_wait/otpr)
                        print (len(pr),pr[:5])

                    #    self.emit(QtCore.SIGNAL("mysignal(QString)"),"textBrowser_6= "+str((a-b)*1000)+' мс, '+str(succ)+' запр<br>')
 			                                
                        succ=0
                        vr_zap=0
                        vr_wait=0
                        otpr=0
                        error=0
                        b=time.time()
                    '''
            except:
          #      self.emit(QtCore.SIGNAL("mysignal(QString)"),"textBrowser_5= failed.."+"<br>")
                print ('delete')
                del s
                
                print (self.id,'..failed')

                self.st_sost='nc '+self.host+' : '+str(self.port)
				
  
            else:
                pass        



def crc(st):

 #   print (st)
    crcc=0
    for i in range(2,len(st),2):
    
     #   simb=st[i]+st[i+1]
      #  print (simb)

        sim= st[i]           
        if sim=='A':
            crc1=160
        elif sim=='B':
            crc1=176
        elif sim=='C':
            crc1=192
        elif sim=='D':
            crc1=208
        elif sim=='E':
            crc1=224
        elif sim=='F':
            crc1=240
        else:
            crc1=int(sim)*16
         
        sim= st[i+1] 

        if sim=='A':
            crc1+=10
        elif sim=='B':
            crc1+=11
        elif sim=='C':
            crc1+=12
        elif sim=='D':
            crc1+=13
        elif sim=='E':
            crc1+=14
        elif sim=='F':
            crc1+=15
        else:
            crc1+=int(sim)  

        crcc+=crc1    
 #   print (crcc,str(hex(crcc%256))[2:].zfill(2))
    return str(hex(crcc%256))[2:].zfill(2),crcc



        
class arm(QtCore.QThread):    
    st_sost=''
    kol_pak=0
    zag_pot=0
    vr_rab=0
    vr_sleep=0
    host=0
    port=0
    period=0
    bait_in=0
    bait_out=0
    
    def _init_(self,parent=None):
        QtCore.QThread._init_(self,parent)		

    def run(self):
        
        global start_en, finish_en
        global param, ind_arm_param_in, ind_arm_param_out

        print ('start arm')	
        
        a=time.time()
        b=time.time()

     
        a1=time.time()
        zad=0
        b1=a1
        kol=0
        dl=0
 
        kol=0
        start_en=0
    
        while True:

            error=0
            succ=0
            b= time.time()
 
            try:
            
                a=time.time()
                time.sleep(1)
                b=time.time()
                
                ugol=0
                t_usr=0
                p_usr=100
                usr=0                
                kol_kan=15
                
                raz=0
            #    self.host=socket.gethostbyname(socket.gethostname())
                self.st_sost='starting at '+self.host+' : '+str(self.port)
        
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.bind((self.host, self.port))
                s.listen(0)
                self.st_sost='listen at '+self.host+' : '+str(self.port)                
                sock, addr = s.accept()                      
                s.close()       
                tmo=0.01
                tmo=1
                
                sock.settimeout(tmo) 
                self.st_sost='accept to '+str(addr)

                error=0                
                tm=2*self.period/tmo
                tmr=10
                
                
 
                while 1:          
                    if finish_en==1:
                        sock.close()
                        print ('finish arm')
                        finish_en=0
                        return   
                    c=time.time()
                    if (c-a)!=0:
                        self.zag_pot=(c-b)/(c-a)
                    self.vr_rab+=c-b
                    self.vr_sleep+=c-a
                    a=time.time()
                    zad=self.period-(c-b)-0.01
                    
                    
                
                    if zad>0:                    
                        time.sleep(zad)
                        
                    b=time.time()    
                    
                    
                    '''
                    zap=[]
                    raz=0
                    while (len(zap)!=self.bait_in):
                        try:
                            raz+=1
                     
                            zap+=(sock.recv(self.bait_in-len(zap))) 
                      
                            if raz>tm:
                    
                                break
                                
                        except : #socket.timeout as err:
                            if raz>tm:                                
                       #         print("BREAK")
                                break         
                             
                    b=time.time()     

                #    print ('rec ', len(zap),self.period,time.time())
 
                    if len(zap)==self.bait_in:
                         
                        error=0
                        self.kol_pak+=1 
                        
                    #    print ('dpwlo')
                        
                     #  for i in range(len(zap)/2):
                        
                      #      param[ind_arm_param_in[i]]=zap[i*2]*256+zap[i*2+1]
                            
                        
                        ot=''
                        i=0
                        while (len(ot)<100):
                            ot+=str(i)
                            i+=1
                        sock.send(ot.encode('latin-1').upper()) 
                   #     print (len(ot)) 
                   
                    else:
                        error+=1 
                        
                        if error>tmr:
                            print("RAISE")
                            raise
                    '''

                 #  kol_kan
                    dlin=kol_kan*2+7
                    
                    ot='@%81'
                    ot+=str(hex(dlin%256))[2:].zfill(2).upper()
                    ot+='0200'
                    ot+=str(hex(kol_kan%256))[2:].zfill(2).upper()
                    
                    crc_ot=crc(ot)[1]%256
                   
                 #   for k in range(kol_kan):
                    for k in range(len(ind_set_param_in[0])):
                    #    z=int(math.sin(ugol/100)*1000)+1000
                        
                    #    z=param[k]
                        
                        z=param[ind_set_param_in[0][k]]
                        
                        if k==1:
                            z=kol
                            kol+=1
                    
                        '''
                        if k==0: 
                            
                            if t_usr<p_usr:
                                usr+=z
                                t_usr+=1
                                z=int(usr/t_usr)
                            else:
                                usr-=usr/t_usr
                                usr+=z
                                z=int(usr/t_usr)
                        '''   
                        if z<0:
                            z=0
                            
                        crc_ot+=z//256
                        crc_ot+=z%256
                        ot+=str(hex(int(z)//256))[2:].zfill(2).upper()
                        ot+=str(hex(int(z)%256))[2:].zfill(2).upper()
                        
        
                #    print (crc(ot),crc_ot)
                 #   ot+=crc(ot)[0]+'$'
                    ot+=str(hex(int(crc_ot)//256))[2:].zfill(2).upper()+'$'
                    
               #     print (str(hex(int(crc_ot)%256))[2:].zfill(2).upper(),ot)
                    ugol+=1
                    
                    data = bytes(ot, 'utf-8')
                    sock.send(data)
                    
            #        print ('arm: ',time.time(),data)
                    
                    
            except:
                
                self.st_sost='..failed at '+self.host+' : '+str(self.port)
                                      
          
#def osn():
class osn(QtCore.QThread):    
 #   someSignal = pyqtSignal(str)
    zag_pot=0
    vr_rab=0
    vr_sleep=0
    def _init_(self,parent=None):
        QtCore.QThread._init_(self,parent)  

    def run(self):

        global start_en, finish_en
        global debug, step,obw,nach,timer, pr_vrem,pr_vrem1,kon
        
        global pr_sit, st_tek_situacii, st_tek_teh_rezim ,st_tek_teh_etap, PERIOD
        
        
        print ('start osn')	
        a=time.time()
        b=time.time()
        
        nach=time.time()
        kon=time.time()

        pr_vrem1=time.time()
        pr_vrem=time.time()
        
        pr_time=time.time()


        #while 1:
        #	pass
        tim=time.time()
        start_en=0
        

        while (1):
        
            if finish_en==1:
                        print ('finish osn')
                        finish_en=0
                        return           

            if debug:
                print ()
                
            nach=time.time()		
            step=nach-pr_vrem		
            obw+=step
                       
            c=time.time()
            if (c-a)!=0:
                self.zag_pot=(c-b)/(c-a)
            self.vr_rab+=c-b
            self.vr_sleep+=c-a
            a=time.time()

       #     print ()
       #     print('osn ', time.time()-tim)
            
            if  PERIOD-step>0:
                time.sleep(0.1-step)
                #	print "sleep"
                
       #     tim=time.time()
            
            b=time.time()
            
            if debug:
                print (time.time())
			
            pr_vrem1=pr_vrem
            pr_vrem=time.time()
            
            if debug:
                print (str((pr_vrem-pr_vrem1)*1000).split('.')[0]," мс")

            step=pr_vrem-pr_vrem1
            
            izm()
            raschet()
            
            if time.time()-kon>0.1:
                kon=time.time()
                #	vivod()
                sit=[wk,pr,dk,st_dk,sp,bwk,lp,ld,wi,ni,cp,pp,wd,cd,dd,teh_etap,teh_rezim,situacii]
                
       
                if pr_sit!=sit:
                
                    if situacii==nadzaboim:
                    #    print (st_nadzaboim,)
                        st_tek_situacii=st_nadzaboim
                    elif situacii==pustoikruk:
                    #            print (st_pustoikruk,)	
                                st_tek_situacii=st_pustoikruk
                    else:	
                    #    print (st_nul,)
                        st_tek_situacii=st_nul
                            


                    if	teh_etap==spo:
                    #        print (st_spo,)
                            st_tek_teh_etap=st_spo
                    elif	teh_etap==burenie:
                    #        print (st_burenie,)
                            st_tek_teh_etap=st_burenie
                    elif	teh_etap==pzr:
                    #        print (st_pzr,)
                            st_tek_teh_etap=st_pzr
                    else:
                    #        print (st_nul,)
                            st_tek_teh_etap=st_nul

                    if	teh_rezim==spo:
                    #        print (st_spo)
                            st_tek_teh_rezim=st_spo
                    elif	teh_rezim==burenie:
                     #       print (st_burenie)
                            st_tek_teh_rezim=st_burenie
                    elif	teh_rezim==pzr:
                    #        print (st_pzr)
                            st_tek_teh_rezim=st_pzr
                    elif	teh_rezim==narawivanie:
                    #        print (st_narawivanie)
                            st_tek_teh_rezim=st_narawivanie
                    elif	teh_rezim==prorabotka:
                    #        print (st_prorabotka)	
                            st_tek_teh_rezim=st_prorabotka
                    elif	teh_rezim==promivka:
                    #        print (st_promivka)
                            st_tek_teh_rezim=st_promivka
                    elif	teh_rezim==pz:
                    #        print (st_pz)
                            st_tek_teh_rezim=st_pz
                    else:
                    #        print (st_nul)	
                            st_tek_teh_rezim=st_nul

                #    print ("вес нагр тб дав глуб длина_инстр ")
                #    print (wk, wd, dk, pr, cd, dd)
                #    print()
                    pr_sit=sit
    
    
                    
                    if time.time()-pr_time>=0.1:
                    #    self.emit(QtCore.SIGNAL("mysignal(QString)"),"html_parameters="+str(situacii)+" "+str(teh_etap)+" "+str(teh_rezim)+" "+str(wk)+" "+str(wd)+" "+str(dk)+" "+str(pr)+" "+str(cd)+" "+str(dd)+" <br>")
                        self.emit(QtCore.SIGNAL("mysignal(QString)"),"")
                        pr_time=time.time()
                    
			
            if debug:
                print (obw)

		#	kon=time.time()	

          
class serv(QtCore.QThread):    
 #   someSignal = pyqtSignal(str)
    zag_pot=0
    vr_rab=0
    vr_sleep=0
    def _init_(self,parent=None):
        QtCore.QThread._init_(self,parent)  

    def run(self):

        global p_osn
        global start_en, finish_en
        global debug, step,obw,nach,timer, pr_vrem,pr_vrem1,kon
        
        global pr_sit, st_tek_situacii, st_tek_teh_rezim ,st_tek_teh_etap, PERIOD
        global shablon_zag,shablon_ot,shablon_ser,shablon_zak,shablon_kon,param_name,param,ind_asu_param_in
        
        global st_tek_situacii, st_tek_teh_rezim ,st_tek_teh_etap
        global error_str
   #     global MyError
        '''
        try:
            server.test(HandlerClass=server.SimpleHTTPRequestHandler)
            
        except:
            print('serv failed')
        '''
        while 1:
            try:
                print ('starting server..')
                http_server = HTTPServer( (socket.gethostbyname(socket.gethostname()), 80), NonameHTTPServer)
                start_en=0
            #    raise MyError(2*2)
                print ('start http server at ',socket.gethostbyname(socket.gethostname()), 80)
                http_server.serve_forever()

            except :
                    print (error_str)
  
            #    emit(QtCore.SIGNAL("mysignal(QString)"),"")
                    '''
                    for i in range(5):   
                        print ('try finish ',i)
                        finish_en=1
                        while finish_en:
                            pass
                        time.sleep(0.1)
                    '''  
                    '''
                    p_osn.terminate()
                    p_arm.terminate()
                    p_asu.terminate()
                    for i in range(len(ind_set_param_in)):
                        mas_set[i].terminate()
                    '''
                    

                    '''
                    a=time.time()
                    while p_osn.isRunning() or p_arm.isRunning() or p_asu.isRunning():
                    
                        for i in range(len(ind_set_param_in)):
                            finish_en=1
                            while mas_set[i].isRunning():
                                while finish_en:
                                    time.sleep(0.1)
                        print ()
                        print (p_osn.isRunning() , p_arm.isRunning() , p_asu.isRunning())
                        print ('trying finish..  ', end=' ')
                        finish_en=1
                        while finish_en:
                            time.sleep(0.1)   
                        if time.time()-a>0.1:
                            break
                    '''

                    '''
                    all=[ind_asu_param_in,ind_asu_param_out,ind_arm_param_in,ind_arm_param_out,ind_set_param_in,ind_set_param_out,ind_rasch,f_rasch,p_asu.host,p_asu.port ,p_asu.bait_in ,p_asu.bait_out,p_arm.host,p_arm.port ,p_arm.bait_in ,p_arm.bait_out]
                    
                    for i in range(len(ind_set_param_in)):
                            all+=[mas_set[i].host,mas_set[i].kol_in_bait,mas_set[i].port,mas_set[i].t_kal ]      
                
                    all+=[PERIOD,bwk,bpr,lp, ld,wi,ni,cp,pp,param_name]  
                    
              
                    
                    with open('config.json', mode='w', encoding='utf-8') as f:
                     #   json.dump(param_name, f)  
                     
                        json.dump( all, f) 

                
                    '''
                    print ('server failled..',error_str)
                    http_server.server_close()

 
                    start_en=0
                    if error_str=='restart':
                        error_str=''
                        self.emit(QtCore.SIGNAL("my_event(QString)"),"restart")
                        return 


'''          
class viv(QtCore.QThread):    
 #   someSignal = pyqtSignal(str)
    zag_pot=0
    vr_rab=0
    vr_sleep=0
    def _init_(self,parent=None):
        QtCore.QThread._init_(self,parent)  

    def run(self):

        global debug, step,obw,nach,timer, pr_vrem,pr_vrem1,kon
        
        global pr_sit, st_tek_situacii, st_tek_teh_rezim ,st_tek_teh_etap, PERIOD
        global shablon_zag,shablon_ot,shablon_ser,shablon_zak,shablon_kon,param_name,param,ind_asu_param_in
        global st_tek_situacii, st_tek_teh_rezim ,st_tek_teh_etap
        
        
        global mas_set
    #    self.html_parameters.setHtml("html='<html><head></head><body >aaa</body></html>'")        
    #    print ('s=',s)
    
    
        ot=time.time()
        b=time.time()
        a=time.time()
              
 
        while (1):
                    
                    zad=PERIOD-(time.time()-ot)
             
                    c=time.time()
                    if (c-a)!=0:
                        self.zag_pot=(c-b)/(c-a)
                    
                    self.vr_rab+=c-b
                    self.vr_sleep+=c-a
                    a=time.time()
                    
                    if zad>0:
                    
                        time.sleep(zad)
                    b=time.time()
                    
                    ot=time.time() 
                    

                    st="<html><br><p><font color='red'  size='5'>Из АСУ: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </font><font color='red'  size='5'> В АСУ: </font></p><br><br> <table>"
            
                     
                    if len(ind_asu_param_in)<len(ind_asu_param_out):
                        r=len(ind_asu_param_out)
                    else:
                        r=len(ind_asu_param_in)
                        
                    for i in range(r):
                        if i<len(ind_asu_param_in):
                            st+=shablon_ot+str(i+1)+shablon_ser+param_name[ind_asu_param_in[i]]+shablon_ser+str(param[ind_asu_param_in[i]])+shablon_ser+"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+shablon_ser
                        else:
                            st+=shablon_ot+shablon_ser+shablon_ser+shablon_ser+"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+shablon_ser  
             
                        if i<len(ind_asu_param_out) :
                            st+=str(i+1)+shablon_ser+param_name[ind_asu_param_out[i]]+shablon_ser+str(param[ind_asu_param_out[i]])+shablon_zak
                        else:
                           st+=shablon_ot+shablon_ser+shablon_ser+shablon_ser+"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+shablon_ser  
                        

                    st+="</table></html>"
                    
                    asu_sh=st
                #    self.ui.html_asu.setHtml(st)

                    
                    
                        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                        #  начало вывода страницы с настройками состоянием и параметрами из сети
                        
                    tm='<html><body><br>'
                    tm+='Состояние сети датчиков'
                    tm+='</body><br>'
                        
                    tm+='<table>'
                    
                 #   print (globals())
                    print (mas_set)                     
                    for i in range(len(ind_set_param_in)):
                    #    tm+=shablon_ot+str(i+1)+"&nbsp;&nbsp;"+mas_set[i].host+shablon_ser+"&nbsp;&nbsp;"+str(mas_set[i].port)+shablon_ser+"&nbsp;&nbsp;"+shablon_ser+mas_set[i].st_sost+"&nbsp;&nbsp;Пакетов&nbsp;&nbsp;"+shablon_ser+str(mas_set[i].kol_pak)+shablon_zak+'<br>'
                    #    mas_set[i].kol_pak=0
                        pass
                            
                    
                    tm+='</table>'
                        
             
                        
                        
                    for j in range(len(ind_set_param_in)):
                            
                            tm+='<br><table>'
                            for i in range(len(ind_set_param_in[j])):
                                tm+=shablon_ot+str(i+1)+"&nbsp;&nbsp;"+param_name[ind_set_param_in[j][i]]#+shablon_ser+"&nbsp;&nbsp;"+str(param[ind_set_param_in[j][i]])
                                #+shablon_ser+"&nbsp;&nbsp;"+shablon_ser+self.mas_set[i].st_sost+"&nbsp;&nbsp;Пакетов&nbsp;&nbsp;"+shablon_ser+str(self.mas_set[i].kol_pak)+shablon_zak+'<br>'
                              
                            #    tm+=shablon_ot+str(i+1)+"&nbsp;&nbsp;"+self.mas_set[i].host+shablon_ser+"&nbsp;&nbsp;"+str(self.mas_set[i].port])+shablon_ser
                        
                            tm+='</table>' 
                        
                        
                    tm+='</table></html>'
                        
                #    self.ui.html_set.setHtml(tm)
                    
                    set_sh=tm
                    
                        #  конец вывода страницы с настройками состоянием и параметрами из сети
                        
                        
                    v=st.split(' ')
                        

                    dt = datetime.datetime.now() 
                    
                    tm=shablon_zag.replace('TEKVR',dt.strftime(' %H:%M:%S %d-%m-%Y'))
                    print (socket.gethostbyname(socket.gethostname()))
                    tm=tm.replace('IPARRD',socket.gethostbyname(socket.gethostname()))
                    tm=tm.replace('SOSTASU',asu.st_sost)
                    tm=tm.replace('SOSTARM',arm.st_sost)
                      
                 

                    
                    if  (asu.vr_sleep==0):
                            tm=tm.replace('ZAGASU','')   
                    else:            
                            viv=str(asu.vr_rab/asu.vr_sleep*100)           
                            tm=tm.replace('ZAGASU',viv[:viv.find('.')+2]+' %')            
                    asu.vr_rab=0          
                    asu.vr_sleep=0
                        
                    if arm.vr_sleep==0:
                            tm=tm.replace('ZAGARM','')
                    else:
                            viv=str(arm.vr_rab/arm.vr_sleep*100)
                            tm=tm.replace('ZAGARM',viv[:viv.find('.')+2]+' %')
                    arm.vr_rab=0
                    arm.vr_sleep=0

                    if osn.vr_sleep==0:
                            tm=tm.replace('ZAGRAS','')     
                    else:
                            viv=str(osn.vr_rab/osn.vr_sleep*100)
                            tm=tm.replace('ZAGRAS',viv[:viv.find('.')+2]+' %')            
                    osn.vr_rab=0
                    osn.vr_sleep=0
                        
                        
                        
                    time_kol_pak=time.time()
                    viv=str(asu.kol_pak/(time_kol_pak-pr_time_kol_pak))
                    tm=tm.replace('PAKASU',viv[:viv.find('.')+2])                       
                    asu.kol_pak=0

                    viv=str(arm.kol_pak/(time_kol_pak-pr_time_kol_pak))
                    tm=tm.replace('PAKARM',viv[:viv.find('.')+2])
                    arm.kol_pak=0
                    
 
                    
                    #    self.sett1.kol_pak=0
                        
                    pr_time_kol_pak=time_kol_pak
                       
                        
                    tm+=shablon_ot+shablon_ser+shablon_zak+"</table>"
                        
                    tm+="<table>"+shablon_ot+st_tek_situacii+"<br>"+st_tek_teh_etap+"<br>"+st_tek_teh_rezim+"<br>"+shablon_zak+"</table>"
                    tm1=''
                    #    print (list(range(0,len(param_name)-2,2)))
                    ser=(len(param_name)-2)//2
                        
                    for i in range(ser):
                        #    tm1+=shablon_ot+param_name[i]+shablon_ser+str(param[i])+shablon_zak
                        #    print(i)
                            tm1+=shablon_ot+str(i)+"&nbsp;&nbsp;"+param_name[i]+shablon_ser+str(param[i])+shablon_ser+"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+shablon_ser+str(ser+i)+"&nbsp;&nbsp;"+param_name[ser+i]+shablon_ser+str(param[ser+i])+shablon_zak
                                  
                            
                        #    tm1+=shablon_ot+shablon_ser+shablon_zak
                                
                    tm+=tm1+"</table>"
                  
                    tm+=shablon_kon
                   #     print (tm)
                       

                    
                #    self.ui.html_parameters.setHtml(tm)
                    html_sh=tm
                   
                 
                    
                    emit(QtCore.SIGNAL("mysignal(QString)"),"html_parameters="+str(situacii)+" "+str(teh_etap)+" "+str(teh_rezim)+" "+str(wk)+" "+str(wd)+" "+str(dk)+" "+str(pr)+" "+str(cd)+" "+str(dd)+" <br>")

'''
class NonameHTTPServer(BaseHTTPRequestHandler):

    MEDIA_TYPES = ('ico', 'png', 'gif')

    def do_GET(self):
     #   u"Обработка GET запросов"
        global error_str
        global p_asu
        global MyError
        
        print ()
        print ('Get request accepted', 'User address: %s:%s' % self.client_address)

        # path dispatching        
        '''
        URLS_MAP = {
            '/': self.get_index_page
        }
        print (URLS_MAP)
        print (self.path)
        URLS_MAP.get(self.path, self.get_static_file)()# вызываем обработчик
        
        '''
        
        ext = self.path.split('/')
        print (ext)
     
        if ext[1]=='':
        #    self.get_index_page()
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()  
            self.osn()
        elif ext[1].find('asu.html')!=-1:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()  
            self.asu()
        elif ext[1].find('arm.html')!=-1:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()  
            self.arm()
        elif ext[1].find('set.html')!=-1:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()  
            self.set()
        elif ext[1].find('param.html')!=-1:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()  
            self.param()   
        elif ext[1].find('cgi')!=-1:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers() 
            
            tm='<html>'
            tm+='cgi'

            rez=0
            try:                
                stroka=ext[2].split('&')
                
                print (stroka[0].split('=')[1],stroka[1].split('=')[1])
                numb=int(stroka[0].split('=')[1])
                param_name[numb]=stroka[1].split('=')[1]
 
                for i1 in ind_set_param_in:
                    if numb in i1: 
                        mas_set[i1.index(numb)].t_kal=[]
                 
                for i in range(9):
                    print (i,stroka[4+i].split('=')[1],len(stroka[4+i].split('=')[1]),ind_set_param_in)
               
                #    print (ind_set_param_in[1].index(numb))
                 #   param[ind_set_param_in[self.id][i]]=self.mas[i]
                    
                    if stroka[4+i].split('=')[1]!='' and len(stroka[4+i].split('=')[1])>0:
 
                        for i1 in ind_set_param_in:
                            if numb in i1:
                                mas_set[i1.index(numb)].t_kal.append(int(stroka[4+i].split('=')[1]))
                    
                   
                '''
                if numb in ind_rasch:             
                    f_rasch[ind_rasch.index(numb)]=stroka[24].split('=')[2]
                else:
                    ind_rasch.append(numb)
                    f_rasch.append(stroka[24].split('=')[2])
                             
                all=[ind_asu_param_in,ind_asu_param_out,ind_arm_param_in,ind_arm_param_out,ind_set_param_in,ind_set_param_out,ind_rasch,f_rasch,p_asu.host,p_asu.port ,p_asu.bait_in ,p_asu.bait_out,p_arm.host,p_arm.port ,p_arm.bait_in ,p_arm.bait_out]
                
                for i in range(len(ind_set_param_in)):
                        all+=[mas_set[i].host,mas_set[i].kol_in_bait,mas_set[i].port,mas_set[i].t_kal ]      
            
                all+=[PERIOD,bwk,bpr,lp, ld,wi,ni,cp,pp,param_name]  

                with open('config.json', mode='w', encoding='utf-8') as f:
                    json.dump( all, f) 
        
                error_str='restart'
                '''
                
            except:

                rez=1
               
            if rez==1:   
                tm+='ERROR'            
                tm+='''<br><br><a href="test.html">test</a><br>
                <a href="/">Главная</a><br>
                <a href="/asu.html">АСУ</a><br>
                <a href="/arm.html">АРМ</a><br>
                <a href="/set.html">Сеть</a><br>
                <a href="/param.html">Все параметры</a><br>'''
                tm+='</html>'
                
                self.wfile.write(tm.encode('utf-8')) 
                
             
            else:

                tm+='Successwull, wait...'
                tm+='''<br><br><a href="test.html">test</a><br>
                <a href="/">Главная</a><br>
                <a href="/asu.html">АСУ</a><br>
                <a href="/arm.html">АРМ</a><br>
                <a href="/set.html">Сеть</a><br>
                <a href="/param.html">Все параметры</a><br>'''
                tm+='</html>'
            
                self.wfile.write(tm.encode('utf-8'))    
                print ('done..')
                error_str='restart'
                raise MyError("restart")
                return

            
        elif ext[1]=='favicon.ico':
            '''
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()  
            '''
           
        #    content = open(path, 'r').read()#.decode('utf-8')
            print ('FAVICON')
            self.send_response(200)
            self.send_header('Content-type', 'image')
            self.end_headers()
            content = open('favicon.ico', 'r').read()#.decode('utf-8')
        #    self.write(content)
            self.wfile.write(content.encode('utf-8'))
            

            
        else:
            print (ext)
            if len(ext[1].split('.'))==2:
                try:
                        numb=int(ext[1].split('.')[0])
                        self.send_response(200)
                        self.send_header('Content-type', 'text/html')
                        self.end_headers()  
                        self.param_n(numb)  
                        
                except:
                    self.send_error(403, 'Forbidden')
            else:
                
                self.send_error(403, 'Forbidden')

    def get_static_file(self):
     #   u"Отдача медиа файлов"
        
        
        # Проверяем, что файл имеет расширение из MEDIA_TYPES
        ext = self.path.split('.')[-1]
        
        print (ext,self.MEDIA_TYPES)
        if ext in self.MEDIA_TYPES:
            # вычисляем абсолютный путь к файлу, защищаясь от злоумышленников
            safe_path = os.path.normpath(self.path.replace('../', ''))
            rel_path = safe_path[1:]
            print ('Media file requested: ', rel_path)

            # считываем файл
            try:
                print ('need ico')
            #    content = file(rel_path, 'r').read()
                content='123'

            except IOError:
                # Обрабатываем случай, когда файл не найден
                print ('error')
                self.send_error(404, 'File not found')
                self.exit()

            else:
                # формируем ответ
                print ('respond')
                self.send_response(200)
                self.send_header('Content-type', 'image')
                self.end_headers()
            #    self.wfile.write(content)
        else:
            self.send_error(403, 'Forbidden')
            
        print ('end')
        
    def get_index_page(self):
     #   u"Формируем ответ для главной страницы"

        print ('Index file rendering')
        
        self.send_response(200)
        
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        
        # рендерим шаблон, получаем тело ответа
        now = datetime.datetime.now()        
      
        content = self.render_template('index.html', {'datetime': now.strftime('%d.%m.%Y %M:%H:%S')})
        self.wfile.write(content.encode('utf-8'))
        print ('dowlo 2')

    def render_template(self, path, context = {}):
    #    u"""Простая реализация шаблонизатора, 
    #    используем стандартный механизм форматирования вывода"""
        content = open(path, 'r').read()#.decode('utf-8')
      #  content = file(path).read().decode('utf-8')
        return content % context
    
    def asu(self):
            global shablon_zag1, p_asu,p_arm,p_osn
            print ('zag asu')
            tm='<htm>'
            tm+='asu'
            tm+='''<br><br><a href="test.html">test</a><br>
            <a href="/">Главная</a><br>
            <a href="/asu.html">АСУ</a><br>
            <a href="/arm.html">АРМ</a><br>
            <a href="/set.html">Сеть</a><br>
            <a href="/param.html">Все параметры</a><br>'''
            tm+='</html>'
            
            self.wfile.write(tm.encode('utf-8'))
            
    def arm(self):
            global shablon_zag1, p_asu,p_arm,p_osn

            tm='<htm>'
            tm+='arm'
            tm+='''<br><br><a href="test.html">test</a><br>
            <a href="/">Главная</a><br>
            <a href="/asu.html">АСУ</a><br>
            <a href="/arm.html">АРМ</a><br>
            <a href="/set.html">Сеть</a><br>
            <a href="/param.html">Все параметры</a><br>'''
            tm+='</html>'
            
            self.wfile.write(tm.encode('utf-8'))
 
    def set(self):
            global shablon_zag1, p_asu,p_arm,p_osn

            tm='<htm>'
            tm+='set'
            tm+='''<br><br><a href="test.html">test</a><br>
            <a href="/">Главная</a><br>
            <a href="/asu.html">АСУ</a><br>
            <a href="/arm.html">АРМ</a><br>
            <a href="/set.html">Сеть</a><br>
            <a href="/param.html">Все параметры</a><br>'''
            tm+='</html>'
            
            self.wfile.write(tm.encode('utf-8'))
            
    def param(self):
            global shablon_zag1, p_asu,p_arm,p_osn,param_name,param
            
            global st_tek_situacii,st_tek_teh_etap,st_tek_teh_rezim,OKR

            tm='<META http-equiv="Refresh" content="1; URL=http://10.0.0.219/param.html">'+'<htm>'
           
            tm+='<TABLE>'+'<TD>'+st_tek_situacii+'<TD>'+'<TD>'+st_tek_teh_etap+'</TD>'+'<TD>'+st_tek_teh_rezim+'</TD>'+'</TABLE><br>'
            tm+='<TABLE>'
            
        #    print (tm)
            ser=((len(param_name)-2))//5

                    
            for row in range(0,ser):
                    '''
                    item= QtGui.QStandardItem(str(row))                       
                    self.mod1.setItem(row,0, item) 
  
                    item= QtGui.QStandardItem(param_name[row])                   
                    self.mod1.setItem(row,1, item) 
                    '''

                    tm+='<TR><TD>'+str(row+1)+'.</TD><TD>'+'<a href="'+str(row)+'.html">'+param_name[row] +'</a> '+'</TD><TD>'+str(round(param[row],OKR))+'</TD><TD>'+3*probel+'</TD>'
                       
                    '''
                    item= QtGui.QStandardItem(str(ser+row))                   
                    self.mod1.setItem(row,4, item) 
  
                    item= QtGui.QStandardItem(param_name[ser+row])                   
                    self.mod1.setItem(row,5, item) 
                    '''
               #     item= QtGui.QStandardItem(str(round(param[ser+row],OKR)))                   
              #      self.mod1.setItem(row,6, item) 
                    tm+='<TD>'+str(ser+row+1)+'.</TD><TD>'+'<a href="'+str(ser+row)+'.html">'+param_name[ser+row] +'</a> '+'</TD><TD>'+str(round(param[ser+row],OKR))+'</TD><TD>'+3*probel+'</TD>'             
                    ''' 
                    item= QtGui.QStandardItem(str(ser*2+row))                   
                    self.mod1.setItem(row,8, item) 
  
                    item= QtGui.QStandardItem(param_name[ser*2+row])                   
                    self.mod1.setItem(row,9, item) 
                    '''
               #     item= QtGui.QStandardItem(str(round(param[ser*2+row],OKR)))                   
               #     self.mod1.setItem(row,10, item) 
               
               #     tm+='<TD>'+str(ser*2+row+1)+'.</TD><TD>'+param_name[ser*2+row]+'</TD><TD>'+str(round(param[ser*2+row],OKR))+'</TD><TD>'+3*probel+'</TD>' 

                    tm+='<TD>'+str(ser*2+row+1)+'.</TD><TD>'+'<a href="'+str(ser*2+row)+'.html">'+param_name[ser*2+row] +'</a> '+'</TD><TD>'+str(round(param[ser*2+row],OKR))+'</TD><TD>'+3*probel+'</TD>' 

    
              
                    ''' 
                    item= QtGui.QStandardItem(str(ser*3+row))                   
                    self.mod1.setItem(row,12, item) 
  
                    item= QtGui.QStandardItem(param_name[ser*3+row])                   
                    self.mod1.setItem(row,13, item) 
                    '''
               #     item= QtGui.QStandardItem(str(round(param[ser*3+row],OKR)))                   
               #     self.mod1.setItem(row,14, item)  
                    tm+='<TD>'+str(ser*3+row+1)+'.</TD><TD>'+'<a href="'+str(ser*3+row)+'.html">'+param_name[ser*3+row] +'</a> '+'</TD><TD>'+str(round(param[ser*3+row],OKR))+'</TD><TD>'+3*probel+'</TD>'                 
                    '''
                     
                    item= QtGui.QStandardItem(str(ser*4+row))                   
                    self.mod1.setItem(row,16, item) 
  
                    item= QtGui.QStandardItem(param_name[ser*4+row])                   
                    self.mod1.setItem(row,17, item) 
                    '''
                    tm+='<TD>'+str(ser*4+row+1)+'</TD><TD>'+'<a href="'+str(ser*4+row)+'.html">'+param_name[ser*4+row] +'</a> '+'</TD><TD>'+str(round(param[ser*4+row],OKR))+'</TD><TD>'+3*probel+'</TD></TR>'                      
                #    item= QtGui.QStandardItem(str(round(param[ser*4+row],OKR)))                   
                #    self.mod1.setItem(row,18, item) 
                    
            tm+='</TABLE>'        
            tm+='''<br><br><a href="test.html">test</a><br>
            <a href="/">Главная</a><br>
            <a href="/asu.html">АСУ</a><br>
            <a href="/arm.html">АРМ</a><br>
            <a href="/set.html">Сеть</a><br>
            <a href="/param.html">Все параметры</a><br>'''
            
            tm+='</html>'


            self.wfile.write(tm.encode('utf-8'))
 
 
 
           
    def param_n(self,numb):
            global shablon_zag1, p_asu,p_arm,p_osn,param_name,param, probel,f_rasch,ind_rasch
            
            global st_tek_situacii,st_tek_teh_etap,st_tek_teh_rezim,OKR
            
            
            
            tm='<TABLE>'+'<TD>'+st_tek_situacii+'<TD>'+'<TD>'+st_tek_teh_etap+'</TD>'+'<TD>'+st_tek_teh_rezim+'</TD>'+'</TABLE><br>'
            tm+='<TABLE>'
            
       #     tm+='<TR><TD>'+param_name[numb]+'</TD></TR>'
            
            
            '''
        #    print (tm)
            ser=((len(param_name)-2))//5

                    
            for row in range(0,ser):
                    
                    tm+='<TR><TD>'+str(row+1)+'.</TD><TD>'+param_name[row]+'</TD><TD>'+str(round(param[row],OKR))+'</TD><TD>'+3*probel+'</TD>'
                       
                    tm+='<TD>'+str(ser+row+1)+'.</TD><TD>'+param_name[ser+row]+'</TD><TD>'+str(round(param[ser+row],OKR))+'</TD><TD>'+3*probel+'</TD>'             
                
                    tm+='<TD>'+str(ser*2+row+1)+'.</TD><TD>'+param_name[ser*2+row]+'</TD><TD>'+str(round(param[ser*2+row],OKR))+'</TD><TD>'+3*probel+'</TD>'                
                    
                    tm+='<TD>'+str(ser*3+row+1)+'.</TD><TD>'+param_name[ser*3+row]+'</TD><TD>'+str(round(param[ser*3+row],OKR))+'</TD><TD>'+3*probel+'</TD>'                 
             
                    tm+='<TD>'+str(ser*4+row+1)+'</TD><TD>'+param_name[ser*4+row]+'</TD><TD>'+str(round(param[ser*4+row],OKR))+'</TD><TD>'+3*probel+'</TD></TR>'                      
            '''
            tm+='</TABLE>'  
            '''
                       <form action="/cgi-bin/forms.cgi" METHOD="GET">
  Организация: <input type="Text" size="20" name="org">
  Ваше имя: <input type="Text" size="20" name="name">
  Ваш e-mail: <input type="Text" size="20" name="email">
  Тема: <input type="Text" size="20" name="tema">
  Сообщение: <textarea cols="20" rows="6" name="message"></textarea>
  <input type="reset" value="Очистить">$nbsp; $nbsp; $nbsp; $nbsp;
  <input type="submit" value="Отправить">
</form>
            '''

            tm+='<form action="cgi/cgi" METHOD="GET" ENCTYPE="utf-8 ">'
       #     tm+='<input placeholder="Введите текст">'
       
            tm+='<input type="HIDDEN" name="numb" value="'+str(numb)+'">'
            tm+='<input type="text" name="name" value="'+param_name[numb]+'">'
            
            st=''
            st_kal=''
            if numb in ind_asu_param_in:
                st='входящее асу'
            if numb in ind_arm_param_in:
                st='входящее арм'  
            for kor in range(len(ind_set_param_in)):
                if numb in ind_set_param_in[kor]:
                    kan=ind_set_param_in[kor].index(numb)
                    st='входящее устройство № '+str(kor+1)+' канал № '+str(kan+1) 
                    
                    st_kal='<br>Код АЦП:'+3*probel+'<input name="kod" type="text" value="'+str(mas_set[kor].mas[kan])+'">'+'<br>'
                    
                    
                    
                    st_kal+='<br>Физ. вличина:'+3*probel+'<input type="text" name="fv" value="'+str(round(param[numb],OKR))+'">'+'<br>'
                    
                    
                    
               #     st_kal+='<br>'+str(len(mas_set[kor].t_kal[kan]))+'<br>'
                    
                #    st_kal+='<br>'+str(len(mas_set[kor].t_kal[kan])//2+2)+'<br>'
                    st_kal+='<br>Таблица калибровки:<br><TABLE>'
                    for stroka in range (0,len(mas_set[kor].t_kal[kan]),2):
                        st_kal+='<TR><TD>'+str(stroka//2+1)+'</TD><TD><input name="kod_'+str(stroka+1)+'" type="text" value="'+str(mas_set[kor].t_kal[kan][stroka])+'"></TD><TD><input name="fz_'+str(stroka+1)+'" type="text" value="'+str(mas_set[kor].t_kal[kan][stroka+1])+'"></TD></TR>'
                    
                    for stroka in range (len(mas_set[kor].t_kal[kan]),20,2):
                        st_kal+='<TR><TD>'+str(stroka//2+1)+'</TD><TD><input name="kod_'+str(stroka+1)+'" type="text" value="">'+'</TD><TD>'+'<input name="fz_'+str(stroka+1)+'" type="text" value="">'+'</TD></TR>'                       
                    st_kal+='</TABLE>'
                    
                    st_kal+='<br>Формула:</br>'
                    fmla=''
                    
                    if numb in ind_rasch:
                        fmla=f_rasch[ind_rasch.index(numb)]
                    st_kal+='<input name="formula" type="text" value="'+fmla+'">'
                    
                    
                
            tm+='<br>Входящее:'+3*probel+st+'<br>' 
            tm+=st_kal


            st=''
            if numb in ind_asu_param_out:
                st='исходящее асу'

            if numb in ind_arm_param_out:
                st='исходящее арм'
                
            for kor in range(len(ind_set_param_out)):
                if numb in ind_set_param_out[kor]:
                    st='исходящее устройство № '+str(kor)                 
            '''
            if numb in ind_set_param_in:
                str=''                
            if numb in ind_set_param_out:
                str=''   
            '''
            if numb in ind_rasch:
                st='формула' 
       
            tm+='<br>Исходящее:'+3*probel+st+'<br>'
            
       #     tm+=''' <p style="text-align: center"><button>Сохранить</button>
       #     <button>Отменить</button></p>'''
            
            tm+='<input type="submit" value="Сохранить">'
            '''
            tm+='<button>Отменить1</button>'
            tm+='<input type="button" class="button" value="Отменить2" onclick="location.href="param.html"" />'
            '''
            
            '''                        
            ind_asu_param_in=[10,11,12,13,14,15,16,17,18]
            ind_asu_param_out=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49]
            ind_arm_param_in=[20,21,22,23,24,25,26,27,28]
            ind_arm_param_out=[30,31,32,33,34,35]
            ind_set_param_in=[[40,41,42,43],[50,51,52,53],[60,61,62,63]]
            ind_set_param_out=[[70,71,72,73],[80,81,82,83],[90,91,92,93]]

            ind_rasch=[80,81,82,83,84,85,86,87,88,89]
            f_rasch=['param[78]/2','param[79]/2','param[80]/2','param[81]/2','param[82]/2','param[83]/2','param[84]/2','param[85]/2','param[86]/2','param[86]+param[85]']
            '''

            tm+='</form>'

            tm+='''<FORM ACTION="param.html"> 
            <INPUT TYPE=submit VALUE="Отменить"> 
            </FORM>'''
          #   оnclick="self.location.href="param.html"
            
            tm+='''<br><br><a href="test.html">test</a><br>
            <a href="/">Главная</a><br>
            <a href="/asu.html">АСУ</a><br>
            <a href="/arm.html">АРМ</a><br>
            <a href="/set.html">Сеть</a><br>
            <a href="/param.html">Все параметры</a><br>'''

       #     tm+='<input type="button"  value="Отменить" onclick="location.href="param.html"" />'   
            
            tm+='</html>'

            self.wfile.write(tm.encode('utf-8'))
 
    def osn(self):
    
            global shablon_zag1, p_asu,p_arm,p_osn
    
            dt = datetime.datetime.now() 
            html_sost=shablon_zag1.replace('TEKVR',dt.strftime(' %H:%M:%S %d-%m-%Y'))
            
          #  print (socket.gethostbyname(socket.gethostname()))
            html_sost=html_sost.replace('IPARRD',socket.gethostbyname(socket.gethostname()))            
            html_sost=html_sost.replace('SOSTASU',p_asu.st_sost)
            html_sost=html_sost.replace('SOSTARM',p_arm.st_sost)
            
        #    tm=tm.replace('SOSTSET',self.sett1.st_sost)
 
            if  (p_asu.vr_sleep==0):
                html_sost=html_sost.replace('ZAGASU','')   
            else:            
                viv=str(p_asu.vr_rab/p_asu.vr_sleep*100)           
                html_sost=html_sost.replace('ZAGASU',viv[:viv.find('.')+2]+' %')            
            p_asu.vr_rab=0          
            p_asu.vr_sleep=0

            
            if p_arm.vr_sleep==0:
                html_sost=html_sost.replace('ZAGARM','')
            else:
                viv=str(p_arm.vr_rab/p_arm.vr_sleep*100)
                html_sost=html_sost.replace('ZAGARM',viv[:viv.find('.')+2]+' %')
            p_arm.vr_rab=0
            p_arm.vr_sleep=0
            
            if p_osn.vr_sleep==0:
                html_sost=html_sost.replace('ZAGRAS','')     
            else:
                viv=str(p_osn.vr_rab/p_osn.vr_sleep*100)
                html_sost=html_sost.replace('ZAGRAS',viv[:viv.find('.')+2]+' %')            
            p_osn.vr_rab=0
            p_osn.vr_sleep=0
            
       #     print ('1 osn ')
            '''
            
            self.time_kol_pak=time.time()
            viv=str(p_asu.kol_pak/(self.time_kol_pak-self.pr_time_kol_pak))
            html_sost=html_sost.replace('PAKASU',viv[:viv.find('.')+2])
            
            p_asu.kol_pak=0
            viv=str(p_arm.kol_pak/(self.time_kol_pak-self.pr_time_kol_pak))
            html_sost=html_sost.replace('PAKARM',viv[:viv.find('.')+2])
            p_arm.kol_pak=0
            html_sost=html_sost.replace('PAKSET',viv[:viv.find('.')+2])
            
            '''
            html_sost+="</table>"
            
            html_sost+='''<br><br><a href="/">test</a><br>
            <a href="/">Главная</a><br>
            <a href="/asu.html">АСУ</a><br>
            <a href="/arm.html">АРМ</a><br>
            <a href="/set.html">Сеть</a><br>
            <a href="/param.html">Все параметры</a><br>'''
            html_sost+="</html>"
            
            
            self.wfile.write(html_sost.encode('utf-8'))
            
            print ('kon osn')
        
class MainWindow(QMainWindow):

    pr_time_kol_pak=0
   
    def __init__(self, parent = None):
    
    
        global start_en,error
        global s_host, s_port, param, param_name,ind_asu_param_in,ind_asu_param_out,ind_arm_param_in,ind_arm_param_out,ind_set_param_in,ind_set_param_out,ind_rasch,f_rasch,PERIOD,bwk,bpr,lp, ld,wi,ni,cp,pp,param_name
        
        global mas_set,p_asu, p_arm,p_osn,vivod
        
        print ('start MAIN')
        
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
    #    for i in range(len(param_name)):
    #        param.append(-1)
 
        ''' 
        param_name=[]
        ind_asu_param_in=[]
        ind_asu_param_out=[]
        ind_arm_param_in=[]
        ind_arm_param_out=[]
        ind_set_param_in=[]
        ind_set_param_out=[]
        ind_rasch=[]
        f_rasch=[]
        '''
        
        error=0


        param=[]
        for i in range(200):
            param.append(i)
            
            
      #  старые потоки запускаются
        '''
        self.pr_time_kol_pak=time.time()
        self.arm=arm()
        self.arm.start()		
        self.connect(self.arm,QtCore.SIGNAL("mysignal(QString)"),self.on_change,QtCore.Qt.QueuedConnection)

        self.asu=asu()
        self.asu.start()		
        self.connect(self.asu,QtCore.SIGNAL("mysignal(QString)"),self.on_change,QtCore.Qt.QueuedConnection)

 
        self.osn=osn()
        self.osn.start()		
        self.connect(self.osn,QtCore.SIGNAL("mysignal(QString)"),self.on_change,QtCore.Qt.QueuedConnection)
        
    
        
        self.mas_set=[]
        for i in range(len(ind_set_param_in)):
        
            self.mas_set.append(sett())
         #   self.sett1=sett()
            self.mas_set[i].host='10.0.0.219'
            self.mas_set[i].kol_in_bait=18
            self.mas_set[i].port=7000+i
            self.mas_set[i].id=i
            
            self.mas_set[i].start()		
        #    self.connect(self.mas_set[i],QtCore.SIGNAL("mysignal(QString)"),self.on_change,QtCore.Qt.QueuedConnection)
        
            time.sleep(1)

  
        self.vivod=viv()
    #    self.vivod.start()		
        self.connect(self.vivod,QtCore.SIGNAL("mysignal(QString)"),self.on_change,QtCore.Qt.QueuedConnection)
        
        
      
        
        '''
        
        
        p_arm=arm()
        p_asu=asu()
        mas_set=[]
        

               
             
        try:
            f=open('config1.json',mode='r', encoding='utf-8')

        except:
                print ('no config file')
        else:
        
            try:
                print ('zag config')
                all = json.load(f)

                        
                ind_asu_param_in = all[0]
                ind_asu_param_out = all[1]
                
                ind_arm_param_in = all[2]
                
                ind_arm_param_out = all[3]

                for i in all[4]:
                    ind_set_param_in.append(i)
               
                for i in range(len(ind_set_param_in)):
                    mas_set.append(sett())
               
                ind_set_param_out = all[5]
                
                ind_rasch = all[6]
                f_rasch = all[7]
                p_asu.host  = all[8]
                p_asu.port = all[9]
 
                p_asu.bait_in  = all[10]
                p_asu.bait_out = all[11] 

                p_arm.host = all[12]
                p_arm.port = all[13]
                p_arm.bait_in  = all[14]
                p_arm.bait_out = all[15]
 
                
                a=16
                for i in range(len(ind_set_param_in)):
                    mas_set[i].host = all[a]
                    a+=1
                    mas_set[i].kol_in_bait  = all[a]
                    a+=1
                    mas_set[i].port   = all[a]
                    a+=1
                    mas_set[i].t_kal = all[a]   
                    a+=1                    
                 
                PERIOD = all[a]  
                a+=1
                bwk =all[a]  
                a+=1
                bpr  = all[a]  
                a+=1
                lp = all[a]  
                a+=1
                
                ld = all[a]  
                a+=1
                wi = all[a]  
                a+=1
                ni  = all[a]  
                a+=1
                cp = all[a]  
                a+=1
                pp = all[a]  
                a+=1
                param_name = all[a]  
                a+=1                
                
            except:
              #  f.close()
                print ('failed config file')
         #   else:
         #       f.close()
 
        print ('prod')
        
        '''
        all= [ind_asu_param_in,ind_asu_param_out,ind_arm_param_in,ind_arm_param_out,ind_set_param_in,ind_set_param_out,ind_rasch,f_rasch,p_asu.host,p_asu.port ,p_asu.bait_in ,p_asu.bait_out,p_arm.host,p_arm.port ,p_arm.bait_in ,p_arm.bait_out]
           
        for i in range(len(ind_set_param_in)):
                    all+=[mas_set[i].host,mas_set[i].kol_in_bait,mas_set[i].port,mas_set[i].t_kal ]      
        
        all+=[PERIOD,bwk,bpr,lp, ld,wi,ni,cp,pp,param_name]  
        print   (all) 
        
        '''
        self.pr_time_kol_pak=time.time()
        
        
        p_arm=arm()
        p_arm.port=56000
        p_arm.host='10.0.0.219' #'localhost'
        p_arm.bait_in=10
        p_arm.bait_out=100
        p_arm.period=0.1
        start_en=1
        finish_en=0
        p_arm.start()		
    #    connect(self.arm,QtCore.SIGNAL("mysignal(QString)"),self.on_change,QtCore.Qt.QueuedConnection)
    
        while start_en:
            time.sleep(0.05)
 

        p_asu=asu()
        p_asu.port=5000
        p_asu.host='10.0.0.219'
        p_asu.bait_in=96
        p_asu.bait_out=200
        p_asu.period=0.1
        start_en=1
        p_asu.start()		
    #    connect(self.asu,QtCore.SIGNAL("mysignal(QString)"),self.on_change,QtCore.Qt.QueuedConnection)
        while start_en:
            time.sleep(0.05)
        
   
       
        mas_set=[]
        for i in range(len(ind_set_param_in)):
        
            mas_set.append(sett())
           
            mas_set[i].host='10.0.0.6'            
            mas_set[i].kol_in_bait=18
            mas_set[i].port=7000+i

                
            if i==0:
                mas_set[i].host='10.0.0.57'
                mas_set[i].port=23
                mas_set[i].kol_in_bait=200
                
            mas_set[i].id=i
            mas_set[i].PERIOD=0.009
            
 
            mas_set[i].kod = list(range(len(ind_set_param_in[i])))
            mas_set[i].mas_per_usr = list(range(len(ind_set_param_in[i])))
            mas_set[i].mas_sum = list(range(len(ind_set_param_in[i])))
            mas_set[i].mas_t_per = list(range(len(ind_set_param_in[i])))
            mas_set[i].mas = list(range(len(ind_set_param_in[i])))
            mas_set[i].t_kal = list(range(len(ind_set_param_in[i])))
            
            
            for ii in range(len(ind_set_param_in[i])):
                mas_set[i].kod[ii] = 0            
                mas_set[i].mas_per_usr[ii] = ii*100  
                mas_set[i].mas_sum[ii] = 0  
                mas_set[i].mas_t_per[ii] = 0  
                mas_set[i].mas[ii] = 0  
                mas_set[i].t_kal[ii] = [0,0,65000,65000] 
                if ii==1:
                    mas_set[i].t_kal[ii] = [5,0,5,5,10,10]
            start_en=1                    
            mas_set[i].start()	
            while start_en:
                time.sleep(0.05)            
        #    self.connect(self.mas_set[i],QtCore.SIGNAL("mysignal(QString)"),self.on_change,QtCore.Qt.QueuedConnection)
        
            
            
    

        p_serv=serv()
        p_serv.start()
        while start_en:
            time.sleep(0.05)  
        self.connect(p_serv,QtCore.SIGNAL("my_event(QString)"),self.on_event,QtCore.Qt.QueuedConnection)
     #   self.connect(p_serv,QtCore.SIGNAL("mysignal(QString)"),self.on_change,QtCore.Qt.QueuedConnection)
        
        p_osn=osn()
        start_en=1
        p_osn.start()
        while start_en:
            time.sleep(0.05)		
        self.connect(p_osn,QtCore.SIGNAL("mysignal(QString)"),self.on_change,QtCore.Qt.QueuedConnection)
            
        
        ser=((len(param_name)-2))//5
        self.mod1=QStandardItemModel(ser,19)
        
        for row in range(0,ser):

                    item= QtGui.QStandardItem(str(row+1)+'.')                       
                    
                    self.mod1.setItem(row,0, item) 
  
                    item= QtGui.QStandardItem(param_name[row]) 
                                  
                    self.mod1.setItem(row,1, item) 

                    item= QtGui.QStandardItem(str(param[row]))                   
                    self.mod1.setItem(row,2, item) 

                    item= QtGui.QStandardItem(str(ser+1+row)+'.')                   
                    self.mod1.setItem(row,4, item) 
  
                    item= QtGui.QStandardItem(param_name[ser+row])                   
                    self.mod1.setItem(row,5, item) 

                    item= QtGui.QStandardItem(str(param[ser+row]))                   
                    self.mod1.setItem(row,6, item) 
 
                    item= QtGui.QStandardItem(str(ser*2+1+row)+'.')                   
                    self.mod1.setItem(row,8, item) 
  
                    item= QtGui.QStandardItem(param_name[ser*2+row])                   
                    self.mod1.setItem(row,9, item) 

                    item= QtGui.QStandardItem(str(param[ser*2+row]))                   
                    self.mod1.setItem(row,10, item)  
 
 
                    item= QtGui.QStandardItem(str(ser*3+row+1)+'.')                   
                    self.mod1.setItem(row,12, item) 
  
                    item= QtGui.QStandardItem(param_name[ser*3+row])                   
                    self.mod1.setItem(row,13, item) 

                    item= QtGui.QStandardItem(str(param[ser*3+row]))                   
                    self.mod1.setItem(row,14, item)  

                     
                    item= QtGui.QStandardItem(str(ser*4+row+1)+'.')                   
                    self.mod1.setItem(row,16, item) 
  
                    item= QtGui.QStandardItem(param_name[ser*4+row])                   
                    self.mod1.setItem(row,17, item) 

                    item= QtGui.QStandardItem(str(param[ser*4+row]))                   
                    self.mod1.setItem(row,18, item) 

        self.ui.table_par.setModel(self.mod1)
        
        for row in range(0,ser):
            self.ui.table_par.setColumnWidth(row,WIDTH_ZN) 
            self.ui.table_par.setRowHeight(row,20) 
            

        for row in range(1,19,4): 
            self.ui.table_par.setColumnWidth(row,100)         
        
 

#    таблица  вкладки асу

        ser=max(len(ind_asu_param_in),len(ind_asu_param_out))
        
        self.mod_asu=QStandardItemModel(ser,7)
        
        for row in range(0,ser):
                
                

                    if row<len(ind_asu_param_in)-1:
 
                        item= QtGui.QStandardItem(str(row+1)+'.')                                           
                        self.mod_asu.setItem(row,0, item) 
                                      
                        item= QtGui.QStandardItem(param_name[ind_asu_param_in[row]])                                   
                        self.mod_asu.setItem(row,1, item) 
                        
                        item= QtGui.QStandardItem(str(param[ind_asu_param_in[row]]))                   
                        self.mod_asu.setItem(row,2, item) 
                    
                    if row<len(ind_asu_param_out)-1:                    
                        item= QtGui.QStandardItem(str(row+1)+'.')                   
                        self.mod_asu.setItem(row,4, item) 
      
                        item= QtGui.QStandardItem(param_name[ind_asu_param_out[row]])                   
                        self.mod_asu.setItem(row,5, item) 

                        item= QtGui.QStandardItem(str(param[ind_asu_param_out[row]]))                   
                        self.mod_asu.setItem(row,6, item) 
 
        
        self.ui.table_asu.setModel(self.mod_asu)
        
        for row in range(0,ser):
            self.ui.table_asu.setColumnWidth(row,WIDTH_ZN) 
            self.ui.table_asu.setRowHeight(row,20) 
            

        self.ui.table_asu.setColumnWidth(1,100)         
        self.ui.table_asu.setColumnWidth(5,100)   


 
#    таблица  вкладки сети

        
        m=0
        for i in ind_set_param_in:
            if m<len(ind_set_param_in):
                m=len(ind_set_param_in)
                       
        self.mod_set=QStandardItemModel(m,len(ind_set_param_in)*4)
 
        for i in range(len(ind_set_param_in)):
           
            ser=len(ind_set_param_in[i])
            
            for row in range(1,ser):

                item= QtGui.QStandardItem(str(row)+'.')                                           
                self.mod_set.setItem(row,0+i*4, item) 
                                          
                item= QtGui.QStandardItem(param_name[ind_set_param_in[i][row]])                                   
                self.mod_set.setItem(row,1+i*4, item) 
                            
                item= QtGui.QStandardItem(str(param[ind_set_param_in[i][row]]))                   
                self.mod_set.setItem(row,2+i*4, item) 
               
        self.ui.table_set.setModel(self.mod_set)
            
        for row in range(0,len(ind_set_param_in)*4):
                self.ui.table_set.setColumnWidth(row,WIDTH_ZN) 
                self.ui.table_set.setRowHeight(row,20)                

        for row in range(0,ser):
            self.ui.table_set.setColumnWidth(row*4+1,100)         
               
 #    таблица  вкладки АРМ

        self.mod_arm=QStandardItemModel(len(ind_arm_param_out),3)
          
        for i in range(1,len(ind_arm_param_out)):
           
                item= QtGui.QStandardItem(str(i)+'.')                                           
                self.mod_arm.setItem(i,0, item) 
                                          
                item= QtGui.QStandardItem(param_name[ind_arm_param_out[i-1]])                                   
                self.mod_arm.setItem(i,1, item) 
                            
                item= QtGui.QStandardItem(str(param[ind_arm_param_out[i-1]]))                   
                self.mod_arm.setItem(i,2, item) 
               
        self.ui.table_arm.setModel(self.mod_arm)
            
        for row in range(3):
                self.ui.table_arm.setColumnWidth(row,WIDTH_ZN) 
                self.ui.table_arm.setRowHeight(row,20)                

        self.ui.table_arm.setColumnWidth(1,100)         
               
 
        p_sohran=sohran()
        start_en=1
        p_sohran.start()
        while start_en:
            time.sleep(0.05)
  
    #    server = HTTPServer(("", 8080), MyHandler)
    #    server.serve_forever()
           
                

        '''
        vivod=viv()
        vivod.start()		
        self.connect(vivod,QtCore.SIGNAL("mysignal(QString)"),self.on_change,QtCore.Qt.QueuedConnection)
        '''
        
        '''
        self.sett2=sett()
        self.sett2.host='10.0.0.219'
        self.sett2.kol_in_bait=18
        self.sett2.port=7001      
        self.sett2.start()		
        self.connect(self.sett2,QtCore.SIGNAL("mysignal(QString)"),self.on_change,QtCore.Qt.QueuedConnection)
        
        time.sleep(1)
   

        self.sett3=sett()
        self.sett3.host='10.0.0.219'
        self.sett3.kol_in_bait=18
        self.sett3.port=6000 
        self.sett3.start()		
        self.connect(self.sett3,QtCore.SIGNAL("mysignal(QString)"),self.on_change,QtCore.Qt.QueuedConnection)
        '''
    def on_event(self,s):
    
    
        if s=='restart':
          #  raise Exception('restart')
               # a=5/0
               self.close() 
      #      pass
          #  raise MyError(2*2)

    
    def on_change(self,s):
            global shablon_zag,shablon_ot,shablon_ser,shablon_zak,shablon_kon,param_name,param,ind_asu_param_in
            global st_tek_situacii, st_tek_teh_rezim ,st_tek_teh_etap
            
            global STRANICA

            global mas_set, p_osn, p_arm, p_osn
            
            mas_kol=['0.0','0.0','0.0','0.0']
            
            pr=0
            t=0
            
            tim=time.time()
        
            '''
       
                       
    #    par=self.asu.param_in

        st="<html><br><p><font color='red'  size='5'>Из АСУ: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </font><font color='red'  size='5'> В АСУ: </font></p><br><br> <table>"
    #    for i in range(len(par)):
    #        st+=str(i)+"   "+param_name[ind_asu_param_in[i]]+" "+str(par[i])+' <br>'
         
         
        if len(ind_asu_param_in)<len(ind_asu_param_out):
            r=len(ind_asu_param_out)
        else:
            r=len(ind_asu_param_in)
            
        for i in range(r):
            if i<len(ind_asu_param_in):
                st+=shablon_ot+str(i+1)+shablon_ser+param_name[ind_asu_param_in[i]]+shablon_ser+str(param[ind_asu_param_in[i]])+shablon_ser+"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+shablon_ser
            else:
                st+=shablon_ot+shablon_ser+shablon_ser+shablon_ser+"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+shablon_ser  
 
            if i<len(ind_asu_param_out) :
                st+=str(i+1)+shablon_ser+param_name[ind_asu_param_out[i]]+shablon_ser+str(param[ind_asu_param_out[i]])+shablon_zak
            else:
               st+=shablon_ot+shablon_ser+shablon_ser+shablon_ser+"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+shablon_ser  

        st+="</table></html>"
        ASU_ST=st

        
    
        ob=s.split('=')[0]
        st=s.split('=')[1]
    #    print ('ob=',ob,'vs=',st)
        if ob=='html_parameters':
        
        
            # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            #  начало вывода страницы с настройками состоянием и параметрами из сети
            
            tm='<html><body><br>'
            tm+='Состояние сети датчиков'
            tm+='</body><br>'
            
            tm+='<table>'

            for i in range(len(ind_set_param_in)):
                tm+=shablon_ot+str(i+1)+"&nbsp;&nbsp;"+mas_set[i].host+shablon_ser+"&nbsp;&nbsp;"+str(mas_set[i].port)+shablon_ser+"&nbsp;&nbsp;"+shablon_ser+mas_set[i].st_sost+"&nbsp;&nbsp;Пакетов&nbsp;&nbsp;"+shablon_ser+str(mas_set[i].kol_pak)+shablon_zak+'<br>'
                mas_set[i].kol_pak=0
            #    tm+=shablon_ot+str(i+1)+"&nbsp;&nbsp;"+self.mas_set[i].host+shablon_ser+"&nbsp;&nbsp;"+str(self.mas_set[i].port])+shablon_ser
        
        
            tm+='</table>'
            
 
            
            
            for j in range(len(ind_set_param_in)):
                
                tm+='<br><table>'
                for i in range(len(ind_set_param_in[j])):
                    tm+=shablon_ot+str(i+1)+"&nbsp;&nbsp;"+param_name[ind_set_param_in[j][i]]#+shablon_ser+"&nbsp;&nbsp;"+str(param[ind_set_param_in[j][i]])
                    #+shablon_ser+"&nbsp;&nbsp;"+shablon_ser+self.mas_set[i].st_sost+"&nbsp;&nbsp;Пакетов&nbsp;&nbsp;"+shablon_ser+str(self.mas_set[i].kol_pak)+shablon_zak+'<br>'
                  
                #    tm+=shablon_ot+str(i+1)+"&nbsp;&nbsp;"+self.mas_set[i].host+shablon_ser+"&nbsp;&nbsp;"+str(self.mas_set[i].port])+shablon_ser
            
                tm+='</table>' 
            
            
            tm+='</table></html>'
            
            html_tm=tm
 #           self.ui.html_set.setHtml(tm)
            #  конец вывода страницы с настройками состоянием и параметрами из сети
            
            
            v=st.split(' ')
            

            dt = datetime.datetime.now() 
            html_sost=shablon_zag.replace('TEKVR',dt.strftime(' %H:%M:%S %d-%m-%Y'))
            
            
            html_sost=html_sost.replace('SOSTASU',p_asu.st_sost)
            html_sost=html_sost.replace('SOSTARM',p_arm.st_sost)
           
        #    tm=tm.replace('SOSTSET',self.sett1.st_sost)
 
            if  (p_asu.vr_sleep==0):
                html_sost=html_sost.replace('ZAGASU','')   
            else:            
                viv=str(p_asu.vr_rab/p_asu.vr_sleep*100)           
                html_sost=html_sost.replace('ZAGASU',viv[:viv.find('.')+2]+' %')            
            p_asu.vr_rab=0          
            p_asu.vr_sleep=0
            
            if p_arm.vr_sleep==0:
                html_sost=html_sost.replace('ZAGARM','')
            else:
                viv=str(p_arm.vr_rab/p_arm.vr_sleep*100)
                html_sost=html_sost.replace('ZAGARM',viv[:viv.find('.')+2]+' %')
            p_arm.vr_rab=0
            p_arm.vr_sleep=0

            if p_osn.vr_sleep==0:
                html_sost=html_sost.replace('ZAGRAS','')     
            else:
                viv=str(p_osn.vr_rab/p_osn.vr_sleep*100)
                html_sost=html_sost.replace('ZAGRAS',viv[:viv.find('.')+2]+' %')            
            p_osn.vr_rab=0
            p_osn.vr_sleep=0
            
            
            
            self.time_kol_pak=time.time()
            viv=str(p_asu.kol_pak/(self.time_kol_pak-self.pr_time_kol_pak))
            html_sost=html_sost.replace('PAKASU',viv[:viv.find('.')+2])
            
            p_asu.kol_pak=0
            viv=str(p_arm.kol_pak/(self.time_kol_pak-self.pr_time_kol_pak))
            html_sost=html_sost.replace('PAKARM',viv[:viv.find('.')+2])
            p_arm.kol_pak=0
         #   viv=str(self.sett1.kol_pak/(time_kol_pak-self.pr_time_kol_pak))
            html_sost=html_sost.replace('PAKSET',viv[:viv.find('.')+2])
            
        #    self.sett1.kol_pak=0
            
            self.pr_time_kol_pak=self.time_kol_pak
           
            html_sost+="</table>"
        #    html_sost+=shablon_ot+shablon_ser+shablon_zak+"</table>"
            
            
            
            tm='<html>'
            
            tm+="<table>"+shablon_ot+st_tek_situacii+"<br>"+st_tek_teh_etap+"<br>"+st_tek_teh_rezim+"<br>"+shablon_zak+"</table>"
            
       
            
           
            
           
            tm1='<table>'
        #    print (list(range(0,len(param_name)-2,2)))
            ser=((len(param_name)-2))//5

            
      #      for i in range(ser):
       #         tm1+= "&nbsp;&nbsp;"+str(i)+ "&nbsp;&nbsp;"+param_name[i][:15]+ "&nbsp;&nbsp;"+str(param[i])+ "&nbsp;&nbsp;"+str(ser+i)+ "&nbsp;&nbsp;"+param_name[ser+i][:15]+ "&nbsp;&nbsp;"+str(param[ser+i])+ "&nbsp;&nbsp;"+str(i+ser*2)+ "&nbsp;&nbsp;"+param_name[ser*2+i][:15]+ "&nbsp;&nbsp;"+str(param[ser*2+i])+ "&nbsp;&nbsp;"+str(i+ser*3)+ "&nbsp;&nbsp;"+param_name[ser*3+i][:15]+ "&nbsp;&nbsp;"+str(param[ser*3+i])+"&nbsp;&nbsp;<br>"
            
        #    for i in range(ser):
        #        tm1+= str(i)+param_name[i][:15]+str(param[i])+str(ser+i)+param_name[ser+i][:15]+str(param[ser+i])+"<br>"

            
            for i in range(ser):
                tm1+=shablon_ot+str(i)+"  "+param_name[i][:15]+shablon_ser+str(param[i])+shablon_ser+"   "+shablon_ser+str(ser+i)+"  "+param_name[ser+i][:15]+shablon_ser+str(param[ser+i])+shablon_ser+"   "+shablon_ser+str(i+2*ser)+"  "+param_name[i+2*ser][:15]+shablon_ser+str(param[i+2*ser])+shablon_ser+"   "+shablon_ser+str(i+3*ser)+"  "+param_name[i+3*ser][:15]+shablon_ser+str(param[i+3*ser])+shablon_ser+"   "+shablon_ser+str(i+4*ser)+"  "+param_name[i+4*ser][:15]+shablon_ser+str(param[i+4*ser])+shablon_zak

                
            tm+=tm1+"</table>"
            
            
      
            tm+=shablon_kon
            
            
           
            print (1,time.time()-tim)
              
            self.ui.html_sost.setHtml(html_sost)
            self.ui.html_asu.setHtml(ASU_ST)
            self.ui.html_set.setHtml(html_tm)
            
            print (2,time.time()-tim)

            ser=((len(param_name)-2))//5
            for row in range(0,ser):

                    item= QtGui.QStandardItem(str(param[row]))                   
                    self.mod1.setItem(row,2, item) 

                    item= QtGui.QStandardItem(str(param[ser+row]))                   
                    self.mod1.setItem(row,6, item) 
 
                    item= QtGui.QStandardItem(str(param[ser*2+row]))                   
                    self.mod1.setItem(row,10, item)  

                    item= QtGui.QStandardItem(str(param[ser*3+row]))                   
                    self.mod1.setItem(row,14, item)  

                    item= QtGui.QStandardItem(str(param[ser*4+row]))                   
                    self.mod1.setItem(row,18, item) 
                    
                    
            self.ui.label_4.setText(st_tek_situacii+'   '+st_tek_teh_rezim+'   '+st_tek_teh_etap)

            print (3,time.time()-tim)
            
            '''

 

            dt = datetime.datetime.now() 
            html_sost=shablon_zag.replace('TEKVR',dt.strftime(' %H:%M:%S %d-%m-%Y'))
            
          #  print (socket.gethostbyname(socket.gethostname()))
            html_sost=html_sost.replace('IPARRD',socket.gethostbyname(socket.gethostname()))            
            html_sost=html_sost.replace('SOSTASU',p_asu.st_sost)
            html_sost=html_sost.replace('SOSTARM',p_arm.st_sost)
           
        #    tm=tm.replace('SOSTSET',self.sett1.st_sost)
 
            if  (p_asu.vr_sleep==0):
                html_sost=html_sost.replace('ZAGASU','')   
            else:            
                viv=str(p_asu.vr_rab/p_asu.vr_sleep*100)           
                html_sost=html_sost.replace('ZAGASU',viv[:viv.find('.')+2]+' %')            
            p_asu.vr_rab=0          
            p_asu.vr_sleep=0
            
            if p_arm.vr_sleep==0:
                html_sost=html_sost.replace('ZAGARM','')
            else:
                viv=str(p_arm.vr_rab/p_arm.vr_sleep*100)
                html_sost=html_sost.replace('ZAGARM',viv[:viv.find('.')+2]+' %')
            p_arm.vr_rab=0
            p_arm.vr_sleep=0

            if p_osn.vr_sleep==0:
                html_sost=html_sost.replace('ZAGRAS','')     
            else:
                viv=str(p_osn.vr_rab/p_osn.vr_sleep*100)
                html_sost=html_sost.replace('ZAGRAS',viv[:viv.find('.')+2]+' %')            
            p_osn.vr_rab=0
            p_osn.vr_sleep=0
            
            
            
            self.time_kol_pak=time.time()
            razn=0
            if  self.time_kol_pak-self.pr_time_kol_pak>1:
                razn=self.time_kol_pak-self.pr_time_kol_pak
                self.pr_time_kol_pak=self.time_kol_pak
                
            if razn!=0:    
                viv=str(p_asu.kol_pak/razn)
                html_sost=html_sost.replace('PAKASU',viv[:viv.find('.')+2])
                mas_kol[0]=viv[:viv.find('.')+2]
            else:
                html_sost=html_sost.replace('PAKASU', mas_kol[0])
                
            p_asu.kol_pak=0
            
            if razn!=0: 
                viv=str(p_arm.kol_pak/razn)
                html_sost=html_sost.replace('PAKARM',viv[:viv.find('.')+2])
                mas_kol[1]=viv[:viv.find('.')+2]
            else:
                html_sost=html_sost.replace('PAKARM', mas_kol[1])
            p_arm.kol_pak=0
   
      
            kol_pak=0  
        
            v_rab=0
            v_sl=0
            for ii in range(len(ind_set_param_in)): 
                
                if self.mod_set.item(0,ii*4+2)!=None:
                  #  print ()
                 #   kol_pak+=int(self.mod_set.item(0,ii*4+2).text().split('.')[0])
                    kol_pak+=float(self.mod_set.item(0,ii*4+2).text())
                    
                v_rab+=mas_set[ii].vr_rab
                v_sl+=mas_set[ii].vr_sleep
            '''    
            if razn!=0:        
                viv=str(kol_pak/len(ind_set_param_in)/razn)	
                html_sost=html_sost.replace('PAKSET',viv[:viv.find('.')+2])
                mas_kol[2]=viv[:viv.find('.')+2]
            else:
                html_sost=html_sost.replace('PAKSET',mas_kol[2])
            '''
            viv=str(kol_pak/len(ind_set_param_in))	
            html_sost=html_sost.replace('PAKSET',viv[:viv.find('.')+2])
                
            if v_sl==0:
                html_sost=html_sost.replace('ZAGSET','0 %')
            else:
                viv=str(v_rab/v_sl*100)           
                html_sost=html_sost.replace('ZAGSET',viv[:viv.find('.')+2]+' %')           

            sost=1
            for ii in range(len(ind_set_param_in)): 
                if mas_set[ii].st_sost.find('con')==-1:   
                    sost=0
                    break
                   
            if sost==1:		
                html_sost=html_sost.replace('SOSTSET','all conn')
            else:
                html_sost=html_sost.replace('SOSTSET','no conn')
                        
            html_sost+="</table></html>"
        #    html_sost+=shablon_ot+shablon_ser+shablon_zak+"</table>"  

            self.ui.html_sost.setHtml(html_sost)        

 #           print (1,time.time()-tim)

#    таблица  вкладки асу

            ser=max(len(ind_asu_param_in),len(ind_asu_param_out))
            
       #     self.mod_asu=QStandardItemModel(ser,7)
            
            for row in range(0,ser):

                if row<len(ind_asu_param_in)-1:
     
                     #       item= QtGui.QStandardItem(str(row+1)+'.')                                           
                     #       self.mod_asu.setItem(row,0, item) 
                                          
                     #       item= QtGui.QStandardItem(param_name[ind_asu_param_in[row]])                                   
                     #       self.mod_asu.setItem(row,1, item) 
                            
                            item= QtGui.QStandardItem(str(param[ind_asu_param_in[row]]))                   
                            self.mod_asu.setItem(row,2, item) 
                        
                if row<len(ind_asu_param_out)-1:                    
                     #       item= QtGui.QStandardItem(str(row+1)+'.')                   
                     #       self.mod_asu.setItem(row,4, item) 
          
                     #       item= QtGui.QStandardItem(param_name[ind_asu_param_out[row]])                   
                     #       self.mod_asu.setItem(row,5, item) 

                            item= QtGui.QStandardItem(str(param[ind_asu_param_out[row]]))                   
                            self.mod_asu.setItem(row,6, item) 
 

            '''
           self.ui.table_arm.setModel(self.mod_arm)
                
            for row in range(3):
                    self.ui.table_arm.setColumnWidth(row,30) 
                    self.ui.table_arm.setRowHeight(row,20)                

            self.ui.table_arm.setColumnWidth(1,100)         
            '''
        
            '''
            self.ui.table_asu.setModel(self.mod_asu)
            
            for row in range(0,ser):
                self.ui.table_asu.setColumnWidth(row,30) 
                self.ui.table_asu.setRowHeight(row,20) 
                

            self.ui.table_asu.setColumnWidth(1,100)         
            self.ui.table_asu.setColumnWidth(5,100)      
            '''
           
        
        
              
       #     self.ui.html_sost.setHtml(html_sost)
        #    self.ui.html_asu.setHtml(ASU_ST)
       #     self.ui.html_set.setHtml(html_tm)
            
 #           print (2,time.time()-tim)

 
 #   обновление таблицы вкладки ПАРАМЕТРЫ
            ser=((len(param_name)-2))//5
            for row in range(0,ser):
                    '''
                    item= QtGui.QStandardItem(str(row))                       
                    self.mod1.setItem(row,0, item) 
  
                    item= QtGui.QStandardItem(param_name[row])                   
                    self.mod1.setItem(row,1, item) 
                    '''
                    item= QtGui.QStandardItem(str(round(param[row],OKR)))                   
                    self.mod1.setItem(row,2, item) 
                    '''
                    item= QtGui.QStandardItem(str(ser+row))                   
                    self.mod1.setItem(row,4, item) 
  
                    item= QtGui.QStandardItem(param_name[ser+row])                   
                    self.mod1.setItem(row,5, item) 
                    '''
                    item= QtGui.QStandardItem(str(round(param[ser+row],OKR)))                   
                    self.mod1.setItem(row,6, item) 
                    ''' 
                    item= QtGui.QStandardItem(str(ser*2+row))                   
                    self.mod1.setItem(row,8, item) 
  
                    item= QtGui.QStandardItem(param_name[ser*2+row])                   
                    self.mod1.setItem(row,9, item) 
                    '''
                    item= QtGui.QStandardItem(str(round(param[ser*2+row],OKR)))                   
                    self.mod1.setItem(row,10, item)  
                    ''' 
                    item= QtGui.QStandardItem(str(ser*3+row))                   
                    self.mod1.setItem(row,12, item) 
  
                    item= QtGui.QStandardItem(param_name[ser*3+row])                   
                    self.mod1.setItem(row,13, item) 
                    '''
                    item= QtGui.QStandardItem(str(round(param[ser*3+row],OKR)))                   
                    self.mod1.setItem(row,14, item)  
                    '''
                     
                    item= QtGui.QStandardItem(str(ser*4+row))                   
                    self.mod1.setItem(row,16, item) 
  
                    item= QtGui.QStandardItem(param_name[ser*4+row])                   
                    self.mod1.setItem(row,17, item) 
                    '''
                    item= QtGui.QStandardItem(str(round(param[ser*4+row],OKR)))                   
                    self.mod1.setItem(row,18, item) 
                    
                    
   # обновлене таблицы  значений параметров из сети

  
            for i in range(len(ind_set_param_in)):
                
                ser=len(ind_set_param_in[i])
                
                item= QtGui.QStandardItem(mas_set[i].st_sost)                   
                self.mod_set.setItem(0,i*4+1, item)                 

                if razn!=0:
                    viv=str(mas_set[i].kol_pak/(razn))      
                    mas_set[i].kol_pak=0                    
                    item= QtGui.QStandardItem(viv[:viv.find('.')+2])
                    '''
                    mas_kol[3]=viv[:viv.find('.')+2]
                else:
                    item= QtGui.QStandardItem(mas_kol[3])
                    
                mas_set[i].kol_pak=0                
                self.mod_set.setItem(0,i*4+2, item)   
                    '''
                    self.mod_set.setItem(0,i*4+2, item)   
                    

                if mas_set[i].vr_sleep!=0:
                    viv=str(mas_set[i].vr_rab/mas_set[i].vr_sleep*100)
                    item= QtGui.QStandardItem(viv[:viv.find('.')+2])                   
                    self.mod_set.setItem(0,i*4+3, item)
                    mas_set[i].vr_rab=0
                    mas_set[i].vr_sleep=0
            
                for row in range(1,ser):

                #    item= QtGui.QStandardItem(str(row+1)+'.')                                           
                #    self.mod_set.setItem(row,0+i*4, item) 
                                              
                #    item= QtGui.QStandardItem(param_name[ind_set_param_in[i][row]])                                   
                #    self.mod_set.setItem(row,1+i*4, item) 
                                
                    item= QtGui.QStandardItem(str(round(param[ind_set_param_in[i][row]],OKR)))                   
                    self.mod_set.setItem(row,2+i*4, item) 
            for ii in range(len(ind_set_param_in)): 
              #  mas_set[ii].kol_pak=0         
                mas_set[ii].vr_rab=0
                mas_set[ii].vr_sleep=0
                
       #     self.pr_time_kol_pak=self.time_kol_pak 

#    таблица  вкладки АРМ

        #    self.mod_arm=QStandardItemModel(len(ind_arm_param_out),3)
              
            for i in range(1,len(ind_arm_param_out)):
               
            #        item= QtGui.QStandardItem(str(i)+'.')                                           
            #        self.mod_arm.setItem(i,0, item) 
                                              
            #        item= QtGui.QStandardItem(param_name[ind_arm_param_out[i]])                                   
            #        self.mod_arm.setItem(i,1, item) 
                                
                    item= QtGui.QStandardItem(str(round(param[ind_arm_param_out[i-1]],OKR)))                   
                    self.mod_arm.setItem(i,2, item) 

            self.ui.label_4.setText(st_tek_situacii+'   '+st_tek_teh_rezim+'   '+st_tek_teh_etap)

 #           print (3,time.time()-tim)	

if __name__ == '__main__':
    
    
    
    while 1:
    
        try:
            print ()
            print ('start program')
            app = QApplication(sys.argv)               
            uw=MainWindow()
        #    time.sleep(1)
            uw.show()
            sys.exit(app.exec_())             
        except:
            try:
                del app
                del uw
            except:
             #   time.sleep(0.1)
                pass
                
                
            a=time.time()
            print (a,'trying finish')
            while time.time()-a<2:
                        if finish_en==0:
                            finish_en=1
                        else:
                            time.sleep (0.1)
                            
            print (time.time(),'must due')
            finish_en=0
                
            
            
            print ('error start program')
         #   pass
        
     #   sys.exit(app.exec_()) 
    
   