## 1. 介绍

**scrcpy(screen copy)**是一个通过提供 USB 或 TCP/IP 连接的 Android设备显示和控制的工具。它不需要任何根访问权限。它可以在 GNU/Linux、 Windows 和 macOS 上运行。

github官网:[https://github.com/Genymobile/scrcpy]

**特点:**

- 原生的，只显示设备屏幕
- 帧率30 ~ 120 fps，取决于设备
- 分辨率1920 × 1080或以上
- 低延迟 35 ~ 70ms
- 启动时间短
- Android 设备上不安装其他应用
- 没有帐户，没有广告，没有互联网的要求
- 免费和开放源码软件

## 2. 使用

### 2.1 前提工作

1. 下载对应系统版本
2. 解压到任意目录，建议不要再中文目录下
3. 将解压目录添加至系统环境变量中

### 2.2 手机端配置

1. 打开手机的开发者模式
2. 打开USB调试
3. 将数据线连接电脑

### 2.3 电脑端操作

1. 使用adb命令创建tcpip端口

```bash
adb tcpip 5555
```

2. 连接端口

```bash
adb connect 手机IP地址:5555
```

3. 拔掉USB线使用scrcpy命令连接手机

```
scrcpy
```

4. 到这应该就连接上手机了

### 2.4 操作失误引起无法连接的问题

1. 正确打开开发者模式，且打开了手机的USB调试功能
2. 使用数据线连接了电脑，且连接模式选择传输文件模式
3. 无法使用adb命令？查看电脑是否为adb配置环境变量，若无则下载并添加即可
4. 无法连接5555端口？检查手机是否与电脑同联一个WIFI，检查手机的IP地址是否输错，检查在IP地址后是否添加5555端口
5. 使用`scrcpy`命令无法连接？检查是否拔掉USB线，检查是否连接同一个WIFI，检查防火墙。

### 2.5 使用USB投屏

如果之前配置了tcpip端口，需要先断开端口

```
adb disconnect IP地址:5555
```

然后使用`scrcpy`命令连接

### 2.6 无法输入的问题

scrcpy不支持输入中文字符，如果输入模式为中文模式，则会出现无法输入的情况，切换为英文输入即可

## 3. 使用sndcpy开启声音

github官网:[https://github.com/rom1v/sndcpy]

### 3.1 配置

1. 安装vlc:[https://free.nchc.org.tw/vlc/vlc/3.0.18/win64/vlc-3.0.18-win64.exe]
2. 记下安装位置
3. 下载sndcpy
4. 解压，修改sndcpy.bat文件中

```bash
if not defined VLC set VLC="vlc目录"
```

5. 在手机端安装sndcpy.apk，打开录制声音权限
6. 使用scrcpy命令连接手机
7. 运行sndcpy.bat脚本

## 4. 使用Bluetooth Audio Recevier开启声音

### 4.1 配置

1. 微软商店搜索Bluetooth Audio Recevier下载安装

2. 打开手机电脑蓝牙，对电脑进行配对
3. 打开Bluetooth Audio Recevier 选择手机设备，点击connect
4. 提示connected即连接成功

## 5. scrcpy命令

**版本信息**

```bash
scrcpy -v
```

**裁剪投屏屏幕(长:宽:偏移x:偏移y)**将某一区域放大

```bash
scrcpy -c 800:800:0:0
```

**设置端口**

```bash
scrcpy -p 27184
```

**帮助**

```bash
scrcpy --help
```

**缩小尺寸**
有时，以较低的清晰度镜像 Android 设备以提高性能很有用。
将宽度和高度限制为某个值（例如 1024）：

```bash
scrcpy --max-size 1024
scrcpy -m 1024  # short version
```

**更改比特率**
默认比特率为 8 Mbps。 要更改视频比特率（例如，更改为 2 Mbps）：

```bash
scrcpy --bit-rate 2M
scrcpy -b 2M  # short version
```

**限制帧率**
可以限制捕获帧速率

```bash
scrcpy --max-fps 15
```

自 Android 10 起正式支持此功能，但可能适用于较早版本。

**Crop**
设备屏幕可能会被裁剪以仅镜像屏幕的一部分。
例如，这对于仅镜像 Oculus Go 的一只眼睛很有用：

```bash
scrcpy --crop 1224:1440:0:0   # 1224x1440 at offset (0,0)
```

如果还指定了 --max-size，则在裁剪后应用调整大小

**锁定视频方向**
要锁定镜像的方向：

```bash
scrcpy --lock-video-orientation     # initial (current) orientation
scrcpy --lock-video-orientation=0   # natural orientation
scrcpy --lock-video-orientation=1   # 90° counterclockwise
scrcpy --lock-video-orientation=2   # 180°
scrcpy --lock-video-orientation=3   # 90° clockwise
```

这会影响录屏方向。窗口也可以独立旋转

**编码器**
有些设备有多个编码器，其中一些可能会导致问题或崩溃。 可以选择不同的编码器：

```bash
scrcpy --encoder OMX.qcom.video.encoder.avc
```

要列出可用的编码器，您可以传递一个无效的编码器名称，错误将给出可用的编码器：

```bash
scrcpy --encoder _
```

**录屏**
可以在镜像时录制屏幕：

```bash
scrcpy --record file.mp4
scrcpy -r file.mkv
```

**在录音时禁用镜像**

```bash
scrcpy --no-display --record file.mp4
scrcpy -Nr file.mkv
# interrupt recording with Ctrl+C
```

“跳过的帧”会被记录下来，即使它们不是实时显示的（出于性能原因）。 帧在设备上带有时间戳，因此数据包延迟变化不会影响录制的文件。

**v4l2loopback**
在 Linux 上，可以将视频流发送到 v4l2 环回设备，以便任何支持 v4l2 的工具都可以像网络摄像头一样打开 Android 设备。
必须安装模块 v4l2loopback：

```bash
sudo apt install v4l2loopback-dkms
```

创建v4l2设备:

```bash
sudo modprobe v4l2loopback
```

这将在/dev/videoN中创建一个新的视频设备，其中N是一个整数(创建多个设备或具有特定id的设备有更多选项)。
列出已启用的设备。

```bash
# requires v4l-utils package
v4l2-ctl --list-devices

# simple but might be sufficient
ls /dev/video*
```

要使用 v4l2 接收器启动 scrcpy：

```bash
scrcpy --v4l2-sink=/dev/videoN
scrcpy --v4l2-sink=/dev/videoN --no-display  # disable mirroring window
scrcpy --v4l2-sink=/dev/videoN -N            # short version
```

（用设备 ID 替换 N，检查 ls /dev/video*）

启用后，您可以使用支持 v4l2 的工具打开视频流：

```bash
ffplay -i /dev/videoN
vlc v4l2:///dev/videoN   # VLC might add some buffering delay
```

例如，您可以在 OBS 中捕获视频。

**缓冲**
可以添加缓冲。 这会增加延迟但会减少抖动（请参阅 #2464）。
该选项可用于显示缓冲：

```bash
scrcpy --display-buffer=50  # add 50 ms buffering for display
```

和 V4L2 接收器：

```bash
scrcpy --v4l2-buffer=500    # add 500 ms buffering for v4l2 sink
```

**无线连接**
sccpy通过adb与设备通信，adb可以通过TCP/IP与设备连接:

1. 将设备连接到与电脑相同的Wi-Fi。
2. 在“设置”→“关于话机”→“状态”或执行以下命令获取设备IP地址:

```bash
adb shell ip route | awk '{print $9}'
```

1. 在您的设备上通过 TCP/IP 启用 adb：adb tcpip 5555。
2. 拔下您的设备。
3. 连接到您的设备：adb connect DEVICE_IP:5555（替换 DEVICE_IP）。
4. 像往常一样运行 scrcpy。

降低比特率和定义可能很有用：

```bash
scrcpy --bit-rate 2M --max-size 800
scrcpy -b2M -m800  # short version
```

**多设备**
如果 adb devices 中列出了多个设备，则必须指定串行：

```bash
scrcpy --serial 0123456789abcdef
scrcpy -s 0123456789abcdef  # short version
```

如果设备通过 TCP/IP 连接：

```bash
scrcpy --serial 192.168.0.1:5555
scrcpy -s 192.168.0.1:5555  # short version
```

您可以为多个设备启动多个sccpy实例。

**设备连接时自动启动**
您可以使用 AutoAdb：

```bash
autoadb scrcpy -s '{}'
```

**SSH隧道**
要连接到远程设备，可以将本地 adb 客户端连接到远程 adb 服务器（前提是它们使用相同版本的 adb 协议）：

```bash
adb kill-server    # kill the local adb server on 5037
ssh -CN -L5037:localhost:5037 -R27183:localhost:27183 your_remote_computer
# keep this open
```

从另一个终端：

```bash
scrcpy
```

为了避免启用远程端口转发，可以强制使用正向连接(请注意-L而不是-R):

```bash
adb kill-server    # kill the local adb server on 5037
ssh -CN -L5037:localhost:5037 -L27183:localhost:27183 your_remote_computer
# keep this open
```

从另一个终端：

```bash
scrcpy --force-adb-forward
```

就像无线连接一样，它可能有助于降低质量:

```bash
scrcpy -b2M -m800 --max-fps 15
```

**窗口配置标题**
默认情况下，窗口标题是设备型号。 它可以改变：

```bash
scrcpy --window-title 192.168.10.202:5555
```

**窗口位置和大小**
初始窗口的位置和大小可以指定:

```bash
scrcpy --window-x 100 --window-y 100 --window-width 800 --window-height 600
```

**窗口无边界**
要禁用窗口装饰：

```bash
scrcpy --window-borderless
```

**窗口总在最前面**
要使 scrcpy 窗口始终在最上面：

```bash
scrcpy --always-on-top
```

**窗口全屏**
该应用程序可以直接全屏启动：

```bash
scrcpy --fullscreen
scrcpy -f  # short version
```

> 然后可以使用 MOD+f 动态切换全屏。

**窗口回转**
窗口可以旋转：

```bash
scrcpy --rotation 1
#可能的值是:
#	0：不旋转
#	1：逆时针90度
#	2：180度
#	3：顺时针90度
```

旋转也可以通过 MOD+←（左）和 MOD+→（右）动态改变。
请注意， scrcpy 管理 3 种不同的旋转：
MOD+r 请求设备在纵向和横向之间切换（当前运行的应用程序可能会拒绝，如果它不支持请求的方向）。
–lock-video-orientation 更改镜像方向（从设备发送到计算机的视频的方向）。 这会影响录制。
–rotation（或 MOD+←/MOD+→）仅旋转窗口内容。 这仅影响显示，不影响录音。

## 6. 其他镜像选项

**只读**
要禁用控件（可以与设备交互的所有内容：输入键、鼠标事件、拖放文件）：

```bash
scrcpy --no-control
scrcpy -n
```

**显示**
如果有几种显示，可以选择镜像的显示:

```bash
scrcpy --display 1
```

可以通过以下方式检索显示 ID 列表：

```bash
adb shell dumpsys display   # search "mDisplayId=" in the output
```

只有在设备至少运行 Android 10 时才能控制辅助显示器（否则它会以只读方式镜像）。

**保持清醒**
为了防止设备在插入设备时延迟一段时间后进入睡眠状态：

```bash
scrcpy --stay-awake
scrcpy -w
```

当sccpy关闭时，恢复初始状态。

**屏幕关闭**

可以使用命令行选项在启动镜像时关闭设备屏幕：

```bash
scrcpy --turn-screen-off
scrcpy -S
```

或者随时按 MOD+o。
要重新打开它，请按 MOD+Shift+o。
在 Android 上，电源按钮始终打开屏幕。 为方便起见，如果通过 scrcpy（通过右键单击或 MOD+p）发送 POWER，它将在一小段延迟后强制关闭屏幕（最大努力）。 物理电源按钮仍会导致屏幕打开。

防止设备休眠也很有用：

```bash
scrcpy --turn-screen-off --stay-awake
scrcpy -Sw
```

**显示触摸**
对于演示，显示物理接触（在物理设备上）可能很有用。
Android 在开发人员选项中提供了此功能。
Scrcpy 提供了一个选项，可以在启动时启用此功能并在退出时恢复初始值：

```bash
scrcpy --show-touches
scrcpy -t
```

请注意，它仅显示物理触摸（手指在设备上）。

**关闭屏幕保护程序**

默认情况下，sccpy不会阻止屏幕保护程序在计算机上运行。
禁用:

```bash
scrcpy --disable-screensaver
```

## 7. 输入控件

**旋转设备的屏幕**
按MOD+r切换纵向和横向模式。
注意，只有当前台的应用程序支持请求的方向时，它才会旋转。

**复制粘贴**
每当 Android 剪贴板发生变化时，它都会自动同步到计算机剪贴板。
任何 Ctrl 快捷键都会转发到设备。 特别是：

```bash
Ctrl+c 通常复制
Ctrl+x 通常是剪切
Ctrl+v 通常粘贴（在计算机到设备剪贴板同步之后）
```

这通常按您的预期工作。

但实际行为取决于活动应用程序。 例如，Termux 在 Ctrl+c 上发送 SIGINT，而 K-9 Mail 会撰写新消息。

在这种情况下复制、剪切和粘贴（但仅在 Android >= 7 上支持）：

```bash
MOD+c 注入 COPY
MOD+x 注入 CUT
MOD+v 注入 PASTE（在计算机到设备剪贴板同步之后）
```

此外，MOD+Shift+v 允许将计算机剪贴板文本作为关键事件序列注入。 当组件不接受文本粘贴（例如在 Termux 中）时，这很有用，但它可以破坏非 ASCII 内容。

**警告:**

将计算机剪贴板粘贴到设备（通过 Ctrl+v 或 MOD+v）会将内容复制到设备剪贴板中。 因此，任何 Android 应用程序都可以读取其内容。 您应该避免以这种方式粘贴敏感内容（如密码）。
以编程方式设置设备剪贴板时，某些设备的行为不符合预期。 提供了一个选项 --legacy-paste 来更改 Ctrl+v 和 MOD+v 的行为，以便它们也将计算机剪贴板文本作为关键事件序列注入（与 MOD+Shift+v 的方式相同）。

**双指缩放**
模拟“双指缩放”：Ctrl+单击并移动。

更准确地说，按住 Ctrl 的同时按下左键单击按钮。 在释放左键单击按钮之前，所有鼠标移动都会相对于屏幕中心缩放和旋转内容（如果应用程序支持）。

具体来说，scrcpy 在屏幕中心反转的位置从“虚拟手指”生成额外的触摸事件。

**文本注入首选项**
键入文本时会生成两种事件：

*按键事件，表示按键被按下或释放；
文本事件，表示已输入文本。*

默认情况下，使用按键事件注入字母，以便键盘在游戏中按预期运行（通常用于 WASD 键）。

但这可能会导致问题。 如果遇到此类问题，可以通过以下方式避免：

```bash
scrcpy --prefer-text
```

（但这会破坏游戏中的键盘行为）

**键重复**

默认情况下，按住某个键会生成重复的键事件。 这可能会在某些游戏中导致性能问题，而这些事件无论如何都是无用的。

为避免转发重复的关键事件：

```bash
scrcpy --no-key-repeat
```

## 8. 文件拖放

**安装 APK**
要安装 APK，请将 APK 文件（以 .apk 结尾）拖放到 scrcpy 窗口。
没有视觉反馈，日志打印到控制台。

**推送文件到设备**

要将文件推送到设备上的 /sdcard/Download/，请将（非 APK）文件拖放到 scrcpy 窗口。

没有视觉反馈，日志打印到控制台。

目标目录可以在启动时更改：

```bash
scrcpy --push-target=/sdcard/Movies/
```

**音频转发**
scrcpy 不转发音频。 使用 sndcpy。

## 9. 快捷方式

在下面的列表中，MOD 是快捷方式修饰符。 默认情况下，它是（左）Alt 或（左）Super。
可以使用 --shortcut-mod 更改它。 可能的键有 lctrl、rctrl、lalt、ralt、lsuper 和 rsuper。 例如：

```bash
# use RCtrl for shortcuts
scrcpy --shortcut-mod=rctrl

# use either LCtrl+LAlt or LSuper for shortcuts
scrcpy --shortcut-mod=lctrl+lalt,lsuper
```

Super 通常是 Windows 或 Cmd 键。

| 操作                                 | 快捷键                    |
| ------------------------------------ | ------------------------- |
| 切换全屏模式                         | MOD+f                     |
| 向左旋转显示                         | MOD+←（向左）             |
| 向右旋转显示                         | MOD+→（右）               |
| 将窗口大小调整为 1:1（像素完美）     | MOD+g                     |
| 调整窗口大小以去除黑边               | MOD+w \| 双击左键¹        |
| 点击 HOME                            | MOD+h \| 中键单击         |
| 点击返回                             | MOD+b \| 右键单击²        |
| 点击APP_SWITCH                       | MOD+s \| 第四次点击³      |
| 点击MENU（解锁屏幕）                 | MOD+m                     |
| 点击VOLUME_UP                        | MOD+↑（向上）             |
| 点击VOLUME_DOWN                      | MOD+↓（向下）             |
| 点击 POWER                           | MOD+p                     |
| 开机                                 | 右击²                     |
| 关闭设备屏幕（保持镜像）             | MOD+o                     |
| 打开设备屏幕                         | MOD+Shift+o               |
| 旋转设备屏幕                         | MOD+r                     |
| 展开通知面板                         | MOD+n \| 第 5 次点击³     |
| 展开设置面板                         | MOD+n+n \| 双击 5 次点击³ |
| 折叠面板                             | MOD+Shift+n               |
| 复制到剪贴板⁴                        | MOD+c                     |
| 剪切到剪贴板⁴                        | MOD+x                     |
| 同步剪贴板和粘贴⁴                    | MOD+v                     |
| 注入电脑剪贴板文本                   | MOD+Shift+v               |
| 启用/禁用 FPS 计数器（在标准输出上） | MOD+i                     |
| 双指缩放                             | Ctrl+单击并移动           |

```bash
¹双击黑色边框将其删除。
²如果屏幕已关闭，则右键单击可打开屏幕，否则按 BACK。
³第 4 和第 5 个鼠标按钮（如果您的鼠标有这些按钮）。
⁴仅适用于 Android >= 7。
```

重复按键的快捷键是通过释放并再次按下按键来执行的。例如，要执行“展开设置面板”

```bash
1.按住 MOD。
2.然后双击 n。
3.最后，释放MOD。
```

所有 Ctrl+key 快捷键都转发到设备，因此它们由活动应用程序处理

**自定义路径**

要使用特定的 adb 二进制文件，请在环境变量 ADB 中配置其路径：

```bash
ADB=/path/to/adb scrcpy
```

要覆盖 scrcpy-server 文件的路径，请在 SCCCPY_SERVER_PATH 中配置其路径。