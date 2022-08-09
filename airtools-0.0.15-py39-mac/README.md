# Airtest/Poco常用工具库

**注意：本仓库源码内容严禁外传，请注意保密。**

更新日期： 2021-02-26

本仓库包含以下功能：

- [自动点击弹窗](#自动点击弹窗)：提供了多种方式，能够自动点击手机各式弹窗
- [Airtest API功能增强](#AirtestAPI功能增强)： 增强部分API，能够有更好的兼容性
- 待添加

## 下载与安装

### 如何安装

在AirtestIDE企业版中，能够直接使用airtools，无需额外安装。

如果使用了本地python环境，可以下载airtools.zip解压到本地后，将里面存放了二进制文件的`airtools`文件夹放到python库目录下，或者是放到脚本目录下，并在脚本内添加`sys.path`即可，例如：

```
# 比如放在目录/data/script/下
# 目录结构是：/data/script/airtools/popup_eliminator
import sys
sys.path.append("/data/script")
from airtools.popup_eliminator import eliminate_popup_once
print(eliminate_popup_once)
```

#### 下载

可以使用之前向我们提交过的邮箱，登录[airtools](https://airtestproject.s3.netease.com/devicekeeper/airtools)，选择最新的一个版本号，下载与本地python环境相符的版本即可。

- 注意：目前mac只提供了py3.6版本，如果需要更多支持，可以联系我们
- `airtools\latest`目录中的zip文件是py3.6的windows版本，与AirtestIDE的win64企业版zip包中的内容一致，可以直接使用。
  - 也就是说，windows包中的AirtestIDE\airtools文件夹，可以直接给python3.6环境使用
- `airtools\latest`目录中还提供了相关的使用文档可以查看
- **请使用python >= 3.5以上版本，我们没有测试过python2的兼容性。**

## 自动点击弹窗


本功能可以自动帮助点击一些手机的安装弹窗，但是对于一些OPPO系手机可能不生效。如果VIVO系手机需要输入安装密码，请查看下面的密码设置接口。

代码示例：

1. 点一次弹窗（仅使用Poco，不适用于部分OPPO手机）：
```py
from airtools.popup_eliminator import eliminate_popup_once
eliminate_popup_once(poco)  # 如果已有poco，可以直接传入poco对象，否则可以什么都不传
```

`eliminate_popup_once()`接口在成功检测到弹窗并点击后，会返回`True`，因此我们也可以这样写：

```py
while eliminate_popup_once(poco):
    sleep(1)
```

2. 在一段时间内一直点击弹窗，直到超时（仅使用poco，部分OPPO手机的安装界面无法点到）：

   注意：这个语句会卡住主流程，等待30秒之后才会继续后面的脚本

```py
from airtools.popup_eliminator import eliminate_popup
eliminate_popup(poco, timeout=30)
```

3. **【推荐】【新增】** 开启线程点可能出现的弹窗，每隔2秒检查一次弹窗，直到with语句内的内容运行结束才会停止点击

   ```
   with eliminate_popup_thread():
   	# 卡住等待10秒
   	sleep(10)
   
   # 可以传入两个参数：poco与interval
   with eliminate_popup_thread(poco, interval=2):
   	start_app("com.netease.cloudmusic")
   ```

   下面是一个完整示例：

   安装网易云音乐并开线程点弹窗，直到安装完成：

   ```
   from airtools.popup_eliminator import *
   from airtools.airtest_ext import install
   from airtest.core.api import *
   
   connect_device("android:///")
   with eliminate_popup_thread():
       # 用airtools提供的install接口，稳定性更高一些
       install("NeteaseCloudMusic.apk", install_options=["-r"])
       start_app("com.netease.cloudmusic")
       time.sleep(30)
   ```

4. 开启一个弹窗点击线程，一直点击可能出现的弹窗，直到手动停止（使用Airtest+Poco一起点，能够点击OPPO手机的安装界面）：

```py
from airtools.popup_eliminator import PopupEliminator
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
# 初始化poco，非必须
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

eliminator = PopupEliminator(poco)
eliminator.start()
# 等待一段时间，或者做一些其他事，等弹窗点击完毕
time.sleep(20)
eliminator.stop()
```

可以直接查看`playground/eliminator.py`内的代码示例。

注： 当开启`PopupEliminator`线程时，将会同时进行poco元素的查找和airtest的截图查找（airtest的截图主要是应对OPPO手机的弹窗）。
我们进行了一些处理，去掉了airtest截图查找时的大量`exists`接口产生的log，只有真正产生了点击时才会有log。

### 增加弹窗规则

如果是临时规则的添加，可以直接调用接口：
```py
from airtools.popup_eliminator import eliminate_popup_once, add_rule
# 添加一条新规则，点击text=确定的按钮
add_rule({"text": "确定", "type": "android.widget.Button"})
eliminate_popup_once(poco)
```

规则可以用`dict`来定义，例如`{"text": "确定", "type": "android.widget.Button"}`相当于`poco(text="确定", type="android.widget.Button")`，越细致越不容易点到错误的控件。
也可以用`list`来定义更简单的控件，例如`["text", "确定"]`，就定义了一个`poco(text="确定")`规则。

规则还支持模糊匹配，传入一个`regular=True`参数即可：

```py
add_rule({"text": ".*体验", "type": "android.widget.TextView"}, regular=True)
```

**如果希望添加一条通用规则，例如某机型的安装界面的弹窗点击，请联系开发者添加。**

### 设置手机安装密码

OPPO和VIVO系手机在使用ADB安装应用时，需要输入对应的密码，`popup_eliminator`模块已经内置了该输入框的检测，只需要设置好安装密码就能自动输入：
```py
from airtools.popup_eliminator import set_password
set_password('new-password')
```

**airtools>0.0.14版本新增功能：**

在环境变量中，可以设置一个叫做`INSTALL_PASSWORD`的值，用于设置默认的安装密码。

在批量执行脚本时，可以在所有脚本运行之前，先设置`os.environ['INSTALL_PASSWORD']='xxxx'`，后续在实际运行脚本时，airtools将会自动读取到这个默认密码。

如果希望在脚本内使用这种方式设置密码，请务必在airtools的import语句执行之前，先执行密码设置语句`os.environ['INSTALL_PASSWORD']`，否则，**脚本中设置密码只需要运行上面的`set_password`接口就足够使用了**。


* * *
## Airtest API功能增强

部分手机和部分操作在`airtest.core.api`中不包括，但是实际使用中常常遇到，因此额外封装了一个库来存放一些公共操作。

所有改动过的API列表如下：

- 优化： `install` 安装大文件时更不容易出错
- 优化： `wake` 在唤醒锁屏手机时，额外增加一个从下往上的滑动，能够解锁VIVO系手机
- 新增： `direction_swipe` 一个简单的从上往下或从左往右滑动的接口
- 新增： `exists_quiet` 一个不会产生log的安静版本的exists接口

引入方法如下，请务必写在airtest api引用的后面，这样部分同名接口就能够覆盖掉airtest的原生接口：
```py
from airtest.core.api import *  # 引入airtest的接口
from airtools.airtest_ext import install, wake, direction_swipe, exists_quiet  # 覆盖部分airtest的接口
```

### 安装大文件接口-install

安装一个大文件到手机里，默认的install方法很容易出错，因此可以换用以下接口：

```py
from airtools.airtest_ext import install
install(r"E:\test\apk\NeteaseCloudMusic.apk")
```

一边安装，一边点击弹窗的完整示例：

```py
from airtest.core.api import *
from airtools.popup_eliminator import PopupEliminator
# 请在airtest.core.api之后import，避免接口被覆盖
from airtools.airtest_ext import install
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

dev = connect_device("android:///c2b1c2a7")
# 初始化poco，非必须
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
eliminator = PopupEliminator(poco)
eliminator.start()
# 安装的过程中点击弹窗
install(r"E:\test\apk\NeteaseCloudMusic_Music_official_7.1.80.1593355734.apk")
eliminator.stop()
```

### 根据方向滑动-direction_swipe

简单根据方向，从左向右滑动，或者是从下往上滑动之类的：

```py
from airtools.airtest_ext import direction_swipe
direction_swipe("bottom", "top")
direction_swipe("left", "right")
```

### 使用滑动解锁屏幕-wake

部分手机（例如VIVO）不能够直接使用`wake()`接口解锁，因此新增了一个`airtools.airtest_ext.wake`接口，能在解锁未成功时自动从下往上滑动一次。

```py
from airtools.airtest_ext import wake
wake()
```

### 不会产生log的exists_quiet

有些时候不断判断某些弹出窗口时，由于代码反复运行，会产生大量的exists的图片判断的log，导致报告中很多无用信息，而我们只关心找到目标并点击的那个步骤。

因此新增一个静默判断目标图片是否存在的接口：

```py
from airtools.airtest_ext import exists_quiet

if exists_quiet(图片):  # 假如图片不存在，不会产生log
    touch(图片)
```

