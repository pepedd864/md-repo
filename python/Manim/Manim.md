Manim是youtube数学视频频道3b1b作者Grant Sanderson用于制作视频的动画引擎，在GitHub上他这样描述这个引擎

> Manim是一个用于精确编程动画的引擎，旨在创建解释性的数学视频。

Manim使用Python语言编程，程式的引擎使得其非常适合数学和编程科普视频的制作。另外，Manim还包括有非常多的动画预设，支持3D场景的铺设。

目前Manim有三个版本分别是

- ManimCairo
- ManimCE
- manimGL

这里使用的是manimGL

## 1. 安装

前置环境要求（必须）

- 电脑已安装ffmpeg且配置环境变量，运行`ffmpeg -version`查看是否正确配置
- LaTeX，在清华源下载安装https://mirrors.tuna.tsinghua.edu.cn/CTAN/systems/texlive/Images/

**安装方法一（推荐）：**

选择一个目录作为视频制作项目的目录，然后使用git执行下面命令

```bash
git clone -b master https://github.com/3b1b/manim.git
```

进入`manim`文件夹，运行cmd，执行下面命令

```bash
pip install -e .
```

此时完成了manim的安装

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/aa492027999d5d5499da2c138006776f.png)

运行命令

```bash
manimgl example_scenes.py OpeningManimExample
```

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/e1321e9b9abffafe0209e69c9f9ee0e2.png)

正常情况下，弹出的窗口在屏幕右上方，并且标题栏溢出屏幕外，无法调整位置，所以需要在项目下配置窗口位置。

打开manim目录下manimlib文件夹下的`default_config.yml`文件

找到`window_position`，默认为UR，要使窗口位于屏幕中间则改为OO

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/2b2555f65cf2b80b46334c5b54574185.png)



**安装方法二：**

打开命令提示符，输入以下命令

```bash
pip install manimgl
```

安装完成后运行下面命令，无报错即成功安装

```bash
manimgl
```

为什么不推荐这种安装方法

- 使用pip安装，manimlib文件夹位于python的site-packages目录下，在后期配置时会不方便
- pip安装的manimlib还是manimCairo版本下的，在**某些新特性方面会有问题**

## 2. 入门

在之前克隆的仓库文件夹下，保留manimlib文件夹，其余文件删除，使manim文件夹的目录结构如下

```
manim/
├── manimlib/
│   ├── animation/
│   ├── ...
│   ├── default_config.yml
│   └── window.py
├── (custom_config.yml)
└── start.py
```

新建start.py文件，写入以下代码

```py
from manimlib import *

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_stroke(BLUE_E, width=4)

        self.add(circle)
```

然后运行下面命令

```bash
manimgl start.py SquareToCircle
```

正常运行结果

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/14d793874588bfd9dcff24c4d42e4464.png)

修改代码如下

```py
from manimlib import *

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_stroke(BLUE_E, width=4)
        square = Square()

        self.play(ShowCreation(square))
        self.wait()
        self.play(ReplacementTransform(square, circle))
        self.wait()
```

你将得到两个文件夹`/images`和`/videos`，里面存放了渲染好的视频和图片

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/f89378813c5e039649a4f9e22784754b.png)

**manimgl新版本支持交互新特性（在pip工具安装的manimlib中没有此特性，故运行时会报错）**，在上面代码末尾加上如下代码启用交互

```py
self.embed()
```

这时再执行 `manimgl start.py SquareToCircle`。

动画运行完毕后，终端显示如下

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/411efddfd8ce6da0e61713a8e48fad4a.png)

此时在终端可以输入代码，逐行运行

```py
# 在水平方向上拉伸到四倍
play(circle.animate.stretch(4, dim=0))
# 旋转90°
play(Rotate(circle, TAU / 4))
# 在向右移动2单位同时缩小为原来的1/4
play(circle.animate.shift(2 * RIGHT), circle.animate.scale(0.25))
# 为了非线性变换，给circle增加10段曲线（不会播放动画）
circle.insert_n_curves(10)
# 给circle上的所有点施加f(z)=z^2的复变换
play(circle.animate.apply_complex_function(lambda z: z**2))
# 关闭窗口并退出程序
exit()
```

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/90c4fa64a86b8ca57520009a855641ab.png)

到这里manim的基本使用就介绍完毕，更多内容参考中文文档https://docs.manim.org.cn/index.html
