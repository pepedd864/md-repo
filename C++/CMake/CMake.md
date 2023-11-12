## 1. 安装配置CMake

### 1.1 安装TDM-GCC编译器

TDM-GCC官网https://jmeubank.github.io/tdm-gcc/download/

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/38e879fa742f21ec54226435d14120b8.png)

安装步骤省略。。。



配置环境变量

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/f9a9c697abe2f2534ef3f3f02e1b104a.png" style="zoom:50%;" />

运行命令检查是否能够正常运行

1. `gcc -v`

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/b3030e03759f3c1259edd4aecc4f76aa.png" alt="" style="zoom: 50%;" />

2. `make -v`

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/e8dd491488c9456351187f72553bd15c.png)

3. 如果无法正常运行`make`命令，可以到`bin`目录下修改`mingw-make.exe`为`make.exe`

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/f41ccbd8789f9c9d98adcc0cd41639be.png" alt="" style="zoom:50%;" />



### 1.2 安装CMake

CMake官网https://cmake.org/download/

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/5dfbbf016b1541a2e676b41b4b140c2a.png)



安装步骤省略。。。



配置环境变量

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/9336a23aeab5a9b4e547ad9abf8b8f4e.png" alt="" style="zoom:50%;" />

运行命令检查是否能够正常运行

1. `cmake -version`

   ![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/b86f6b7c740af15a1c66d53b843bf23d.png)

   



## 2. 使用vscode+cmake进行c/c++开发

1. 安装vscode，省略

2. 安装cmake-tools插件

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/8d5c18a5b6d577c41bd2be74c7530cf3.png)

3. 新建一个目录，按照图中创建文件，添加CMake配置和c测试代码

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/aec20f4029ccd3679e8dbebda3ccb272.png)

4. 注意CMake配置文件的命令为`CMakeLists.txt`

5. 使用CMake插件进行项目配置

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/8a1a48863322f826f6fcc794d0232e91.png)

6. 选择GCC编译器

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/f9594c51fdbc5d4f823a8113c4b4e9de.png)

7. 如果安装有Visual Studio也可使用Visual Studio进行开发

8. 输出窗口显示成功配置

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/8fff6e43b818e0bf86cff9d3abfd8b85.png)

9. 编译运行文件

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/43c9036c5930f0281e8212bd8da8674a.png)

10. 成功打印

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/ecedb11aa65683f13e7b7476dbf1bdb3.png)

11. 如果有配置其他库需要引入，例如使用easyx，也可参考如下的CMake配置

```cmake
cmake_minimum_required(VERSION 3.25)
project(CMAKE-DEMO-2)
set(EasyX_INC C:\\TDM-GCC-64\\include) # 你的include地址
set(EasyX_LINK C:\\TDM-GCC-64\\lib\\x64) # 找与自己的环境配置对应的版本
set(CMAKE_CXX_STANDARD 17)
include_directories(${EasyX_INC})
link_directories(${EasyX_LINK})
#在lib对应的文件夹里面找lib文件（一般只有EasyXa和EasyXw这两个，进行链接）
link_libraries(libeasyx.a)
add_executable(CMAKE-DEMO-2 src/main.cpp)
```

12. 编写测试代码

```c++
#include <stdlib.h>
#include <easyx.h>

int main() {
  initgraph(800, 600);
  // easyx demo
  setbkcolor(WHITE);
  cleardevice();
  settextcolor(BLACK);
  settextstyle(50, 0, _T("宋体"));
  outtextxy(270, 240, _T("Hello, world!"));
  system("pause");
  closegraph();
  return 0;
}
```

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/364ecba335f53a6b965ab58195a522e0.png)

