# -*- encoding=utf8 -*-
import io
import os.path
import jinja2
import json
import os,sys
import subprocess

from airtest.core.api import *
from airtest.report.report import LogToHtml
from airtest.utils.compat import script_dir_name


auto_setup(__file__)

from poco.drivers.unity3d import UnityPoco
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.android import *

    
root_path = os.path.abspath(__file__)
root_path = '/'.join(root_path.split('/')[:-1])
login_path=root_path+'/'+'login.json'

airtools_path='/'.join(root_path.split('/')[:-1])+'/airtools-0.0.17-py39-mac/airtools'


PACKAGE_NAME = "com.tuyoo.fish3d.official"
CHANGE_SERVER="com.tuyoo.fish3d.fishlauncher"

#android=Android()

def common_click_by_node_name(obj, wait_time=0):
    try:
        for item in obj:
            item.click()
            if wait_time > 0:
                sleep(wait_time)
    except:
        print("Exception!!! common_func common_click_by_node_name:%s" % obj)


def common_click_by_image_name(poco, name, wait_time=0, area=[0.5, 0.5]):
    try:
        for item in poco(texture=name):
            item.click(area)
            if wait_time > 0:
                sleep(wait_time)
    except:
        print("Exception!!! common_func common_click_by_image_name:%s" % name)


def common_click_by_obj(obj, tip="", wait_time=0.5):
    assert_equal(obj.exists(), True, tip or "")
    obj.click()
    sleep(wait_time)


def common_click_by_text_content(poco, text_content, wait_time=0):
    try:
        for item in poco(text=text_content):
            item.click()
            if wait_time > 0:
                sleep(wait_time)
    except:
        print("Exception!!! common_func common_click_by_text_content:%s" % text_content)


def common_exists_by_obj(obj):
    return obj.exists()

#仿真服重新打开捕鱼app
def common_restart_app():
    print("aaabbb_common_restart_app")
    sleep(5)
    #stop_app(PACKAGE_NAME)
    sleep(5)
    start_app(PACKAGE_NAME)
    #待优化睡眠时长
    sleep(20)
    
#切线上服打开捕鱼app
def online_restart_app():
    print('jjjjj线上服打开捕鱼')
    start_app(CHANGE_SERVER)
    sleep(5)
    touch(Template(r"tpl1658201562276.png", record_pos=(0.207, -0.566), resolution=(1080, 2376)))
    touch(Template(r"tpl1658201572521.png", record_pos=(-0.406, -0.145), resolution=(1080, 2376)))
    sleep(20)

    
#线上服登录
def online_login():
    poco=UnityPoco()
    while True:
        if poco('Title',text='网络异常').exists():
            poco('BtnGreen').click()
        else:
            break
    sleep(5)
    if exists(Template(r"tpl1658201835865.png", record_pos=(-0.002, -0.101), resolution=(2376, 1080))):
        touch(Template(r"tpl1658201854332.png", record_pos=(0.003, 0.054), resolution=(2376, 1080)))
    if exists(Template(r"tpl1658201935379.png", record_pos=(-0.138, 0.149), resolution=(2376, 1080))):
        touch(Template(r"tpl1658201952993.png", record_pos=(-0.138, 0.149), resolution=(2376, 1080)))




    
#实名认证
def real_name():
    sleep(20)
    name="袁冠鹏"
    identification='420528198302174734'
    poco=UnityPoco()
    poco.use_render_resolution()
    #老实名认证
    if poco('certification').exists():
        print('老实名认证存在')
        poco('name').click()
        text(name)
        poco("ID").click()
        poco("ID").click()
        text(identification)
        poco("ID").click()
        poco("Button (1)").click()
        if poco('message_box').exists():
            poco('message_box').offspring('btnOK').click()
            poco('name').click()
            text(name)
            poco("ID").click()
            poco("Button (1)").click()
    #新实名认证
    if poco('certificationNew').exists():
        print('新实名认证存在')
        poco('NameInput').click()
        text(name)
        poco('IDInput').click()
        poco('IDInput').click()
        text(identification)
        poco('IDInput').click()
        poco('SubmitButton').click()
        if poco('message_box').exists():
            poco('message_box').offspring('btnOK').click()
            poco('NameInput').click()
            text(name)
            poco('IDInput').click()
            poco('SubmitButton').click()
            
    #绑定手机号存在
    if poco('certification').exists():
        poco('certification').child('anchor').child('Button').click()
                 
    if poco('btnShowMenu').exists():
        poco("btnShowMenu").click()
        poco("btnLeave").click()
        poco("btnOK").click()
        if poco('loading').exists():
            print('loading')
            poco('loading').wait_for_disappearance(timeout=600)
            log('返回大厅')
#读取登录账号密码            
def read_account():
    with open(login_path,'r') as f:
        account_data=json.load(f)
    return account_data

#获取设备的device_id
def get_device_id():
    x = os.popen("adb devices").readlines()
    print(x)
    log(x)
    if len(x) == 3:
        devices = x[1].split('\t')[0]
        log(devices)
        return devices

#仿真服隐私协议&实名认证
def common_test_nameid_login():
    
    print('jjj nameid_login')
    if exists(Template(r"tpl1659607241129.png", record_pos=(0.023, 0.083), resolution=(2376, 1080))):
        print('识别到隐私保护提示')
        sleep(5)
        flag=common_test_poco_is_connect()
        if flag:
            poco = UnityPoco()
            poco.use_render_resolution()
            poco("agreebtn").click()
        else:
            print('poco初始化失败')
            common_restart_app_and_go_to_hall_anyway()
        #同意隐私协议

    sleep(5)
    '''
    poco.use_render_resolution()
    if poco('loginNew').child('loginView').child('signUp').offspring('loginTypes').offspring('login').exists():
        poco('loginNew').child('loginView').child('signUp').offspring('loginTypes').offspring('login').click()
    if poco(text='密码登录').exists():
        print('new login exist')
    else:
        print('error error error !!! new login not exist!!!!!!!!!!!!!!!')
    #新登录判定'''
    #if exists(Template(r"tpl1659520122223.png", record_pos=(0.024, 0.091), resolution=(2376, 1080))):
        #touch(Template(r"tpl1659520151144.png", record_pos=(0.022, 0.092), resolution=(2376, 1080)))

    #if exists(Template(r"tpl1658225484070.png", record_pos=(-0.143, 0.147), resolution=(2400, 1080))):
        #touch(Template(r"tpl1658225493171.png", record_pos=(-0.145, 0.146), resolution=(2400, 1080)))

    
    poco=UnityPoco()
    poco.use_render_resolution()
    if poco("guest").exists():
        poco("guest").click()
        log('快速开始')
            
    #开始游戏
    log('开始游戏')
    if poco('btnPlay').exists():
        poco("btnPlay").click()
        if poco('loading').exists():
            print('loading')
            poco('loading').wait_for_disappearance(timeout=600)
            
    real_name()
    
def common_test_poco_is_connect():
    print("test_poco_is_connect")
    poco=UnityPoco()
    poco.use_render_resolution()
    try:
        poco("Main Camera").exists()
        return True
    except:
        return False

def common_restart_app_and_go_to_hall_anyway():
    print("common_restart_app_and_go_to_hall_anyway")
    common_restart_app()
    common_test_nameid_login()
    common_try_to_go_to_hall()


def common_try_to_go_to_hall():
    print("try_to_go_to_hall")
    is_poco_ok = common_test_poco_is_connect()
    if not is_poco_ok:
        log('无poco')
        # poco没法链接说明游戏还没有启动，重启app然后尝试进入大厅
        print("aaabbb_common_try_to_go_to_hall is_poco_ok:False")
        common_restart_app_and_go_to_hall_anyway()
        return
    print("try_to_go_to_hall is_poco_ok:True")
    real_name()
    poco=UnityPoco()
    poco.use_render_resolution()
    
    try:
        poco('main_canvas').child('UI').wait_for_appearance(timeout=120)
        if poco('main_canvas').child('UI').exists() :
            common_close_popups_one_by_one_if_need()
            log('返回大厅成功')
    except:
        print('返回大厅失败')
        # 最后还是没有回到大厅，只能重启应用
        if poco('main_canvas').child('UI').exists()==False:
            print("common_try_to_go_to_hall Main Camera still not avaliable, restart the app!!!!!")
            common_restart_app_and_go_to_hall_anyway()
            log('返回大厅失败')







def anyway_login():  # 多种方式登录

    print("jjjjjj_common_login")
    sleep(1)
    poco = UnityPoco()
    poco.use_render_resolution()
    poco("wechat").click()
    from poco.drivers.android.uiautomation import AndroidUiautomationPoco
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
    poco(text="请填写微信号/QQ号/邮箱").click()
    shell("input text '15011268475'")
    poco(text="请填写密码").click()
    shell("input text 'Tuyoo@123'")
    poco("com.tencent.mm:id/eh").click()  # 关闭微信
    poco = UnityPoco()
    sleep(5.0)
    poco("ui_popup").offspring("mobile").child("Text").click()
    # common_click_by_text_content(poco, ("ui_popup").offspring("mobile").child("Text").wait_time=0)
    shell("input text '17640509447'")
    # common_click_by_text_content(poco, (text='请输入密码').wait_time=0)
    poco(text="请输入密码").click()
    shell("input text 'lyh970707970707'")
    poco = UnityPoco()
    sleep(5)
    poco("title").click()
    # poco("title").click()
    poco("loginBtn").click()
    # poco("loginBtn").click()
    poco("btnOther").click()
    # poco("btnOther").click()
    poco("loginBtn").click()
    # poco("loginBtn").click()
    sleep(2.0)
    poco("logout").click()
    poco("guest").click()
    poco("btnPlay").click()




def common_close_popups_one_by_one_if_need():
    print("jjjjjj_common_close_popups_one_by_one_if_need")
    # 这里从节点名称穷举，节点图片名称穷举，以及类似段位赛季结束弹窗等全屏UI的特殊处理，来实现进入大厅后将弹窗关闭
    sleep(10)
    while True:
        poco=UnityPoco()
        poco.use_render_resolution()
            
        #概率公示
        if poco('ui_popup').child('Canvas').child('notice').exists():
            poco('ui_popup').child('Canvas').child('notice').offspring('btnClose').click()
            print('关闭概率公式弹窗')
            
        #三日惊喜
        if poco('ui_popup').offspring('3day_gift').exists():
            poco('ui_popup').offspring('3day_gift').offspring('btnClose').click()
            print('关闭三日惊喜弹窗')
            
        #签到
        if poco('ui_popup').offspring('sign_in').exists():
            poco('ui_popup').offspring('sign_in').offspring('btnClose').click()
            sleep(4)
            poco('ui_popup').offspring('sign_in').offspring('btnClose').click()
            print('关闭签到弹窗')
            
        #新赛季热卖
        if poco('ui_popup').offspring('main_season_journeytothewest').exists():
            poco('ui_popup').offspring('main_season_journeytothewest').offspring('btnClose').click()
            print('关闭新赛季热卖弹窗')
            
            
        #超时空魔盒、赛季热卖、支付宝一分购
        if poco('ui_popup').child('Canvas').child('main').exists():
            if poco('ui_popup').child('Canvas').child('main').offspring('btnClose').exists():
                poco('ui_popup').child('Canvas').child('main').offspring('btnClose').click()
                print('关闭超时空魔盒或赛季热卖弹窗')
            elif poco('ui_popup').child('Canvas').child('main').offspring('Close').exists():
                poco('ui_popup').child('Canvas').child('main').offspring('Close').click()
                print('关闭支付宝一分购弹窗')

        #赛季补给
        if poco('ui_popup').offspring('season_new_open').exists():
            poco('ui_popup').offspring('season_new_open').offspring('btnGo').wait_for_appearance(60)
            poco('ui_popup').offspring('season_new_open').offspring('btnGo').click()
            #关闭提示活动快结束弹窗
            if poco('message_box').exists():
                poco('message_box').offspring('btnOK').click()
            if poco('ui_popup').offspring('season_new').exists():
                poco('ui_popup').offspring('season_new').offspring('btnOK').click()
            if poco('ui_popup').offspring('main').exists():
                poco('ui_popup').offspring('main').offspring('btnClose').click()
        #活动
        if poco('ui_popup').offspring('activity').exists():
            poco('ui_popup').offspring('activity').offspring('btnClose').click()
            print('关闭精彩活动弹窗')
        
        #超级大转盘
        if poco("dole_main").offspring("title").exists():
            poco("dole_main").offspring("btnClose").click()
            print('关闭超级大转盘弹窗')
        #狮子赠礼
        if poco('ui_popup').offspring('update_gift_main').exists():
            poco('ui_popup').offspring('update_gift_main').offspring('btnClose').click()
            print('关闭狮子赠礼弹窗')
        
        #成就
        if poco('ui_popup').offspring('achievement_main').exists():
            poco('ui_popup').offspring('achievement_main').offspring('Button').click()
            print('关闭成就弹窗')
        #月卡
        if poco('ui_popup').offspring('month_card').exists():
            poco('ui_popup').offspring('month_card').offspring('close').click()
            print('关闭月卡弹窗')
            
        #七夕筑梦
        if poco('ui_popup').child('Canvas').child('seven_dream_face').exists():
            poco('ui_popup').child('Canvas').child('seven_dream_face').offspring('btnClose').click()
            print('关闭七夕筑梦弹窗')
            
        #神器降临
        if poco('ui_popup').child('Canvas').child('artifact_coming_face').exists():
            poco('ui_popup').child('Canvas').child('artifact_coming_face').offspring('btnClose').click()
            
        #左右滑动
        if poco('ui_popup').offspring('lobby_mode_tips').exists():
            poco('ui_popup').offspring('lobby_mode_tips').offspring('btnOk').click()
            print('关闭左右滑动弹窗')
            
            
        if len(poco('ui_popup').child('Canvas').child())==1:
            print('jjjjj弹窗关闭完')
            sleep(1)
            break

            
            
#点击大厅图标
"""
Scroll_node:leftDockScroll表示大厅左侧图标
            rightDockScrollpoco("rightNext01")表示大厅右侧图标
icon_node:图标名字
"""

def click_icon(Scroll_node,icon_node):
    poco=UnityPoco()
    poco.use_render_resolution()
    #判断左右下滑按钮名称
    if Scroll_node is 'leftDockScroll':
        icon_name='leftBtnDown'
    else:
        icon_name='rightBtnDown'
    #下滑按钮存在
    if poco(Scroll_node).offspring(icon_node).exists()==False:
        print('大厅不存在此icon')
    elif poco(Scroll_node).child(icon_name).exists():
        while True:
            pos=poco(Scroll_node).offspring(icon_node).attr('pos')
            #隐藏，点击下滑
            if pos[1]>0.7:
                poco(Scroll_node).child(icon_name).click()
            else:
                poco(Scroll_node).offspring(icon_node).click()
                break
    else:
        poco(Scroll_node).offspring(icon_node).click()

        

#初始化大厅图标
"""
Scroll_node:leftDockScroll表示大厅左侧图标
            rightDockScroll表示大厅右侧图标
"""     
def init_icon(Scroll_node):
    poco=UnityPoco()
    poco.use_render_resolution()
    #判断左右下滑按钮名称
    if Scroll_node is 'leftDockScroll':
        icon_name='leftBtnUp'
    else:
        icon_name='rightBtnUp'
    #上滑按钮存在
    while True:
        if poco(Scroll_node).child(icon_name).exists():
            poco(Scroll_node).child(icon_name).click()
        else:
            print('左右侧导航栏按钮初始化完毕')
            break
            
def payment():
    sleep(10)
    start_app(PACKAGE_NAME)
    sleep(10)
    if exists(Template(r"tpl1659596409731.png", record_pos=(-0.005, -0.037), resolution=(2376, 1080))):
        touch(Template(r"tpl1659596432920.png", record_pos=(-0.025, -0.037), resolution=(2376, 1080)))
        list_zfb=[Template(r"zfb1.png"),Template(r"zfb2.png"),Template(r"zfb3.png"),Template(r"zfb4.png")]
        for pic_zfb in list_zfb:
            pos=exists(pic_zfb)
            if pos:
                stop_app('com.eg.android.AlipayGphone')

      
    touch(Template(r"tpl1658299726004.png", record_pos=(0.293, -0.134), resolution=(2376, 1080)))
        
        
def payment_zfb():
    sleep(10)
    start_app(PACKAGE_NAME)
    sleep(10)
    if exists(Template(r"tpl1659084430600.png", record_pos=(0.079, -0.039), resolution=(2376, 1080))):
        touch(Template(r"tpl1659084448829.png", record_pos=(0.081, -0.035), resolution=(2376, 1080)))
        sleep(10)        
        if exists(Template(r"tpl1659341541692.png", record_pos=(0.006, 0.224), resolution=(1080, 2400))):
            touch(Template(r"tpl1659341550974.png", record_pos=(0.193, 0.235), resolution=(1080, 2400)))
            sleep(5)
       
        """if exists(Template(r"tpl1659341593723.png", record_pos=(0.0, 0.727), resolution=(1080, 2400))):
            print('刷脸登录')
            touch(Template(r"tpl1659341602297.png", record_pos=(0.006, 0.983), resolution=(1080, 2400)))
            touch(Template(r"tpl1659341609706.png", record_pos=(-0.16, 0.358), resolution=(1080, 2400)))
            sleep(5)"""



        
        if exists(Template(r"tpl1659319972103.png", record_pos=(-0.222, -0.138), resolution=(1080, 2400))):
            touch(Template(r"tpl1659319995335.png", record_pos=(-0.217, -0.14), resolution=(1080, 2400)))
            sleep(5)
            text("Tuyoo@123")
            sleep(5)
        if exists(Template(r"tpl1659320090665.png", record_pos=(0.002, 0.933), resolution=(1080, 2400))):
            touch(Template(r"tpl1659320101609.png", record_pos=(-0.002, 0.933), resolution=(1080, 2400)))
            sleep(5)
            text("284119")
            sleep(5)
            
        if exists(Template(r"tpl1659344455338.png", record_pos=(-0.001, 0.833), resolution=(1080, 2400))):
            touch(Template(r"tpl1659344467824.png", record_pos=(-0.001, 0.832), resolution=(1080, 2400)))

      

        
        


        

#精彩活动tab选择
"""
  Toggle：toggleActivity表示选择活动页面
          toggleNotice表示选择公告页面
  tab_text:活动tab的text文本
"""
def activity_click(Toggle,tab_text):
    flag=0
    list_text=[]
    poco=UnityPoco()
    poco.use_render_resolution()
    poco(Toggle).click()
    for text_item in poco('list').offspring('Content').offspring(type='TMPROUGUI'):
        list_text.append(text_item.get_text())
    if tab_text in list_text:
        for item in poco('list').offspring('Content').child(type='Toggle'):
            if item.offspring('Label1').attr('text') == tab_text:
                item.click()
                flag=1
                break
            else:
                pos=item.attr('pos')
                if pos[1]>0.8:
                    item.swipe([0,-0.3])
    else:
        print('无此活动')
    return flag
                   
    




