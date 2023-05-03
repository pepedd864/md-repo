

## 1. ESP32简介

### 1.1 esp32是什么

- ESP32是乐鑫公司推出的一款微处理器
- ESP32使用40nm工艺、双核32位MCU、主频高达230MHz2.4GHz双模Wi-Fi和蓝牙4.0芯片
- 具有丰富的外设接口: GPIO、ADC、DAC、SPI、I2C、I2S、UART
- 可以使用多种语言进行开发:C, C++, python, javascript等，新手建议使用python或Arduino ide开发
- 物联网项目的理想选择

<img src="https://gitee.com/pepedd864/cdn-repos/raw/master/img/8ca85aa553ac0212e9a639f1944e4cbe.png" style="zoom:67%;" />

### 1.2 ESP32和Arduino的关系

- ESP32是一个微处理器
- Arduino指的是一个生态，包括了开发板、IDE、驱动库等内容，并不是指某一款开发版
- Arduino生态目前支持许多的主控芯片，如mega328p(这个就是著名的Arduino Uno开发板使用的主控芯片) 、mega2560 (Arduino Nano开发板使用的主控芯片) 、ESP8266、ESP32等。所以使用ESP32芯片的开发板是可以使用Arduino IDE进行开发的
- 现在某宝上大家可以发现ESP32的开发板和Arduino Uno和Nano的价格相当，但ESP32的功能比Uno和Nano强了不是一点点，所以现在使用Arduino Uno和Nano的人变少了，而使用ESP32的人变多了。

### 1.3 ESP32开发板的选择

- 芯片产品目录：[模组概览 | 乐鑫科技](https://www.espressif.com.cn/zh-hans/products/modules)

- 某宝上卖的最多的就是DOIT_ESP32-DevkitV1和ESP32-DevKitC这两款开发板,文档使用ESP32-DevkitV1的开发板

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/0a634b0a9153d4845e7e80a4ca895aa1.png)

### 1.4 ESP32 devkit v1开发板

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/68fce516d29f608d50acb7cbcd38b699.png)

### 1.5 ESP32的一些直流特性

- 开发板的输入电压是7-12V，电流至少要能达到500mA
- GPIO口做为输出模式时切记不能直接接地!
- 单IO输出的最大电流为40mA(拉电流)
- 单IO输入的最大电流为28mA（灌电流)
- 开发板IO输出总电流最大为1.1A
- 管脚的上拉电阻和下拉电阻都为45kΩ

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/2828d57ab19a3e5619b967bc47985282.png)

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/ee5a560d5a6383ca898516b58a9e4f60.png)

### 1.6 ESP32-DevkitV1供电问题

- 直接使用板载的USB接口供电
- 使用VIN进行供电，供电电压是7-12v

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/2d2b1a2cb6d52700b36f0f8a513928bb.png)

### 1.7 Arduino IDE开发环境配置

Arduino lDE下载地址: https://www.arduino.cc/en/software

ESP32及CP210X的开发工具及驱动包:
https://pan.baidu.com/s/1WGdqSRZbzMg1MQO2gbBAbQ?pwd=O3cw提取码:03cw

其它开发板管理地址: https://github.com/espressif/arduinesp32/releases/download/2.0.5/package_esp32_index.json

把下载下来的8个离线文件放在`C:\Users\你的用户名\AppData\Local\Arduino15\staging\packages`下，没有这一个文件夹请自行新建。

### 1.8 vscode + platformio开发环境配置

vscode下载地址https://code.visualstudio.com/

在vscode插件中搜索`platformio`

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/7f1cba70f82f3980ddc6a92ceed82cdf.png)

### 1.9 在Arduino IDE 上编写代码

1. 编写代码

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/824727010a8976bd91c62864c856333e.png)

2. 上传代码

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/c3b6297ddd11511e1ba364aaa66f9935.png)

3. 查看串口监视器,每两秒开发板就会向电脑发送一条"hello world"

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/fd414397915099a5ec39bb45cc4820da.png)

## 2 ESP32点灯

实验目标

- 实现ESP32开发板上的蓝色LED灯以2S的周期进行闪烁

- 使用ESP32的GPIO点点亮外围发光二极管
- 认识LED发光二极管
- 学会GPIO做为数字输出口的方法

### 2.1发光二极管

直插发光LED压降

- 黄、红:2.0-2.2V
- 绿、白、蓝:3.0-3.2V

额定电流约20mA,—般用作指示时10mA的电流就够了



正负极的判断

1. 如果发光二极管的引脚没有剪掉，长的引脚为正极，短的引脚为负极。
2. 也可以从引脚连接的发光二极管内的金属面的大小判断，金属面小的是正极，金属面大的是负极。
3. 使用万用表通断档进行测试

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/de92157807725b60099b44fa87be0e1b.png)



发光二极管串联电阻计算

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/b118bceb7af552455537cb21677ebbb2.png)

1. 红色led正常工作时压降为2v
2. esp32管脚输出高电平时为3.3v
3. 所以电阻上的电压为3.3-2= 1.3 v
4. 发光led正常工作时电流约为10mA
5. 所以电阻为1.3/0.01= 130Ω
6. 取标称值120Ω

### 2.2 GPIO接口

GPIO

- GPIO=General Purpose InputOutput,通用输入输出接口
- 可以通过设置,将GPIO口指定具体的工作模式，如做为数字口，做为模拟口，做为SPI口等

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/d0a64de66b75f8938d241f8dd55a88e6.png)



GPIO口做为数字输出

- 数字输出
  - 数字输出就是指接口输出的是高电平、低电平
  - 高电平输出的最低电压为`0.8*VDD=0.8*3.3=2.64V`
  - 低电平输出的最高电压为`0.1*VDD =0.1*3.3=0.33V`
  - 单管脚输出的最大电流是40mA
  - 所有管脚输出的最大总电流为1.1A
  - 做为数字输出模式时管脚不能直接接地

![](https://cdn.staticaly.com/gh/pepedd864/cdn-repos@main/img/ee5a560d5a6383ca898516b58a9e4f60.png)



  数字输出建议使用的GPIO口

- 建议使用的GPIO口的编号如下:2、4、5、12-33
- **GPIO2口接着一个LED灯**
- 右边涂绿色的就是建议使用的GPIO口

<img src="https://gitee.com/pepedd864/cdn-repos/raw/master/img/c69b51ef40f618bf2c56ca41f8de90dc.png" style="zoom:50%;" />

### 2.3 pinMode

pinMode

- 功能
  - 设置数字口的模式
- 定义
  - pinMode(pin, mode)
- mode的值有
  - INPUT,OUTPUT,INPUT_PULLUP,INPUT_PULLDOWN
  - 返回值:无

### 2.4 digitalWrite

digitalWrite

- 功能
  - 设定指定数字输出口的值
- 定义
  - digitalWrite(pin, value)
    value的取值是HIGH或者Low
    设置成HIGH输出高电平、设置成LOW输出低电平
- 返回值
  - 无

### 2.5 GPIO设置为数字输出口流程

GPIO设置为数字输出口流程

1. 使用pinMode设置指定的端口为OUTPUT模式
2. 使用digitalWrite设置指定端口的电平(高或低)

<img src="https://cdn.staticaly.com/gh/pepedd864/cdn-repos@main/img/28976dd5c73c2b2c6bbb615f79a21622.png" style="zoom:67%;" />

### 2.6 delay

delay

- 功能
  - 停止程序运行一段时间定义: delay(ms)
    参数的单位是ms，所以2s，要传入2000
- 返回值
  - 无
- 注意
  - 使用此函数会暂停程序的运行，真的程序什么事都不干了!

### 2.7 直接使用开发板上的蓝色led

```c
int ledPin = 2;//代表GPIO
void setup() {
	// put your setup code here, to run once
    pinMode(ledPin,OUTPUT);
}
void loop() {
	//put your main code here, to run repeatedly :
    digitalwrite(ledPin,HIGH);
	delay(2000);
	digitalwrite(ledPin,LOw);
	delay(2000);
}
```

<img src="https://cdn.staticaly.com/gh/pepedd864/cdn-repos@main/img/b3a83d47d9590618069a25ba85aa0ace.png" style="zoom:67%;" />

### 2.8 使用GPIO4进行实验

![](https://cdn.staticaly.com/gh/pepedd864/cdn-repos@main/img/666ac399c6b956c98a6967d9c935b7b6.png)

```c
int ledPin = 4;//代表GPIO
void setup() {
	// put your setup code here, to run once
    pinMode(ledPin,OUTPUT);
}
void loop() {
	//put your main code here, to run repeatedly :
    digitalwrite(ledPin,HIGH);
	delay(2000);
	digitalwrite(ledPin,LOw);
	delay(2000);
}
```



### 2.9 millis、micros函数

millis

- 功能
  - 获取本程序已经运行了多少毫秒
- 定义
  - millis()
- 返回
  - 本程序已经运行的时间（毫秒）

micros

- 功能
  - 获取本程序已经运行多少微秒
- 定义
  - micros()
- 返回
  - 本程序已经运行的时间（微秒）



### 2.10 两个不同闪烁周期的LED灯

GPIO4口外接LED红灯，以2S的周期进行闪烁，同时让板载的蓝色LED灯以3S的周期进行闪烁。

![](https://cdn.staticaly.com/gh/pepedd864/cdn-repos@main/img/67dec29f8b4d75a132d1cb1923fa3e99.png)

---



不使用delay函数实现闪烁的思路

- **关键点：loop 函数一次运行的时间非常短**

- prevTime: 上一次led改变发光状态的时间

- now: 当前测试时的时间

- ledStatus: led灯目前的状态

```c
//单个led闪烁代码
int ledPin2 = 2;
int ledStatus2 = 0;//led灯现在的状态
unsigned int prevTime2 = 0;//上一次改变状态时的时间

void setup(){
	pinMode(ledPin2,OUTPUT);
  digitalWrite(ledPin2,HIGH);
  ledStatus2 = HIGH;
	prevTime2 = millis();
}
void loop() {
	unsigned int now = millis();//程序运行的时间
    if(now - prevTime2 > 3000)//上次改变状态后已经经过3S
	{
		//要把状态改变成和现在相反的
		int status = ledStatus2 == HIGH ? LOW:HIGH;
        digitalWrite(ledPin2,status);
		ledStatus2 = status;
		prevTime2 = now;
	}
}
```

```c
//两个led灯交替闪烁代码
int ledPin2 = 2;
int ledStatus2 = 0;//led灯现在的状态
unsigned int prevTime2 = 0;//上一次改变状态时的时间

int ledPin4 = 2;
int ledStatus4 = 0;//led灯现在的状态
unsigned int prevTime4 = 0;//上一次改变状态时的时间

void setup(){
	pinMode(ledPin2,OUTPUT);
  digitalWrite(ledPin2,HIGH);
  ledStatus2 = HIGH;
	prevTime2 = millis();

  pinMode(ledPin4,OUTPUT);
  digitalWrite(ledPin4,HIGH);
  ledStatus4 = HIGH;
	prevTime4 = millis();
}
void loop() {
	unsigned int now = millis();//程序运行的时间
    if(now - prevTime2 > 3000)//上次改变状态后已经经过3S
	{
		//要把状态改变成和现在相反的
		int status = ledStatus2 == HIGH ? LOW:HIGH;
        digitalWrite(ledPin2,status);
		ledStatus2 = status;
		prevTime2 = now;
	}

    if(now - prevTime4 > 2000)//上次改变状态后已经经过3S
	{
		//要把状态改变成和现在相反的
		int status = ledStatus4 == HIGH ? LOW:HIGH;
        digitalWrite(ledPin4,status);
		ledStatus4 = status;
		prevTime4 = now;
	}
}
```



### 2.11 按键控制LED灯

实验目标

- GPIO25口连接一个轻触开关
- GPIO4口外接一个LED灯
- 板子启动时自动点亮LED灯，之后每按一次轻触开关就改变LED的状态

![](https://cdn.staticaly.com/gh/pepedd864/cdn-repos@main/img/42b6016e1e7eb7e9fc79db12c4979023.png)

#### 2.11.1 轻触开关

轻触开关，又叫按键开关。在开关上施加一定的力往下压实现电路闭合接通，当撤除压力时电路就会断开。简单来说,就是轻轻按下去便能瞬间接通的开关。

![](https://cdn.staticaly.com/gh/pepedd864/cdn-repos@main/img/ce9c1a2e4ca849079f7fc0598d2f9ece.png)

#### 2.11.2 GPIO口做为数字输入

- 数字输入功能就是将lO做为检测输入电平的口，用来检测输入信号是高电平还是低电平
  - 高电平输出的最低电压为`0.75*VDD=0.75*3.3=2.475V`
  - 高电平输入的最高电压为`VDD+0.3 = 3.3+0.3=3.6V`
  - **[2.48,3.6]之间的电压被视为高电平(HIGH)**
  - 低电平输出的最小电压为-0.3V
  - 低电平输出的最高电压为`0.25*VDD =0.25*3.3=0.825 V`
  - **[-0.3,0.82]之间的电压被视为低电平(Low)**

![](https://cdn.staticaly.com/gh/pepedd864/cdn-repos@main/img/ee5a560d5a6383ca898516b58a9e4f60.png)

三种数字输入模式

![](https://cdn.staticaly.com/gh/pepedd864/cdn-repos@main/img/01479c44e67aa5743085ba79fa153ba2.png)



数字输入建议使用的GPIO口

- 放心使用的GPIO口:2、4、13、16-33
- 仅作为输入，且没有上下拉电阻功能的IO口:34、35、36、39
- 板子启动时会短暂输出高电平或PWM信号的IO口5、12、14、15
- 其它的IO口就不能使用了

<img src="https://cdn.staticaly.com/gh/pepedd864/cdn-repos@main/img/e0e8217c6cbf2e530a8529fc20bbfb80.png" style="zoom: 50%;" />

#### 2.11.3 digitalRead

digitalRead

- 功能
  - 检测指定数字输入口电平的高低
- 定义
  - digitalRead(pin)
- 返回值
  - 指定IO口输入信号的电平状态(HIGH,LOW)

#### 2.11.4 GPIO设置为数字输入口流程

GPIO设置为数字输入口流程

1. 使用pinMode设置指定的端口为INPUT, INPUT_PULLUP,INPUT_PULLDOWN模式
2. 使用digitalRead读取指定端口的电平（高或低)

```c
int ledPin = 4;
pinMode(ledPin,INPUT_PULLUP);
int val = digitalRead(ledPin);
```



---

连线图

![](https://cdn.staticaly.com/gh/pepedd864/cdn-repos@main/img/42b6016e1e7eb7e9fc79db12c4979023.png)

GPIO25使用INPUT_PULLUP方式，所以是低电平有效,在程序中如果检测到25口有低电平表明按键已经按下。



---

代码

```c
int switchPin = 25;	//按键所接的GPIO口
int ledPin = 4;		//led所接的GPIO口
int ledStatus = 0;	//led目前的状态
void setup() {
	pinMode(switchPin,INPUT_PULLUP);
    pinMode (ledPin,OUTPUT);
	digitalWrite(ledPin,HIGH);
    ledStatus = HIGH;
}
void loop() {
	int val = digitalRead(switchPin);//读取开关引脚的电平状态
	if(val == LOW)//低电平有效
  {
		ledStatus = ! ledStatus;
		digitalWrite(ledPin,ledStatus);
	}
}
```

#### 2.11.5 机械开关的抖动问题

抖动问题

- 按键按下时LED的亮灭不是很准确，是因为产生了按键抖动问题
- 抖动
  - 当开关按下或弹起时，人们通常视之为瞬间单一反应，但实际上可能涉及几十上百个以上的接合或断开动作，这些动作持续几百到几十分之一秒，最后接触才会稳定下来。



使用上拉输入方式（低电平有效)

![](https://cdn.staticaly.com/gh/pepedd864/cdn-repos@main/img/38597f585a3f9e3fb9f879e0cd3624e0.png)

#### 2.11.6  软件去除抖动

1. 自己写
   - 抖动时间基本都是在10-50ms之间，只要忽略这期间的输入即可
2. 使用RBD_Button 库（建议使用）
   - 这个库专门用来给机械按键消除抖动问题，效果实测非常好。

#### 2.11.7 RBD_Button库常用方法

Button类位于RBD命名空间中，所以在代码里要使用`RBD::Button`

- `RBD::Button constructor(pin,[input_pullup])`构造函数
  - pin: GPIO的编号
  - 第二个参数可以是input, input_pullup, input_pulldown
- `button.setDebounceTimeout(value)`设置消除抖动的时间
  参数的单位是ms
- `button.onPressed()`检测按钮是否按下去（下降沿）仅第
  一次返回true
- `button.onReleased()`检测按钮是否弹起来（上升沿）仅第一次返回true
- `button.isPressed()`检测按钮是否还处在按下去的状态（低电平）
- `button.isReleased()`检测按钮是否处在没有按下去的状态



示例代码

```c
#include <RBD_Timer.h>
#include <RBD_Button.h>

int switchPin = 25;  //按键所接的GPIO口
int ledPin = 4;      //led所接的GPIO口
int ledStatus = 0;   //led目前的状态

//创建一个可以消除抖动的按键对象
RBD::Button button(switchPin, INPUT_PULLUP);

void setup() {
  pinMode(ledPin, OUTPUT);
  button.setDebounceTimeout(20);    //消除抖动时间是20ms
  digitalWrite(ledPin, HIGH);
  ledStatus = HIGH;
}
void loop() {
  if (button.onPressed())           //检测按键按下去的事件（下降沿）
  {
    ledStatus = !ledStatus;
    digitalWrite(ledPin, ledStatus);
  }
}
```



## 3.PWM和LEDC的使用

### 3.1 PWM信号简介

PWM

- 脉冲宽度调制,简称脉宽调制

频率(f)

- —秒钟PWM有多少个周期(单位Hz)

周期(T)

- 一个周期多少时间
- f = 1/T

占空比(duty)

- 一个脉冲周期内，高电平的时间与整个周期时间的比例

脉冲时间

- 一个周期内高电平时间



**占空比越高，输出的有效电压越高，占空比越低，输出的有效电压越低**

![](https://cdn.staticaly.com/gh/pepedd864/cdn-repos@main/img/75f5f8d1529693bb103e89afd0e7724d.png)

上图中间PWM信号:

T= 200微秒
f = 1/200微秒= 5000 Hz
脉宽时间为50微秒
所以占空比= 50/200= 25%



### 3.2 PWM在调光电路中的应用

- —般人眼睛对于80Hz以上刷新频率则完全没有闪烁感。频率太小的话看起来就会闪烁。
- LED发光的功率和信号占空比成正比,还是线性关系，我们就可以通过简单地调节占空比来实现对LED的线性调光
  - 占空比0%		不亮
  - 占空比100%    最亮
- PWM信号的频率不影响LED的亮度，但为了不让人眼感觉闪烁,频率要大于80Hz



### 3.3 ESP32中的LEDC（PWM控制器）

LEDC

- LEDC是指LED PWM控制器，实际上就是PWM信号产生器
- 主要用于控制LED的亮度和颜色，也可以产生PWM信号用于其他用途。LED_PWM有16路通道(0~15)，即8路高速通道（O~7)和8路低速通道(8~15)。这16路通道能够产生独立的数字波形来驱动RGB LED设备。高速通道(0~7)由80MHz时钟驱动，低速通道(8~15)由8MHz时钟驱动。
- 该PWM输出主要针对LED的驱动（但实际应用中不限制）可以在不占用处理器资源的情况下，实现对占空比和频率的控制。
- ESP32中所有支持数据输出口的接口都可以用于输出PWM信号。

![](https://cdn.staticaly.com/gh/pepedd864/cdn-repos@main/img/42d5623c7a3845f8621936b6a1344a7f.png)



### 3.4 ledc头文件与产生PWM信号流程

```c
typedef enum {
	NOTE_C,NOTE_Cs,NOTE_D，NOTE_Eb,NOTE_E,NOTE_F,NOTE_Fs,NOTE_G,NOTE_Gs,NOTE_A,NOTE_Bb，NOTE_B,NOTE_MAX
}note_t;

// channel 0-15 resolution 1-16bits freq limits depend on resolution
uint32_t 	ledcSetup(uint8_t channel，uint32_t freq, uint8_t resolution_bits);
void		ledcwrite(uint8_t channel, uint32_t duty );
uint32_t	ledcwriteTone(uint8_t channel,uint32_t freq);
uint32_t	ledcwriteNote(uint8_t channel， note_t note,uint8_t octave);
uint32_t	ledcRead(uint8_t channel);
uint32_t	ledcReadFreq(uint8_t channel);
void		ledcAttachPin(uint8_t pin，uint8_t channel);
void		ledcDetachPin(uint8_t pin);
uint32_t	ledcChangeFrequency(uint8_t channel，uint32_t freq, uint8_t resolution_bits);
```



产生PWM信号流程

1. 建立ledc通道
2. 将GPIO口与ledc通道关联
3. Write、WriteTone、WriteNote
4. 解除GPIO口与ledc通道的关联



### 3.5 ledc初始化

ledcSetup

```c
double ledcSetup(uint8_t channel,double freq,uint8_t resolution_bits);
```

- 此函数设置LEDC通道对应的频率和分辨率（占空比分辨率）
- channel 为通道号，取值0~15;
- freq期望设置频率;
- resolution_bits分辨率位数，取值o~20(多少个二进制位)比如分辨率设置成12,就可以把一个周期分成212等分
- 设置成功返回ledc的通道号，如果失败,函数返回0



### 3.6 ledc频率与分辨率关系

<img src="https://cdn.staticaly.com/gh/pepedd864/cdn-repos@main/img/f4fe7a0d0f075ede9fd6977511934eb3.png" style="zoom:67%;" />



![](https://raw.githubusercontent.com/pepedd864/cdn-repos/main/img/eb843fb3cd26a5307128e837e6587a87.png)

高速定位器的时钟源采用了REF_TICK或APB_CLK,低速定位器采用了REF_TICK或SLOw_CLOCK。置位LEDC_APB_CLK_SEL寄存器,SLow_CLOCK的频率为80 MHz，否则为8MHz。



### 3.7 ledc频率与最大分辨率表

<img src="https://raw.githubusercontent.com/pepedd864/cdn-repos/main/img/6094128431186fca7350d6f407efaef6.png" style="zoom:67%;" />



### 3.8 将LEDC绑定到GPIO口上

ledcAttachPin 

- 将LEDC通道绑定到指定GPIO口上以实现输出,一个通道可以同时绑定到多个GPIO口上

```c
void ledcAttachPin(uint8_t pin,uint8_t chan);
```

ledcDetachPin

- 解除指定GPIO口的LEDC功能

 ```c
 void ledcDetachPin(uint8_t pin);
 ```

ledcWrite

- 功能:设置指定ledc通道的占空比

 ```c
 void ledcWrite(uint8_t chan,uint8_t duty);
 ```



### 3.9 和音乐相关的两个函数

ledcWriteTone

- 设置LEDC通道的频率，固定占空比为50%

```c
double ledcWriteTone(uint8_t chan,double freq);
```

ledcWriteNote

- 给LEDC通道设置特殊的映射

```c
double ledcWriteNote(uint8_t chan, note_t note,uint_8 octave);
```



### 3.10 获取ledc参数的函数

ledcRead

- 获取指定通道的占空比

```c
uint32_t ledcRead(uint8_t chan);
```



ledcReadFreq

- 获取指定通道的频率

```c
double ledcReadFreq(uint8_t chan);
```



### 3.11  改变ledc的频率和精度

ledcChangeFrequency

- 设置指定通道的频率

```c
double ledcChangeFrequency(uint8_t chan,double freq,uint8_t bit_num);
```



### 3.12 输出PWM信号示例

```c
int ret = 0;
Serial.begin(115200);
int ch0 = 0;
int gpio4 = 4;
ret = ledcSetup(ch0,5000,12);

//--------------测试------------------
delay(200);
if(ret == 0)
    Serival.println("Error Setup");
else
    Serival.println("Success Setup");
//--------------测试------------------

ledcAttachPin(gpio,ch0);
ledcWrite(ch0,pow(2,11));	//占空比50%
/*
精度12 →>共有2^12个等分格子
pow(2,11)>高电平取2^11个格式
所以占空比是50%
*/
```

建议在测试程序的时候调好串口的波特率，我们可以在串口打印一些调试的信息，而且在ledc频率和精度设定不正确的时候，ESP32会在串口中输出如下的提示，我们好进行更改



### 3.13 LED呼吸灯

通过ESP32使LED实现从亮到灭，再从灭到亮的变化

#### 3.13.1 调光思路

调光思路

- 采取的策略是每秒钟固定调整占空比50次
- 假设T为呼吸周期，则光从灭到最亮经过的时间就是T/2(半个周期)
- 半个周期要进行`50*T/2`次调整占空比
- count表示占空比为100%时等分的格子
- step就是每次调整时要加上的步进值(增量)`step = count/(50*T/2)= 2*count/(50*T)`
- 占空比超过`100%(count)`时，就要以step步进值递减直到0

<img src="https://raw.githubusercontent.com/pepedd864/cdn-repos/main/img/81568600dbc82b81c9963df95b3178dc.png" style="zoom:50%;" />

#### 3.13.2  调光代码

阻塞调光代码

```c
int gpio4 =4;
int ch1 = 1;		//ledc通道号
int duty = 0;		//目前信号的占空比
int count = 0;		//100%占空比时的格子
int step = 0;		//占空比步进值(增量)
int breatheTime = 3;//呼吸的周期，单位s

void setup() {
	ledcSetup(ch1，1000，12);				   //建立ledc通道
    count = pow(2，12);					    //计算占空比为100%时共几份
	step = 2*count / (50 * breatheTime);	//计算一次增加多少占空比格子
	ledcAttachPin(gpio4,ch1);				//绑定ch1和GPI04
}

void loop() {
	ledcWrite(ch1,duty);
    duty += step;
	if(duty > count){
		duty = count;
        step = -step;
    }
	else if(duty < 0){
		duty = 0;
		step = -step;
    }
	delay(20);//程序在这里阻塞了
}
```



使用millis函数(不阻塞)

```c
int gpio4 =4;
int ch1 = 1;		//ledc通道号
int duty = 0;		//目前信号的占空比
int count = 0;		//100%占空比时的格子
int step = 0;		//占空比步进值(增量)
int breatheTime = 3;//呼吸的周期，单位s
int prevTime = 0;

void setup() {
	ledcSetup(ch1，1000，12);				   //建立ledc通道
    count = pow(2，12);					    //计算占空比为100%时共几份
	step = 2*count / (50 * breatheTime);	//计算一次增加多少占空比格子
    
	ledcAttachPin(gpio4,ch1);				//绑定ch1和GPI04
    prevTime = millis();
}

void loop() {
	int now = millis();
    if(now - prevTime >= 20)
    {
        ledcWrite(ch1,duty);
        duty += step;
        step = -step;
    }else if(duty < 0)
    {
        duty = 0;
        step = -step;
    }
    prevTime = now;
}
```



## 4. 软件定时器AsyncTimer库的使用

### 4.1 定时器

定时器

- 定时器(Timer)的主要模式
  - 等待多长时间后触发一个事件
  - 每隔多久时间触发一个事件
  - 到某个时间点触发一个事件

- 定时器的类型
  - 硬件定时器:
    - 硬件定时器是芯片本身提供的定时功能。
    - 数量有限,ESP32只有4个
    - 硬件定时器的精度—般很高，可以达到纳秒级别,并且是中断触发方式。
  - 软件定时器
    - 精度较低，一般只有毫秒级别的精度,用于对精度要求不是很高的辅助场合
    - 数量可以很多
    - 是在回调函数里处理信息

使用**硬件定时器**时，每次在定时时间到达之后就会自动触发一个中断，用户在**中断中处理信息**;而使用**软件定时器**时，需要我们在创建软件定时器的时候指定时间到达后要去调用的函数(称为回调函数)，在**回调函数中处理信息**。

### 4.2 定时器的主要操作

定时器的主要操作

- 定时器的创建
- 定时器的运行
- 定时器的停止
- 定时器的更改周期



### 4.3 AsyncTimer库的安装

Arduino IDE

![](https://raw.githubusercontent.com/pepedd864/cdn-repos/main/img/3bf652478e53d8a20282ca4d747fb7fb.png)



vscode + platformio

![](https://raw.githubusercontent.com/pepedd864/cdn-repos/main/img/199caeada062dd81b2e1ad7ccb63c3f3.png)



### 4.4 AsyncTimer使用基础

```c
#include <AsyncTimer.h>
AsyncTimer t;	//定义一个定时器

void setup(){
    
}
void loop(){
    t.handle();	//再loop函数里必须写上这句
    
    //开始处理其他事情
}
```

运行原理:

- 生成配置好一个定时器后，所有的操作都在handle函数中完成,每一次loop时定时器都在handle中执行一次所有和定时器有关的操作。



### 4.5 创建单次运行的定时任务

setTimeout

功能

- 创建一个单次运行的定时任务

定义

- `setTimeout(callbackFunction,delayInMs)`

参数

- callbackFunction使回调函数
- delayInMs是超时的时间，单位为ms

返回值

- 成功返回定时任务的编号，失败返回0

回调函数

- 可以使用普通的函数，形式为`void func(){}`
- 也可以使用lamda表达式，无参无返回值

一创建好定时任务，定时任务就开始工作了，且只执行一次

```c
//使用lambda函数
AsyncTimer t;
t.setTimeout([](){
    Serial.println("hello world");
},2000);

//使用普通函数
AsyncTimer t;
void functionToCall()
{
    Serial.println("hello world");
}
t.setTimeout(functionToCall,2000);
```



### 4.6  创建周期运行的定时任务

setInterval

功能

- 创建一个周期运行的定时任务

定义

- `setInterval(callbackFunction,delayInMs)`

参数

- callbackFunction是回调函数
- delayInMs是超时的时间，单位为ms

返回值

- 成功返回定时任务的编号，失败返回0

回调函数

- 可以使用普通函数，形式为`void func(){}`
- 也可以使用lamda表达式，无参无返回值

一创建好定时任务，定时任务就开始工作了，且周期执行

```c
//使用lambda函数
AsyncTimer t;
t.setInterval([](){
    Serial.println("hello world");
},2000);

//使用普通函数
AsyncTimer t;
void functionToCall()
{
    Serial.println("hello world");
}
t.setInterval(functionToCall,2000);
```

### 4.7 停止单个定时任务

cancel

功能

- 停止单个定时任务

定义

- `cancel(interval Or TimeoutId)`

参数

- interval和TimeoutId是指定的定时任务的编号

```c
// 取消一个interval
AsyncTimer t;

unsigned short intervalId = t.setInterva1([]() {
    Serial.println("Hello world!");
},2000);
//Cancel the interval after i seconds :
t.setTimeout([=](){
	t.cancel(intervalId );
},7000);

//取消一个timeout
AsyncTimer t;

// This timeout will never run
unsigned short timeoutId = t.setTimeout([](){
    Serial.println("Hello world!");
},3000);

// Cancel the timeout before it's executed
t.cancel(timeoutId);
```

### 4.8 停止多个定时任务

cancelAll

功能

- 停止多个定时任务

定义

- `cancelAll(includeIntervals = true)`
- 如果includeIntervals为true，是取消所有定时任务，包括周期性和一次性，如果为false，则只取消单次的定时任务

```c
//停止所有的定时任务
AsyncTimer t;

t.setInterval([](){
	Serial.println("foo");
},2000);

t.setTimeout([](){
	Serial.println("bar");
},7000);

t.setTimeout([](){
	Serial.print1n("baz");
},7000);

// After this call，nothing will be running inside AsyncTimer
t.cancelAll();

//只取消单次的定时任务
AsyncTimer t;

t.setInterval([](){
	Serial.println("foo");
},2000);

t.setTimeout([](){
	Serial.println("bar");
},7000);

t.setTimeout([](){
	Serial.print1n("baz");
},7000);

// After this call，nothing will be running inside AsyncTimer
t.cancelAll(false);
```

### 4.9 改变定时任务周期

changeDelay

功能

- 改变定时任务周期

定义

- `changeDelay(interval Or TimeoutId, delayInMs)`

参数

- interval Or TimeoutId定时器编号
- delayInMs新的超时时间（ms）

```c
AsyncTimer t;

unsigned short intervalId = t.setInterval([](){
    Serial.println("Hello world!");
}，2000) ;

t.setTimeout([=](){
	t.changeDelay(intervalId，3500);
	//Now the interval runs every 35eems instead of the old 2000ms
},7000);
```

### 4.10 重置定时任务

reset

功能

- 重置定时任务

定义

- `reset(interval Or TimeoutId)`

参数

- interval Or TimeoutId定时器编号

注意

- 只能重置还没有停止的（活跃）的定时任务，重置完后重新从0开始计时

```c
AsyncTimer t;

unsigned short intervalId = t.setInterval([](){
    serial.println("Hello world!");
},2000);

t.setTimeout([=](){
    t.reset(intervalId);
	// Now the interval will be reset， this means that it willl / execute exactly 200ems after the reset function call.
},7000);
```

### 4.11 额外延时一个定时任务

delay

- 将活跃的定时任务的超时时长再临时延长delaylnMs

定义

- `delay(interval Or TimeoutId, delayInMs)`

参数

- interval Or TimeoutId定时器任务的编号
- delayInMs额外延时的时间



### 4.12 获取定时任务剩余时间

getRemaining

功能

- 获取指定定时任务本轮还剩多久时间超时

定义

- `getRemaining(interval Or TimeoutId)`

参数

- interval Or TimeoutId定时器任务的编号



### 4.13 改造闪烁led灯的程序

![](https://cdn.staticaly.com/gh/pepedd864/cdn-repos@main/img/42b6016e1e7eb7e9fc79db12c4979023.png)

任务

- led灯刚启动时以1s的周期进行闪烁
- 按键按下去后在 1s 和 3s的周期进行切换



程序实现

```c
#include <RBD_Button.h>
#include <AsyncTimer.h>

int switchPin = 25;
int ledPin = 4;
int ledStatus = HIGH;
int t = 1;  //闪烁周期

//带消抖功能的按键
RBD::Button button(switchPin, INPUT_PULLUP);

AsyncTimer timer;
int taskId = 0;

void changeLedStatus() {
  ledStatus = !ledStatus;
  digitalWrite(ledPin, ledStatus);
}

void setup() {
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);  //点亮LED
  //创建周期任务
  taskId = timer.setInterval(changeLedStatus, t * 1000);
}

void loop() {
  timer.handle();

  if (button.onPressed()) {
    t = t == 1 ? 3 : 1;
    timer.changeDelay(taskId, t * 1000);
  }
}

```



## 5. ADC数模转换器

### 5.1 ADC

ADC

- ADC是Analog-to-Digital Converter的缩写。指模/数转换器或者模拟/数字转换器。是指将连续变量的模拟信号转换为离散的数字信号的器件。
- 典型的模拟数字转换器将模拟信号转换为表示一定比例电压值的数字信号。

![](https://raw.githubusercontent.com/pepedd864/cdn-repos/main/img/3c7da3854d9b4d7bd9bff9d840f4a922.png)

### 5.2 ADC关键参数

ADC关键参数

- 支持测量的模拟量的范围
- 输出数字信号的精度（bit）
- 采样的频率

<img src="https://raw.githubusercontent.com/pepedd864/cdn-repos/main/img/7e71d8bb6a5fad5040b4fac0d856964e.png" style="zoom:50%;" />

### 5.3 ESP32的ADC

ESP32的ADC

- ESP32集成了12-bit ADC，共支持18个模拟通道输入。最多可配置18个管脚的ADC，用于电压模数转换。
- 当有使用WIFI时，将无法使用ADC2的通道，只能使用ADC1
- 蓝牙可以和ADC2同时使用
- 两个ADC默认的量化位宽（精度)是12bit
- 使用Arduino库中的函数得到的电压值是已经经过修正过的，误差在20-60mV之间，但ADC不是非常线性的!
- 测量电压的引脚不能悬空，如果悬空采集到的将是一个随机值。
- **ADC1可以安全使用的GPIO口:4,12,13,14,25,26,27**
- **ADC2可以安全使用的GPIO口:32-36,39**
- 36，39口内置霍尔传感器，请勿将其他任何东西连接到这些引脚，也不要更改其配置。否则可能会影响传感器的低值信号的测量。

![](https://raw.githubusercontent.com/pepedd864/cdn-repos/main/img/ffddf3d329ad5986d794a9b8922d4cae.png)

### 5.4 减少噪声

ESP32 ADC对噪声很敏感，导致ADC读数的巨大差异。根据使用情况,用户可以在使用中的ADC输入焊盘上连接一个旁路电容(例如，**一个100nF的陶瓷电容**)，以尽量减少噪声。此外，也可以使用**多次采样**来进—步减轻噪声的影响。

![](https://raw.githubusercontent.com/pepedd864/cdn-repos/main/img/f6427a765386f8d2af8530718a760967.png)

### 5.5 ADC的参考电压及衰减设置

ESP32默认的参考电压是1.1V(每个芯片间有差异，非精准)，所以只能测量0-1.1V的电压;

为了能够测量更大量程的电压，需要使用其衰减配置;每个通道都可以单独配置

![](https://raw.githubusercontent.com/pepedd864/cdn-repos/main/img/b5a64babdf67e2c3bc530f2184b3e0d9.png)

### 5.6 设置ADC的位宽（精度）

`void analogReadResolution(uint8_t bits);	//参数的范围为[9,12]`

`void analogSetWidth(uint8_t bits);`

### 5.7 设置ADC的衰减值（测量范围）

设置所有通道的衰减值

`void analogSetAttenuatiion(adc_attenuation_t attenuation);`



设置指定GPIO口的衰减值

`void analogSetPinAttenuaation(uint8_t pin,adc_attenuation_t attenuation);`



```c
typedef enum {
    ADC_Odb,
    ADC_2_5db,
    ADC_6db,
    ADC_11db
}adc_attenuation_t;
```



![](https://raw.githubusercontent.com/pepedd864/cdn-repos/main/img/227949589427089345b1872f609b8be4.png)



### 5.8 读取电压函数

获取指定GPIO口ADC的值

`uint16_t analogRead(uint8_t pin);`



获取指定GPIO口电压值（毫伏值）

 `uint32_t analogReadMilliVolts(uint8_t pin);`

- 获取到的这两个值都是已经经过修正过的
- 获取到的电压值在150-2450 mv之间精度还可以，在这个区间之后误差比较大。



### 5.9 获取霍尔传感器的ADC值

`int hallRead();`

- 这个返回的是ADC的值，而不是电压值。
- 精度是12位
- 霍尔传感器是连接到36,39GPIO口的



### 5.10 ESP32使用ADC流程

- 找一个可用的ADC的口，接入电路
- 设置读取的精度（位宽)
  analogReadResolution
- 设置通道的衰减值（不设置的话是11db)
  analogSetAttenuation 或analogSetPinAttenuation
- 读取ADC值或电压值
  analogRead或analogReadMilliVolts



![](https://raw.githubusercontent.com/pepedd864/cdn-repos/main/img/8f6ff8cf2ce65bee9109085e864cf55b.png)



### 5.11 ESP32使用电位器控制LED亮度

ADC及LEDC的使用

![](https://raw.githubusercontent.com/pepedd864/cdn-repos/main/img/ac8a4421f00c6b5dd0aa1fa0d536f6dc.png)

GPIO32接5OK电位器
GPIO4接LED灯，限流电阻120欧

要求:使用电位器控制LED的亮度

PWM信号:调光
电位器控制输入电压大小
电位器→电压→占空比→LED亮度



#### 5.11.1 电位器

![](https://raw.githubusercontent.com/pepedd864/cdn-repos/main/img/8e168ed8b766b20d02b127566f9e7f66.png)

GPIO32口的电压变化范围为0-3.3V使用ADC来采集,并控制PWM信号的占空比



#### 5.11.2 代码

三大组件：ADC、LEDC、定时器

```c
#include <AsyncTimer.h>

int pmPin = 32;		//电位器接的GPIO口
int ledPin = 4;		//LED
int ch0 = 0;		//ledc的通道

AsyncTimer timer;
int taskId = 0;

void changeLedLightness()
{
    int val = analogRead(pmPin);			//读入电位器的ADC值
    Serial.println("%d: ",val);
    
    auto vol = analogReadMilliVolts(pmPin);	//读入电位器的电压
    Serial.println(vol);
    
    int duty = val/4095.0*1024;				//计算占空比
    ledcWrite(ch0,duty);					//设置占空比
}

void setup()
{
    Serial.begin(115200);
    analogReadResolution(12);
    analogSetAttenuation(ADC_11db);
    
    ledcSetup(ch0,1000,10);
    ledcAttachPin(ledPin,ch0);
    
    taskId = timer.setInterval(changeLedLightness,20);
}

void loop()
{
    timer.handle();
}
```



## 6. I2C协议与Wire库



### 6.1 I2C协议简介

I2C

- 两线式串行总线,用于连接微控制器及其外围设备。它是串行的半双工通信方式。
- I2C总线具有两根双向信号线，一根是数据线SDA,另―根是时钟线SCL,特别注意，有些资料上会把SDA说成是SDI, SCL说成是SCK。
- 时钟是由主机产生的
- 通信由主设备发起,并主导传输过程,从设备按I2C协议接收主设备发送的数据，并及时给出响应。
- 每个接到I2C总线上的器件（从设备)都有唯一的地址(地址有7位和10位两种，我们常见7位的）
- 用于低速设备的连接,速度不及SPI,快于串口通信，接线简单。标准模式(100kbps)，快速模式(400kbps)





![](https://raw.githubusercontent.com/pepedd864/cdn-repos/main/img/e09cc14069abfeb3a8fc21f135eb5f94.png)



### 6.2 ESP32的I2C控制器

- ESP32有2个I2C控制器（(也称为端口），负责处理在I2C总线上的通信。每个控制器都可以设置为主机或从机。
- ESP32有两个I2C通道，任何引脚都可以设置为SDA或SCL。不过一般情况下不要去改变它。默认的I2C引脚是
  - GPIO 21(SDA)
  - GPIO 22(SCL)

![](https://raw.githubusercontent.com/pepedd864/cdn-repos/main/img/3af3016a3139c6e599fbf80d2a5e9040.png)



### 6.3 ESP32 I2C操作库Wire

- `#include <Wire.h>`
- 库里面已经预定义好了两个I2C的对象,可以直接拿来使用
  - Wire
  - Wire1
- 库默认的时钟频率是100KHz(标准模式)
- 从机加入总线时要确定自己的地址(1-127)



加入I2C总线（begin）

```c
//做为主机加入, sda: 21 scl:22频率100kHz
Wire.begin();
//做为主机加入, sda:25 scl:26频率100kHz
Wire.begin(25,26);
//做为主机加入, sda:21 scl:22频率200kHz
Wire.begin(-1,-1,200000);
//做为从机加入,地址是27, sda: 21 scl:22频率100kHz
Wire.begin(27);
//做为从机加入,地址是27， sda: 25 scl:26频率200kHz
Wire.begin(27,25，26,200000);
```

- 函数返回true,成功加入，返回false，失败,后续都不能进行操作。
