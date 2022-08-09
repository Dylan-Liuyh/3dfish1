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



#遍历机甲神器
def travers_jijia():
    #机甲神器存在
    if poco('tab_jijia').exists():
        poco('tab_jijia').click()
        for item in poco('artifact_jijia').child('models').child(type='Node'):
            item.click()
            poco(texture="artifact_desc").click()
            poco('artifact_jijia_rule').wait_for_appearance()
            poco('artifact_jijia_rule').child('ScrollView').swipe([0,-0.4])
            poco('artifact_jijia_rule').child('btnDescClose').click()
            poco('artifact_jijia').offspring('btnUse').click()
            poco('artifact_jijia_source').offspring('btnClose').click()
            poco('artifact_jijia').offspring('backDetailBtn').click()
            poco('artifact_jijia').offspring('backSimpleBtn').click()       
    else:
        print('机甲神器不存在')

#遍历星甲神器
def travers_xingjia():
    #存在星甲神器
    if poco('tab_xingjia').exists():
        poco('tab_xingjia').click()
        name_list=['xingjia_shizi','xingjia_juxie','xingjia_shuangzi','xingjia_jinniu','xingjia_baiyang']
        for item in name_list:
            poco('artifact_xingjia').offspring('btnPreview').click()
            i=0
            while(i<10):
                poco('artifact_xingjia').offspring('btnNext').click()
                i=i+1
            poco('artifact_xingjia').offspring('btnQuitView').click()
            poco('artifact_xingjia').offspring(item).swipe([0.1,0])
        if poco('artifact_xingjia').offspring('btnShowRule').exists():
            poco('artifact_xingjia').offspring('btnShowRule').click()
            poco('artifact_xingjia_rule').wait_for_appearance()
            poco('artifact_xingjia_rule').child('btnClose').click()
    else:
        print('星甲神器不存在')
            
#遍历山海神器
def travers_shanhai():
    #存在山海神器
    if poco('tab_shanhai').exists():
        poco('tab_shanhai').click()
        for item in poco('artifact_shanhai').child('models').child(type='Node'):
            item.click()
            poco('btnDesc').click()
            poco('artifact_shanhai_rule').wait_for_appearance()
            poco('artifact_shanhai_rule').child('ScrollView').swipe([0,-0.4])
            poco('artifact_shanhai_rule').child('btnDescClose').click()
    else:
        print('山海神器不存在')
    
def test_artifact():
    #神器icon存在
    if poco(texture="lobby_btn_artifact").exists():
        poco(texture="lobby_btn_artifact").click()
        travers_jijia()
        travers_xingjia()
        travers_shanhai()
        poco('btnClose').click()
    else:
        print('神器不存在大厅')
        





if __name__=='__main__':
    try:
        common_try_to_go_to_hall()
        poco=UnityPoco()
        poco.use_render_resolution()
        test_artifact()
    except AssertionError as msg:
        raise msg
