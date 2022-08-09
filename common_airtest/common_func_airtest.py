import io
import os.path
import jinja2

from airtest.core.api import *
from airtest.report.report import LogToHtml
from airtest.utils.compat import script_dir_name
from poco.drivers.unity3d import UnityPoco
from airtest.core.android import Android
#PACKAGE_NAME_LIST=["com.tuyoo.fish3d.mi","com.tuyoo.fish3d.huawei","com.tuyoo.fish3d.vivo","com.tuyoo.fish3d.nearme.gamecenter"]
#android=Android()
#appPackageList = android.list_app(third_only=True)



def package_name_confirm(PACKAGE_NAME_LIST,appPackageList):
    
    PACKAGE_NAME="hyper"
    for i in range(0,len(PACKAGE_NAME_LIST)):
        if PACKAGE_NAME_LIST[i] in appPackageList:
            PACKAGE_NAME=PACKAGE_NAME_LIST[i]
    return PACKAGE_NAME




def login():
    #pcg_name=package_name_confirm(PACKAGE_NAME_LIST,appPackageList)
    start_app("com.tuyoo.fish3d.vivo")
    sleep(5)
    if exists(Template(r"tpl1657682711174.png", record_pos=(0.001, 0.143), resolution=(2408, 1080))):
        touch(Template(r"tpl1657682719542.png", record_pos=(0.375, -0.164), resolution=(2408, 1080)))
    sleep(5)

    if exists(Template(r"tpl1657529632300.png", record_pos=(0.007, 0.106), resolution=(2408, 1080))):
        touch(Template(r"tpl1657529632300.png", record_pos=(0.007, 0.106), resolution=(2408, 1080)))
    sleep(5)
    if exists(Template(r"tpl1657677672212.png", record_pos=(-0.107, 0.114), resolution=(2400, 1080))):
        touch(Template(r"tpl1657677680308.png", record_pos=(0.375, -0.164), resolution=(2400, 1080)))


    wait(Template(r"tpl1657008129356.png", record_pos=(0.019, -0.007), resolution=(2700, 1228)),timeout=300)
    #sleep(120)
    if exists(Template(r"tpl1657008129356.png", record_pos=(0.019, -0.007), resolution=(2700, 1228))):
        touch(Template(r"tpl1657008142126.png", record_pos=(0.111, 0.085), resolution=(2700, 1228)))
        sleep(10)

    if exists(Template(r"tpl1657008169585.png", record_pos=(-0.139, 0.163), resolution=(2700, 1228))):
        touch(Template(r"tpl1657008169585.png", record_pos=(-0.139, 0.163), resolution=(2700, 1228)))
        sleep(5)

    touch(Template(r"tpl1657006894699.png", record_pos=(0.016, 0.115), resolution=(2700, 1228)))
    sleep(5)
    while True:
        if exists(Template(r"tpl1657338200511.png", record_pos=(0.021, -0.013), resolution=(2400, 1080))):
            touch(Template(r"tpl1657338216870.png", record_pos=(0.022, 0.039), resolution=(2400, 1080)))
            sleep(2)
            touch(Template(r"tpl1657008169585.png", record_pos=(-0.139, 0.163), resolution=(2700, 1228)))
            sleep(5)

            touch(Template(r"tpl1657006894699.png", record_pos=(0.016, 0.115), resolution=(2700, 1228)))
        else:
            break
    
    
    
    sleep(300)
    if exists(Template(r"tpl1657505284632.png", threshold=0.8500000000000001, record_pos=(-0.433, -0.112), resolution=(2400, 1080))):
            touch(Template(r"tpl1657505284632.png", record_pos=(-0.433, -0.112), resolution=(2400, 1080)))
            sleep(2)
            touch(Template(r"tpl1657505335924.png", record_pos=(-0.302, -0.111), resolution=(2400, 1080)))
            sleep(2)
            touch(Template(r"tpl1657505358422.png", record_pos=(-0.055, 0.04), resolution=(2400, 1080)))
            sleep(200)
    popwindows()        
    sleep(10)
    
    
    
def popwindows():   
    while True:
               
        if exists(Template(r"tpl1657010528094.png", threshold=0.8500000000000001, record_pos=(0.057, 0.165), resolution=(2376, 1080))):
            touch(Template(r"tpl1657010534589.png", record_pos=(0.293, -0.161), resolution=(2376, 1080)))
            sleep(10)
            continue
        elif exists(Template(r"tpl1657165822001.png", record_pos=(0.022, -0.147), resolution=(2400, 1080))):
            touch(Template(r"tpl1657165831936.png", record_pos=(0.02, 0.092), resolution=(2400, 1080)))
            sleep(10)
            continue
        elif exists(Template(r"tpl1657010554679.png", record_pos=(0.034, -0.17), resolution=(2376, 1080))):
            touch(Template(r"tpl1657010575407.png", record_pos=(0.346, -0.173), resolution=(2376, 1080)))
            sleep(10)
            continue
            
        #touch(Template(r"tpl1657091216177.png", record_pos=(-0.378, -0.181), resolution=(2376, 1080)))
    
        elif exists(Template(r"tpl1657091172760.png", record_pos=(0.357, 0.167), resolution=(2376, 1080))):
            touch(Template(r"tpl1657010669226.png", record_pos=(0.024, 0.203), resolution=(2376, 1080)))
            sleep(10)
            continue
        elif exists(Template(r"tpl1657089414581.png", record_pos=(-0.02, -0.169), resolution=(2700, 1228))):
            touch(Template(r"tpl1656986985582.png", record_pos=(0.351, -0.179), resolution=(2700, 1228)))
            sleep(10)
            continue
        elif exists(Template(r"tpl1657089790735.png", record_pos=(0.023, -0.195), resolution=(2700, 1228))):
            touch(Template(r"tpl1657010622111.png", record_pos=(0.343, -0.184), resolution=(2376, 1080)))
            sleep(10)
            continue
        elif exists(Template(r"tpl1657093351712.png", record_pos=(0.022, 0.085), resolution=(2376, 1080))):
            touch(Template(r"tpl1657093351712.png", record_pos=(0.022, 0.085), resolution=(2376, 1080)))
            sleep(10)
            continue
            
        elif exists(Template(r"tpl1657272900561.png", record_pos=(-0.058, -0.182), resolution=(2400, 1080))):
            touch(Template(r"tpl1657010622111.png", record_pos=(0.343, -0.184), resolution=(2376, 1080)))     
            sleep(10)
            continue
        
        elif exists(Template(r"tpl1657354939110.png", record_pos=(0.02, -0.193), resolution=(2376, 1152))):
            touch(Template(r"tpl1657010534589.png", record_pos=(0.293, -0.161), resolution=(2376, 1080)))
            sleep(10)
            continue
     
    

        else:
            break