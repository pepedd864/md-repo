## 1. OpenCV 基础

### 1.1 OpenCV 简介

`OpenCV`是一款由`Intel`公司俄罗斯团队发起并参与和维护的一个计算机视觉处理开源软件库，支持与计算机视觉和机器学习相关的众多算法，并且正在日益扩展。

`OpenCV`的优势︰

1. **编程语言**
   `OpenCV`基于`C++`实现，同时提供`python`,`Ruby`, `Matlab`等语言的接口。`OpenCV-Python`是`OpenCV`的`Python APl`，结合了`OpenCV C++API`和`Python`语言的最佳特性。
2. **跨平台**
   可以在不同的系统平台上使用，包括`Windows`，`Linux`，`OS X`，`Android`和`ios`。基于CUDA和OpenCL的高速GPU操作接口也在积极开发中
3. **活跃的开发团队**
4. **丰富的API**
   完善的传统计算机视觉算法，涵盖主流杓机器学习算法，同时添加了对深度学习的支持。

### 1.2 OpenCV-Python

`OpenCV-Python`是一个`Python`绑定库，旨在解决计算机视觉问题。

`Python`是一种由`Guido van Rossum`开发的通用编程语言，它很快就变得非常流行，主要是因为它的简单性和代码可读性。它使程序员能够用更少的代码行表达思想，而不会降低可读性。

与C/C++等语言相比, "`Python`速度较慢。
也就是说，`Python`可以使用C/C++轻松扩展，这使我们可以在C/C++中编写计算密集型代码，并创建可用作`Python`模块的`Python`包装器。
这给我们带来了两个好处:首先，代码与原始`C/C++`代码一样快（因为它是在后台工作的实际C++代码)，其次，在`Python`中编写代码比使用C/C++更容易。`OpenCV-Python`是原始`OpenCV C++`实现的`Python`包装器。

`OpenCV-Python`使用`Numpy`，这是一个高度优化的数据库操作库，具有`MATLAB`风格的语法。所有`OpenCV`数组结构都转换为`Numpy`数组。这也使得与使用`Numpy`的其他库〈如`SciPy`和`Matplotlib`)集成更容易。

### 1.3. OpenCV配置

安装OpenCV之前需要先安装numpy, matplotlib。创建Python虚拟环境cv,在cv中安装即可。
先安装OpenCV-Python,由于一些经典的算法被申请了版权，新版本有很大的限制，所以选用3.4.3以下的版本

```
pip install opencv-python==3.4.2.17
```

现在可以测试下是否安装成功，运行以下代码无报错则说明安装成功。
```python
import cv2
#读一个图片并进行显示(图片路径需自己指定)
lena=cv2.imread("1.jpg")
cv2.imshow("image",lena)
cv2.waitKey(0)
```

如果我们要利用SIFT和SURF等进行特征提取时，还需要安装:
```
pip install opencv-contrib-python==3.4.2.17
```

### 1.4 OpenCV的模块

下面是OpenCV中的各个模块:

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/7cba39c78d94ae0fd9cc53873880166b.png)

其中`core`、`highgui`、`imgproc`是最基础的模块

- **core模块**实现了最核心的数据结构及其基本运算，如绘图函数、数组操作相关函数等。
- **highgui模块**实现了视频与图像的读取、显示、存储等接口。
- **imgproc模块**实现了图像处理的基础方法，包括图像滤波、图像的几何变换、平滑、阈值分割、形态学处理、边缘检测、目标检测、运动分析和对象跟踪等。

对于图像处理其他更高层次的方向及应用，`OpenCV`也有相关的模块实现

- **features2d模块**用于提取图像特征以及特征匹配,`nonfree`模块实现了一些专利算法，如`sift`特征。
- **objdetect模块**实现了一些目标检测的功能，经典的基于`Haar`、`LBP`特征的人脸检测，基于`HOG`的行人、汽车等目标检测，分类器使用`Cascade Classification`(级联分类)"和`Latent SVM`等。

- **stitching模块**实现了图像拼接功能。
- **FLANN模块**（`Fast Library for Approximate Nearest Neighbors`)，包含快速近似最近邻搜索`FLANN`和聚类`Clustering`算法。
- **ml模块**机器学习模块(SVM，决策树，Boosting等等)。
- **photo模块**包含图像修复和图像去噪两部分。
- **video模块**针对视频处理，如背景分离，前景检测、对象跟踪等。
- **calib3d模块**即`Calibration`(校准)3D，这个模块主要是相机校准和三维重建相关的内容。包含了基本的多视角几何算法，单个立体摄像头标定，物体姿态估计，立体相似性算法，3D信息的重建等等。
-  **G-API模块**包含超高效的图像处理`pipeline`引擎

## 2. 基本操作

