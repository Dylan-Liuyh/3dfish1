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

#炮台属性遍历
def travers_cannon_attribute():
    #获取按钮
    if poco('btnEquip').exists():
        poco('btnEquip').click()
        if poco('pop_get_material').offspring('btnClose').exists():
            poco('pop_get_material').offspring('btnClose').click()
    #炮台效果
    if poco('detail').offspring('Content').child().exists():
        for item in poco('detail').offspring('Content').child():
            item.click()
    #炮台特性
    if poco('speciality').offspring('Content').child().exists():
        for item in poco('speciality').offspring('Content').child():
            item.click()
    #炮台星级
    if poco('level').offspring('btnAdd').exists():
        poco('level').offspring('btnAdd').click()
        poco("anchor").offspring("btnClose").click()

            
    '''#前往poco("btnClose")
    if poco('btn',text='前往').exists():
        poco('btn',text='前往').click()'''



#遍历炮台
def travers_cannon():
    
    #选择炮台
    poco('tabs').child('cannon').click()
    
    #遍历已解锁炮台
    for num in range(0,len(poco('unlocked').child(name='item_cannon'))):
        cannon=poco('unlocked').child(name='item_cannon')[num]
        pos=cannon.attr('pos')
        if pos[1]>0.6:
            cannon.swipe([0,-0.2])
        cannon.click()
        travers_cannon_attribute()
    
    #遍历未解锁炮台
    for num in range(0,len(poco('locked').child(name='item_cannon'))):
        cannon=poco('locked').child(name='item_cannon')[num]
        pos=cannon.attr('pos')
        if pos[1]>0.6:
            cannon.swipe([0,-0.2])
        cannon.click()
        travers_cannon_attribute()
        print(num)
        if num>3:
            break

    
    #规则说明
    if poco('cannon').offspring('btnRule').exists():
        poco('cannon').offspring('btnRule').click()
        poco('cannon').offspring('btnClose').click()
    #设置
    if poco('cannon').offspring('btnSetting').exists():
        poco('cannon').offspring('btnSetting').click()
        poco(text="获得新炮台时自动装备新炮台").click()
        poco(text="获得新翅膀时自动装备新翅膀").click()
        poco(text="确定").click()
    
    


def test_battery():
    #判断炮台icon是否存在
    if poco('bubble').exists():
        #点击进入炮台
        poco('bubble').parent().click()
        travers_cannon()
        poco('btnClose').click()
        
    else:
        print('jjjjj未找到炮台jjjjj')




if __name__=='__main__':
    try:
        common_try_to_go_to_hall()
        poco=UnityPoco()
        poco.use_render_resolution()
        test_battery()
    except AssertionError as msg:
        raise msg



