# -*- encoding=utf8 -*-
__author__ = "Lucia"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

auto_setup(__file__)


from poco.drivers.unity3d import UnityPoco

root_path = os.path.abspath(__file__)
root_path = '/'.join(root_path.split('/')[:-3])
sys.path.append(root_path)
from common.common_func import *




#前两个房间,需要第三个房间向右滑动
room_right_swipe=['room_28002','room_28003']

#最后一个房间，需要第四个房间向左滑动
room_left_swipe=['room_28008']
                 
#第三个房间
room_three='room_28005'
                 
#第四个房间
room_four='room_28007'                 

"""#第一个房间进入游戏画面
def test_first(room_id):
    #判定展示房间
    show_room=''
    for room in room_id:
        pos=poco(room).attr('pos')
        if pos[0]>0.2:
            show_room=room
            break
    #滑动已展示房间，使第一个房间进入游戏画面
    print(show_room)
    poco(show_room).swipe([0.4,0])"""
    
#循环下载渔场
def test_downloading(room):
    if room in room_right_swipe:
        poco(room_three).swipe([0.4,0])
    elif room in room_left_swipe:
        poco(room_four).swipe([-0.2,0])
    #房间未下载，下载房间并进入渔场
    if poco(room).child('download_waiting').exists():
        poco(room).offspring('download').click()
        poco(room).offspring('waiting').wait_for_disappearance(timeout=600)
        poco('loading').wait_for_disappearance(timeout=600)
        poco('btnShowMenu').click()
        poco('btnLeave').click()
        poco("btnOK").click()
        if poco('loading').exists():
            poco('loading').wait_for_disappearance(timeout=600)
        common_close_popups_one_by_one_if_need()
    

#渔场下载
def test_yuchang_download():
    #获取渔场房间名字
    room_id=[]
    for yuchang in poco('lobby_mode_new').offspring('Content').child(type='Node'):
        room_id.append(yuchang.get_name())
    room_id.append('room_28009')
    for room in room_id:
        test_downloading(room)
    
    
    


if __name__=='__main__':
    try:
        common_try_to_go_to_hall()
        poco=UnityPoco()
        poco.use_render_resolution()
        test_yuchang_download()
    except AssertionError as msg:
        raise msg