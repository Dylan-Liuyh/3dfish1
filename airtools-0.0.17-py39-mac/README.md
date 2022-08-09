# Airtest/Poco常用工具库

**注意：本仓库源码内容严禁外传，请注意保密。**

更新日期： 2021-12-09

本仓库包含以下功能：

- [自动点击弹窗](#自动点击弹窗)：继承了之前klay的代码，原仓库不再维护
- [Airtest API功能增强](#AirtestAPI功能增强)： 增强部分API，能够有更好的兼容性
- [自动初始化各品牌设备](#自动初始化各品牌设备)：在手机已经开启USB调试+已经安装PocoService的前提下，自动进行一些选项的设置

## 自动点击弹窗

本功能可以自动帮助点击一些手机的安装弹窗，如果VIVO/OPPO系手机需要输入安装密码，请查看下面的密码设置接口。


代码示例：

1. 点一次弹窗：

```py
from airtools.popup_eliminator import eliminate_popup_once
eliminate_popup_once(poco)  # 如果已有poco，可以直接传入poco对象，否则可以什么都不传
```

`eliminate_popup_once()`接口在成功检测到弹窗并点击后，会返回`True`，因此我们也可以这样写：

```py
while eliminate_popup_once(poco):
    sleep(1)
```

2. 在一段时间内一直点击弹窗，直到超时：

   注意：这个语句会卡住主流程，等待30秒之后才会继续后面的脚本

```py
from airtools.popup_eliminator import eliminate_popup
eliminate_popup(poco, timeout=30)
```

`airtools>=0.0.16`以上版本新增：

在当前环境已经安装有`airtest_ocr`库的情况下（无论是python环境中已经安装、还是企业版用户使用了airtest_ocr的二进制文件），默认会额外启用OCR支持来点击弹窗，针对一些OPPO手机的安装窗口有更好的效果。

```python
from airtools.popup_eliminator import eliminate_popup
eliminate_popup(poco, timeout=30, ocr=False)  # 传入ocr=False可以关闭OCR功能，减少系统的性能消耗
```

3. **【推荐】【新增】** 开启线程点可能出现的弹窗，每隔2秒检查一次弹窗，直到with语句内的内容运行结束才会停止点击

   ```python
   with eliminate_popup_thread():
       # 卡住等待10秒
   	   sleep(10)
   
   # 可以传入两个参数：poco与interval
   with eliminate_popup_thread(poco, interval=2):
   	   start_app("com.netease.cloudmusic")
   ```

   下面是一个完整示例：

   安装网易云音乐并开线程点弹窗，直到安装完成：

   ```python
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


`airtools 0.0.16`以上版本新增：

在当前环境已经安装有`airtest_ocr`库的情况下（无论是python环境中已经安装、还是企业版用户使用了airtest_ocr的二进制文件），默认会额外启用OCR支持来点击弹窗，针对一些OPPO手机的安装窗口有更好的效果。

```python
from airtools.popup_eliminator import eliminate_popup_thread
with eliminate_popup_thread(ocr=False):  # airtools >= 0.0.16版本新增ocr开关，默认为True
    install(r"2048.apk")
    time.sleep(20)
```

4. 开启一个弹窗点击线程，一直点击可能出现的弹窗，直到手动停止：

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

注： 在airtools>=0.0.16以上版本时，当开启`PopupEliminator`线程时，将会同时进行poco元素的查找和OCR文字识别（主要是应对OPPO手机的安装弹窗）。

可以传入`PopupEliminator(poco, ocr=False)`来关闭默认启用的OCR功能，减少系统性能消耗，但代价是无法点击部分OPPO手机的安装弹窗。

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

OPPO和VIVO系手机在使用ADB安装应用时，需要输入对应的密码，`set_password`可以设置账号对应的密码，在需要输入密码时能够自动进行输入：

```py
from airtools.popup_eliminator import set_password
set_password('new-password')
```

密码设置注意点：

1. 需要事先在手机-设置中，登录好OPPO或VIVO账号，否则在安装时airtools只会自动输入密码，无法自动输入账号（因为通常需要手机验证码才能登录）
2. 部分手机有防止恶意截屏的设置，会导致在输入密码时截不到当前画面的图像，airtools会在截到黑屏时尝试进行密码输入并自动发送回车响应，但并不能完全确保顺利安装。如果遇到此类情况，可以先在设置中关闭安全输入/防止恶意截屏等相关选项，或是手工点一下确认，保证安装过程顺利。
3. 如果希望手动输入密码，请强制运行`set_password("")`接口，否则airtools会输入默认密码


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

### 安装大文件接口-install（废弃）

本接口已废弃，请正常使用airtest中的pm_install接口即可：

```
from airtest.core.api import *
dev = device()
dev.adb.pm_install(r"D:\test.apk")
```

`pm_install`接口的功能是：先使用`adb push`将文件推送至手机sdcard中，然后再执行安装。当安装大文件时，使用这个接口，相比于直接使用`adb install`来说稳定性更好。

### 根据方向滑动-direction_swipe

简单根据方向，从左向右滑动，或者是从下往上滑动之类的：

```py
from airtools.airtest_ext import direction_swipe
direction_swipe("bottom", "top")
direction_swipe("left", "right")
```

### 使用滑动解锁屏幕-wake（即将废弃）

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



## 自动初始化各品牌设备

`airtools`新增了手机初始化接口，能够在手机**已经打开USB调试**、**且已安装PocoService**的前提下，进行一些手机相关设置项的自动设置工作。

### 重要！准备工作：

请务必确认以下所有步骤都已完成，否则无法使用脚本进行自动初始化：

1. 打开手机的开发者选项开关、以及USB调试开关
2. 使用USB连接手机，当手机弹出信任弹窗时，点击信任

3. 确认电脑上能够用`adb devices`指令，看到手机出现在列表中

4. 启动初始化脚本时，会首先进行PocoService.apk的安装，**请务必确认已成功执行此过程**
   - 部分品牌如OPPO/VIVO手机，需要事先登录账号才能够进行APK的安装，请登录后、确认PocoService.apk成功安装
   - 建议所有的OPPO/VIVO/Realme手机登录的账号，都设置为相同的密码，方便后续自动安装脚本的运行

几个注意事项：

- 如果是小米手机，请参考[文档](https://airtest.doc.io.netease.com/IDEdocs/device_connection/2_android_faq/#_4)，需要提前做好设置、允许模拟点击，才可以顺利运行初始化脚本
- 注意：本功能会关闭手机很多安全性相关的选项，主要为自动化测试提供方便，如果是自己平时使用的手机，请先阅读好下方的各个配置项列表，确认内容无误后再运行。

### 使用方法

初始化脚本内容如下：

```python
from airtest.core.api import *
from airtools.init_device.api import init_device
from airtools.popup_eliminator import set_password


auto_setup(__file__)
# 这里可以设置OPPO/VIVO手机的安装密码，但仅用于安装Yosemite.apk，PocoService还是需要手工输入密码进行安装
set_password('new-password')
init_device(device())
```

初始化**一台手机**：在AirtestIDE中，仅连接一台当前需要初始化的手机，执行上述脚本即可。

初始化**多台手机**：在企业版AirtestIDE中，选择多台手机，并选中上述脚本，选择**并行式运行**（即将脚本在每一台手机上各运行一次）。



脚本执行过程中，主要执行的内容如下：

- 先进行手机图像查看、点击操作的初始化
- 安装PocoService.apk，**这个步骤可能需要人工在手机上进行安装确认或输入密码**
- 安装Yosemite.apk，此步骤同样可能需要人工确认
- 根据各品牌手机的一些设置规则，依次进行手机设置的修改，部分手机可能会因为PocoService被手机自动杀后台，导致初始化失败，可以尝试重复运行、或是人工设置

### 结果查看

脚本运行结束后，**会将该品牌的设置项都显示在终端中**，同时也会列出失败的项目，部分失败原因是本机型没有相关设置项、或是无需设置，这种情况可以人工检查复核后忽略就行。

部分失败原因是因为我们预先写好的规则中不包括该机型的相关设置，如果遇到了此种情况，可以将该机型+对应的正确设置方法反馈给我们，我们将会及时更新规则和相关文档。

若是多机运行结果，如果出现了设置失败的情况，可以点击查看对应的报告，然后查找报告末尾失败步骤的前一个步骤，我们将错误作为一条log显示在了该步骤中，示例如下：

```
-----------------------  * * * -----------------------

OPPO手机的设置项：
- 连接模式-传输文件
- 【需手动设置】请事先登录好OPPO账号
- 【需手动设置】开发者选项开启方式：连续点击【设置-系统管理-关于手机-版本信息-软件版本】
- 设置-电池-应用耗电管理-pocoservice-允许应用自启动，允许完全后台行为
- 设置-其他设置-开发者选项-禁止权限监控 打开，充电时屏幕不休眠 打开
- 设置-其他设置-键盘与输入法-管理输入法-yosemite 启用
- 设置-其他设置-键盘与输入法-输入密码时启用安全键盘 关闭
- 设置-安全与隐私-允许安装未知来源的应用 打开 （不是所有机型都有）
- 【无需设置】如OPPO出现10分钟断连的情况，不要插拔手机，直接在屏幕上方下拉的选项里再次打开 USB调试

-----------------------  以下步骤设置失败： -----------------------

    - 设置-安全与隐私-允许安装未知来源的应用 打开
    （本选项不是所有的机型都有）

    
错误原因：
Cannot find any visible node by query UIObjectProxy of "text=安全与隐私"
```

可以根据log中列出的选项，检查手机上的各个选项是否正确被处理了。

出现错误的可能原因：

- 该手机并没有相关的设置项，由于机型版本不同，导致设置项在同一品牌手机上也有很大差异，有些选项如果找不到可以忽略
- 部分手机有相关选项，但因为机型或系统版本不同，导致我们目前的规则并没有能够覆盖到该款手机，若出现该情况，**可以将手机机型和对应的设置反馈给我们**
- 部分选项不是必须的，如果不做处理，可能影响很小，可以视情况忽略（例如充电时保持屏幕常亮、或是监控ADB安装应用等选项，并非必须要处理的选项）
- 几乎绝大多数品牌手机都需要允许PocoSerivce.apk能够在后台启动，部分手机可能在还没来得及做出修改前，poco进程就被手机杀后台了，可能需要手工处理（例如一加8T）

### 支持的品牌

以下是当前支持的品牌：

- 三星
- 华为（包含荣耀）
- OPPO
- VIVO
- 一加
- Realme真我（大体与OPPO类似）
- 小米
- 魅族


以下是相关的设置项，也可以根据该设置项进行手工设置，更多新设置请参考官网文档：

- **小米手机（请务必登录账号先进行设置！！！！）**
  - 【需手动设置】需要**插入sim卡并登录小米账号**（小米开启权限时需要插入SIM卡，完成选项开启后可以拔卡）
  - 【需手动设置】开启开发者选项：连续点击【设置 - 我的设备 - 全部参数 - MIUI版本】
  - 【需手动设置】设置开发者选项：（根据MIUI版本不同，描述可能不一样）
    - 开启【USB调试】、【USB安装】、【USB调试（安全设置）-允许模拟点击】
    - 禁用开发者选项底部【启动MIUI优化】、【高风险功能开启提醒】
  - 禁用手机管家-应用管理-权限-右上角的设置- 【应用权限监控】和 【USB安装管理】
  - 启用手机管家-应用管理-权限-自启动管理-PocoService，允许PocoService自启动
  - 语言与输入法：关闭【安全键盘】，在输入法管理中，启用【Yosemite输入法】
  - 如果手机依然无法看到屏幕，可以检查Yosemite.apk是否成功安装（可以手动安装），并且对应的权限都开启了
- 华为手机的设置项：
  - 【手动设置】USB模式-文件，若开启了仅充电模式下允许调试才能直连
  - 设置-高级设置-语言和输入法-安全输入 关闭 （不同机型该选项有不同入口）
  - 设置-开发者选项-监控 ADB 安装应用 关闭
  - 设置-开发者选项-“仅充电”模式下允许 ADB 调试 打开
  - 手机管家（大于8.0版本）-应用启动管理-PocoService允许自启动和后台活动
- OPPO手机的设置项：
  - 【需手动设置】请事先登录好OPPO账号
  - 设置-电池-应用耗电管理-pocoservice-允许应用自启动，允许完全后台行为
  - 设置-其他设置-开发者选项-禁止权限监控 打开
  - 设置-其他设置-键盘与输入法-管理输入法-yosemite 启用
  - 设置-其他设置-键盘与输入法-输入密码时启用安全键盘 关闭
  - 【手动设置】如OPPO出现10分钟断连的情况，不要插拔手机，直接在屏幕上方下拉的选项里再次打开 USB调试
- VIVO手机的设置项：
  - 【需手动设置】请事先登录好VIVO账号
  - 【需手动设置】设置-开发者选项-USB模拟点击 打开（如有）
  - 电池-后台高耗电-> PocoService 开启
  - 设置-输入法-安全输入 关闭
  - 开发者选项-安全权限 打开（暂未添加）
  - 设置-安全与隐私-防止恶意截屏录屏 关闭
  - 设置-更多设置（或系统管理）-开发者选项->通过USB验证应用 关闭
  - 【可选】开发者选项-不锁定屏幕 开启 （此选项能避免长时间连接时，手机自动关闭开发者选项的问题，若需要长期连接可以开启）
- 三星手机：
  - 【需手动设置】插入USB时，允许访问手机数据
  - 【需手动设置】选择安装PocoService（如果是国际版，可能会被google play检测）
  - 设置-显示-屏幕分辨率-WQHD+-应用-确定，将分辨率调到最大
  - 【暂未实现】部分型号手机在开发者选项中，打开未知来源、取消权限监控。
- Realme真我（与OPPO基本一致）：
  - 【需手动设置】请事先登录好Realme账号
  - 设置-电池-应用耗电管理-pocoservice-允许应用自启动，允许完全后台行为
  - 设置-其他设置-开发者选项-禁止权限监控 打开（必须），充电时屏幕不休眠 打开（非必须）
  - 设置-其他设置-键盘与输入法-【管理输入法-yosemite】 启用， 【输入密码时启用安全键盘】 关闭
- 一加手机的设置项：
  - 【可能需手动设置】设置-电池-电池优化-PocoService-不优化 （可能在设置成功前，进程就已经被手机终止了，因此本选项可能需要手工进行设置）
  - 设置-其他设置-键盘与输入法-输入密码时启用安全键盘 关闭
  - 设置-其他设置-键盘与输入法-管理输入法-Yosemite输入法 启用
  - 设置-其他设置-开发者选项-禁止权限监控 打开， 充电时屏幕不休眠 打开（非必选） 
- 魅族手机的设置项：
  - 手机管家-权限管理-后台管理-PocoService-允许后台运行
  - 手机管家-USB安装管理-USB安装管理 取消选中，可以在安装apk时不再出现弹窗
  - 设置-语言和时间-Yosemite输入法 勾选，取消密码安全保护



## 企业版下载与安装

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



**0.0.16以上版本新增的OCR模块**：

在airtools>=0.0.16版本时，我们为弹窗点击增加了OCR功能，能够更好地点击OPPO手机的安装按钮。

若希望启用此功能，需要在本地环境中，`pip install -r requirements.txt` 安装好airtools文件夹内提供的环境文件，才能够成功使用新功能，否则只会使用普通的poco进行点击。

但值得注意的是，开启OCR功能也会导致占用更多的系统资源，相关的弹窗接口也都提供了`ocr=False`来关闭OCR识别，请根据实际情况来选择是否启用。

#### 下载

可以使用之前向我们提交过的邮箱，登录[airtools](https://airtestproject.s3.netease.com/devicekeeper/airtools)，选择最新的一个版本号，下载与本地python环境相符的版本即可。

- 注意：请根据本地python环境版本，选择对应版本的二进制文件下载，如果需要更多支持，可以联系我们
- `airtools\latest`目录中的zip文件是py3.6的windows版本，与AirtestIDE的win64企业版zip包中的内容一致，可以直接使用。
  - 也就是说，windows包中的AirtestIDE\airtools文件夹，可以直接给python3.6环境使用
- `airtools\latest`目录中还提供了相关的使用文档可以查看
- **请使用python >= 3.5以上版本，我们没有测试过python2的兼容性。**



### 版本更新记录

- 0.0.14：新增`with eliminate_popup_thread()`的写法，另开线程点弹窗，不卡住主流程
- 0.0.15: 新增`init_device`模块，能够初始化手机设置
- 0.0.16：新增`airtest_ocr`模块，需要执行`pip install -r requirements.txt`后，即可让弹窗点击额外增加OCR功能