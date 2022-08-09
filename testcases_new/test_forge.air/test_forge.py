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


#锻造
def test_duanzao():
    
    #选择翅膀
    poco('tabs').child('forge').click()
    
    #小于10000倍
    if poco('anchor').child('frame').exists():
        poco('btnOK').click()

    
    


def test_forge():
    #判断炮台icon是否存在
    if poco('bubble').exists():
        #点击进入炮台
        poco('bubble').parent().click()
        test_duanzao()
        poco('btnClose').click()
        
    else:
        print('jjjjj未找到炮台jjjjj')




if __name__=='__main__':
    try:
        common_try_to_go_to_hall()
        poco=UnityPoco()
        poco.use_render_resolution()
        test_forge()
    except AssertionError as msg:
        raise msg
