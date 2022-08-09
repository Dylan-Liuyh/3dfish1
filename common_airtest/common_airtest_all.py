import io
import os.path
import jinja2

from airtest.core.api import *
from airtest.report.report import LogToHtml
from airtest.utils.compat import script_dir_name
from poco.drivers.unity3d import UnityPoco
from airtest.core.android import Android

def login_huawei():
    #pcg_name=package_name_confirm(PACKAGE_NAME_LIST,appPackageList)
    if exists(Template(r"tpl1658816869429.png", rgb=True, record_pos=(0.401, 0.181), resolution=(2700, 1228))):      
        #popwindows()
        if exists(Template(r"tpl1659348858975.png", record_pos=(-0.437, 0.119), resolution=(2400, 1080)))==False:
            touch(Template(r"tpl1659348800453.png", record_pos=(-0.436, 0.193), resolution=(2400, 1080)))
            sleep(2)
            touch(Template(r"tpl1659348858975.png", record_pos=(-0.437, 0.119), resolution=(2400, 1080)))
            if exists(Template(r"tpl1659361149030.png", threshold=0.9000000000000001, record_pos=(0.017, -0.089), resolution=(2700, 1228))):
                touch(Template(r"tpl1659361149030.png", threshold=0.9000000000000001, record_pos=(0.017, -0.089), resolution=(2700, 1228)))
                sleep(2)
            
            touch(Template(r"tpl1657780913763.png", threshold=0.8500000000000001, record_pos=(0.211, -0.131), resolution=(2400, 1080)))
             

    else:
        start_app("com.tuyoo.fish3d.huawei")
        sleep(5)
        while True:
            if exists(Template(r"tpl1658714256494.png", record_pos=(0.219, -0.161), resolution=(2400, 1080))):
                touch(Template(r"tpl1658714256494.png", record_pos=(0.219, -0.161), resolution=(2400, 1080)))
                continue
            elif exists(Template(r"tpl1659776660711.png", record_pos=(0.209, -0.18), resolution=(2340, 1080))):
                touch(Template(r"tpl1659776660711.png", record_pos=(0.209, -0.18), resolution=(2340, 1080)))

            elif exists(Template(r"quxiao.png", threshold=0.8500000000000001, record_pos=(0.001, 0.143), resolution=(2408, 1080))):
                touch(Template(r"cha.png", threshold=0.8500000000000001, record_pos=(0.375, -0.164), resolution=(2408, 1080)))
                continue
            elif exists(Template(r"tpl1657682711174.png", threshold=0.8500000000000001, record_pos=(0.001, 0.143), resolution=(2408, 1080))):
                touch(Template(r"tpl1657682719542.png", threshold=0.8500000000000001, record_pos=(0.375, -0.164), resolution=(2408, 1080)))
                continue

            elif exists(Template(r"tpl1657529632300.png", threshold=0.8500000000000001, record_pos=(0.007, 0.106), resolution=(2408, 1080)),):
                touch(Template(r"tpl1657529632300.png", threshold=0.8500000000000001, record_pos=(0.007, 0.106), resolution=(2408, 1080)))
                continue
            elif exists(Template(r"tpl1657677680308.png", threshold=0.8500000000000001, record_pos=(0.375, -0.164), resolution=(2400, 1080))):
                touch(Template(r"tpl1657677680308.png", threshold=0.8500000000000001, record_pos=(0.375, -0.164), resolution=(2400, 1080)))
                continue
            elif exists(Template(r"tpl1657765351166.png", threshold=0.8500000000000001, record_pos=(0.003, -0.17), resolution=(2040, 1080))):
                touch(Template(r"tpl1657765359675.png", threshold=0.8500000000000001, record_pos=(0.107, 0.169), resolution=(2040, 1080)))
                continue
   
            elif exists(Template(r"tpl1657008129356.png", threshold=0.8500000000000001, record_pos=(0.019, -0.007), resolution=(2700, 1228))):
                touch(Template(r"tpl1657008142126.png", threshold=0.8500000000000001, record_pos=(0.111, 0.085), resolution=(2700, 1228)))
                break
        while True:
            if exists(Template(r"tpl1659776502675.png", record_pos=(-0.159, 0.063), resolution=(2340, 1080))):
                touch(Template(r"tpl1659776502675.png", record_pos=(-0.159, 0.063), resolution=(2340, 1080)))
                sleep(5)
            else:
                break
        if exists(Template(r"tpl1657765351166.png", threshold=0.8500000000000001, record_pos=(0.003, -0.17), resolution=(2040, 1080))):
            touch(Template(r"tpl1657765359675.png", threshold=0.8500000000000001, record_pos=(0.107, 0.169), resolution=(2040, 1080)))
            sleep(5)
        

        while True:     
            if exists(Template(r"tpl1659602512481.png", record_pos=(-0.207, 0.962), resolution=(1080, 2400))):
                touch(Template(r"tpl1659602512481.png", record_pos=(-0.207, 0.962), resolution=(1080, 2400)))
                continue
            if exists(Template(r"tpl1659602536460.png", record_pos=(-0.217, 0.967), resolution=(1080, 2400))):
                touch(Template(r"tpl1659602536460.png", record_pos=(-0.217, 0.967), resolution=(1080, 2400)))
                continue
            if exists(Template(r"tpl1658714256494.png", record_pos=(0.219, -0.161), resolution=(2400, 1080))):
                touch(Template(r"tpl1658714256494.png", record_pos=(0.219, -0.161), resolution=(2400, 1080)))
                continue
                
    
            if exists(Template(r"tpl1657766391509.png", threshold=0.8500000000000001, record_pos=(0.004, 0.092), resolution=(2040, 1080))):
                touch(Template(r"tpl1657766391509.png", threshold=0.8500000000000001, record_pos=(0.004, 0.092), resolution=(2040, 1080)))
                continue
                
            if exists(Template(r"tpl1657008169585.png", record_pos=(-0.139, 0.163), resolution=(2700, 1228))):
                touch(Template(r"tpl1657008169585.png", record_pos=(-0.139, 0.163), resolution=(2700, 1228)))
                break
            if exists(Template(r"tpl1659942429373.png", record_pos=(-0.137, 0.162), resolution=(2700, 1228))):
                break

        touch(Template(r"tpl1657006894699.png", threshold=0.8500000000000001, record_pos=(0.016, 0.115), resolution=(2700, 1228)))
        sleep(5)
        while True:
            if exists(Template(r"tpl1657338200511.png", threshold=0.8500000000000001, record_pos=(0.021, -0.013), resolution=(2400, 1080))):
                touch(Template(r"tpl1657338216870.png", threshold=0.8500000000000001, record_pos=(0.022, 0.039), resolution=(2400, 1080)))
                sleep(2)
                touch(Template(r"tpl1657008169585.png", record_pos=(-0.139, 0.163), resolution=(2700, 1228)))
                sleep(2)

                touch(Template(r"tpl1657006894699.png", threshold=0.8500000000000001, record_pos=(0.016, 0.115), resolution=(2700, 1228)))
            else:
                break
    
    
                
        sleep(240)
        if exists(Template(r"tpl1657505358422.png", threshold=0.8500000000000001, record_pos=(-0.055, 0.04), resolution=(2400, 1080))):
            touch(Template(r"tpl1657505358422.png", threshold=0.8500000000000001, record_pos=(-0.055, 0.04), resolution=(2400, 1080)))
            sleep(10) 
            if exists(Template(r"tpl1657780903689.png", threshold=0.8500000000000001, record_pos=(0.021, -0.128), resolution=(2400, 1080))):
                if exists(Template(r"tpl1659361149030.png", threshold=0.9000000000000001, record_pos=(0.017, -0.089), resolution=(2700, 1228))):
                    touch(Template(r"tpl1659361149030.png", threshold=0.9000000000000001, record_pos=(0.017, -0.089), resolution=(2700, 1228)))
                    sleep(2)
                touch(Template(r"tpl1657780913763.png", threshold=0.8500000000000001, record_pos=(0.211, -0.131), resolution=(2400, 1080)))
                sleep(2)

       
            if exists(Template(r"tpl1657505284632.png", threshold=0.8500000000000001, record_pos=(-0.433, -0.112), resolution=(2400, 1080))):
                touch(Template(r"tpl1657505284632.png", threshold=0.8500000000000001, record_pos=(-0.433, -0.112), resolution=(2400, 1080)))
                sleep(2)
                touch(Template(r"tpl1657505335924.png", threshold=0.8500000000000001, record_pos=(-0.302, -0.111), resolution=(2400, 1080)))
                sleep(2)
                
                touch(Template(r"tpl1657505358422.png", threshold=0.8500000000000001, record_pos=(-0.055, 0.04), resolution=(2400, 1080)))
                sleep(120)
                #wait(Template(r"tpl1658816869429.png", record_pos=(0.401, 0.181), resolution=(2700, 1228)),timeout=300)
                popwindows()
        elif exists(Template(r"tpl1657505284632.png", threshold=0.8500000000000001, record_pos=(-0.433, -0.112), resolution=(2400, 1080))):
            touch(Template(r"tpl1657505284632.png", threshold=0.8500000000000001, record_pos=(-0.433, -0.112), resolution=(2400, 1080)))
            sleep(2)
            touch(Template(r"tpl1659348589595.png", record_pos=(-0.348, -0.111), resolution=(2400, 1080)))
            if exists(Template(r"tpl1659361149030.png", threshold=0.9000000000000001, record_pos=(0.017, -0.089), resolution=(2700, 1228))):
                touch(Template(r"tpl1659361149030.png", threshold=0.9000000000000001, record_pos=(0.017, -0.089), resolution=(2700, 1228)))
                sleep(2)

                
            touch(Template(r"tpl1657780913763.png", threshold=0.8500000000000001, record_pos=(0.211, -0.131), resolution=(2400, 1080)))
            touch(Template(r"tpl1657505335924.png", threshold=0.8500000000000001, record_pos=(-0.302, -0.111), resolution=(2400, 1080)))
            sleep(2)
            touch(Template(r"tpl1657505358422.png", threshold=0.8500000000000001, record_pos=(-0.055, 0.04), resolution=(2400, 1080)))
            sleep(120)
            #wait(Template(r"tpl1658816869429.png", record_pos=(0.401, 0.181), resolution=(2700, 1228)),timeout=300)
            popwindows()
            
        else:#if exists(Template(r"tpl1658816869429.png", record_pos=(0.401, 0.181), resolution=(2700, 1228))):      
            popwindows()
            if exists(Template(r"tpl1659348858975.png", record_pos=(-0.437, 0.119), resolution=(2400, 1080)))==False:
                touch(Template(r"tpl1659348800453.png", record_pos=(-0.436, 0.193), resolution=(2400, 1080)))
                sleep(2)
                touch(Template(r"tpl1659348858975.png", record_pos=(-0.437, 0.119), resolution=(2400, 1080)))
                if exists(Template(r"tpl1659361149030.png", threshold=0.9000000000000001, record_pos=(0.017, -0.089), resolution=(2700, 1228))):
                    touch(Template(r"tpl1659361149030.png", threshold=0.9000000000000001, record_pos=(0.017, -0.089), resolution=(2700, 1228)))
                    sleep(2)
            
                touch(Template(r"tpl1657780913763.png", threshold=0.8500000000000001, record_pos=(0.211, -0.131), resolution=(2400, 1080)))
            
            
def login_mi():
    #pcg_name=package_name_confirm(PACKAGE_NAME_LIST,appPackageList)
    if exists(Template(r"tpl1658816869429.png", rgb=True, record_pos=(0.401, 0.181), resolution=(2700, 1228))):      
        #popwindows()
        if exists(Template(r"tpl1659348858975.png", record_pos=(-0.437, 0.119), resolution=(2400, 1080)))==False:
            touch(Template(r"tpl1659348800453.png", record_pos=(-0.436, 0.193), resolution=(2400, 1080)))
            sleep(2)
            touch(Template(r"tpl1659348858975.png", record_pos=(-0.437, 0.119), resolution=(2400, 1080)))
            if exists(Template(r"tpl1659361149030.png", threshold=0.9000000000000001, record_pos=(0.017, -0.089), resolution=(2700, 1228))):
                touch(Template(r"tpl1659361149030.png", threshold=0.9000000000000001, record_pos=(0.017, -0.089), resolution=(2700, 1228)))
                sleep(2)
            
            touch(Template(r"tpl1657780913763.png", threshold=0.8500000000000001, record_pos=(0.211, -0.131), resolution=(2400, 1080)))
             

    else:
        start_app("com.tuyoo.fish3d.mi")
        sleep(5)
        while True:
            if exists(Template(r"tpl1659766799634.png", record_pos=(0.086, 0.07), resolution=(2400, 1080))):
                touch(Template(r"tpl1659766799634.png", record_pos=(0.086, 0.07), resolution=(2400, 1080)))
                sleep(2)
                touch(Template(r"tpl1659766799634.png", record_pos=(0.086, 0.07), resolution=(2400, 1080)))
            elif exists(Template(r"tpl1658714256494.png", record_pos=(0.219, -0.161), resolution=(2400, 1080))):
                touch(Template(r"tpl1658714256494.png", record_pos=(0.219, -0.161), resolution=(2400, 1080)))
            elif exists(Template(r"tpl1659776660711.png", record_pos=(0.209, -0.18), resolution=(2340, 1080))):
                touch(Template(r"tpl1659776660711.png", record_pos=(0.209, -0.18), resolution=(2340, 1080)))    
            elif exists(Template(r"quxiao.png", threshold=0.8500000000000001, record_pos=(0.001, 0.143), resolution=(2408, 1080))):
                touch(Template(r"cha.png", threshold=0.8500000000000001, record_pos=(0.375, -0.164), resolution=(2408, 1080)))
                
            elif exists(Template(r"tpl1657682711174.png", threshold=0.8500000000000001, record_pos=(0.001, 0.143), resolution=(2408, 1080))):
                touch(Template(r"tpl1657682719542.png", threshold=0.8500000000000001, record_pos=(0.375, -0.164), resolution=(2408, 1080)))
                

            elif exists(Template(r"tpl1657529632300.png", threshold=0.8500000000000001, record_pos=(0.007, 0.106), resolution=(2408, 1080))):
                touch(Template(r"tpl1657529632300.png", threshold=0.8500000000000001, record_pos=(0.007, 0.106), resolution=(2408, 1080)))
                
            elif exists(Template(r"tpl1657677672212.png", threshold=0.8500000000000001, record_pos=(-0.107, 0.114), resolution=(2400, 1080))):
                touch(Template(r"tpl1657677680308.png", threshold=0.8500000000000001, record_pos=(0.375, -0.164), resolution=(2400, 1080)))
                
            elif exists(Template(r"tpl1657765351166.png", threshold=0.8500000000000001, record_pos=(0.003, -0.17), resolution=(2040, 1080))):
                touch(Template(r"tpl1657765359675.png", threshold=0.8500000000000001, record_pos=(0.107, 0.169), resolution=(2040, 1080)))
                
   
            elif exists(Template(r"tpl1657008129356.png", threshold=0.8500000000000001, record_pos=(0.019, -0.007), resolution=(2700, 1228))):
                touch(Template(r"tpl1657008142126.png", threshold=0.8500000000000001, record_pos=(0.111, 0.085), resolution=(2700, 1228)))
                break
        while True:
            if exists(Template(r"tpl1659776502675.png", record_pos=(-0.159, 0.063), resolution=(2340, 1080))):
                touch(Template(r"tpl1659776502675.png", record_pos=(-0.159, 0.063), resolution=(2340, 1080)))
                sleep(5)
            else:
                break
        if exists(Template(r"tpl1657765351166.png", threshold=0.8500000000000001, record_pos=(0.003, -0.17), resolution=(2040, 1080))):
            touch(Template(r"tpl1657765359675.png", threshold=0.8500000000000001, record_pos=(0.107, 0.169), resolution=(2040, 1080)))
            sleep(5)
        while True:                
            if exists(Template(r"tpl1658714256494.png", record_pos=(0.219, -0.161), resolution=(2400, 1080))):
                touch(Template(r"tpl1658714256494.png", record_pos=(0.219, -0.161), resolution=(2400, 1080)))
                continue
    
            if exists(Template(r"tpl1657766391509.png", threshold=0.8500000000000001, record_pos=(0.004, 0.092), resolution=(2040, 1080))):
                touch(Template(r"tpl1657766391509.png", threshold=0.8500000000000001, record_pos=(0.004, 0.092), resolution=(2040, 1080)))
                continue
            if exists(Template(r"tpl1657008169585.png", threshold=0.7999999999999999, record_pos=(-0.139, 0.163), resolution=(2700, 1228))):
                touch(Template(r"tpl1657008169585.png", record_pos=(-0.139, 0.163), resolution=(2700, 1228)))
                break
            if exists(Template(r"tpl1659942429373.png", record_pos=(-0.137, 0.162), resolution=(2700, 1228))):
                break
        touch(Template(r"tpl1657006894699.png", threshold=0.8500000000000001, record_pos=(0.016, 0.115), resolution=(2700, 1228)))
        sleep(5)
        while True:
            if exists(Template(r"tpl1657338200511.png", threshold=0.8500000000000001, record_pos=(0.021, -0.013), resolution=(2400, 1080))):
                touch(Template(r"tpl1657338216870.png", threshold=0.8500000000000001, record_pos=(0.022, 0.039), resolution=(2400, 1080)))
                sleep(2)
                touch(Template(r"tpl1657008169585.png", record_pos=(-0.139, 0.163), resolution=(2700, 1228)))
                sleep(2)

                touch(Template(r"tpl1657006894699.png", threshold=0.8500000000000001, record_pos=(0.016, 0.115), resolution=(2700, 1228)))
            else:
                break
    
    
                
        sleep(180)
        if exists(Template(r"tpl1657505358422.png", threshold=0.8500000000000001, record_pos=(-0.055, 0.04), resolution=(2400, 1080))):
            touch(Template(r"tpl1657505358422.png", threshold=0.8500000000000001, record_pos=(-0.055, 0.04), resolution=(2400, 1080)))
            sleep(10) 
            if exists(Template(r"tpl1657780903689.png", threshold=0.8500000000000001, record_pos=(0.021, -0.128), resolution=(2400, 1080))):
                if exists(Template(r"tpl1659361149030.png", threshold=0.9000000000000001, record_pos=(0.017, -0.089), resolution=(2700, 1228))):
                    touch(Template(r"tpl1659361149030.png", threshold=0.9000000000000001, record_pos=(0.017, -0.089), resolution=(2700, 1228)))
                    sleep(2)
                touch(Template(r"tpl1657780913763.png", threshold=0.8500000000000001, record_pos=(0.211, -0.131), resolution=(2400, 1080)))
                sleep(2)

       
            if exists(Template(r"tpl1657505284632.png", threshold=0.8500000000000001, record_pos=(-0.433, -0.112), resolution=(2400, 1080))):
                touch(Template(r"tpl1657505284632.png", threshold=0.8500000000000001, record_pos=(-0.433, -0.112), resolution=(2400, 1080)))
                sleep(2)
                touch(Template(r"tpl1657505335924.png", threshold=0.8500000000000001, record_pos=(-0.302, -0.111), resolution=(2400, 1080)))
                sleep(2)
                
                touch(Template(r"tpl1657505358422.png", threshold=0.8500000000000001, record_pos=(-0.055, 0.04), resolution=(2400, 1080)))
                sleep(120)
                #wait(Template(r"tpl1658816869429.png", record_pos=(0.401, 0.181), resolution=(2700, 1228)),timeout=300)
                popwindows()
        elif exists(Template(r"tpl1657505284632.png", threshold=0.8500000000000001, record_pos=(-0.433, -0.112), resolution=(2400, 1080))):
            touch(Template(r"tpl1657505284632.png", threshold=0.8500000000000001, record_pos=(-0.433, -0.112), resolution=(2400, 1080)))
            sleep(2)
            touch(Template(r"tpl1659348589595.png", record_pos=(-0.348, -0.111), resolution=(2400, 1080)))
            if exists(Template(r"tpl1659361149030.png", threshold=0.9000000000000001, record_pos=(0.017, -0.089), resolution=(2700, 1228))):
                touch(Template(r"tpl1659361149030.png", threshold=0.9000000000000001, record_pos=(0.017, -0.089), resolution=(2700, 1228)))
                sleep(2)

                
            touch(Template(r"tpl1657780913763.png", threshold=0.8500000000000001, record_pos=(0.211, -0.131), resolution=(2400, 1080)))
            touch(Template(r"tpl1657505335924.png", threshold=0.8500000000000001, record_pos=(-0.302, -0.111), resolution=(2400, 1080)))
            sleep(2)
            touch(Template(r"tpl1657505358422.png", threshold=0.8500000000000001, record_pos=(-0.055, 0.04), resolution=(2400, 1080)))
            sleep(120)
            #wait(Template(r"tpl1658816869429.png", record_pos=(0.401, 0.181), resolution=(2700, 1228)),timeout=300)
            popwindows()
        else:#if exists(Template(r"tpl1658816869429.png", record_pos=(0.401, 0.181), resolution=(2700, 1228))):      
            popwindows()
            if exists(Template(r"tpl1659348858975.png", record_pos=(-0.437, 0.119), resolution=(2400, 1080)))==False:
                touch(Template(r"tpl1659348800453.png", record_pos=(-0.436, 0.193), resolution=(2400, 1080)))
                sleep(2)
                touch(Template(r"tpl1659348858975.png", record_pos=(-0.437, 0.119), resolution=(2400, 1080)))
                if exists(Template(r"tpl1659361149030.png", threshold=0.9000000000000001, record_pos=(0.017, -0.089), resolution=(2700, 1228))):
                    touch(Template(r"tpl1659361149030.png", threshold=0.9000000000000001, record_pos=(0.017, -0.089), resolution=(2700, 1228)))
                    sleep(2)
            
                touch(Template(r"tpl1657780913763.png", threshold=0.8500000000000001, record_pos=(0.211, -0.131), resolution=(2400, 1080)))
def login_vivo():
    if exists(Template(r"tpl1658816869429.png", record_pos=(0.401, 0.181), resolution=(2700, 1228))):      
        if exists(Template(r"tpl1659348858975.png", record_pos=(-0.437, 0.119), resolution=(2400, 1080)))==False:
            touch(Template(r"tpl1659348800453.png", record_pos=(-0.436, 0.193), resolution=(2400, 1080)))
            sleep(2)
            touch(Template(r"tpl1659348858975.png", record_pos=(-0.437, 0.119), resolution=(2400, 1080)))
            if exists(Template(r"tpl1659361149030.png", threshold=0.9000000000000001, record_pos=(0.017, -0.089), resolution=(2700, 1228))):
                touch(Template(r"tpl1659361149030.png", threshold=0.9000000000000001, record_pos=(0.017, -0.089), resolution=(2700, 1228)))
                sleep(2)
            
            touch(Template(r"tpl1657780913763.png", threshold=0.8500000000000001, record_pos=(0.211, -0.131), resolution=(2400, 1080)))
             

    else:
        start_app("com.tuyoo.fish3d.vivo")
        sleep(5)
        while True:
            if exists(Template(r"tpl1658801141512.png", record_pos=(-0.0, -0.007), resolution=(2400, 1080))):
                touch(Template(r"tpl1658801141512.png", record_pos=(-0.0, -0.007), resolution=(2400, 1080)))
                sleep(5)
            elif exists(Template(r"tpl1657682711174.png", record_pos=(0.001, 0.143), resolution=(2408, 1080))):
                touch(Template(r"tpl1657682719542.png", record_pos=(0.375, -0.164), resolution=(2408, 1080)))
                continue

            elif exists(Template(r"tpl1657529632300.png", record_pos=(0.007, 0.106), resolution=(2408, 1080))):
                touch(Template(r"tpl1657529632300.png", record_pos=(0.007, 0.106), resolution=(2408, 1080)))
                continue
            elif exists(Template(r"tpl1658801309960.png", record_pos=(0.374, -0.164), resolution=(2400, 1080))):
                touch(Template(r"tpl1658801309960.png", record_pos=(0.374, -0.164), resolution=(2400, 1080)))
                continue
            elif exists(Template(r"tpl1657677672212.png", record_pos=(-0.107, 0.114), resolution=(2400, 1080))):
                touch(Template(r"tpl1657677680308.png", record_pos=(0.375, -0.164), resolution=(2400, 1080)))
                continue
                
            elif exists(Template(r"tpl1657008129356.png", record_pos=(0.019, -0.007), resolution=(2700, 1228))):
                touch(Template(r"tpl1657008142126.png", record_pos=(0.111, 0.085), resolution=(2700, 1228)))
                break

        if exists(Template(r"tpl1657008169585.png", record_pos=(-0.139, 0.163), resolution=(2700, 1228))):
            touch(Template(r"tpl1657008169585.png", record_pos=(-0.139, 0.163), resolution=(2700, 1228)))
            

        touch(Template(r"tpl1657006894699.png", record_pos=(0.016, 0.115), resolution=(2700, 1228)))
        sleep(5)    
        while True:
            if exists(Template(r"tpl1657338200511.png", record_pos=(0.021, -0.013), resolution=(2400, 1080))):
                touch(Template(r"tpl1657338216870.png", record_pos=(0.022, 0.039), resolution=(2400, 1080)))
                sleep(2)
                touch(Template(r"tpl1657008169585.png", record_pos=(-0.139, 0.163), resolution=(2700, 1228)))
                touch(Template(r"tpl1657006894699.png", record_pos=(0.016, 0.115), resolution=(2700, 1228)))
            else:
                break   
        sleep(180)
        if exists(Template(r"tpl1657505358422.png", threshold=0.8500000000000001, record_pos=(-0.055, 0.04), resolution=(2400, 1080))):
            touch(Template(r"tpl1657505358422.png", threshold=0.8500000000000001, record_pos=(-0.055, 0.04), resolution=(2400, 1080)))
            sleep(10) 
            if exists(Template(r"tpl1657780903689.png", threshold=0.8500000000000001, record_pos=(0.021, -0.128), resolution=(2400, 1080))):
                if exists(Template(r"tpl1659361149030.png", threshold=0.9000000000000001, record_pos=(0.017, -0.089), resolution=(2700, 1228))):
                    touch(Template(r"tpl1659361149030.png", threshold=0.9000000000000001, record_pos=(0.017, -0.089), resolution=(2700, 1228)))
                    sleep(2)
                    touch(Template(r"tpl1657780913763.png", threshold=0.8500000000000001, record_pos=(0.211, -0.131), resolution=(2400, 1080)))
                    sleep(2)

       
            if exists(Template(r"tpl1657505284632.png", threshold=0.8500000000000001, record_pos=(-0.433, -0.112), resolution=(2400, 1080))):
                touch(Template(r"tpl1657505284632.png", threshold=0.8500000000000001, record_pos=(-0.433, -0.112), resolution=(2400, 1080)))
                sleep(2)
                touch(Template(r"tpl1657505335924.png", threshold=0.8500000000000001, record_pos=(-0.302, -0.111), resolution=(2400, 1080)))
                sleep(2)
                
                touch(Template(r"tpl1657505358422.png", threshold=0.8500000000000001, record_pos=(-0.055, 0.04), resolution=(2400, 1080)))
                sleep(120)
                #wait(Template(r"tpl1658816869429.png", record_pos=(0.401, 0.181), resolution=(2700, 1228)),timeout=300)
                popwindows()
        elif exists(Template(r"tpl1657505284632.png", threshold=0.8500000000000001, record_pos=(-0.433, -0.112), resolution=(2400, 1080))):
            touch(Template(r"tpl1657505284632.png", threshold=0.8500000000000001, record_pos=(-0.433, -0.112), resolution=(2400, 1080)))
            sleep(2)
            touch(Template(r"tpl1659348589595.png", record_pos=(-0.348, -0.111), resolution=(2400, 1080)))
            if exists(Template(r"tpl1659361149030.png", threshold=0.9000000000000001, record_pos=(0.017, -0.089), resolution=(2700, 1228))):
                touch(Template(r"tpl1659361149030.png", threshold=0.9000000000000001, record_pos=(0.017, -0.089), resolution=(2700, 1228)))
                sleep(2)

                
            touch(Template(r"tpl1657780913763.png", threshold=0.8500000000000001, record_pos=(0.211, -0.131), resolution=(2400, 1080)))
            touch(Template(r"tpl1657505335924.png", threshold=0.8500000000000001, record_pos=(-0.302, -0.111), resolution=(2400, 1080)))
            sleep(2)
            touch(Template(r"tpl1657505358422.png", threshold=0.8500000000000001, record_pos=(-0.055, 0.04), resolution=(2400, 1080)))    
            sleep(120)
            #wait(Template(r"tpl1658816869429.png", record_pos=(0.401, 0.181), resolution=(2700, 1228)),timeout=300)
            popwindows()
        else:#if exists(Template(r"tpl1658816869429.png", record_pos=(0.401, 0.181), resolution=(2700, 1228))):      
            popwindows()
            if exists(Template(r"tpl1659348858975.png", record_pos=(-0.437, 0.119), resolution=(2400, 1080)))==False:
                touch(Template(r"tpl1659348800453.png", record_pos=(-0.436, 0.193), resolution=(2400, 1080)))
                sleep(2)
                touch(Template(r"tpl1659348858975.png", record_pos=(-0.437, 0.119), resolution=(2400, 1080)))
                if exists(Template(r"tpl1659361149030.png", threshold=0.9000000000000001, record_pos=(0.017, -0.089), resolution=(2700, 1228))):
                    touch(Template(r"tpl1659361149030.png", threshold=0.9000000000000001, record_pos=(0.017, -0.089), resolution=(2700, 1228)))
                    sleep(2)
            
                touch(Template(r"tpl1657780913763.png", threshold=0.8500000000000001, record_pos=(0.211, -0.131), resolution=(2400, 1080)))
    
    
     
    
    
    
    
    
    
    
    
    
def login_oppo():
    if exists(Template(r"tpl1658816869429.png", record_pos=(0.401, 0.181), resolution=(2700, 1228))):      
        #popwindows()
        if exists(Template(r"tpl1659348858975.png", record_pos=(-0.437, 0.119), resolution=(2400, 1080)))==False:
            touch(Template(r"tpl1659348800453.png", record_pos=(-0.436, 0.193), resolution=(2400, 1080)))
            sleep(2)
            touch(Template(r"tpl1659348858975.png", record_pos=(-0.437, 0.119), resolution=(2400, 1080)))
            if exists(Template(r"tpl1659361149030.png", threshold=0.9000000000000001, record_pos=(0.017, -0.089), resolution=(2700, 1228))):
                touch(Template(r"tpl1659361149030.png", threshold=0.9000000000000001, record_pos=(0.017, -0.089), resolution=(2700, 1228)))
                sleep(2)
            
            touch(Template(r"tpl1657780913763.png", threshold=0.8500000000000001, record_pos=(0.211, -0.131), resolution=(2400, 1080)))
             

    else:
        start_app("com.tuyoo.fish3d.nearme.gamecenter")
        sleep(5)
        if exists(Template(r"tpl1657508064342.png", record_pos=(0.033, 0.066), resolution=(2400, 1080))):
            touch(Template(r"tpl1657508073881.png", record_pos=(0.136, 0.062), resolution=(2400, 1080)))
            sleep(5)
        while True:
            if exists(Template(r"tpl1657508064342.png", record_pos=(0.033, 0.066), resolution=(2400, 1080))):
                touch(Template(r"tpl1657508073881.png", record_pos=(0.136, 0.062), resolution=(2400, 1080)))
                
            elif exists(Template(r"tpl1657008129356.png", record_pos=(0.019, -0.007), resolution=(2700, 1228))):
                touch(Template(r"tpl1657008142126.png", record_pos=(0.111, 0.085), resolution=(2700, 1228)))
                break
        while True:
            if exists(Template(r"tpl1657508064342.png", record_pos=(0.033, 0.066), resolution=(2400, 1080))):
                touch(Template(r"tpl1657508073881.png", record_pos=(0.136, 0.062), resolution=(2400, 1080)))
                continue 
            elif exists(Template(r"tpl1657508167274.png", record_pos=(0.019, 0.101), resolution=(2400, 1080))):
                touch(Template(r"tpl1657508167274.png", record_pos=(0.019, 0.101), resolution=(2400, 1080)))
                continue
            elif exists(Template(r"tpl1657008169585.png", record_pos=(-0.139, 0.163), resolution=(2700, 1228))):
                touch(Template(r"tpl1657008169585.png", record_pos=(-0.139, 0.163), resolution=(2700, 1228)))
                break
        sleep(5)
        touch(Template(r"tpl1657508209681.png", record_pos=(0.02, 0.125), resolution=(2400, 1080)))
        sleep(5)
        while True:
            if exists(Template(r"tpl1657338200511.png", record_pos=(0.021, -0.013), resolution=(2400, 1080))):
                touch(Template(r"tpl1657338216870.png", record_pos=(0.022, 0.039), resolution=(2400, 1080)))
                sleep(2)
                touch(Template(r"tpl1657008169585.png", record_pos=(-0.139, 0.163), resolution=(2700, 1228)))
                sleep(5)

                touch(Template(r"tpl1657508209681.png", record_pos=(0.02, 0.125), resolution=(2400, 1080)))
            else:
                break
    
    
        if exists(Template(r"tpl1657006894699.png", record_pos=(0.016, 0.115), resolution=(2700, 1228))):
            touch(Template(r"tpl1657006894699.png", record_pos=(0.016, 0.115), resolution=(2700, 1228)))        
        
        sleep(180)    
        if exists(Template(r"tpl1657505358422.png", threshold=0.8500000000000001, record_pos=(-0.055, 0.04), resolution=(2400, 1080))):
            touch(Template(r"tpl1657505358422.png", threshold=0.8500000000000001, record_pos=(-0.055, 0.04), resolution=(2400, 1080)))
            sleep(10) 
            if exists(Template(r"tpl1657780903689.png", threshold=0.8500000000000001, record_pos=(0.021, -0.128), resolution=(2400, 1080))):
                if exists(Template(r"tpl1659361149030.png", threshold=0.9000000000000001, record_pos=(0.017, -0.089), resolution=(2700, 1228))):
                    touch(Template(r"tpl1659361149030.png", threshold=0.9000000000000001, record_pos=(0.017, -0.089), resolution=(2700, 1228)))
                    sleep(2)
                touch(Template(r"tpl1657780913763.png", threshold=0.8500000000000001, record_pos=(0.211, -0.131), resolution=(2400, 1080)))
                sleep(2)

       
            if exists(Template(r"tpl1657505284632.png", threshold=0.8500000000000001, record_pos=(-0.433, -0.112), resolution=(2400, 1080))):
                touch(Template(r"tpl1657505284632.png", threshold=0.8500000000000001, record_pos=(-0.433, -0.112), resolution=(2400, 1080)))
                sleep(2)
                touch(Template(r"tpl1657505335924.png", threshold=0.8500000000000001, record_pos=(-0.302, -0.111), resolution=(2400, 1080)))
                sleep(2)
                
                touch(Template(r"tpl1657505358422.png", threshold=0.8500000000000001, record_pos=(-0.055, 0.04), resolution=(2400, 1080)))
                sleep(120)
                #wait(Template(r"tpl1658816869429.png", record_pos=(0.401, 0.181), resolution=(2700, 1228)),timeout=300)
                popwindows()
        elif exists(Template(r"tpl1657505284632.png", threshold=0.8500000000000001, record_pos=(-0.433, -0.112), resolution=(2400, 1080))):
            touch(Template(r"tpl1657505284632.png", threshold=0.8500000000000001, record_pos=(-0.433, -0.112), resolution=(2400, 1080)))
            sleep(2)
            touch(Template(r"tpl1659348589595.png", record_pos=(-0.348, -0.111), resolution=(2400, 1080)))
            if exists(Template(r"tpl1659361149030.png", threshold=0.9000000000000001, record_pos=(0.017, -0.089), resolution=(2700, 1228))):
                touch(Template(r"tpl1659361149030.png", threshold=0.9000000000000001, record_pos=(0.017, -0.089), resolution=(2700, 1228)))
                sleep(2)

                
            touch(Template(r"tpl1657780913763.png", threshold=0.8500000000000001, record_pos=(0.211, -0.131), resolution=(2400, 1080)))
            touch(Template(r"tpl1657505335924.png", threshold=0.8500000000000001, record_pos=(-0.302, -0.111), resolution=(2400, 1080)))
            sleep(2)
            touch(Template(r"tpl1657505358422.png", threshold=0.8500000000000001, record_pos=(-0.055, 0.04), resolution=(2400, 1080)))    
            sleep(120)
            #wait(Template(r"tpl1658816869429.png", record_pos=(0.401, 0.181), resolution=(2700, 1228)),timeout=300)
            popwindows()
        else:#if exists(Template(r"tpl1658816869429.png", record_pos=(0.401, 0.181), resolution=(2700, 1228))):      
            popwindows()
            if exists(Template(r"tpl1659348858975.png", record_pos=(-0.437, 0.119), resolution=(2400, 1080)))==False:
                touch(Template(r"tpl1659348800453.png", record_pos=(-0.436, 0.193), resolution=(2400, 1080)))
                sleep(2)
                touch(Template(r"tpl1659348858975.png", record_pos=(-0.437, 0.119), resolution=(2400, 1080)))
                if exists(Template(r"tpl1659361149030.png", threshold=0.9000000000000001, record_pos=(0.017, -0.089), resolution=(2700, 1228))):
                    touch(Template(r"tpl1659361149030.png", threshold=0.9000000000000001, record_pos=(0.017, -0.089), resolution=(2700, 1228)))
                    sleep(2)
            
                touch(Template(r"tpl1657780913763.png", threshold=0.8500000000000001, record_pos=(0.211, -0.131), resolution=(2400, 1080)))
        
        
            
            
            
            
            
            
            
def popwindows(): 
    while True:       
        if exists(Template(r"tpl1657010528094.png", threshold=0.7499999999999999, record_pos=(0.057, 0.165), resolution=(2376, 1080))):
            touch(Template(r"tpl1657010534589.png", threshold=0.8500000000000001, record_pos=(0.293, -0.161), resolution=(2376, 1080)))            
            continue
        elif exists(Template(r"tpl1657165822001.png", threshold=0.8500000000000001, record_pos=(0.022, -0.147), resolution=(2400, 1080))):
            touch(Template(r"tpl1657165831936.png", threshold=0.8500000000000001, record_pos=(0.02, 0.092), resolution=(2400, 1080))) 
            continue
        elif exists(Template(r"tpl1657505358422.png", threshold=0.8500000000000001, record_pos=(-0.055, 0.04), resolution=(2400, 1080))):
            touch(Template(r"tpl1657505358422.png", threshold=0.8500000000000001, record_pos=(-0.055, 0.04), resolution=(2400, 1080)))
            continue
        elif exists(Template(r"tpl1657010554679.png", threshold=0.8500000000000001, record_pos=(0.034, -0.17), resolution=(2376, 1080))):
            touch(Template(r"tpl1657010575407.png", threshold=0.8500000000000001, record_pos=(0.346, -0.173), resolution=(2376, 1080)))
            sleep(10)
            touch(Template(r"tpl1657010575407.png", threshold=0.8500000000000001, record_pos=(0.346, -0.173), resolution=(2376, 1080)))
            continue
            
        #touch(Template(r"tpl1657091216177.png", threshold=0.8500000000000001, record_pos=(-0.378, -0.181), resolution=(2376, 1080)))
    
        elif exists(Template(r"tpl1657091172760.png", threshold=0.8500000000000001, record_pos=(0.357, 0.167), resolution=(2376, 1080))):
            touch(Template(r"tpl1657010669226.png", threshold=0.8500000000000001, record_pos=(0.024, 0.203), resolution=(2376, 1080)))
            continue
        elif exists(Template(r"tpl1657089414581.png", threshold=0.8500000000000001, record_pos=(-0.02, -0.169), resolution=(2700, 1228))):
            touch(Template(r"tpl1656986985582.png", threshold=0.8500000000000001, record_pos=(0.351, -0.179), resolution=(2700, 1228)))
            continue
        elif exists(Template(r"tpl1657089790735.png", threshold=0.8500000000000001, record_pos=(0.023, -0.195), resolution=(2700, 1228))):
            touch(Template(r"tpl1657010622111.png", threshold=0.8500000000000001, record_pos=(0.343, -0.184), resolution=(2376, 1080)))
            continue
        elif exists(Template(r"tpl1657093351712.png", threshold=0.8500000000000001, record_pos=(0.022, 0.085), resolution=(2376, 1080))):
            touch(Template(r"tpl1657093351712.png", threshold=0.8500000000000001, record_pos=(0.022, 0.085), resolution=(2376, 1080)))
            continue
            
        elif exists(Template(r"tpl1657272900561.png", threshold=0.8500000000000001, record_pos=(-0.058, -0.182), resolution=(2400, 1080))):
            touch(Template(r"tpl1657010622111.png", threshold=0.8500000000000001, record_pos=(0.343, -0.184), resolution=(2376, 1080)))     
            continue
        
        elif exists(Template(r"tpl1657354939110.png", threshold=0.8500000000000001, record_pos=(0.02, -0.193), resolution=(2376, 1152))):
            touch(Template(r"tpl1657010534589.png", threshold=0.8500000000000001, record_pos=(0.293, -0.161), resolution=(2376, 1080)))

            continue
     
        elif exists(Template(r"tpl1659404851584.png", record_pos=(0.018, 0.161), resolution=(2700, 1228))):
            touch(Template(r"tpl1659404851584.png", record_pos=(0.018, 0.161), resolution=(2700, 1228)))
            continue
            
        elif exists(Template(r"tpl1657010622111.png", threshold=0.8500000000000001, record_pos=(0.343, -0.184), resolution=(2376, 1080))):
            touch(Template(r"tpl1657010622111.png", threshold=0.8500000000000001, record_pos=(0.343, -0.184), resolution=(2376, 1080)))

        else:
            break

def daozhang():
    touch(Template(r"tpl1656928606504.png", record_pos=(0.043, -0.2), resolution=(2408, 1080)))
    sleep(5)
    '''touch(Template(r"tpl1659424632988.png", record_pos=(0.47, -0.083), resolution=(2400, 1080)))
    touch(Template(r"tpl1659424645672.png", record_pos=(0.343, -0.084), resolution=(2400, 1080)))'''
    if exists(Template(r"tpl1659431954114.png", record_pos=(-0.005, -0.163), resolution=(2700, 1228))):
        touch(Template(r"tpl1659424695788.png", record_pos=(0.284, -0.171), resolution=(2400, 1080)))
        #touch(Template(r"tpl1659424719551.png", threshold=0.7499999999999999, record_pos=(0.203, -0.117), resolution=(2400, 1080)))
    sleep(5)
    #touch(Template(r"tpl1656986558172.png", record_pos=(-0.207, -0.004), resolution=(2700, 1228)))
    touch(Template(r"tpl1659512160950.png", record_pos=(-0.181, 0.072), resolution=(2400, 1080)))
    
    
    
def zhifubao_xiaomi():
    touch(Template(r"tpl1657160110656.png", record_pos=(0.077, -0.097), resolution=(2400, 1080)))       #在拉起渠道支付的情况下选择支付宝支付
    sleep(2)
    touch(Template(r"tpl1657160069063.png", record_pos=(0.327, 0.167), resolution=(2400, 1080)))
    sleep(60)   
    if exists(Template(r"tpl1655432762735.png", threshold=0.6999999999999998, record_pos=(-0.001, 0.233), resolution=(1080, 2400))):   #多台手机登录同一个支付宝账号会出现提示框
        touch(Template(r"tpl1655363311706.png", record_pos=(0.206, 0.207), resolution=(1080, 2400)))     #关闭提示框
        sleep(5)
    if exists(Template(r"tpl1658200632659.png", threshold=0.7499999999999999, record_pos=(0.002, 0.229), resolution=(1080, 2400))):   #多台手机登录同一个支付宝账号会出现提示框
        touch(Template(r"tpl1658200638807.png", record_pos=(0.194, 0.232), resolution=(1080, 2400)))    #关闭提示框
        sleep(5)
    #if exists(Template(r"tpl1655256436380.png", threshold=0.9000000000000001, record_pos=(-0.002, 0.777), resolution=(1080, 2400))):
    #if exists(Template(r"tpl1655434450750.png", record_pos=(0.002, 0.774), resolution=(1080, 2400))):
    if exists(Template(r"tpl1655434504354.png", record_pos=(-0.065, 0.777), resolution=(1080, 2400))):   #第一种情况：支付宝未登录-部分手机会要求刷脸登录，我们选择密码登录
        touch(Template(r"tpl1655256449928.png", record_pos=(0.002, 1.025), resolution=(1080, 2400)))
        wait(Template(r"tpl1655256483902.png", record_pos=(-0.281, 0.188), resolution=(1080, 2400)))
        touch(Template(r"tpl1655256465925.png", record_pos=(-0.354, 0.392), resolution=(1080, 2400)))
        sleep(20)
        touch(Template(r"tpl1655273716094.png", record_pos=(-0.241, -0.103), resolution=(1080, 2400)))
        sleep(20)
        text("Tuyoo@123")
        sleep(20)
        if exists(Template(r"tpl1659498780436.png", record_pos=(0.426, -0.988), resolution=(1080, 2400))):    #有时候支付宝会要求开启指纹验证，这里不用理会，点击关闭即可
            touch(Template(r"tpl1659498780436.png", record_pos=(0.426, -0.988), resolution=(1080, 2400)))
    elif exists(Template(r"tpl1655359988724.png", record_pos=(-0.212, -0.109), resolution=(1080, 2400))):    #第二种情况：支付未登录-未要求刷脸登录，只要求密码登录
        sleep(20)               
        touch(Template(r"tpl1655273716094.png", record_pos=(-0.241, -0.103), resolution=(1080, 2400)))
        sleep(20)
        text("Tuyoo@123")
        if exists(Template(r"tpl1659498780436.png", record_pos=(0.426, -0.988), resolution=(1080, 2400))):     #有时候支付宝会要求开启指纹验证，这里不用理会，点击关闭即可
            touch(Template(r"tpl1659498780436.png", record_pos=(0.426, -0.988), resolution=(1080, 2400)))    
        sleep(20)
    if exists(Template(r"tpl1655804546181.png", record_pos=(0.007, 0.249), resolution=(1080, 2408))):    
        touch(Template(r"tpl1655804554247.png", record_pos=(-0.003, 0.247), resolution=(1080, 2408)))
        sleep(10)                      
    touch(Template(r"tpl1655435660272.png", record_pos=(0.0, 0.944), resolution=(1080, 2400)))    #无论支付宝是否登录，最终都会到达确认付款这一步，所以放在if判断外

    sleep(20)
    text("284119")                    #输入支付密码
    sleep(20)  
    if exists(Template(r"tpl1659499100155.png", record_pos=(0.041, 0.13), resolution=(1080, 2400))):     #前面我们没有开启指纹验证，这里有时会再次询问，我们还是不用理会，选择取消
        touch(Template(r"tpl1659499100155.png", record_pos=(0.041, 0.13), resolution=(1080, 2400)))
    touch(Template(r"tpl1651116160468.png", record_pos=(0.421, -0.985), resolution=(1080, 2400)))            # 点击完成，付款流程结束，此时返回游戏支付界面
    

def zhifubao_huawei():                              
    touch(Template(r"tpl1656670696400.png", record_pos=(0.073, 0.114), resolution=(2700, 1228)))
    sleep(2)
    touch(Template(r"tpl1655456665945.png", record_pos=(0.226, 0.183), resolution=(2700, 1228)))
    sleep(5)
    if exists(Template(r"tpl1655432762735.png", threshold=0.8500000000000001, record_pos=(-0.001, 0.233), resolution=(1080, 2400))):
 
        touch(Template(r"tpl1655363311706.png", record_pos=(0.206, 0.207), resolution=(1080, 2400)))
        sleep(5)

    if exists(Template(r"tpl1658200632659.png", threshold=0.8500000000000001, record_pos=(0.002, 0.229), resolution=(1080, 2400))):
        touch(Template(r"tpl1658200638807.png", record_pos=(0.194, 0.232), resolution=(1080, 2400)))
        sleep(5)


        
    #if exists(Template(r"tpl1655256436380.png", threshold=0.9000000000000001, record_pos=(-0.002, 0.777), resolution=(1080, 2400))):
    #if exists(Template(r"tpl1655434450750.png", record_pos=(0.002, 0.774), resolution=(1080, 2400))):
    if exists(Template(r"tpl1655434504354.png", record_pos=(-0.065, 0.777), resolution=(1080, 2400))):

        touch(Template(r"tpl1655256449928.png", record_pos=(0.002, 1.025), resolution=(1080, 2400)))
        wait(Template(r"tpl1655256483902.png", record_pos=(-0.281, 0.188), resolution=(1080, 2400)))

        touch(Template(r"tpl1655256465925.png", record_pos=(-0.354, 0.392), resolution=(1080, 2400)))
        sleep(20)
        touch(Template(r"tpl1655273716094.png", record_pos=(-0.241, -0.103), resolution=(1080, 2400)))
        sleep(20)
        text("Tuyoo@123")
        sleep(20)
        if exists(Template(r"tpl1659498780436.png", record_pos=(0.426, -0.988), resolution=(1080, 2400))):
            touch(Template(r"tpl1659498780436.png", record_pos=(0.426, -0.988), resolution=(1080, 2400)))
    elif exists(Template(r"tpl1655359988724.png", record_pos=(-0.212, -0.109), resolution=(1080, 2400))):
        sleep(20)               
        touch(Template(r"tpl1655273716094.png", record_pos=(-0.241, -0.103), resolution=(1080, 2400)))
        sleep(20)
        text("Tuyoo@123")
        if exists(Template(r"tpl1659498780436.png", record_pos=(0.426, -0.988), resolution=(1080, 2400))):
            touch(Template(r"tpl1659498780436.png", record_pos=(0.426, -0.988), resolution=(1080, 2400)))

        
        sleep(20)
    if exists(Template(r"tpl1655804546181.png", record_pos=(0.007, 0.249), resolution=(1080, 2408))):
        touch(Template(r"tpl1655804554247.png", record_pos=(-0.003, 0.247), resolution=(1080, 2408)))
        sleep(10)


    



                              
   
    touch(Template(r"tpl1655435660272.png", record_pos=(0.0, 0.944), resolution=(1080, 2400)))

    sleep(10)
    text("284119")
    sleep(10)
    if exists(Template(r"tpl1659499100155.png", record_pos=(0.041, 0.13), resolution=(1080, 2400))):
        touch(Template(r"tpl1659499100155.png", record_pos=(0.041, 0.13), resolution=(1080, 2400)))

    touch(Template(r"tpl1651116160468.png", record_pos=(0.421, -0.985), resolution=(1080, 2400)))
    sleep(10)
    
    if exists(Template(r"tpl1655459674760.png", record_pos=(0.004, 0.979), resolution=(1228, 2700))):
        touch(Template(r"tpl1655459674760.png", record_pos=(0.004, 0.979), resolution=(1228, 2700)))
    sleep(5)
    if exists(Template(r"tpl1655866825316.png", record_pos=(0.09, -0.077), resolution=(2400, 1080))):
        touch(Template(r"tpl1655866871742.png", record_pos=(0.29, -0.144), resolution=(2400, 1080)))

        
def zhifubao_oppo():
    touch(Template(r"tpl1657504980210.png", record_pos=(0.092, -0.106), resolution=(2400, 1080)))
    sleep(2)
    touch(Template(r"tpl1659578981599.png", record_pos=(0.129, 0.136), resolution=(2400, 1080)))

    sleep(5)
    if exists(Template(r"tpl1659579210295.png", record_pos=(-0.041, -0.301), resolution=(1080, 2400))):
        touch(Template(r"tpl1659579210295.png", record_pos=(-0.041, -0.301), resolution=(1080, 2400)))
        text("Tuyoo@123")
        sleep(5)
    touch(Template(r"tpl1655435660272.png", record_pos=(0.0, 0.944), resolution=(1080, 2400)))
    sleep(2)
    text("284119")
    sleep(2)
    touch(Template(r"tpl1651116160468.png", record_pos=(0.421, -0.985), resolution=(1080, 2400)))
    if exists(Template(r"tpl1658717678023.png", record_pos=(0.021, 0.125), resolution=(2400, 1080))):
        touch(Template(r"tpl1658717678023.png", record_pos=(0.021, 0.125), resolution=(2400, 1080)))
    '''if exists(Template(r"tpl1657520019675.png", record_pos=(0.016, 0.17), resolution=(1080, 2400))):
        touch(Template(r"tpl1657520030779.png", record_pos=(-0.215, 0.193), resolution=(1080, 2400)))
        sleep(5)


    if exists(Template(r"tpl1655432762735.png", threshold=0.8500000000000001, record_pos=(-0.001, 0.233), resolution=(1080, 2400))):
 
        touch(Template(r"tpl1655363311706.png", record_pos=(0.206, 0.207), resolution=(1080, 2400)))
        sleep(5)

    if exists(Template(r"tpl1658200632659.png", threshold=0.8500000000000001, record_pos=(0.002, 0.229), resolution=(1080, 2400))):
        touch(Template(r"tpl1658200638807.png", record_pos=(0.194, 0.232), resolution=(1080, 2400)))
        sleep(5)


        
    #if exists(Template(r"tpl1655256436380.png", threshold=0.9000000000000001, record_pos=(-0.002, 0.777), resolution=(1080, 2400))):
    #if exists(Template(r"tpl1655434450750.png", record_pos=(0.002, 0.774), resolution=(1080, 2400))):
    if exists(Template(r"tpl1655434504354.png", record_pos=(-0.065, 0.777), resolution=(1080, 2400))):

        touch(Template(r"tpl1655256449928.png", record_pos=(0.002, 1.025), resolution=(1080, 2400)))
        wait(Template(r"tpl1655256483902.png", record_pos=(-0.281, 0.188), resolution=(1080, 2400)))

        touch(Template(r"tpl1655256465925.png", record_pos=(-0.354, 0.392), resolution=(1080, 2400)))
        sleep(20)
        touch(Template(r"tpl1655273716094.png", record_pos=(-0.241, -0.103), resolution=(1080, 2400)))
        sleep(20)
        text("Tuyoo@123")
        sleep(20)
        if exists(Template(r"tpl1659498780436.png", record_pos=(0.426, -0.988), resolution=(1080, 2400))):
            touch(Template(r"tpl1659498780436.png", record_pos=(0.426, -0.988), resolution=(1080, 2400)))
    elif exists(Template(r"tpl1655359988724.png", record_pos=(-0.212, -0.109), resolution=(1080, 2400))):
        sleep(20)               
        touch(Template(r"tpl1655273716094.png", record_pos=(-0.241, -0.103), resolution=(1080, 2400)))
        sleep(20)
        text("Tuyoo@123")

        
        sleep(20)
        if exists(Template(r"tpl1659498780436.png", record_pos=(0.426, -0.988), resolution=(1080, 2400))):
            touch(Template(r"tpl1659498780436.png", record_pos=(0.426, -0.988), resolution=(1080, 2400)))
    if exists(Template(r"tpl1655804546181.png", record_pos=(0.007, 0.249), resolution=(1080, 2408))):
        touch(Template(r"tpl1655804554247.png", record_pos=(-0.003, 0.247), resolution=(1080, 2408)))
        sleep(10)


    



                              
   
    touch(Template(r"tpl1655435660272.png", record_pos=(0.0, 0.944), resolution=(1080, 2400)))

    sleep(20)
    text("284119")
    sleep(20)  
    if exists(Template(r"tpl1659499100155.png", record_pos=(0.041, 0.13), resolution=(1080, 2400))):
        touch(Template(r"tpl1659499100155.png", record_pos=(0.041, 0.13), resolution=(1080, 2400)))
    touch(Template(r"tpl1651116160468.png", record_pos=(0.421, -0.985), resolution=(1080, 2400)))
    sleep(20)

    if exists(Template(r"tpl1656931276943.png", record_pos=(0.021, -0.036), resolution=(2700, 1228))):
        touch(Template(r"tpl1656931284320.png", record_pos=(0.018, 0.042), resolution=(2700, 1228)))
        sleep(2)
    if exists(Template(r"tpl1658717678023.png", record_pos=(0.021, 0.125), resolution=(2400, 1080))):
        touch(Template(r"tpl1658717678023.png", record_pos=(0.021, 0.125), resolution=(2400, 1080)))'''
    
        
        
        
        
        
def zhifubao_vivo():
    if exists(Template(r"tpl1655432762735.png", threshold=0.8500000000000001, record_pos=(-0.001, 0.233), resolution=(1080, 2400))):
 
        touch(Template(r"tpl1655363311706.png", record_pos=(0.206, 0.207), resolution=(1080, 2400)))
        sleep(5)

    if exists(Template(r"tpl1658200632659.png", threshold=0.8500000000000001, record_pos=(0.002, 0.229), resolution=(1080, 2400))):
        touch(Template(r"tpl1658200638807.png", record_pos=(0.194, 0.232), resolution=(1080, 2400)))
        sleep(5)


        
    #if exists(Template(r"tpl1655256436380.png", threshold=0.9000000000000001, record_pos=(-0.002, 0.777), resolution=(1080, 2400))):
    #if exists(Template(r"tpl1655434450750.png", record_pos=(0.002, 0.774), resolution=(1080, 2400))):
    if exists(Template(r"tpl1655434504354.png", record_pos=(-0.065, 0.777), resolution=(1080, 2400))):

        touch(Template(r"tpl1655256449928.png", record_pos=(0.002, 1.025), resolution=(1080, 2400)))
        wait(Template(r"tpl1655256483902.png", record_pos=(-0.281, 0.188), resolution=(1080, 2400)))

        touch(Template(r"tpl1655256465925.png", record_pos=(-0.354, 0.392), resolution=(1080, 2400)))
        sleep(20)
        touch(Template(r"tpl1655273716094.png", record_pos=(-0.241, -0.103), resolution=(1080, 2400)))
        sleep(20)
        text("Tuyoo@123")
        sleep(20)
        if exists(Template(r"tpl1659498780436.png", record_pos=(0.426, -0.988), resolution=(1080, 2400))):
            touch(Template(r"tpl1659498780436.png", record_pos=(0.426, -0.988), resolution=(1080, 2400)))
    elif exists(Template(r"tpl1655359988724.png", record_pos=(-0.212, -0.109), resolution=(1080, 2400))):
        sleep(20)               
        touch(Template(r"tpl1655273716094.png", record_pos=(-0.241, -0.103), resolution=(1080, 2400)))
        sleep(20)
        text("Tuyoo@123")
        if exists(Template(r"tpl1659498780436.png", record_pos=(0.426, -0.988), resolution=(1080, 2400))):
            touch(Template(r"tpl1659498780436.png", record_pos=(0.426, -0.988), resolution=(1080, 2400)))

        
        sleep(20)
    if exists(Template(r"tpl1655804546181.png", record_pos=(0.007, 0.249), resolution=(1080, 2408))):
        touch(Template(r"tpl1655804554247.png", record_pos=(-0.003, 0.247), resolution=(1080, 2408)))
        sleep(10)


    



                              
   
    touch(Template(r"tpl1655435660272.png", record_pos=(0.0, 0.944), resolution=(1080, 2400)))

    sleep(10)
    text("284119")
    sleep(10)
    if exists(Template(r"tpl1659499100155.png", record_pos=(0.041, 0.13), resolution=(1080, 2400))):
        touch(Template(r"tpl1659499100155.png", record_pos=(0.041, 0.13), resolution=(1080, 2400)))

    touch(Template(r"tpl1651116160468.png", record_pos=(0.421, -0.985), resolution=(1080, 2400)))    
        
        
def guizuyueka():
    touch(Template(r"tpl1659430416024.png", record_pos=(0.464, -0.08), resolution=(2400, 1080)))
    
    touch(Template(r"tpl1659430450822.png", record_pos=(0.257, -0.082), resolution=(2400, 1080)))
    

def looprest():
    touch(Template(r"tpl1656928606504.png", record_pos=(0.043, -0.2), resolution=(2408, 1080)))
    sleep(5)
    #touch(Template(r"tpl1659430416024.png", record_pos=(0.464, -0.08), resolution=(2400, 1080)))
    #touch(Template(r"tpl1659430582150.png", record_pos=(0.383, -0.083), resolution=(2400, 1080)))
    if exists(Template(r"tpl1659431954114.png", record_pos=(-0.005, -0.163), resolution=(2700, 1228))):
        touch(Template(r"tpl1659424695788.png", record_pos=(0.284, -0.171), resolution=(2400, 1080)))

        #touch(Template(r"tpl1659424719551.png", threshold=0.7499999999999999, record_pos=(0.203, -0.117), resolution=(2400, 1080)))
    
def jijiamohe():
    touch(Template(r"tpl1659430928632.png", record_pos=(0.465, -0.022), resolution=(2400, 1080)))
    touch(Template(r"tpl1659430940760.png", record_pos=(0.255, -0.025), resolution=(2400, 1080)))
    
def guizuyueka():
    touch(Template(r"tpl1659430416024.png", record_pos=(0.464, -0.08), resolution=(2400, 1080)))
    touch(Template(r"tpl1659431326737.png", record_pos=(0.255, -0.084), resolution=(2400, 1080)))

def yuchang():
    if exists(Template(r"tpl1656988160172.png", record_pos=(-0.241, -0.0), resolution=(2700, 1228))):
        touch(Template(r"tpl1656988160172.png", record_pos=(-0.241, -0.0), resolution=(2700, 1228)))
        sleep(10)
    elif exists(Template(r"tpl1657017971616.png", record_pos=(-0.218, -0.001), resolution=(2376, 1080))):
        touch(Template(r"tpl1657017971616.png", record_pos=(-0.218, -0.001), resolution=(2376, 1080)))
        sleep(120)
    if exists(Template(r"tpl1656986985582.png", threshold=0.8500000000000001, record_pos=(0.351, -0.179), resolution=(2700, 1228))):
        touch(Template(r"tpl1656986985582.png", threshold=0.8500000000000001, record_pos=(0.351, -0.179), resolution=(2700, 1228)))
        
        sleep(5)
    touch(Template(r"tpl1659431653259.png", record_pos=(0.471, 0.016), resolution=(2400, 1080)))
    sleep(5)
    if exists(Template(r"tpl1659431954114.png", record_pos=(-0.005, -0.163), resolution=(2700, 1228))):
        touch(Template(r"tpl1659424695788.png", record_pos=(0.284, -0.171), resolution=(2400, 1080)))

    if exists(Template(r"tpl1659424719551.png", threshold=0.75, rgb=True, record_pos=(0.203, -0.117), resolution=(2400, 1080))):
        touch(Template(r"tpl1659424719551.png", threshold=0.7, record_pos=(0.203, -0.117), resolution=(2400, 1080)))

    
def shouchong():
    touch(Template(r"tpl1659430416024.png", record_pos=(0.464, -0.08), resolution=(2400, 1080)))
    if exists(Template(r"tpl1659941092359.png", record_pos=(0.381, -0.084), resolution=(2700, 1228))): 
        touch(Template(r"tpl1659941092359.png", record_pos=(0.381, -0.084), resolution=(2700, 1228)))
        sleep(5)

    #touch(Template(r"tpl1659430582150.png", record_pos=(0.383, -0.083), resolution=(2400, 1080)))
        if exists(Template(r"tpl1659431954114.png", record_pos=(-0.005, -0.163), resolution=(2700, 1228))):
            touch(Template(r"tpl1656924187789.png", record_pos=(0.0, 0.103), resolution=(2700, 1228)))

    