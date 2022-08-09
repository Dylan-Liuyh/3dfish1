# -*- encoding=utf8 -*-
__author__ = "lucia"

from airtest.core.api import *
from airtest.cli.parser import cli_setup


auto_setup(__file__)


from poco.drivers.unity3d import UnityPoco

import sys
root_path = os.path.abspath(__file__)
root_path = '/'.join(root_path.split('/')[:-3])
sys.path.append(root_path)
from common.common_func import *


#翅膀属性遍历
def travers_wing_attribute():
    #翅膀效果
    if poco('detail').offspring('Content').child().exists():
        for item in poco('detail').offspring('Content').child():
            item.click()
    #翅膀特性
    if poco('speciality').offspring('Content').child().exists():
        for item in poco('speciality').offspring('Content').child():
            item.click()
            
    #获取、装备、卸载
    if poco('brnQuiStart').exists():
        poco('brnQuiStart').click()
        if poco('anchor').child('frame').exists():
            poco('btnOk').click()
        
        
        
#遍历翅膀
def travers_wing():
    
    #选择翅膀
    poco('tabs').child('wing').click()
    
    #遍历翅膀
    for num in range(0,len(poco('Content').child(name='item_wing'))):
        wing=poco('Content').child(name='item_wing')[num]
        pos=wing.attr('pos')
        if pos[1]>0.7:
            wing.swipe([0,-0.2])
        wing.click()
        travers_wing_attribute()
        if num>3:
            break
    
def test_wing():
    #判断炮台icon是否存在
    if poco('bubble').exists():
        #点击进入炮台
        poco('bubble').parent().click()
        travers_wing()
        poco('btnClose').click()
        
    else:
        print('jjjjj未找到炮台jjjjj')




if __name__=='__main__':
    try:
        common_try_to_go_to_hall()
        poco=UnityPoco()
        poco.use_render_resolution()
        test_wing()
    except AssertionError as msg:
        raise msg
