# QT

## QMainWindow

- **QMainWindow**是一个为用户提供主窗口程序的类,包含一个菜单栏(**menubar**)、多个工俱栏(**tool bars**)、多个停靠部件(**dock widgets**)、一个状态栏(**statusbar**)及一个中心部件(**central widget**)，是许多应用程序的基础，如文本编辑器，图片编辑器等。

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/0f0b2172ad939579e6c6c00255aa4a16.png)

### 菜单栏

**简单用法**

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/9c439055f9f039290a0fa88df03d2023.png)

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/cbeeee53cf1d5155e82d788966c26cbb.png" style="zoom:150%;" />

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/dcc46fbda07166fbfc4479f2d48bdb89.png)

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/fcaa7fe58dcafa67cf56ada26c0cc4b6.png)

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/e16a6d4f0b3b326700cd8ad0430ae481.png)

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/ebfa41a8d7ed2cc41e3a628c6085bc8f.png)

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/e1759436f2c4ce907560b7aa7ddb7c36.png)

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/e1b697e77d59661a8a809fe4f2f1a33b.png)

**重载函数**

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/d205541630141fe91bc9e73103d7c623.png)

1. 传入一个QMenu的类名

2. 添加一个带标题的菜单

3. 添加一个带图标的菜单

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/81549e725a97cf2628158cf320447e78.png)

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

![QT2](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/0e705bed23ecaffe9cbb553ef3c90bc6.png)



- 在 qt creator 工具->选项中勾选“Enable high DPI scaling”后，菜单栏、工具栏、侧边栏又变得特别大，，似乎是缩放倍数不对，应该放大 1.5 倍，qt creator 放大了 2 倍

![QT1](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/82634e98c85a06e8a0a1e3c1d1a28cf2.png)

- 针对这样的应用缩放异常，我们可以手动调节放大倍数，方法是在 windows 环境变量中创建如下两个环境变量

```shell
QT_AUTO_SCREEN_SCALE_FACTOR = 0
QT_SCREEN_SCALE_FACTORS = 1.5;1
```

![Qt_5](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/0536114875e87f2e0825a0ba8ef176ed.png)

- 不过这样做有个问题：环境变量会影响到其他使用 QT 库的程序，，比如之前显示正常的 Pyside6 中的 Qt Designer 在设置此环境变量后缩放出了问题。

- 所以只能单独给 qt creator 设置上述环境变量才行，方法是新建一个文件 QtCreator.bat ，写入如下内容：

```shell
set QT_AUTO_SCREEN_SCALE_FACTOR=0
set QT_SCREEN_SCALE_FACTORS=1.5;1
C:\Programs\QtCreator\bin\qtcreator.exe
```

- 将应用快捷方式改成QtCreator.bat的路径，这样点击快捷方式便可以直接打开缩放正常的应用。

![Qt_3](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/b55af5beac57c6f17a440ffdf7fc9003.png)

- 另外还有一种不使用 Qt 库提供的缩放功能，而是使用操作系统缩放的方法，就是在 QtCreator.exe 上右键->属性->兼容性->更改高 DPI 设置，勾选“替代高 DPI 缩放行为”，缩放执行选择“系统”

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/8af9380990dbd6597f4cef76d405e8d3.png)

- 这样缩放确实正常，不过字体会变模糊，菜单栏、工具栏字体模糊还能忍，代码编辑器里的字体也会变模糊，这就没法忍了(最好就是设置一下环境变量)

## Qt的安装和VS2022安装Qt拓展的方式

- Qt最后一个免费的版本下载地址：https://download.qt.io/archive/qt/5.14/5.14.2/

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/af9470812dd20a9c6c12819912f75eed.png)

选择系统对应的版本即可

- 安装时，需要输入Qt 账号，如果没有可以选择断网安装的方法

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/3839bed34d8b638982a6886d59f941b7.png)

**安装目录不能带空格和中文，会报错**

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/065eb95359829f0394d28b85893ce933.png)

选择需要的组件

 ![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/97af3f96f2bb890428144ed5bec7cee8.png)

### Qt&VS联合开发

#### 1. 下载拓展

- 选择拓展->点击管理拓展->输入"Qt"搜索->点击"Qt Visual Studio Tools"安装(此处需要科学上网)

 ![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/e1aa4e6c5330d36cba97642e91c273b4.png)
   ![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/615aef788b1e750b203bbdedcf4f0dae.png)

Tips:可以点击右侧的详细信息,使用IDM下载.如果遇到下载完无法安装,可以查看自己的VS下载缓存目录,如果被删了,那么恭喜你,你的VS要重装了

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/63b4f15b3376be4de78b9f4dfff22e48.png)

#### 2. 启用拓展

- 选择拓展->点击Qt VS Tools,此时会显示正在初始化,等待几分钟即可.

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/dda93f981e0bff1b0ed03e913525ba99.png)

点击Qt Versions,选择已安装的Qt目录下的MSVC目录.

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/66c504554bea324de818495f24e74f54.png)

同时确保MSBuild目录为正确的路径,否则你将无法编译程序.

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/cd30049d449681724228d2117f94899b.png)

### VS&Qt开发中文乱码问题

- VS默认ASCII编码，VS编译器在处理中文字符时就会出现乱码。

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/951664b0bf9531f6f93811cab2d2522a.png)



**解决方法：**

1. 在头文件中加入以下代码

```c++
#ifdef WIN32  
#pragma execution_character_set("utf-8")  
#endif
```

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/7038e137773d0a2c9566c3af00fc4c8f.png)

2. 使用以下代码替代单独的中文字符

```c++
this->setWindowTitle(QString::fromLocal8Bit("中文字符"));
```

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/0c052c1d6f22c330a558fa72a6a89262.png)

3. 在中文字符前加上”u8"转换为utf-8编码

````c++
w.setWindowTitle(u8"窗口");
````

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/711de8f0f70598aaa7ea2932d9fb4c6a.png)

### VS QT开发中ui文件无法打开或闪退的问题

---

**问题描述：**

- 双击ui文件无法打开，或者打开后一秒闪退的解决方案

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/5521d9bc7305a8ed13cb8637094d144e.png)

---

**解决方案：**

步骤一：

1. 找到ui文件，点击右键，找到打开方式
2. 选中QT Designer
3. 点击设为默认值
4. 点击确定

出现提示：未能完成操作。未指定的错误

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/4d7c2e5a9a5b235f42554b2308a96fa1.png)

步骤二：

1. 点击“添加”
2. 选择“Qt designer.exe"的目录
3. 点击确定

此时打开的ui文件就不会出现闪退现象

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/fa263b08f32641446c792d50370dd314.png)

### QT VS 项目互换 && 中文乱码

---

#### 1. 项目互换：

1. 导出.pri文件

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/f1e892c06aa24371c9a5f3b29491c8ef.png)

2. 导出.pro文件

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/0349259b92e570980439627c08f8283d.png)

3. 取消勾选创建.pri文件

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/e1873a1b2de75bca4317df57cbae1679.png)

#### 2. 用QT Creator打开项目

1. 在.pro文件中加入

```cmake
greaterThan(QT_MAJOR_VERSION, 4): QT += widgets
```

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/d1378800215f2f454f62b8dbc7977610.png)

### 中文乱码解决方案：

步骤一：

- 在工具->选项->文本编辑器->行为->文件编码中选择UTF-8+BOM

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/3b5d7d69ddeebe128d9fc4c5ce8d4605.png)

步骤二:

- 在VS拓展中下载ForceUTF8 (with BOM)

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/9d821e023335c3b4f1390cc394ff73f2.png)

**如果编译器是MSVC,请在预编译头stdafx.h文件加入**

```c#
# pragma execution_character_set("utf-8")
```

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/1bcc4946bfd90239dd3b782c64404702.png)	

如果没有预编译头文件,则需要在新建文件时勾选创建预处理文件,或者在头文件中加入代码

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/95278e7096b1cf7910946515ff8cfc32.png)

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/0a238c78668279122a882d4b438f53bb.png)

### vs项目添加模块

[项目]=>[项目属性页]=>[Qt project settings]=>[Qt Modules]

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/dcd3d11de57f76b9966d42d568bfb741.png)

下拉=>[select modules]

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/0331575bbb325692dbd81bdba3255dec.png)



### vs qt打包exe方法

项目在VS+Qt联合开发环境下、使用[qwt](https://so.csdn.net/so/search?q=qwt&spm=1001.2101.3001.7020)工具库；因此项目中需要分三步打包；

在实现之前将可执行文件(`.exe`)文件单独放到一个文件夹中，本步骤中的目标项目为`C:\\项目名称`；

1、Qt 查找项目中使用到的qt[动态链接库](https://so.csdn.net/so/search?q=动态链接库&spm=1001.2101.3001.7020)；

步骤如下

①打开项目使用的windeployqt工具[如本文使用的：`Qt 5.12.0 64-bit for Desktop`；

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/4a1196146daa1e6aa874e8c8a053cc9f.png" style="zoom:50%;" />

②CMD命令 `cd` 进入到项目所在根目录；使用`c:`切换盘符

③CMD命令 `cd` 进入到`x64/Debug`或`Release` 文件夹下 ，该文件夹包含`ProjectName.exe`；

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/4c06652d09e5ecc94658827db0740f90.png)

④使用命令：`windeployqt ProjectName.exe` (在目标文件夹所在目录下执行该命令)；

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/19648590d9ea7893cee2001e6740271e.png)

可以看到依赖文件已添加到目录下

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/734c9c68fdd8a1b5cc4f917f1c3e101c.png)



# Visual Studio

## 修改默认的目录配置问题

默认vs的工程项目源文件都是在同一级目录下，使用vs内部的过滤器管理，实际在硬盘的文件还是原样，因此需要设置目录

**接下来是设置的方法**

1. 首先，按照需要的目录结构创建对应的过滤器

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/29a2ee2ae7074a87ab7e9e3b03646aeb.png" style="zoom:50%;" />

2. 创建对应的文件夹

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/fbaea3bc23989cf6dd29cad1d8ac4b01.png" alt="" style="zoom:50%;" />

3. 设置附加包含目录

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/869cf1d1dfe0b364ae1539c795c4c909.png" style="zoom:50%;" />

4. 注意有可选的宏，可保证项目在不同的目录下也可正常编译

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/c605995b3705e71e40ad05ad5f11c8e7.png" alt="" style="zoom:50%;" />

5. 因为VS可联合QT开发，因此如果选用了QT的预编译头文件选项，需要添加对应的目录

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/659cbd6e2397c40d4aebb3ab0500729d.png" style="zoom:50%;" />

6. 最后将所有文件加入到过滤器和实际的文件目录中

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/9d2f68228d0471de8ba16133a0b4e369.png" alt="" style="zoom:50%;" />

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/e8c591cfe1e491ef8e47e9f07d944c15.png" style="zoom:50%;" />

7. 根据目录层级修改引用头文件

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/63e8d7d2f1e15c1b4338403426054f25.png" alt="" style="zoom:50%;" />

