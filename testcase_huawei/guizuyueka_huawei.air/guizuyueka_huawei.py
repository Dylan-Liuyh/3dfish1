# -*- encoding=utf8 -*-
__author__ = "Hyper"
import sys
import codecs
import traceback

from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco

import sys
root_path = os.path.abspath(__file__)
root_path = '/'.join(root_path.split('/')[:-3])
sys.path.append(root_path)
from common_airtest.common_airtest_all import *

def guizuyueka_huawei():
    login_huawei()
    guizuyueka()
    '''if exists(Template(r"tpl1659680508065.png", record_pos=(-0.099, 0.152), resolution=(2700, 1228))):        #300
        touch(Template(r"tpl1659680508065.png", record_pos=(-0.099, 0.152), resolution=(2700, 1228)))
        while True:
            if exists(Template(r"tpl1659671744136.png", record_pos=(0.019, -0.034), resolution=(2700, 1228))):
                touch(Template(r"tpl1659436329024.png", record_pos=(-0.062, 0.04), resolution=(2400, 1080)))    
                sleep(5)
            elif exists(Template(r"tpl1659672170495.png", record_pos=(0.023, -0.033), resolution=(2700, 1228))):

                touch(Template(r"tpl1659436329024.png", record_pos=(-0.062, 0.04), resolution=(2400, 1080)))
                sleep(5)       
                wait(Template(r"tpl1656670610049.png", record_pos=(-0.287, -0.193), resolution=(2700, 1228)))  
                sleep(2)
                touch(Template(r"tpl1656906028821.png", record_pos=(-0.418, -0.193), resolution=(2700, 1228)))
                sleep(2)
                touch(Template(r"tpl1656906039738.png", record_pos=(0.184, 0.023), resolution=(2700, 1228)))
                sleep(3)
                touch(Template(r"tpl1656986073992.png", record_pos=(0.02, 0.04), resolution=(2700, 1228)))
                break
    elif exists(Template(r"tpl1659671979419.png", record_pos=(-0.011, 0.151), resolution=(2700, 1228))):
        touch(Template(r"tpl1659671979419.png", record_pos=(-0.011, 0.151), resolution=(2700, 1228)))
        while True:
            if exists(Template(r"tpl1659671744136.png", record_pos=(0.019, -0.034), resolution=(2700, 1228))):
                touch(Template(r"tpl1659436329024.png", record_pos=(-0.062, 0.04), resolution=(2400, 1080)))    
                sleep(5)
            elif exists(Template(r"tpl1659672170495.png", record_pos=(0.023, -0.033), resolution=(2700, 1228))):

                touch(Template(r"tpl1659436329024.png", record_pos=(-0.062, 0.04), resolution=(2400, 1080)))
                sleep(5)       
                wait(Template(r"tpl1656670610049.png", record_pos=(-0.287, -0.193), resolution=(2700, 1228)))  
                sleep(2)
                touch(Template(r"tpl1656906028821.png", record_pos=(-0.418, -0.193), resolution=(2700, 1228)))
                sleep(2)
                touch(Template(r"tpl1656906039738.png", record_pos=(0.184, 0.023), resolution=(2700, 1228)))
                sleep(3)
                touch(Template(r"tpl1656986073992.png", record_pos=(0.02, 0.04), resolution=(2700, 1228)))
                break
    if exists(Template(r"tpl1659436393151.png", record_pos=(0.35, -0.157), resolution=(2400, 1080))):        
        touch(Template(r"tpl1659436393151.png", record_pos=(0.35, -0.157), resolution=(2400, 1080)))
    if exists(Template(r"tpl1656986985582.png", record_pos=(0.351, -0.179), resolution=(2700, 1228))):
        touch(Template(r"tpl1656986985582.png", record_pos=(0.351, -0.179), resolution=(2700, 1228)))'''
        
    if exists(Template(r"tpl1657163003633.png", record_pos=(-0.049, -0.18), resolution=(2400, 1080))):
        touch(Template(r"tpl1657163011346.png", record_pos=(0.264, 0.157), resolution=(2400, 1080)))
    


    #if exists(Template(r"tpl1656985840552.png", record_pos=(0.02, -0.035), resolution=(2700, 1228))):
        if exists(Template(r"tpl1657102545475.png", record_pos=(0.02, 0.043), resolution=(2700, 1228))):
            touch(Template(r"tpl1656986011036.png", record_pos=(-0.059, 0.04), resolution=(2700, 1228)))
    
        if exists(Template(r"tpl1656986011036.png", record_pos=(-0.059, 0.04), resolution=(2700, 1228))):
            touch(Template(r"tpl1656986011036.png", record_pos=(-0.059, 0.04), resolution=(2700, 1228)))
            sleep(10)
    elif exists(Template(r"tpl1657163136698.png", record_pos=(0.022, -0.148), resolution=(2400, 1080))):
        if exists(Template(r"tpl1657163153068.png", threshold=0.95, record_pos=(0.122, 0.163), resolution=(2700, 1228))):
            touch(Template(r"tpl1657163153068.png", threshold=0.95, record_pos=(0.122, 0.163), resolution=(2700, 1228)))
        
            if exists(Template(r"tpl1657102545475.png", record_pos=(0.02, 0.043), resolution=(2700, 1228))):
                touch(Template(r"tpl1656986011036.png", record_pos=(-0.059, 0.04), resolution=(2700, 1228)))
                sleep(10)
              
                if exists(Template(r"tpl1658130819855.png", record_pos=(0.004, 0.955), resolution=(1228, 2700))):
                    touch(Template(r"tpl1658130832046.png", record_pos=(0.223, 0.958), resolution=(1228, 2700)))
                    sleep(5)
                wait(Template(r"tpl1656670610049.png", record_pos=(-0.287, -0.193), resolution=(2700, 1228)))  
                sleep(2)
                touch(Template(r"tpl1656906028821.png", record_pos=(-0.418, -0.193), resolution=(2700, 1228)))
                sleep(2)
                touch(Template(r"tpl1656906039738.png", record_pos=(0.184, 0.023), resolution=(2700, 1228)))
                sleep(2)
                wait(Template(r"tpl1656986062616.png", record_pos=(0.019, -0.034), resolution=(2700, 1228)))
                touch(Template(r"tpl1656986073992.png", record_pos=(0.02, 0.04), resolution=(2700, 1228)))
                sleep(2)
                touch(Template(r"tpl1656986084545.png", record_pos=(0.305, -0.157), resolution=(2700, 1228)))
        elif exists(Template(r"tpl1657164219829.png", threshold=0.9500000000000001, record_pos=(0.124, 0.162), resolution=(2400, 1080))):
            touch(Template(r"tpl1657164219829.png", threshold=0.95, record_pos=(0.124, 0.162), resolution=(2400, 1080)))
            sleep(2)
            if exists(Template(r"tpl1657102545475.png", record_pos=(0.02, 0.043), resolution=(2700, 1228))):
                touch(Template(r"tpl1656986011036.png", record_pos=(-0.059, 0.04), resolution=(2700, 1228)))
                sleep(10) 
                if exists(Template(r"tpl1658130819855.png", record_pos=(0.004, 0.955), resolution=(1228, 2700))):
                    touch(Template(r"tpl1658130832046.png", record_pos=(0.223, 0.958), resolution=(1228, 2700)))
                    sleep(5)
                wait(Template(r"tpl1656670610049.png", record_pos=(-0.287, -0.193), resolution=(2700, 1228)))  
                sleep(2)
                touch(Template(r"tpl1656906028821.png", record_pos=(-0.418, -0.193), resolution=(2700, 1228)))
                sleep(2)
                touch(Template(r"tpl1656906039738.png", record_pos=(0.184, 0.023), resolution=(2700, 1228)))
                sleep(2)
                wait(Template(r"tpl1656986062616.png", record_pos=(0.019, -0.034), resolution=(2700, 1228)))
                touch(Template(r"tpl1656986073992.png", record_pos=(0.02, 0.04), resolution=(2700, 1228)))
                sleep(2)
                if exists(Template(r"tpl1656986084545.png", record_pos=(0.305, -0.157), resolution=(2700, 1228))):
                    touch(Template(r"tpl1656986084545.png", record_pos=(0.305, -0.157), resolution=(2700, 1228)))
                sleep(5)

    if exists(Template(r"tpl1656986985582.png", record_pos=(0.351, -0.179), resolution=(2700, 1228))):
        touch(Template(r"tpl1656986985582.png", record_pos=(0.351, -0.179), resolution=(2700, 1228)))
                
    #大厅检测
    popwindows()
    
        
if __name__=='__main__':
    guizuyueka_huawei()      
        
        
        
        