# Windows终端美化

总所周知，Windows默认的终端非常难看且不好用，本文介绍使用Windows Terminal+nerd-fonts+Oh my posh+PSReadLine 实现终端的美化字体样式和自动补全。

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/aa3de8f6bda0d052061d6b9f73e92163.png)

## 1. 安装Chocolatey

在[Chocolatey Software | Installing Chocolatey](https://chocolatey.org/install)网页下，复制安装脚本

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/135dba74fade69aaada79a0025f5312e.png)

安装脚本

```shell
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

复制到终端中

即可自动安装`Chocolatey`

## 2. 安装字体

推荐使用等宽连体带图标(终端显示的花样多一点)的字体

我使用[Nerd Fonts](https://www.nerdfonts.com/)

安装使用`Chocolatey`即可

```bash
choco install nerd-fonts-hack
```



## 3. 编辑windows terminal 配置使用Nerd Fonts字体

这里很多人都会去下载一个powershell，其实没有必要，Windows自带的powershell的版本和功能已经可以满足要求。

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/e0547c1027f29d4dc2590790efab2f4c.png)

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/ebeaabf0f74eb37d41173f7f4bfbbc47.png)

当然也可以直接使用配置文件，`"defaults"`在`"profiles"`属性下

```json
"defaults": 
{
    "backgroundImage": null,
    "colorScheme": "Campbell",
    "cursorShape": "filledBox",
    "experimental.retroTerminalEffect": false,
    "font": 
    {
        "face": "CodeNewRoman Nerd Font Mono",
        "size": 14.0,
        "weight": "normal"
    },
    "opacity": 90,
    "padding": "0",
    "scrollbarState": "hidden",
    "useAcrylic": false
},
```

其余的配置文件内容

```json
"copyFormatting": "none",
"copyOnSelect": false,
"defaultProfile": "{61c54bbd-c2c6-5271-96e7-009a87ff44bf}",
"alwaysOnTop": false,
"alwaysShowTabs": true,
"autoHideWindow": false,
"disableAnimations": false,
"firstWindowPreference": "defaultProfile",
"focusFollowMouse": false,
"initialCols": 88,
"initialPosition": "750,350",
"initialRows": 24,
"launchMode": "focus",
```

大概在这个行数

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/075e892a965f8d16d6aae7516bf7a769.png)

添加快捷键

```json
"actions": 
[
    {
        "command": 
        {
            "action": "copy",
            "singleLine": false
        },
        "keys": "ctrl+c"
    },
    {
        "command": "paste",
        "keys": "ctrl+v"
    },
    {
        "command": 
        {
            "action": "splitPane",
            "split": "auto",
            "splitMode": "duplicate"
        },
        "keys": "alt+shift+d"
    },
    {
        "command": "find",
        "keys": "ctrl+shift+f"
    },
    {
        "command": "toggleFocusMode",
        "keys": "alt+z"
    }
],
```

这样可以使用`alt+z`打开标题栏

## 4. 设置管理员权限启动

没有这个选项的更新即可

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/cebec2ec3649bda0fb0350cdf9c7b2e1.png)



## 5. 使用oh-my-posh

1. 安装，还是使用`Chocolatey`

```bash
choco install oh-my-posh
```

2. 创建`powershell`配置文件

```bash
if (!(Test-Path -Path $PROFILE )) { New-Item -Type File -Path $PROFILE -Force }
```

3. 打开配置文件

```bash
notepad $PROFILE
```

4. 写入指令，这里是让终端在启动时加载`oh-my-posh`配置文件，其中`~/.omp.theme.json`是配置文件的所在路径，windows的话就是在`C:\Users\Administrator`下创建`.omp.theme.json`文件并写入配置即可

```bash
oh-my-posh init pwsh --config ~/.omp.theme.json | Invoke-Expression
```

5. 使用`kushal`主题，其他主题在这里选择[Themes | Oh My Posh](https://ohmyposh.dev/docs/themes)

6. 复制内容粘贴到配置文件中即可

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/ec786192c578bf9e93fc91282ecc58e3.png)

7. 关闭启动时的banner，添加`-nologo`项即可

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/3714b3074d1258af263f5a066f6e03c5.png)



## 6.终端禁止运行脚本解决方案

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/77680a9388ce0afedeffe5407637f452.png)

输入这个命令即可

```bash
set-ExecutionPolicy RemoteSigned
```

## 7. 使用自动补全

1. 先安装最新的`PowerShellGet`

```bash
Install-Module -Name PowerShellGet -Force
Exit
```

2. 再安装`PSReadLine`

```bash
Install-Module PSReadLine -AllowPrerelease -Force
```

3. 在`powsershell`输入

```bash
notepad.exe $PROFILE
```

4. 在打开的界面输入下面内容

```bash
Set-PSReadLineKeyHandler -Key Tab -Function MenuComplete #Tab键会出现自动补全菜单
Set-PSReadlineKeyHandler -Key UpArrow -Function HistorySearchBackward
Set-PSReadlineKeyHandler -Key DownArrow -Function HistorySearchForward
# 上下方向键箭头，搜索历史中进行自动补全
```

5. 保存重启`powershell`即可