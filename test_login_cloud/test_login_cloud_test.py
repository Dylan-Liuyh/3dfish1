# -*- encoding=utf8 -*-
__author__ = "Dylan"
import sys
import os
import codecs
import traceback
from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
from airtest.report.report import simple_report
from airtest.core.android.recorder import *
from airtest.core.android.adb import *

sys.path.append(os.path.abspath(__file__))
root_path = os.path.abspath(__file__)
root_path = "/".join(root_path.split("/")[:-3])
sys.path.append(root_path)
from common.common_func import *

"""
adb = ADB(serialno="86cbd937")
recorder = Recorder(adb)
# 开启录屏
#recorder.start_recording(max_time=600)#云测注掉
"""


class Testpack:
    def __init__(self):
        super().__init__()

    def app_start():
        clear_app("com.tencent.mm")  # 清除微信数据
        clear_app("com.tuyoo.fish3d.official")  # 清除3D捕鱼大作战的全部数据
        start_app("com.tuyoo.fish3d.official") #打开3D捕鱼大作战

    app_start()

    def yinsixieyi_exist():
        wait(
            Template(
                r"tpl1655110166871.png",
                record_pos=(0.013, -0.006),
                resolution=(1600, 720),
            )
        )
#等待隐私协议弹窗出现
    yinsixieyi_exist()
    from poco.drivers.unity3d import UnityPoco

    def test_privacy_agreement():
        poco = UnityPoco()
        common_click_by_node_name(poco("agreebtn"))#同意隐私协议

    # 同意隐私协议
    test_privacy_agreement()
    poco = UnityPoco()
    poco("wechat").click([1, 0.5])#点击使用微信登录
    from poco.drivers.android.uiautomation import AndroidUiautomationPoco

    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
    android_poco = AndroidUiautomationPoco

    def weixin_login():
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco

        poco = AndroidUiautomationPoco(
            use_airtest_input=True, screenshot_each_action=False
        )
        android_poco = AndroidUiautomationPoco
        poco(text="请填写微信号/QQ号/邮箱").click()
        shell("input text '15011268475'")
        poco(text="请填写密码").click()
        shell("input text 'Tuyoo@123'")
        poco("com.tencent.mm:id/fz").click()  # 关闭微信界面

    weixin_login()
    from poco.drivers.unity3d import UnityPoco

    poco = UnityPoco()
    sleep(5.0)

    def phone_login():
        from poco.drivers.unity3d import UnityPoco

        poco = UnityPoco()
        poco("ui_popup").offspring("mobile").child("Text").click()
        # common_click_by_text_content(poco, ("ui_popup").offspring("mobile").child("Text").wait_time=0)
        shell("input text '17640509447'")
        # common_click_by_text_content(poco, (text='请输入密码').wait_time=0)
        poco(text="请输入密码").click()
        shell("input text 'lyh970707970707'")
        common_click_by_node_name(poco("title"))
        # poco("title").click()
        common_click_by_node_name(poco("loginBtn"))
        # poco("loginBtn").click()
        common_click_by_node_name(poco("btnOther"))
        # poco("btnOther").click()
        common_exists_by_obj
        (
            Template(
                r"tpl1655899426770.png",
                record_pos=(-0.008, -0.151),
                resolution=(2400, 1080),
            )
        )

    phone_login()
    from poco.drivers.unity3d import UnityPoco

    poco = UnityPoco()
    common_click_by_node_name(poco("loginBtn"))
    # poco("loginBtn").click()
    sleep(2.0)
    common_click_by_node_name(poco("logout"))
    # poco("logout").click()

    def quick_login():
        from poco.drivers.unity3d import UnityPoco

        poco = UnityPoco()
        common_click_by_node_name(poco("guest"))
        # poco("guest").click()

    quick_login()

    def test_name_Anti_addiction():
        from poco.drivers.unity3d import UnityPoco

        poco = UnityPoco()
        poco("age").click([1.0, 1.0])
        assert_exists(
            Template(
                r"tpl1655257062028.png",
                record_pos=(0.022, -0.001),
                resolution=(2400, 1080),
            ),
            "存在适龄提示",
        )
        common_click_by_node_name(poco("btnClose"))
        # poco("btnClose").click()

    test_name_Anti_addiction()

    def test_yonghuertongyinsi():
        from poco.drivers.unity3d import UnityPoco

        poco = UnityPoco()
        poco("btnCustomer").wait_for_appearance()
        poco("btnCustomer").click([0, 0])
        poco("ui_popup").offspring("sliderEffect").offspring("Handle").swipe(
            [0.0904, -0.0075]
        )
        common_click_by_node_name(poco("btnProtocol"))
        # poco("btnProtocol").click()
        assert_exists(
            Template(
                r"tpl1655696751664.png",
                record_pos=(0.023, -0.096),
                resolution=(2400, 1080),
            ),
            "存在途游游戏用户服务协议",
        )
        common_click_by_node_name(
            poco("ui_popup").offspring("user_protocol").offspring("btnClose")
        )
        # poco("ui_popup").offspring("user_protocol").offspring("btnClose").click()
        common_click_by_node_name(poco("btnChildren"))
        # poco("btnChildren").click()
        assert_exists(
            Template(
                r"tpl1655696798554.png",
                record_pos=(0.023, -0.087),
                resolution=(2400, 1080),
            ),
            "存在儿童隐私政策",
        )
        poco("ui_popup").child("Canvas").child("child_privacy").offspring(
            "btnClose"
        ).click()

    test_yonghuertongyinsi()

    def test_yinsizhengce():
        from poco.drivers.unity3d import UnityPoco

        poco = UnityPoco()
        common_click_by_node_name(poco("btnPrivacy"))
        # poco("btnPrivacy").click()
        x, y = poco("title").get_position()
        end = [x, y - 32.5]
        dir = [0, -0.1]
        # 从点A滑动到点B
        poco.swipe([x, y], end, duration=8)
        sleep(2.0)

        def test_snapshot():
            try:
                wait(
                    Template(
                        r"tpl1655891795023.png",
                        record_pos=(-0.052, 0.1),
                        resolution=(2400, 1080),
                    )
                )

                touch(
                    Template(
                        r"tpl1655691797138.png",
                        record_pos=(-0.049, -0.013),
                        resolution=(2400, 1080),
                    )
                )
                assert_exists(
                    Template(
                        r"tpl1655696865969.png",
                        record_pos=(0.021, -0.119),
                        resolution=(2400, 1080),
                    ),
                    "已跳转至注销须知",
                )
                poco("ui_popup").child("Canvas").child("privacy").offspring(
                    "btnClose"
                ).click()
                poco("btnClose").click()
            except Exception as msg:
                snapshot(msg="没有找到注销超链接.")

        test_snapshot()

    test_yinsizhengce()
    poco("btnCustomer").click([1, 0])
    from poco.drivers.android.uiautomation import AndroidUiautomationPoco

    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
    android_poco = AndroidUiautomationPoco
    # 定义一个安卓的poco，并将其取名为android_poco
    def test_vip():
        from poco.drivers.unity3d import UnityPoco

        poco = UnityPoco()
        assert_exists(
            Template(
                r"tpl1655797169331.png",
                record_pos=(0.024, -0.14),
                resolution=(2400, 1080),
            ),
            "标题捕鱼大作战正确",
        )
        poco(textMatches="^3D捕鱼大作战.*$", type="android.widget.TextView", enable=True)
        assert_exists(
            Template(
                r"tpl1655797211816.png",
                record_pos=(-0.102, -0.073),
                resolution=(2400, 1080),
            ),
            "3d捕鱼大作战正确",
        )
        poco(text="· 充值未到").long_click()
        assert_exists(
            Template(
                r"tpl1655797283796.png",
                record_pos=(-0.234, 0.066),
                resolution=(2400, 1080),
            ),
            "存在充值问题反馈超链接",
        )

    clear_app("com.tuyoo.fish3d.official")  # 后台杀掉APP
    start_app("com.tuyoo.fish3d.official")

    def yinsixieyi_exist():
        from poco.drivers.unity3d import UnityPoco

        poco = UnityPoco()
        wait(
            Template(
                r"tpl1655110166871.png",
                record_pos=(0.013, -0.006),
                resolution=(1600, 720),
            )
        )

    yinsixieyi_exist()
    from poco.drivers.unity3d import UnityPoco

    poco = UnityPoco()

    def test_privacy_agreement():
        from poco.drivers.unity3d import UnityPoco

        poco = UnityPoco()
        common_click_by_node_name(poco("agreebtn"))
        # poco("agreebtn").click()  # 同意隐私协议
        common_click_by_node_name(poco("guest"))
        # poco("guest").click()

    test_privacy_agreement()

    def test_name_start_children():
        from poco.drivers.unity3d import UnityPoco

        poco = UnityPoco()
        common_click_by_node_name(poco("btnPlay"))
        # poco("btnPlay").click()
        touch(
            Template(
                r"tpl1654742567983.png",
                record_pos=(0.036, -0.028),
                resolution=(1600, 720),
            )
        )
        shell("input text '211481200709230054'")
        common_click_by_node_name(poco("name"))
        # poco("name").click()
        common_click_by_node_name(poco("name"))
        # poco("name").click()
        text("于家旭", search=True)
        common_click_by_node_name(poco("name"))
        # poco("name").click()
        common_click_by_node_name(poco("Button (1)"))
        # poco("Button (1)").click()
        assert_exists(
            Template(
                r"tpl1655256852900.png",
                record_pos=(0.022, -0.013),
                resolution=(2400, 1080),
            ),
            "未成年人禁止进入游戏",
        )

        poco("exitgamebtn").click()

    test_name_start_children()

    clear_app("com.tuyoo.fish3d.official")
    start_app("com.tuyoo.fish3d.official")
    # 部分手机不支持
    # sleep(1.0)
    wait(
        Template(
            r"tpl1655110166871.png", record_pos=(0.013, -0.006), resolution=(1600, 720)
        )
    )

    # 初始化poco
    from poco.drivers.unity3d import UnityPoco

    poco = UnityPoco()

    def test_privacy_agreement():
        from poco.drivers.unity3d import UnityPoco

        poco = UnityPoco()
        common_click_by_node_name(poco("agreebtn"))
        # poco("agreebtn").click()
        # 同意隐私协议

    def test_name_start_false():
        from poco.drivers.unity3d import UnityPoco

        poco = UnityPoco()
        common_click_by_node_name(poco("guest"))
        # poco("guest").click()
        common_click_by_node_name(poco("btnPlay"))
        # poco("btnPlay").click()
        touch(
            Template(
                r"tpl1654742567983.png",
                record_pos=(0.036, -0.028),
                resolution=(1600, 720),
            )
        )
        shell("input text '420528198302174734'")
        common_click_by_node_name(poco("name"))
        # poco("name").click()
        common_click_by_node_name(poco("name"))
        # poco("name").click()
        text("姓名袁冠鹏", search=True)
        common_click_by_node_name(poco("name"))
        # poco("name").click()
        common_click_by_node_name(poco("Button (1)"))
        # poco("Button (1)").click()
        assert_exists(
            Template(
                r"tpl1654934729253.png",
                record_pos=(0.012, -0.015),
                resolution=(1600, 720),
            ),
            "认证失败请重新认证",
        )
        common_click_by_node_name(poco("btnOK"))
        # poco("btnOK").click()

    test_privacy_agreement()
    test_name_start_false()

    clear_app("com.tuyoo.fish3d.official")
    start_app("com.tuyoo.fish3d.official")
    # 部分手机不支持
    # sleep(1.0)
    wait(
        Template(
            r"tpl1655110166871.png", record_pos=(0.013, -0.006), resolution=(1600, 720)
        )
    )

    # 初始化poco
    from poco.drivers.unity3d import UnityPoco

    poco = UnityPoco()

    def test_privacy_agreement():
        from poco.drivers.unity3d import UnityPoco

        poco = UnityPoco()
        common_click_by_node_name(poco("agreebtn"))
        # poco("agreebtn").click()
        # 同意隐私协议

    def test_name_start_true():
        from poco.drivers.unity3d import UnityPoco

        poco = UnityPoco()
        common_click_by_node_name(poco("guest"))
        # poco("guest").click()
        common_click_by_node_name(poco("btnPlay"))
        # poco("btnPlay").click()
        touch(
            Template(
                r"tpl1654742567983.png",
                record_pos=(0.036, -0.028),
                resolution=(1600, 720),
            )
        )
        shell("input text '420528198302174734'")
        common_click_by_node_name(poco("name"))
        # poco("name").click()
        common_click_by_node_name(poco("name"))
        # poco("name").click()
        text("袁冠鹏", search=True)
        common_click_by_node_name(poco("name"))
        # poco("name").click()
        common_click_by_node_name(poco("Button (1)"))
        # poco("Button (1)").click()

    def test_exit_fishingground():
        from poco.drivers.unity3d import UnityPoco

        poco = UnityPoco()
        poco("btnShowMenu").click([1.0, 0.5])
        if poco("btnLeave").exists():
            poco("btnLeave").click([1.0, 0.5])
            common_click_by_node_name(poco("btnOK"))
            # poco("btnOK").click()

    def test_system_menu():
        from poco.drivers.unity3d import UnityPoco

        poco = UnityPoco()
        poco("btnMenu").wait_for_appearance(timeout=100)
        try:
            assert_not_exists(
                Template(
                    r"tpl1655176551024.png",
                    record_pos=(0.028, 0.003),
                    resolution=(2400, 1080),
                )
            )
            poco("btnMenu").click([1.0, 0.5])
        except:
            common_click_by_node_name(poco("btnClose"))
            # poco("btnClose").click()
            sleep(3.0)
            common_click_by_node_name(poco("btnClose"))
            # poco("btnClose").click()
        touch(
            Template(
                r"tpl1655949865199.png",
                record_pos=(-0.42, 0.03),
                resolution=(2400, 1080),
            )
        )

        assert_exists(
            Template(
                r"tpl1654744171032.png",
                record_pos=(0.072, -0.051),
                resolution=(1600, 720),
            ),
            "实名认证已发送奖励",
        )
        common_click_by_node_name(poco("btnClose"))
        # poco("btnClose").click()
        # 返回至大厅

    test_privacy_agreement()
    test_name_start_true()
    test_exit_fishingground()
    test_system_menu()


# recorder.stop_recording(output="test_login_03.mp4")#云测时注掉

