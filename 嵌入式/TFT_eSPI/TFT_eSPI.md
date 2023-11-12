

## 1.TFT_eSPI库的安装和配置

### 1.1 安装

platformio安装和配置

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/476ea790cb6e19e43f7b9c532417489d.png)

使用库需要包含头文件

```c
#include <TFT_eSPI.h>
```

要修改的文件

```
./.pio/libdeps/../TFT_eSPI/User_Setup.h
```

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/10b30f0a7a823564147aafea299e793e.png)



### 1.2 选择芯片及屏幕大小

- 选择芯片驱动，把使用的芯片前面的注释去掉

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/7477fc09c751fd35751a2649a7596a96.png)

- 设置屏幕大小

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/713d096f956b0e40406876b44baab3ce.png)



### 1.3 屏幕颜色异常矫正

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/33471953baa7c4e1441c423c1e8cbd67.png)



![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/2e8becc69ff2bd47e37447981615fb33.png)



### 1.4 TFT_eSPI引脚的定义

#### 1.4.1 SPI连接模式

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/09a7d82729de558dcfd5ddd81564e927.png)



| 序号 | 引脚 | 说明                                                  |
| ---- | ---- | ----------------------------------------------------- |
| 1    | VCC  | 液晶屏电源正(3.3V~5V)                                 |
| 2    | GND  | 液晶屏电源地                                          |
| 3    | GND  | 液晶屏电源地                                          |
| 4    | NC   | 无定义，保留                                          |
| 5    | NC   | 无定义，保留                                          |
| 6    | NC   | 无定义，保留                                          |
| 7    | CLK  | 液晶屏SPI总线时钟信号                                 |
| 8    | SDA  | 液晶屏SPI总线写数据信号                               |
| 9    | RS   | 液晶屏寄存器/数据选择信号，低电平:寄存器，高电平:数据 |
| 10   | RST  | 液晶屏复位信号，低电平复位                            |
| 11   | CS   | 液晶屏片选信号，低电平使能                            |

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/a0937c6811200e6b91be71498d10de9e.png" style="zoom:50%;" />

| 程序     | 引脚 |
| -------- | ---- |
| TFT_MISO | 无   |
| TFT_MOSI | SDA  |
| TFT_SCLK | CLK  |
| TFT_CS   | CS   |
| TFT_DC   | RS   |
| TFT_RST  | RST  |
| FTF_BL   | 无   |



#### 1.4.2 8位并口连接模式

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/33b6c583a7668c039967236f26a52bc7.png)



| 序号 | 引脚标号 | 说明                                               |
| ---- | -------- | -------------------------------------------------- |
| 1    | LCD_RST  | LCD总线复位信号，低电平复位                        |
| 2    | LCD_CS   | LCD总线片选信号，低电平使能                        |
| 3    | LCD_RS   | LCD总线命令/数据选择信号，低电平:命令，高电平:数据 |
| 4    | LCD_WR   | LCD总线写信号                                      |
| 5    | LCD_RD   | LCD总线读信号                                      |
| 6    | GND      | 电源地                                             |
| 7    | 5V       | 5V电源输入                                         |
| 8    | 3V3      | 3.3V电源输入，此引脚可不接                         |
| 9    | LCD_D0   | LCD 8位数据Bit0                                    |
| 10   | LCD_D1   | LCD 8位数据Bit1                                    |
| 11   | LCD_D2   | LCD8位数据Bit2                                     |
| 12   | LCD_D3   | LCD 8位数据Bit3                                    |
| 13   | LCD_D4   | LCD8位数据Bit4                                     |
| 14   | LCD_D5   | LCD8位数据Bit5                                     |
| 15   | LCD_D6   | LCD8位数据Bit6                                     |
| 16   | LCD_D7   | LCD 8位数据Bit7                                    |
| 17   | SD_SS    | SD卡SPI总线片选信号，低电平使能                    |
| 18   | SD_DI    | SD卡SPI总线MOSI信号                                |
| 19   | SD_DO    | SD卡SPI总线MISO信号                                |
| 20   | SD_SCK   | SD卡SPI总线时钟信号                                |

LCD_RS就是程序中定义的TFT_DC



<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/1db8489923eb74fed3766f11f1c74985.png" style="zoom:50%;" />



### 1.5 TFT_eSPI库初始化

```c
#include <SPI.h>
#include <TFT_eSPI.h>

TFT_eSPI tft = TFT_eSPI();	//创建TFT对象

tft.init();					//初始化

tft.setRotation(1);			//0-3 顺时针转0度、90度、180度、270度
tft.fiilScreen(TFT_BLACK);	//设置屏幕背景颜色
```



## 2. TFT_eSPI坐标系与颜色系统

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/21a601ca3d1f9964eff9f5a7eecdc9ab.png" style="zoom:50%;" />



TFT_eSPI的颜色模式是RGB565色彩模式

R原色占用5 bit ,G原色占用6 bit , B原色占用5 bit,即每像素点占用5+6+5= 16 bit，对应一个两字节的无符号整数

```c
uint16_t color565(uint8_t red,uint8_t green,uint8_t blue);
```



将常规的RGB转换成RGB565

```c
uint16_t red = tft.color565(255,0,0);
uint16_t green = tft.color565(0,255,0);
uint16_t blue = tft.color565(0,0,255);
uint16_t yellow = tft.color565(255,255,0);
```



## 3. TFT_eSPI字体文字常用函数

### 3.1 TFT_eSPI自带字体

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/7a602f0cacde83883c33ebb5006c3323.png)



### 3.2 光标位置和文本相关函数

光标位置和字体

- `setCursor(int16_t x, int16_t y)`将光标位置设置为x和y

- `setCursor(int16_t x, int16_t y, uint8_t font)`将光标位置设置为x和y,字体为font

- `getCursorx(void)`
  `getCursorY(void)`
  获取光标位置，X，Y



文本相关函数

- `textWidth(const String& string)`
  返回字符串在当前字体下的像素宽度
- `textWidth(const String& string , uint8_t font)`返回字符串在字体font下的像素宽度
- `fontHeight(int16_t font)`return the height of a font (yAdvancefor free fonts)
- `fontHeight(void)`
- `setTextSize(uint8_t s)`
  设置文本放大倍数,S是1-7之间的数字，实测对自定义字体无效
- `setTextColor(uint16_t c)`
  设置文本的颜色，背景色不会被重写
- `setTextColor(uint16_t c, uint16_t b)`设置文本的颜色及其背景
- `setTextWrap(boolean wrapX, boolean wrapY=false)`
  设置文本是否换行(使用print系列函数)，不设置时轴默认会换行,drawString系列函数都不会换行
- `setTextPadding(uint16_t x_width)`
  设置填充宽度，擦除原来的文字和数字(就是在字符串后面加上一个长width的色块)
- `getTextPadding(void);`



### 3.3 设置文本的基准（drawString）

- `setTextDatum(uint8_t d)`
  设置文本基准（相对于光标坐标）
- `getTextDatum(void)`
  获取文本基准

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/c22178baee9367080d326eb789408023.png" style="zoom:67%;" />



![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/6ad95dacfd27c352b61a3a0a8e2da8db.png)



### 3.4 输出文字使用的函数

- `setTextFont(uint8_t f)`
  设置字体
-  `loadFont(const uint8_t array[])`
  加载自定义字体
- `unloadFont(void)`
  释放字库文件
- `print()`
  `println()`
  `printf()`
  以上三个函数默认在x轴碰到末尾时自动换行



<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/1d650e52e1d6f311e61792e77a137bf0.png" style="zoom:67%;" />

### 3.5 输出文字例子

```c
tft.init();

tft.fillScreen(TFT_BLACK);
tft.setTextColor(TFT_WHITE,TFT_BLACK);	//设置字体前景和背景色
tft.setTextFont(2);				//设置字体
tft.println("hello world");		//输出

tft.drawString("ESP32 using TFT_eSPI.",0,50,2);
tft.setTextFont(4);
tft.drawNumber(2023,0,70);
tft.drawFloat(3.1415926,5,0,90);
```

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/d66e5e630b863b422cdb887ffca27266.png" style="zoom:50%;" />



### 3.6 自定义字体库

- TFT_eSPI默认不支持中文字体，想要显示中文及图标，僬侥自定义字体库
- 先下载processing软件，解压
  https://processing.org/download
- 打开生成字库软件

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/7e987743244229c06ac78a2820220f5e.png" style="zoom:50%;" />

- 选择processing-java路径和选择的字体
- 生成字库，将生成的.h文件复制到项目文件夹下，包含，就可以使用了

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/831e17365fb05fbbc1d29bb018aca9da.png" style="zoom:67%;" />

- 使用完字体后，卸载字体即可



### 3.7 输出图标字体的方法

- 制作图标字体的自定义字库
- 使用tft.drawGlyph(unicode编码)来镜像输出

- 选择图标字体生成字库，这里选择的是系统自带的 Segoe MDL2 Assets

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/7b6d403fc198551bbfc8e364a8adfed1.png" style="zoom:67%;" />

- 复制字库文件到项目文件夹下，使用`#include ""`包含在内

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/a08ccc8dd959d92a40e67729ad0b9d41.png" style="zoom:67%;" />



### 3.8 TFT_eSPI使用SD卡字库

- TFT_eSPI库自带了一个加载SD卡vlw字库的方法，但只适用于小容量的字库，对于大容量的字库绝对板子不停重启
- 为了使用SD卡字库，我们继续使用之前U8G2库中一位网友制作的库进行魔改，把它起名为ESDFont，为了和之前的TSDFont相区分开
- ESDFont库使用的是SdFat的SD卡库
- 使用过程:
  - 使用GuiTool软件制作.bin字库
  - 将bin字库存放到sd卡上
  - 定义全局ESDFont对象
  - 初始化ESDFont对象
  - 加载字库
  - 输出文字或图标

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/d2ce4d47325965668b688b57f078582f.png)



## 4. TFT_eSPI图形绘制

### 4.1 画点和背景

- `drawPixel(int32_t x, int32_t y, uint32_t color);`
  - 画点
- `fillScreen(uint32_t color);`
  - 用color颜色填充整个屏幕

### 4.2 画直线

- `drawLine(int32_t xs,int32_t ys,int32_t xe,int32_t ye,uint32_t color)`
  - 过(xs,ys) (xe,ye)点画线
- `drawFastVline(int32_t x, int32_t y, int32_t h, uint32_t color);`
  - 从(x,y)开始画长为h的垂直的线
- `drawFastHline(int32_t x, int32_t y, int32_t w, uint32_t color);`
  - 从(x,y)开始画长为w的水平的线

 

```c
tft.drawLine(20,20,200,200,TFT_RED);
tft.drawFastHLine(20,20,180,TFT_GREEN);
tft.drawFastVLine(20,20,180,TFT_YELLOW);
```



<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/f65fe046d1054c4d8c0fd14959383845.png" style="zoom:50%;" />



### 4.3 画矩形

- `fillRect(int32_t x, int32_t y, int32_t w, int32_t h,
  uint32_t color ) ;`
  - 实心的矩形,填充color 左上角(×,y)宽w高h
- `drawRect(int32_t x, int32_t y, int32_t w, int32_t h, uint32_t color);`
  - 空心的矩形,边是color 左上角(x,y)宽w高h



```c
tft.fillRect(20,20,200,100,TFT_GREEN);
tft.drawRect(20,150,200,100,TFT_GREEN);
```



<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/0dab2074fd512cedf917599f7887a697.png" style="zoom:50%;" />



### 4.4 圆角矩形

- `drawRoundRect(int32_t x, int32_t y, int32_t w, int32_t h， int32_t radius, uint32_t color);`
  - 实心的矩形，填充color左上角(x,y)宽w高h，4个角的半径为radius
- `fillRoundRect(int32_t x, int32_t y, int32_t w, int32
  t h, int32_t radius, uint32_t color);`
  - 空心的矩形，边是color左上角(x,y)宽w高h ,4个角的半径为radius

```c
tft.fillRoundRect(20,20,200,100,8,TFT_GREEN);
tft.drawRoundRect(20,150,200,100,9,TFT_GREEN);
```

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/58e42c350755b6333e187ac528e83428.png" style="zoom:50%;" />



### 4.5 渐变矩形

- `fillRectVGradient(int16_t x, int16_t y, int16_t w, int16_t h,uint32_t color1, uint32_t color2);`
  - 实现的矩形，填充的颜色在垂直方向由color1渐变到color2
- `fillRectHGradient(int16_t x, int16_t y, int16_t w, int16_t h, uint32_t color1, uint32_t color2);`
  - 实现的矩形,填充的颜色在水平方向由color1渐变到color2

 ```c
 tft.fillRectVGradient(20,10,200,100,TFT_GREEN,TFT_BLUE);
 tft.fillRectHGradient(20,30,200,100,TFT_GREEN,TFT_BLUE);
 ```

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/855fa273c1c38ca2ee9205c97e94b567.png" style="zoom:50%;" />



### 4.6 画圆

- `drawSpot(float ax,float ay, float r, uint32_t fg_color,uint32_t bg_color =0x00FFFFFF);`
  - 画个小圆点，圆心(ax，ay)半径r，边框颜色fg_color，填充bg_color
- `drawCircle(int32_t x, int32_t y, int32_t r, uint32_t color);`
  - 画个空心圆，圆心(×,y)半径r，边颜色color
- `drawCircleHelper(int32_t x, int32_t y, int32_t r, uint8_t cornername,uint32_t color);`
  - 画个指定部分的空心圆，圆心(x,y)半径r边颜色color
  - cornername  0x01 左上角  0x02右上角  0x04 右下角  0x08左下角

- `fillcircle(int32_t x, int32_t y, int32_t r, uint32_t color`
  - 画个实心圆.圆心( x, y)半径r填充颜色color
- `fillCircleHelper(int32_t x, int32_t y, int32_t r, uint8_t cornername，int32_t delta,uint32_t color);`
  - 画个指定部分的半圆，圆心(x,y)半径r填充颜色color，delta在x轴方向增加的量
  - cornername  0x1 画上半圆  0x2画下半圆

```c
tft.drawSpot(50，50，40，TFT_BLUE，TFT_YELLOw);
tft.drawCircle(50，150，50，TFT_GREEN);
tft.fillcircle(170，150，50，TFT_GREEN);
tft.drawCircleHelper(50，270，50，5，TFT_GREEN);
tft.fillcircleHelper(170，270，50，3，10，TFT_GREEN);
```

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/0009333241c0a69219884c06198106bb.png" style="zoom:50%;" />



### 4.7 画椭圆

- `drawEllipse(int16_t x， int16_t y, int32_t rx，int32_t ry, uint16_t color);`
  - 画空心椭圆，中心(x,y) x轴长rxy轴长ry边颜色color
- `fillEllipse(int16_t x, int16_t y, int32_t rx, int32_t ry, uint16_t color);`
  - 画实心椭圆，中心(x,y)x轴长rxy轴长ry填充颜色color



```c
tft.drawEllipse(100,100,80,50,TFT_GREEN);
tft.fil1E1lipse(100,220,80,50,TFT_GREEN);
```

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/89296a41689351a1a7dda397237423d4.png" style="zoom: 50%;" />



### 4.8 画三角形

- `drawTriangle(int32_t x1,int32_t y1， int32_t x2,int32_t y2,int32_t x3,int32_t y3, uint32_t color);`
  - 连接三个点画空心三角形
- `fillTriangle(int32_t x1,int32_t y1, int32_t x2,int32_t y2,int32_t x3,int32_t y3,uint32_t color);`
  - 连接三个点画实心三角形



```c
tft.drawTriangle(30,30,120,50,80,150,TFT_GREEN);
tft.fillTriangle(30,180,120,200,80,300,TFT_GREEN);
```

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/15a0758e77d1fe428fd2eeed9dc2508f.png" style="zoom:50%;" />



### 4.9 画粗线

- `drawWideLine(float ax,float ay,float bx,float by,float wd,uint32_t fg_color,uint32_t bg_color =0x0OFFFFFF);`
  - 从(ax,ay)）到(bx,by)画一条线宽为wd的直线，边颜色bg_color填充颜色fg_color
- `drawWedgeLine(float ax，float ay，float bx，float by,float
  aw,float bw, uint32_t fg_color,uint32_t bg_color = 0x0BFFFFFF);`
  - 从(ax,ay)到(bx,by)画一条直线, a点处线粗aw， b点处线粗bw，边颜色bg_color填充颜色fg_color

```c
tft.drawWedgeLine(30,30,220,200,5,9,TFT_GREEN,TFT_BLUE);
tft.drawWideLine(0,60,220,230,6,TFT_GREEN,TFT_BLUE);
```

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/dffe5fa86a0f19d5e67b0eee6020f696.png" style="zoom:50%;" />



### 4.10 视口(viewport)

- 可以把视口定义为我们屏幕上一小块区域（虚拟的TFT屏幕）
- 视口的坐标系和常规屏幕的坐标系是一样的（左上角是0,0）
- 只要定义了视口后， tft的所有绘制函数都是在视口里进行的，它就像—块真实的屏幕一样，使用的坐标要看setViewport时的vpDatum的实
  参，如果不传的话，默认使用视口的坐标系

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/ca1b8c067445fc9a7575db9ede23f4ee.png" style="zoom:50%;" />



<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/10b6ac1a7e777e9720339a38168b447a.png" style="zoom:67%;" />



#### 4.10.1 视口例子

```c
void drawCircle()
{
  tft.drawCircle(30, 30, 20, TFT_GREEN);
}

void setup()
{
  tft.init();                //初始化
  tft.fillScreen(TFT_BLACK); //填充屏幕
  drawCircle();
  tft.drawRect(150, 150, 70, 70, TFT_RED);
  tft.setViewport(150, 150, 70, 70);
  drawCircle();
  tft.setTextFont(2);
  tft.setCursor(2, 2);
  tft.println("viewport");

  tft.resetViewport();
  tft.drawRect(0, 150, 70, 70, TFT_RED);
  tft.setViewport(0, 150, 70, 70, true);
  drawCircle();
  tft.drawLine(0, 35, 70, 35, TFT_YELLOW);
  tft.frameViewport(TFT_BLUE, -10);
}
```

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/d07b391d100c649d225c056ecc09a086.png" style="zoom: 50%;" />



### 4.11 图片绘制

#### 4.11.1 图片函数

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/bf2bc7e99113998e04caa625c3d5bab5.png" style="zoom:67%;" />

#### 4.11.2 图片取模

- 将图片裁剪成小于你屏幕大小的位图(bmp)
- 用取模软件进行取模
- 取模软件下载地址: https://lcd-image-converter.riuson.com/
- 制作一个.h的文件，如：
  - <img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/e48469e0f29491f3d7f2fe3e338f02fb.png" style="zoom:50%;" />

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/ec55e0ea55748eaa1851653c070cbd8e.png" style="zoom:67%;" />



#### 4.11.3 图片绘制

```c
#include <SPI.h>
#include <TFT eSPI.h>
#include "pic.h"

TFT_eSPI tft =TFT.eSPI();

void setup(void) {
	serial.begin(115200);
    tft.init();
	tft.fillScreen(TFT_BLACK);
    
	auto a = millis();
	tft.setSwapBytes(true);
	tft.pushImage(0,e,240,320,pic);
    auto b = millis();
	Serial.println(b-a);
}
void loop(){
    
}
```



<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/a4c4b780e4461bc4e75a7e6f1328a514.png" alt="" style="zoom:50%;" />



## 5. 屏幕刷新的方式

关于屏幕的刷新
有两种方案:

- 每次绘制新图形时，用fillScreen函数刷下背景，然后再画图(结果:刷新率极低，无法直视)
- 每次绘制新图形时，先图出该图形，一定时间后，再用背景色绘制一次(结果∶结果还可以接受)



```c
//方式一
tft.fillRect(TFT_BLUE);
...一段操作后
tft.fillSrceen(TFT_BLACK);
tft.fillRect(TFT_BLUE);

//方式二
tft.fillRect(TFT_BLUE);
delay(30);
tft.fillRect(TFT_BLACK);
```



## 6. 使用MPU6050陀螺仪控制显示立方体案例

### 6.1 实验内容

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/f6e2c55519cf81097873e7b153380a2d.png" style="zoom:67%;" />

使用MPU6050接收陀螺仪的数据,用来控制屏幕中的立方体同步运动。



### 6.2 MPU6050简介

简介

- 供电电源:3-5v(内部低压差稳压)
- 通信方式:标准IC通信协议
- 陀螺仪范围: ±250 500 1000 2000 /s
- 加速度范围:±2+4+8+16g

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/f4b48a3f1e2ae79acc59db3bb86cf1b3.png" style="zoom:50%;" />

用MPU6050可以获取到模块瞬时的加速度和角速度

本次使用主要是使用MPU 6050获得模块在x,y,z轴旋转的角度

要通过不停地采样角速度进行积分运算来获得当前旋转的度，但是由于各种原因Y轴存在飘移现象，这个问题我们不讨论。

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/cb3c08cf55b20ba16883da10f4f30976.png" style="zoom:50%;" />



### 6.3 MPU6050_light库

操作MPU 6050的库非常多，这里选了个比较简单的库(MPU6050_light),可以直接获取当前模块旋转的角度值(x,y,z轴)

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/edf6767313476dcc2c9b670de23b5a13.png" style="zoom:67%;" />

```c
#include <MPU6050_light.h>

MPU6050 mpu(wire);

Wire.begin(14,27);	//GPIO口
mpu.begin();
mpu.calcGyroOffsets();

mpu.update();//每次读取前更新下
double xa = mpu.getAnglex();//x轴角度（度)
double ya = mpu.getAngleY();
double za = mpu.getAnglez();
```



### 6.4 图形学

#### 6.4.1 齐次坐标系

齐次坐标就是将一个原本是n维的向量用一个n+1维向量来表示

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/15b185d1be2bcb3ee68db44d71ef40f5.png" style="zoom:50%;" />



平面上的点(x,y)表示为(x, y, 1)
三维空间上的点(x,y,z)表示为(x, y,z,1)
我们在后续的算法中点都是以行向量来表示的

**任何一个点的基本变换都可以用行向量(齐次坐标)乘以一个变换矩阵的方式来表示**
$$
[x^* & y^* & 1] = [x & y & 1]\times\left[\begin{matrix}a_1 & a_2 & 0\\ b_1 & b_2 & 0\\ c_1 & c_2 & 1\end{matrix}\right]
$$


#### 6.5.2 二维图形-平移变换

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/35ffca7d9ad44870bdb4284dda014c47.png" style="zoom:67%;" />

$$
[x^* & y^* & 1]=[x & y & 1]\times\left[\begin{matrix}1 & 0 & 0\\0 & 1 & 0\\T_x & t_y & 1\end{matrix}\right]
$$


#### 6.4.3 二维图形-缩放变换

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/bab3f8571ba2d5cee444fbd1be6c7905.png" style="zoom:67%;" />

相对于坐标原点沿x方向放缩Sx倍，沿y方向放缩Sy倍。S>1放大,S<1缩小。

$$
[x^* & y^* & 1]=[x & y & 1]\times\left[\begin{matrix}S_x & 0 & 0\\0 & S_x & 0\\0 & 0 & 1\end{matrix}\right]
$$


#### 6.4.4 二维图形-旋转变换

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/ab67d3926c0b5e87bb07c6bc2e86e944.png" style="zoom:67%;" />




$$
[x^* & y^* & 1]=[x & y & 1]\times\left[\begin{matrix}\cos\theta & \sin\theta & 0\\-\sin\theta & \cos\theta & 0\\0 & 0 & 1\end{matrix}\right]
$$




#### 6.4.5 二维图形-对称变换

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/1c95f50667df1d50c8c41f526c052d64.png" style="zoom:67%;" />



<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/f35bfe0a82953e3d07cf70c63fc20fb7.png" style="zoom:67%;" />

#### 6.4.6 二维图形多边形-基本变换

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/a6574b5c11d64cbc113ac567bb39aff9.png" style="zoom:67%;" />



如果存在多步变换的话，使用
`P'=P*T1*T2*T3`
来计算（其中T1,T2,T3是基本变换对应的变换矩阵)



#### 6.4.7 三维图形齐次坐标系与变换

齐次坐标`P(x,y,z)=>(x, y,z,1)`
所有的三维图形的基本变换都可以用下列式子来表示
`P' = P*T`
其中T是变换矩阵`P(x,y,z) P'(x, y',z')`



#### 6.4.8 三维图形-平移变换

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/34e7356f373d4192dbc26026ddfc0fba.png" style="zoom:67%;" />

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/68f5f4514605f3bad1b3b60a9b4a0734.png" style="zoom: 50%;" />

#### 6.4.9 三维图形-缩放变换

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/2b05c2c58bc30d0a39179911638568a4.png" style="zoom: 50%;" />



#### 6.4.10 三维图形-旋转变换

绕X,Y,Z轴正方向旋转Θ角度的变换矩阵分别为
Θ角的正负按右手规则确定， 【右手大拇指】指向旋转轴的【正方向】，其余四个手指指向旋转角的【正方向】。

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/8fc4dece72553ef894d0ff9daa1025c7.png" style="zoom:67%;" />



#### 6.4.11 三维图形-对称变换

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/f65381c5cbc895ae8e723b63174c1359.png" style="zoom:67%;" />



#### 6.4.12 三维图形的投影

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/948911127e8f3bee3db611c5e67475f3.png" style="zoom:67%;" />

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/5ef3d20915566f4517daf83efc49ff8e.png" style="zoom:67%;" />

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/04da5538737b6616e83f2fc7aca9961f.png" style="zoom:67%;" />



#### 6.4.13 三维图形复合变换

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/d26620c9a41c194cfc196ba891f5d643.png" style="zoom:67%;" />

多次基本变换

`P'=P*T1*T2*T3`
T1,T2,T3是变换矩阵



### 6.5 C++数值计算库Eigen

#### 6.5.1 安装

Eigen是一个高层次的C++库，有效支持线性代数，矩阵和矢量运算，数值分析及其相关的算法。

除了C++标准库以外，不需要任何其他的依赖包。

如果使用Eigen库，只需包特定模块的的头文件即可。

使用头文件

```c
#include <ArduinoEigen.h>
using namespace Eigen;
```

快速入门:
https://eigen.tuxfamily.org/dox/group__QuickRefPage.html

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/0de561e0ab226e5f47dc872fbf6da49c.png" style="zoom:67%;" />

#### 6.5.2 Eigen矩阵类型

矩阵的定义

```c
template<typename Scalar_, int Rows_, int Cols_, int Options_, int MaxRows_, int MaxCols_>
class Eigen::Matrix< Scalar_, Rows_, Cols_, Options_ MaxRows_, MaxCols_>
```

- Scalar_:矩阵元素的类型，支持所有本地所支持的浮点型，整形，比如long , int , short, float, double等，还支持std:.complex
- Rows_:矩阵的行数或是Dynamic
- Cols_:矩阵的列数或是Dynamic



#### 6.5.3 Eigen预定义宏

数字:2-4，X(动态类型)
类型: d(double), f(float), i(int)

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/5732f8a837928a9b10a05484df5c0744.png" style="zoom:67%;" />

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/5e8985505734cf0637e7ae62f9fa1da0.png" style="zoom:67%;" />

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/fb8f35501c4c3443d11d4b0641284472.png" style="zoom:67%;" />



#### 6.5.4 Eigen向量类型

列向量: Vector2, Vector3, Vector4, VectorX
行向量: RowVector2, RowVector3,RowVector4, RowVectorX

这些都是Matrix的子类

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/13b941933153f8fec2d4b2d61a97abde.png" style="zoom:67%;" />

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/6fd490d27e8f87ab62bba0f4a1168001.png" style="zoom:67%;" />

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/c08e26aaeeffdb8b74c47978a70daa29.png" style="zoom:67%;" />

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/d7dcde92476eb39776c0cfdba68eeb95.png" style="zoom:67%;" />



#### 6.5.5 Eigen矩阵定义与初始化

```c
//方式一
Matrix3f m;
m<<1,2,3,
	4,5,6,
	7,8,9;

//方式二
Matrix<double,2,3> b{
    {2,3,4},
    {5,6,7},
}

//方式三
MatrixXd matA(2,2);
matA<<1,2,3,4;
```



#### 6.5.6 Eigen基础操作

- rows()
  - 获取行数
- cols()
  -  获取列数
- (i,j)
  - 获取(i,j)处元素
- row(i)
  - 获取第i行(左右值)
- col(i)
  - 获取第i列(左右值)



特殊矩阵生成

```c
MatrixXd::Identity(rows,cols);	//单位矩阵
C.setIdentity(rows,cols);		//C=eye(rows,cols)

MatrixXd::Zero(rows,cols);		//全0
C.setZero(rows,cols);			//C=zero(rows,cols)

MatrixXd::Ones(rows,cols);		//全1
C.setOnes(rows,cols);			//C=ons(rows,cols)

MatrixXd::Random(rows,cols);	//返回(-1,1)之间的随机数
C.setRandom(rows,cols);
```

#### 6.5.7 Eigen基础运算

Eigen对于矩阵的运算重载了`+,-,*,/,+=,-=,*=,/=`等运算符



### 6.6 旋转的立方体的实现

我们旋转的中心点位于立方体的中心位置，所以我们建模的时候要以立方体的中心位置为原点。

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/de92a16442f92788b56c16966b253413.png" style="zoom:67%;" />



每个点都以行向量表示，然后组成一个点的矩阵

```c
MatrixXd pt(8,4);		//立方体顶点

pt<< -1,-1,1,1,			//A 0
    1,-1,1,1,			//B 1
	1,1,1,1,			//C 2
	-1,1,1,1,			//D 3
	-1,-1,-1,1,			//E 4
	1,-1,-1,1,			//F 5
	1,1,-1,1,			//G 6
	-1,1,-1,1;			//H 7
```



记录立方体边的拓扑信息(到时每条边都得绘制出来)

用一个矩阵表示，每一行表示一条连接，第一列是起点，第二列是终点

```c
MatrixXd tp(12,2);		//立方体边
tp<<0,1,				//A-B
	1,2,				//B-C
	2,3,				//C-D
	3,0,				//D-A
	0,4,				//A-E
	1,5,				//B-F
	2,6,				//C-G
	3,7,				//D-H
	4,5,				//E-F
	5,6,				//F-G
	6,7,				//G-H
	7,4;				//H-E
```



获取模块的旋转角度

```c
MPU6050 mpu(Wire);
Wire.begin(14,27);
mpu.begin();
mpu.calcGyroOffsets();
xTaskCreatePinnedToCore(mpuTask,"mpuTask",4096,NULL,5,NULL,1);

void mpuTask(void* param){
    while(true){
        if(xSemaphoreTake(xMutex,portMAX_DELAY)){
            //临界资源处理
            mpu.update();
            xa = mpu.getAngleX();
            ya = mpu.getAngleY();
            za = mpu.getAngleZ();
            xSemaphoreGive(xMutex);
        }
        delay(5);
    }
}

void loop(){
    ...
    double xxa,yya,zza;
    if(xSemaphoreTake(xMutex,portMAX_DELAY))
    {
        //临界资源处理
        xxa = xa;
        yya = ya;
        zza = za;
        xSemaphoreGive(xMutex);
    }
    ...
}
```



这个立方体太小了，我们把它放大60倍，因为我们的屏幕是240*240的，边长120比较合适

放大60倍的变化的变换矩阵是

$$
\left[\begin{matrix}60 & 0 & 0 & 0\\0 & 60 & 0 & 0\\0 & 0 & 60 &0\\ 0 & 0 & 0 & 1\end{matrix}\right]
$$

```c
MatrixXd tm0(4,4);

tm0 << 60,0,0,0,
		0,60,0,0,
		0,0,60,0,
		0,0,0,1;
pt *= tm0;	//这个就是我们最初的大个立方体
```



我们从MPU获取到各轴的旋转角度后，要对图形进行旋转，所以我们要定义三个用于各个轴旋转的矩阵

```c
Matrix4d txr;	//x轴
Matrix4d tyr;	//y轴
Matrix4d tzr;	//z轴

txr.setIdentity(4,4);
tyr.setIdentity(4,4);
tzr.setIdentity(4,4);

void setZRotationTranslation(double angle)
{
    double tmp = 3.1415926 * angle/180.0;
    double c = cos(tmp);
    double s = sin(tmp);
    tzr(0,0) = c;
    tzr(0,1) = s;
    tzr(1,0) = -s;
    tzr(1,1) = c;
}

void setXRotationTranslation(double angle)
{
    double tmp = 3.1415926 * angle/180.0;
    double c = cos(tmp);
    double s = sin(tmp);
    tzr(1,1) = c;
    tzr(1,2) = s;
    tzr(2,1) = -s;
    tzr(2,2) = c;
}

void setYRotationTranslation(double angle)
{
    double tmp = 3.1415926 * angle/180.0;
    double c = cos(tmp);
    double s = sin(tmp);
    tzr(0,0) = c;
    tzr(0,2) = s;
    tzr(2,0) = -s;
    tzr(2,2) = c;
}

MatrixXd tmp(8, 4);

setXRotationTranslation(xxa);
setYRotationTranslation(yya);
setZRotationTranslation(zza);

tmp = pt;	//每次都从最初的大立方体开始
tmp *= txr;	//x轴旋转
tmp *= tyr;	//y轴旋转
tmp *= tzr; //z轴旋转
```



立方体完成旋转后，它的中心点在0,0有大概一半的图形我们看不到，我们要把它平移到x,y,z都为正的那个区域,我们只要在各个维度平移120就够了

```c
MatrixXd tm1(4,4);	//平移矩阵
tm1 << 1,0,0,0,
		0,1,0,0,
		0,0,1,0,
		120,120,120,1;
tmp *= tm1;			//完成平移
```



我们选择将此立体图形投影到x0y平面，因为立方体是一个封闭的图形，我们可以根据前面的拓扑信息将线也画出来就行了

投影到x0y平面只要简单的将z置0，也就是我们只要最终坐标中的x,y的信息就可以了。

 ```c
 void drawTube(const MatrixXd& m,uint16_t color)	//画出投影线
 {
     int nr = tp.rows();	//拓扑信息的行数
     for(int i=0;i<nr;i++)
     {
         auto start = m.row(tp(i,0));
         auto end = m.row(tp(i,1));
         tft.drawLine(start(0),start(1),end(0),end(1),color);//第0列是x,第1列是y
     }
 }
 ```



代码

```c
// ESP32多核代码
#include <ArduinoEigen.h>
#include <SPI.h>
#include <TFT_eSPI.h>
#include <Wire.h>
#include <MPU6050_light.h>

using namespace Eigen;

struct Line
{
  uint8_t start;
  uint8_t end;
};

MatrixXd pt(8, 4);    //立边体顶点
MatrixXi tp(12, 2);   //立方体边

MatrixXd tm0(4, 4);   //放大60位
MatrixXd tm1(4, 4);   //平移
Matrix4d txr;
Matrix4d tyr;
Matrix4d tzr;

double xa;
double ya;
double za;

xSemaphoreHandle xMutex = xSemaphoreCreateMutex();

TFT_eSPI tft = TFT_eSPI();

void drawTube(uint16_t color)
{
  int nr = tp.rows();  //行数
  for(int i=0; i<nr; i++)
  {
    auto start = pt.row(tp(i,0));
    auto end = pt.row(tp(i,1));
    tft.drawLine(start(0), start(1), end(0), end(1), color);
  }
}

void drawTube(const MatrixXd& m, uint16_t color)
{
  int nr = tp.rows();  //行数
  for(int i=0; i<nr; i++)
  {
    auto start = m.row(tp(i,0));
    auto end = m.row(tp(i,1));
    tft.drawLine(start(0), start(1), end(0), end(1), color);
  }
}

//angle是角度
void SetXRotationTranslation(double angle)
{
  double tmp = 3.1415926 * angle/180.0;
  double c = cos(tmp);
  double s = sin(tmp);
  txr(1,1) = c;
  txr(1,2) = s;
  txr(2,1) = -s;
  txr(2,2) = c;
}

//angle是角度
void SetYRotationTranslation(double angle)
{
  double tmp = 3.1415926 * angle/180.0;
  double c = cos(tmp);
  double s = sin(tmp);
  tyr(0,0) = c;
  tyr(0,2) = -s;
  tyr(2,0) = s;
  tyr(2,2) = c;
}

//angle是角度
void SetZRotationTranslation(double angle)
{
  double tmp = 3.1415926 * angle/180.0;
  double c = cos(tmp);
  double s = sin(tmp);
  tzr(0,0) = c;
  tzr(0,1) = s;
  tzr(1,0) = -s;
  tzr(1,1) = c;
}

MPU6050 mpu(Wire);

void setup() {
  Serial.begin(115200);
  delay(1000);
  tft.init();
  tft.setRotation(1);
  tft.fillScreen(TFT_BLACK);

  Wire.begin(14,27);
  mpu.begin();
  mpu.calcGyroOffsets(); // gyro and accelero
  Serial.println("Done!\n");

  pt << -1, -1, 1, 1,   //A 0
        1, -1, 1, 1,    //B 1
        1, 1, 1, 1,     //c 2
        -1, 1, 1, 1,    //d 3
        -1, -1, -1, 1,  //e 4
        1, -1, -1, 1,   //f 5
        1, 1, -1, 1,    //g 6
        -1, 1, -1, 1;   //h 7

  tp <<0, 1,  //A-B
       1, 2,  //b-c
       2, 3,  //c-d
       3, 0,  //d-a
       0, 4,  //a-e
       1, 5,  //b-f
       2, 6,  //c-g
       3, 7,  //d-h
       4, 5,  //e-f
       5, 6,  //f-g
       6, 7,  //g-h
       7, 4;  //h-e
  
  tm0 <<60, 0, 0, 0,
        0, 60, 0, 0,
        0, 0,  60, 0,
        0, 0, 0, 1;

  tm1 <<1, 0, 0, 0,
       0, 1, 0, 0,
       0, 0, 1, 0,
       120, 120, 120, 1;

  txr.setIdentity(4,4);
  tyr.setIdentity(4,4);
  tzr.setIdentity(4,4);

  pt*=tm0;    //这个就是我们最初的大个立方体

  xTaskCreatePinnedToCore(mpuTask, "mpuTask", 4096, NULL, 5, NULL, 1); 
}

void mpuTask(void* param)
{
  while(true)
  {
    if(xSemaphoreTake(xMutex, portMAX_DELAY))
    {
      //临界资源处理
      mpu.update();
      xa = mpu.getAngleX();
      ya = mpu.getAngleY();
      za = mpu.getAngleZ();
      xSemaphoreGive(xMutex);
    }

    delay(5);
  };
}

void loop() {
  unsigned long start = millis();
  /***********************************/
  MatrixXd tmp(8, 4);
  double xxa, yya, zza;
  if(xSemaphoreTake(xMutex, portMAX_DELAY))
  {
    //临界资源处理
    xxa = xa;
    yya = ya;
    zza = za;
    xSemaphoreGive(xMutex);
  }

  SetXRotationTranslation(xxa);
  SetYRotationTranslation(yya);
  SetZRotationTranslation(zza);

  tmp = pt;
  tmp *=txr;
  tmp*=tyr;
  tmp*=tzr;
  tmp*=tm1;
  
  drawTube(tmp, TFT_WHITE);
  delay(30);
  drawTube(tmp, TFT_BLACK);
  /***********************************/
  unsigned long end = millis();
  tft.setCursor(3, 5);
  tft.setTextColor(TFT_RED, TFT_BLACK);
  tft.setTextSize(2);
  tft.print("FPS:");
  tft.print(1000 / (end - start));
  tft.setTextColor(TFT_BLACK, TFT_BLACK);
  tft.print(1000 / (end - start));
}

//ESP8266 单核代码
#include <Arduino.h>
#include <SPI.h>
#include <TFT_eSPI.h>
#include <MPU6050_light.h>
#include <ArduinoEigen.h>
using namespace Eigen;

struct Line
{
  uint8_t start;
  uint8_t end;
};

TFT_eSPI tft = TFT_eSPI(); //创建TFT对象
MPU6050 mpu(Wire);         //创建MPU6050对象

MatrixXd pt(8, 4);  //立方体顶点
MatrixXd tp(12, 2); //立方体边
MatrixXd tm0(4, 4); //放大60位
MatrixXd tm1(4, 4); //平移
double xa, ya, za;  //角度

Matrix4d txr; //x轴
Matrix4d tyr; //y轴
Matrix4d tzr; //z轴

void mpuTask(void *param)
{
  //临界资源处理
  mpu.update();
  xa = mpu.getAngleX();
  ya = mpu.getAngleY();
  za = mpu.getAngleZ();
}

void drawTube(uint16_t color)
{
  int nr = tp.rows(); //行数
  for (int i = 0; i < nr; i++)
  {
    auto start = pt.row(tp(i, 0));
    auto end = pt.row(tp(i, 1));
    tft.drawLine(start(0), start(1), end(0), end(1), color);
    // tft.drawWideLine(start(0), start(1), end(0), end(1), 2, color, color);
  }
}

void drawTube(const MatrixXd &m, uint16_t color)
{
  int nr = tp.rows(); //行数
  for (int i = 0; i < nr; i++)
  {
    auto start = m.row(tp(i, 0));
    auto end = m.row(tp(i, 1));
    tft.drawLine(start(0), start(1), end(0), end(1), color);
    // tft.drawWideLine(start(0), start(1), end(0), end(1), 2, color, color);
  }
}

void setZRotationTranslation(double angle)
{
  double tmp = 3.1415926 * angle / 180.0;
  double c = cos(tmp);
  double s = sin(tmp);
  tzr(0, 0) = c;
  tzr(0, 1) = s;
  tzr(1, 0) = -s;
  tzr(1, 1) = c;
}

void setXRotationTranslation(double angle)
{
  double tmp = 3.1415926 * angle / 180.0;
  double c = cos(tmp);
  double s = sin(tmp);
  tzr(1, 1) = c;
  tzr(1, 2) = s;
  tzr(2, 1) = -s;
  tzr(2, 2) = c;
}

void setYRotationTranslation(double angle)
{
  double tmp = 3.1415926 * angle / 180.0;
  double c = cos(tmp);
  double s = sin(tmp);
  tzr(0, 0) = c;
  tzr(0, 2) = s;
  tzr(2, 0) = -s;
  tzr(2, 2) = c;
}

void setup()
{
  Serial.begin(9600);
  tft.init();
  tft.fillScreen(TFT_BLACK);

  Wire.begin(12, 4); // sda, scl
  mpu.begin();
  mpu.calcGyroOffsets();

  pt << -1, -1, 1, 1, //A 0
      1, -1, 1, 1,    //B 1
      1, 1, 1, 1,     //C 2
      -1, 1, 1, 1,    //D 3
      -1, -1, -1, 1,  //E 4
      1, -1, -1, 1,   //F 5
      1, 1, -1, 1,    //G 6
      -1, 1, -1, 1;   //H 7

  tp << 0, 1, //A-B
      1, 2,   //B-C
      2, 3,   //C-D
      3, 0,   //D-A
      0, 4,   //A-E
      1, 5,   //B-F
      2, 6,   //C-G
      3, 7,   //D-H
      4, 5,   //E-F
      5, 6,   //F-G
      6, 7,   //G-H
      7, 4;   //H-E

  tm0 << 60, 0, 0, 0,
      0, 60, 0, 0,
      0, 0, 60, 0,
      0, 0, 0, 1;

  tm1 << 1, 0, 0, 0,
      0, 1, 0, 0,
      0, 0, 1, 0,
      120, 120, 120, 1;

  txr.setIdentity(4, 4);
  tyr.setIdentity(4, 4);
  tzr.setIdentity(4, 4);

  pt *= tm0; //这个就是我们最初的大个立方体
}

void loop()
{
  unsigned long start = millis();
  /***********************************/
  MatrixXd tmp(8, 4);
  double xxa, yya, zza;
  mpuTask(NULL);
  xxa = xa;
  yya = ya;
  zza = za;

  setXRotationTranslation(xxa);
  setYRotationTranslation(yya);
  setZRotationTranslation(zza);

  tmp = pt;   //每次都从最初的大立方体开始
  tmp *= txr; //x轴旋转
  tmp *= tyr; //y轴旋转
  tmp *= tzr; //z轴旋转
  tmp *= tm1; //平移

  drawTube(tmp, TFT_WHITE);
  delay(35);
  drawTube(tmp, TFT_BLACK);
  /***********************************/
  unsigned long end = millis();
  tft.setCursor(3, 5);
  tft.setTextColor(TFT_RED, TFT_BLACK);
  tft.setTextSize(2);
  tft.print("FPS:");
  tft.print(1000 / (end - start));
  tft.setTextColor(TFT_BLACK, TFT_BLACK);
  tft.print(1000 / (end - start));
}

```

