# QT

## QMainWindow

- **QMainWindow**是一个为用户提供主窗口程序的类,包含一个菜单栏(**menubar**)、多个工俱栏(**tool bars**)、多个停靠部件(**dock widgets**)、一个状态栏(**statusbar**)及一个中心部件(**central widget**)，是许多应用程序的基础，如文本编辑器，图片编辑器等。

![](https://cdn.staticaly.com/gh/pepedd864/cdn-repos@main/img/0f0b2172ad939579e6c6c00255aa4a16.png)

### 菜单栏

**简单用法**

![](https://cdn.staticaly.com/gh/pepedd864/cdn-repos@main/img/9c439055f9f039290a0fa88df03d2023.png)

<img src="https://cdn.staticaly.com/gh/pepedd864/cdn-repos@main/img/cbeeee53cf1d5155e82d788966c26cbb.png" style="zoom:150%;" />

![](https://cdn.staticaly.com/gh/pepedd864/cdn-repos@main/img/dcc46fbda07166fbfc4479f2d48bdb89.png)

![](https://cdn.staticaly.com/gh/pepedd864/cdn-repos@main/img/fcaa7fe58dcafa67cf56ada26c0cc4b6.png)

![](https://cdn.staticaly.com/gh/pepedd864/cdn-repos@main/img/e16a6d4f0b3b326700cd8ad0430ae481.png)

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/ebfa41a8d7ed2cc41e3a628c6085bc8f.png)

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/e1759436f2c4ce907560b7aa7ddb7c36.png)

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/e1b697e77d59661a8a809fe4f2f1a33b.png)

**重载函数**

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/d205541630141fe91bc9e73103d7c623.png)

1. 传入一个QMenu的类名

2. 添加一个带标题的菜单

3. 添加一个带图标的菜单

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/81549e725a97cf2628158cf320447e78.png)

**其他函数以此类推**

## QDialog

### 标准对话框

所谓标准对话框，是Qt 内置的一系列对话框，用于简化开发。事实上，有很多对话框都是通用的，比如打开文件、设置颜色、打印设置等。这些对话框在所有程序中几乎相同，因此没有必要在每一个程序中都自己实现这么一个对话框。

**Qt的内置对话框大致分为以下几类:**

1. QMessageBox:模态对话框，用于显示信息、询问问题等;
2. QColorDialog :选择颜色;
3. QFontDialog:选择字体;
4. QFileDialog:选择文件或者目录;
5. QlnputDialog:允许用户输入一个值，并将其值返回;
6. QPageSetupDialog:为打印机提供纸张相关的选项;
7. QPrintDialog:打印机配置;
8. QPrintPreviewDialog:打印预览;
9. QProgressDialog :显示操作过程。

## qss部分用法

### 一. 设置背景

#### 1.颜色篇

**color：字体颜色**

示例：`color:rgb(231,234,213)`

`background-color：背景颜色`

示例：`background-color: rgb(114, 79, 255)`

`alternate-background-color：`

示例：`alternate-background-color: rgb(115, 60, 255);`



示例：



示例：



示例：



示例：



示例：



示例：



示例：

#### 2.图片篇

## QT Creator在高分辨率下界面不适配的解决方案（缩放设定）

- 未开启高DPI缩放时，QT creator的界面非常小，很难操作。

![QT2](https://gitee.com/pepedd864/cdn-repos/raw/master/img/0e705bed23ecaffe9cbb553ef3c90bc6.png)



- 在 qt creator 工具->选项中勾选“Enable high DPI scaling”后，菜单栏、工具栏、侧边栏又变得特别大，，似乎是缩放倍数不对，应该放大 1.5 倍，qt creator 放大了 2 倍

![QT1](https://gitee.com/pepedd864/cdn-repos/raw/master/img/82634e98c85a06e8a0a1e3c1d1a28cf2.png)

- 针对这样的应用缩放异常，我们可以手动调节放大倍数，方法是在 windows 环境变量中创建如下两个环境变量

```shell
QT_AUTO_SCREEN_SCALE_FACTOR = 0
QT_SCREEN_SCALE_FACTORS = 1.5;1
```

![Qt_5](https://gitee.com/pepedd864/cdn-repos/raw/master/img/0536114875e87f2e0825a0ba8ef176ed.png)

- 不过这样做有个问题：环境变量会影响到其他使用 QT 库的程序，，比如之前显示正常的 Pyside6 中的 Qt Designer 在设置此环境变量后缩放出了问题。

- 所以只能单独给 qt creator 设置上述环境变量才行，方法是新建一个文件 QtCreator.bat ，写入如下内容：

```shell
set QT_AUTO_SCREEN_SCALE_FACTOR=0
set QT_SCREEN_SCALE_FACTORS=1.5;1
C:\Programs\QtCreator\bin\qtcreator.exe
```

- 将应用快捷方式改成QtCreator.bat的路径，这样点击快捷方式便可以直接打开缩放正常的应用。

![Qt_3](https://gitee.com/pepedd864/cdn-repos/raw/master/img/b55af5beac57c6f17a440ffdf7fc9003.png)

- 另外还有一种不使用 Qt 库提供的缩放功能，而是使用操作系统缩放的方法，就是在 QtCreator.exe 上右键->属性->兼容性->更改高 DPI 设置，勾选“替代高 DPI 缩放行为”，缩放执行选择“系统”

![Qt_4](https://gitee.com/pepedd864/cdn-repos/raw/master/img/16.png)

- 这样缩放确实正常，不过字体会变模糊，菜单栏、工具栏字体模糊还能忍，代码编辑器里的字体也会变模糊，这就没法忍了(最好就是设置一下环境变量)

## Qt的安装和VS2022安装Qt拓展的方式

- Qt最后一个免费的版本下载地址：https://download.qt.io/archive/qt/5.14/5.14.2/

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/af9470812dd20a9c6c12819912f75eed.png)

选择系统对应的版本即可

- 安装时，需要输入Qt 账号，如果没有可以选择断网安装的方法

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/3839bed34d8b638982a6886d59f941b7.png)

**安装目录不能带空格和中文，会报错**

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/065eb95359829f0394d28b85893ce933.png)

选择需要的组件

 ![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/97af3f96f2bb890428144ed5bec7cee8.png)

### Qt&VS联合开发

#### 1. 下载拓展

- 选择拓展->点击管理拓展->输入"Qt"搜索->点击"Qt Visual Studio Tools"安装(此处需要科学上网)

 ![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/e1aa4e6c5330d36cba97642e91c273b4.png)
   ![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/615aef788b1e750b203bbdedcf4f0dae.png)

Tips:可以点击右侧的详细信息,使用IDM下载.如果遇到下载完无法安装,可以查看自己的VS下载缓存目录,如果被删了,那么恭喜你,你的VS要重装了

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/63b4f15b3376be4de78b9f4dfff22e48.png)

#### 2. 启用拓展

- 选择拓展->点击Qt VS Tools,此时会显示正在初始化,等待几分钟即可.

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/dda93f981e0bff1b0ed03e913525ba99.png)

点击Qt Versions,选择已安装的Qt目录下的MSVC目录.

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/66c504554bea324de818495f24e74f54.png)

同时确保MSBuild目录为正确的路径,否则你将无法编译程序.

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/cd30049d449681724228d2117f94899b.png)

### VS&Qt开发中文乱码问题

- VS默认ASCII编码，VS编译器在处理中文字符时就会出现乱码。

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/951664b0bf9531f6f93811cab2d2522a.png)



**解决方法：**

1. 在头文件中加入以下代码

```c++
#ifdef WIN32  
#pragma execution_character_set("utf-8")  
#endif
```

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/7038e137773d0a2c9566c3af00fc4c8f.png)

2. 使用以下代码替代单独的中文字符

```c++
this->setWindowTitle(QString::fromLocal8Bit("中文字符"));
```

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/0c052c1d6f22c330a558fa72a6a89262.png)

3. 在中文字符前加上”u8"转换为utf-8编码

````c++
w.setWindowTitle(u8"窗口");
````

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/711de8f0f70598aaa7ea2932d9fb4c6a.png)

### VS QT开发中ui文件无法打开或闪退的问题

---

**问题描述：**

- 双击ui文件无法打开，或者打开后一秒闪退的解决方案

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/5521d9bc7305a8ed13cb8637094d144e.png)

---

**解决方案：**

步骤一：

1. 找到ui文件，点击右键，找到打开方式
2. 选中QT Designer
3. 点击设为默认值
4. 点击确定

出现提示：未能完成操作。未指定的错误

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/4d7c2e5a9a5b235f42554b2308a96fa1.png)

步骤二：

1. 点击“添加”
2. 选择“Qt designer.exe"的目录
3. 点击确定

此时打开的ui文件就不会出现闪退现象

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/fa263b08f32641446c792d50370dd314.png)

### QT VS 项目互换 && 中文乱码

---

#### 1. 项目互换：

1. 导出.pri文件

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/f1e892c06aa24371c9a5f3b29491c8ef.png)

2. 导出.pro文件

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/0349259b92e570980439627c08f8283d.png)

3. 取消勾选创建.pri文件

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/e1873a1b2de75bca4317df57cbae1679.png)

#### 2. 用QT Creator打开项目

1. 在.pro文件中加入

```cmake
greaterThan(QT_MAJOR_VERSION, 4): QT += widgets
```

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/d1378800215f2f454f62b8dbc7977610.png)

### 中文乱码解决方案：

步骤一：

- 在工具->选项->文本编辑器->行为->文件编码中选择UTF-8+BOM

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/3b5d7d69ddeebe128d9fc4c5ce8d4605.png)

步骤二:

- 在VS拓展中下载ForceUTF8 (with BOM)

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/9d821e023335c3b4f1390cc394ff73f2.png)

**如果编译器是MSVC,请在预编译头stdafx.h文件加入**

```c#
# pragma execution_character_set("utf-8")
```

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/1bcc4946bfd90239dd3b782c64404702.png)	

如果没有预编译头文件,则需要在新建文件时勾选创建预处理文件,或者在头文件中加入代码

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/95278e7096b1cf7910946515ff8cfc32.png)

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/0a238c78668279122a882d4b438f53bb.png)

### vs项目添加模块

[项目]=>[项目属性页]=>[Qt project settings]=>[Qt Modules]

![](https://cdn.staticaly.com/gh/pepedd864/cdn-repos@main/img/dcd3d11de57f76b9966d42d568bfb741.png)

下拉=>[select modules]

![](https://cdn.staticaly.com/gh/pepedd864/cdn-repos@main/img/0331575bbb325692dbd81bdba3255dec.png)
