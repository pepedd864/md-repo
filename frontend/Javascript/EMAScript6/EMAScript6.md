[TOC]



# 1. ES6简介

`ECMAScript 6.0`（以下简称 ES6）是` JavaScript` 语言的下一代标准，已经在 2015 年 6 月正式发布了。它的目标，是使得 JavaScript 语言可以用来编写复杂的大型应用程序，成为企业级开发语言

**关于ES6:**

- 1996 年 11 月，`JavaScript` 的创造者 Netscape 公司，决定将` JavaScript` 提交给标准化组织 ECMA，希望这种语言能够成为国际标准。次年，ECMA 发布 262 号标准文件（ECMA-262）的第一版，规定了浏览器脚本语言的标准，并将这种语言称为 `ECMAScript`，这个版本就是 1.0 版。

**ES6的支持情况:**

- [https://kangax.github.io/compat-table/es6/]:

# 2. 作用域

作用域

- 作用域（ scope）规定了变量能够被访问的“范围”，离开了这个“范围”变量便不能被访问

作用域分为

- 局部作用域
- 全局作用域

## 2.1 局部作用域

局部作用域分为函数作用域和块作用域。

1. 函数作用域
   - 函数内部声明的变量，在函数外部无法被访问
   - 函数的参数也是函数内部的局部变量
   - 不同函数内部声明的变量无法互相访问
   - 函数执行完毕后，函数内部的变量实际被清空了

2. 块作用域
   - 在JavaScript 中使用{}包裹的代码称为代码块，代码块内部声明的变量外部将【**有可能**】无法被访问。
   - let声明的变量会产生块作用域,var不会产生块作用域
   - const声明的常量也会产生块作用域
   - 不同代码块之间的变量无法互相访问
   - 推荐使用let或const

## 2.2 全局作用域

`<script>`标签和`.js`文件的【最外层】就是所谓的全局作用域，在此声明的变量在函数内部也可以被访问。全局作用域中声明的变量，任何其它作用域都可以被访问

- 为window对象动态添加的属性默认也是全局的，不推荐!
- 函数中未使用任何关键字声明的变量为全局变量，不推荐!
- 尽可能少的声明全局变量，防止全局变量被污染

## 2.3 作用域链

作用域链本质上是底层的**变量查找机制**。

- 在函数被执行时，会**优先查找当前函数作用域**中查找变量
- 如果当前作用域查找不到则会依次**逐级查找父级作用域**直到全局作用域



1. 嵌套关系的作用域串联起来形成了作用域链
2. 相同作用域链中按着从小到大的规则查找变量
3. 子作用域能够访问父作用域，父级作用域无法访问子级作用域



## 2.4 垃圾回收机制(内存回收)

**垃圾回收机制(Garbage Collection)简称GC**

- JS中内存的分配和回收都是自动完成的，内存在不使用的时候会被垃圾回收器自动回收

**内存的生命周期**

- JS环境中分配的内存，一般有如下生命周期:
  1. **内存分配**:当我们声明变量、函数、对象的时候，系统会自动为他们分配内存
  2. **内存使用**:即读写内存，也就是使用变量、函数等
  3. **内存回收**:使用完毕，由**垃圾回收器**自动回收不再使用的内存

## 2.5 垃圾回收机制-算法说明

两种常见的浏览器垃圾回收算法:

- 引用计数法
- 标记清除法

**引用计数**

- IE采用的引用计数算法，定义“内存不再使用”，就是看一个对象是否有指向它的引用，没有引用了就回收对象
  算法:
  1. 跟踪记录被引用的次数
  2. 如果被引用了一次，那么就记录次数1,多次引用会累加++
  3. 如果减少一个引用就减1 --
  4. 如果引用次数是0，则释放内存
- 缺点
  - 它存在一个致命的问题:**嵌套引用**（循环引用)
  - 如果两个对象**相互引用**，尽管他们已不再使用，垃圾回收器不会进行回收，导致内存泄露。

**标记清除法**

- 现代浏览器通用的大多是基于标记清除算法的某些改进算法,
  总体思想都是一致的。核心:
  1. 标记清除算法将“不再使用的对象”定义为“无法达到的对象”。
  2. 就是从**根部**(root)（在JS中就是全局对象）出发定的扫描内存中的对象。凡是能从根部到达的对象，都是还需要使用的。
  3. 那些**无法**由根部出发触及到的**对象被标记**为不再使用，稍后进行回收。

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/cf14d27a43cd66bec1057f0a28b2dbae.png)

## 2.6 闭包

闭包

- 概念:一个函数对周围状态的引用捆绑在一起，内层函数中访问到其外层函数的作用域
- 简单理解: **闭包=内层函数＋外层函数的变量**

```js
function outer(){
    const a = 1
    function f(){
        console.log(a)	//内部函数使用到了外部函数的变量
    }
    f()
}
outer()
```

- 作用:封闭数据，提供操作，外部也可以访问函数内部的变量
- 基本格式

```js
function outer(){
    let i = 1
    function fn(){
        console.log(i)
    }
    return fn
}
const fun = outer()
fun()			// 1
// 外层函数使用内部函数的变量

// 简约写法
function outer(){
    let i = 1
    return ()=>{
        console.log(i)
    }
}
const fun = outer()
fun()
```

- 可能引发的问题
  - 内存泄漏

## 2.7 变量提升

javascript中允许变量声明前被访问（仅存在于var声明变量）

注意

1. 变量在未声明即被访问时会报语法错误
2. 变量在var声明之前即被访问，变量的值为undefined
3. let/const声明的变量不存在变量提升
4. 变量提升出现在相同作用域当中
5. **实际开发中推荐先声明再访问变量**



# 3. 函数

## 3.1 函数提升

函数提升

- 函数提升与变量提升比较类似，是指函数在声明之前即可被调用。

```js
// 调用函数
foo()
// 声明函数
function foo(){
    console.log('声明之前即被调用')
}

// 不存在提升现象
bar()	//错误
var bar = function(){
    console.log('...')
}
```

- 函数提升能够使函数的声明调用更灵活
- 函数表达式不存在提升的现象
- 函数提升出现在相同作用域当中



## 3.2 函数参数

### 3.2.1 动态参数

`arguments`是函数内部内置的伪数组变量，它包含了调用函数时传入的所有实参

```js
// 求和函数，计算所有参数的和
function sum(){		// 动态参数不需要指定参数
    let s = 0;
    for(let i = 0;i< arguments.length;i++){
        s += arguments[i]
    }
    console.log(s)
}
// 调用求和函数
sum(5,10)	
sum(1,2,4)	
```

- arguments是一个伪数组，只存在于函数中
- arguments的作用是动态获取函数的实参
- 可以通过for循环依次得到传递过来的实参

### 3.2.2 剩余参数

剩余参数允许我们将一个不定数量的参数表示为一个数组

```js
function getSum(...other) {
    console.log(other)
}
getSum(1,2,3)
```

- `...`是语法符号，置于最末函数形参之前，用于获取多余的实参
- 借助`...`获取的剩余实参，是个真数组

```js
funcyion config(baseURL,...other) {
}
//调用函数
config('http://baidu.com', 'get','json');
```

- 提倡使用**剩余参数**

### 3.2.3 展开运算符

展开运算符(`...`)，将一个数组进行展开

```js
const arr = [1,5,3,8,2]
console.log(..arr) // 1 5 3 8 2
```

- 不会修改原数组

典型应用：求数组最大值（最小值）

```js
const arr = [1,2,3]
// ...arr === 1,2,3
console.log(Math.max(...arr))
```

典型应用：合并数组

```js
const arr1 = [1,2,3]
const arr2 = [3,4,5]
const arr = [...arr1,...arr2]	// 1,2,3 , 3,4,5
```

### 3.2.4 展开运算符和剩余参数的区别

剩余参数

- 函数参数使用，得到真数组

展开运算符

- 数组使用，数组展开



## 3.3 箭头函数

### 3.3.1 形式

箭头函数

- 引入箭头函数的目的是更简短的函数写法并且不绑定this，箭头函数的语法比函数表达式更简洁
- 箭头函数更适合那些**需要使用匿名函数的地方**

语法1：普通形式

```js
// 普通函数
const fn = function() {
    console.log('普通函数')
}
fn()

// 箭头函数
const fn = () => {
    console.log('箭头函数')
}
fn()
```

语法2：只有一个参数可以省略小括号

```js
const fn = function (x) {
    return x + x
}
console.log(fn(1))

// 箭头函数
const fn = x => {
    return x + x
}
console.log(fn(1))
```

语法3：如果函数体只有一行代码，可以写到一行上，并且无需写return直接返回值

```js
const fn = (x,y) => x + y
console.log(fn(1,2))
```

语法4：加括号的函数体返回对象字面量表达式

```js
const fn = uname => ({uname: uname})
console.log(fn('箭头函数'))
```

### 3.3.2 参数

- 普通函数有`arguments`动态参数
- 箭头函数没有`arguments`动态参数，但是有剩余参数`...args`



### 3.3.3 this

以前`this`的指向

- 谁调用这个函数，`this`就指向谁

```js
// 
console.log(this) // window
function fn() {
    console.log(this)	// window
}
fn()

// 对象
const obj = {
    uname: '对象',
    whichThis: function() {
        console.log(this)	// obj
    }
}
obj.whichThis()
```

箭头函数不会创建自己的`this`,它只会从自己的作用域链的上一层沿用`this`。

```js
const fn = () => {
    console.log(this) // window
}
fn()

// 对象方法this
const obj = {
    uname: '对象',
    whichThis: () => {
        console.log(this)	// 指向window
    }
}
obj.whichThis()

// 对象成员函数中嵌套箭头函数
const obj = {
    uname: '对象',
    whichThis: function() {
        let i = 10
        const count = () => {
            console.log(this)	// obj, 箭头函数寻找上层函数指向的this 即obj
        }
    }
}
```

在开发中【使用箭头函数前需要考虑函数中this 的值】，事件回调函数使用箭头函数时，this为全局的window，**因此DOM事件回调函数为了简便，还是不太推荐使用箭头函数**

```js
// 箭头函数
btn.addEventListener('click', () => {
    console.log(this)		// this指向window
})

// 普通函数
btn.addEventListener('click', function () {
    console.log(this)		// this指向DOM对象
})
```



# 4. 解构赋值

## 4.1 数组解构

### 4.1.1 基本使用

数组解构

- 数组解构是将数组的单元值快速批量赋值给一系列变量的简洁语法。

基本语法:

1. 赋值运算符=左侧的[]用于批量声明变量，右侧数组的单元值将被赋值给左侧的变量
2. 变量的顺序对应数组单元值的位置依次进行赋值操作

```js
// 赋值
 const arr = [100,60,80]
 const [max,min,avg] = arr
// 等价于
 const max = arr[0]
 const min = arr[1]
 const avg = arr[2]
```

典型应用：交换两个变量

```js
let a = 1
let b = 3;		// 必须加分号
[b,a] = [a,b]
console.log(a)	// 3
console.log(b)  // 1
```

javascript必须加分号的情况

```js
// 1. 立即执行函数
(function t() { })();
// 或者
;(function t() { })()

// 2. 数组解构
;[b,a] = [a,b]
```

### 4.1.2 特殊情况

-  变量多，单元值少，underfined

```js
const [a,b,c,d] = [1,2,3]
console.log(a) // 1
console.log(b) // 2
console.log(c) // 3
console.log(d) // undefined

// 防止underfined传递
const [a=0,b=0] = []
console.log(a)	// 0
console.log(b)  // 0
```

- 变量少，单元值多

```js
const [a,b] = [1,2,3,4]
console.log(a)	// 1
consloe.log(b)  // 2 

// 剩余参数
const [a,b,...c] = [1,2,3,4]
console.log(a)	// 1
consloe.log(b)  // 2 
console.log(c)  // [3,4] 真数组
```

- 按需导入，忽略某些值

```js
// 按需导入
const [a,,c,d] = [1,2,3,4]
console.log(a) // 1
console.log(c) // 3
console.log(d) // 4
```

### 4.1.3 多维数组解构

支持多维数组解构

```js
const [a,b,c] = [1,2,[3,4]]
console.log(a)	// 1
console.log(b)  // 2
console.log(c)  // [3,4]

const [a,b,[c,d]] = [1,2,[3,4]]
console.log(a)	// 1
console.log(b)  // 2
console.log(c)  // 3
console.log(d)  // 4
```



## 4.2 对象解构

### 4.2.1 基本使用

对象解构

- 对象解构是将对象属性和方法快速批量赋值给一系列变量的简洁语法

基本语法:

1. 赋值运算符=左侧的0用于批量声明变量，右侧对象的属性值将被赋值给左侧的变量

2. 对象属性的值将被赋值给与属性名相同的变量
3. 注意解构的变量名不要和外面的变量名冲突否则报错
4. 对象中找不到与变量名一致的属性时变量值为undefined

```js
const {uname, age} = {uname: 'zhangsan', age: 18}
// 等价于 const uname = obj.uname
console.log(uname,age);		// zhangsan 18

// 解构变量名要与对象成员属性名相同
const {vname,age} = {uname:'zhangsan',age:18}
console.log(vname,age);		// underfined 18

// 但也可以重新改名
const { uname: username, age } = { uname: 'zhangsan', age: 18 }
console.log(username, age);		// zhangsan 18
```

### 4.2.2 数组对象

```js
// 解构数组对象
const obj = [
    {
        uname: 'zhangsan',
        age: 18
    }
]
const [{uname,age}] = obj
console.log(uname,age);
```

### 4.2.3 多级对象解构

```js
// 多级对象解构
const obj = {
    a: {
        b: {
            c: 1
        }
    }
}
const { a: { b: { c } } } = obj
console.log(c)  // 1
```

### 4.2.4 使用对象解构案例

```js
// 处理后台数据
const obj = {
    "code": 20041,
    "msg": "查询成功",
    "data": [
        "娱乐",
        "其他活动",
        "学习",
        "工作区",
        "视频"
    ]
}
const { data } = obj	//获得data对象

// 将解构的对象传递给函数
// 方式一：
function render(obj) {
    const { data } = obj
    // 处理data
    console.log(arr)
}
render(obj)

// 方式二：参数直接解构
function redner({ data }) {
    // 处理数据
    console.log(data)
}
render(obj)
```



# 5. 数组方法

## 5.1 forEach

forEach

- `forEach()`方法用于调用数组的每个元素，并将元素传递给回调函数
- 主要使用场景:遍历数组的每个元素

```js
const arr = ['red','green','pink']
arr.forEach(function(item,index){
    console.log(item)	// red green pink
    console.log(index)	// 索引
})
```

## 5.2 map

map

- 用于迭代数组

```js
const arr = ['red','green','pink']
arr.map(function(item,index){
    console.log(item)	// red green pink
    console.log(index) // 索引
})
```

- 使用场景
  - map可以处理数据，并返回新的数组

```js
const arr = ['red', 'green', 'pink']
const arrMap = arr.map(function (item, index) {
    return item + ' pig'	// 处理数组元素
})
console.log(arrMap); // [ 'red pig', 'green pig', 'pink pig' ]

const arr = [10,20,30]
const newArr = arr.map(function(item){
    return item + 10
})
console.log(newArr);    // [20,30,40]
```

## 5.3 join

join

- 把数组中所有元素转换为一个字符串
- `join(分割符)`，join的参数为转换成的字符串的分隔符

```js
const arr = [1, 2, 3, 4, 5];
console.log(arr.join('-')); // 1-2-3-4-5
```

## 5.4 filter

filter

- `filter()`方法创建一个新的数组，新数组中的元素是通过检查指定数组中符合条件的所有元素
- 主要使用场景:**筛选数组符合条件的元素**，并返回筛选之后元素的新数组

```js
const arr = [30, 20, 12, 10, 5, 1];
const newArr = arr.filter(item => {
    return item > 10;
})
console.log(newArr);    // [30, 20, 12]
```

## 5.5 reduce

reduce返回累计处理的结果，经常用于求和等

```js
// 没有初始值
const arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
const total = arr.reduce(function(prev,curr){
    return prev + curr
})
console.log(total);	// 55

// 有初始值
const arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
const total = arr.reduce(function(prev,curr){
    return prev + curr
},20)	// 初始值
console.log(total);
```

实现过程

1. 如果没有起始值，则上一次值以数组的第一个数组元素的值
2. 每一次循环，把返回值给做为下一次循环的上一次值
3. 如果有起始值，则起始值做为上一次值

# 6. 对象

## 6.1 创建对象的三种方式

1. 使用对象字面量创建对象

```js
const obj = {
    a: 1,
    b: 2,
    c: 3
}
```

2. 使用new Object方式

```js
const obj = new Object()
console.log(obj)
```

3. 使用构造函数创建

## 6.2 构造函数

### 6.2.1 基本使用

构造函数∶

- 是一种特殊的函数，主要用来初始化对象

使用场景:

- 常规的`{...}`语法允许创建一个对象。比如我们创建了佩奇的对象，继续创建乔治的对象还需要重新写一遍，此时**可以通过构造函数来快速创建多个类似的对象**。

```js
// 构造函数
function Person(name, age) {
    this.name = name;
    this.age = age;
}
const p = new Person('张三', 20);
console.log(p.name); // 张三
```

本质

- 构造函数仍然是常规函数

约定

1. 命名使用大写字母开头
2. 只能使用`new`操作符来执行

### 6.2.2 原理

1. 使用`new`创建对象
2. 构造函数`this`指向新对象
3. 执行构造函数代码，修改`this`指向的对象，添加新的属性
4. 返回新对象

## 6.3 实例成员和静态成员

实例成员:

- 通过构造函数创建的对象称为实例对象，**实例对象中的属性和方法称为实例成员(实例属性和实例方法)**

```js
// 实例成员
function Person(name, age) {
    this.name = name
    this.age = age
}
// 实例成员
var p1 = new Person('zs', 18)
var p2 = new Person('ls', 20)
// 实例属性
p1.name = 'zs'
p1.age = 18
p2.name = 'ls'
p2.age = 20
// 实例方法
p1.say = function () {
    console.log('...')
}
p2.say = function () {
    console.log('...')
}
```

静态成员

- 构造函数的属性和方法被称为静态成员（静态属性和静态方法）

```js
// 静态成员
function Person(name,age) {
    // 省略实例成员
}
// 静态属性
Person.eyes = 2
Person.arms = 2
//静态方法
Person.walk = function() {
    console.log('...')
    console.log(this.eyes)
}
```

说明

1. 静态成员只能构造函数来访问

2. 静态方法中的this指向构造函数

   比如 `Date.now()`  `Math.PI`  `Math.random()`

## 6.4 内置构造函数

在JavaScript中最主要的数据类型有6种:

- 基本数据类型
  - 字符串、数值、布尔、undefined、null

- 引用类型
  - 对象

字符串、数值、布尔等基本类型也有专门的构造函数，这些我们称为包装类型

### 6.4.1 Object

Object是内置的构造函数，用于创建普通对象

```js
const user = new Object({name: '小明',age: 15})
```

- 推荐使用字面量构造对象

### 6.4.2 Object的三个静态方法

1. `Object.keys(对象)`获得所有的属性名

```js
const o = { name: 'zhangsan', age: 6 }
console.log(Object.keys(o));    // [ 'name', 'age' ]
```

2. `Object.values(对象)`获得所有的属性值

```js
const o = { name: 'zhangsan', age: 6 }
console.log(Object.values(o));   // [ 'zhangsan', 6 ]
```

3. `Object.assign(对象)`静态方法，常用于对象拷贝

```js
// 拷贝对象 把 o 拷贝给 obj
const o = {name: 'zhangsan', age: 6}
const obj = {}
Object.assign(obj,o)
console.log(obj)	// 	 {name: 'zhangsan', age: 6}
```

- 应用
  - 给对象添加属性

```js
const o = {name: 'zhangsan',age: 18}
Object.assign(o,{gender: '女'})
console.log(o)	// { name: 'zhangsan', age: 18, gender: '女' }
```

### 6.4.3 Array

1. 常用实例方法

| 方法      | 作用     | 说明                                                         |
| --------- | -------- | ------------------------------------------------------------ |
| `forEach` | 遍历数组 | 不返回数组，经常用于查找遍历数组元素                         |
| `filter`  | 过滤数组 | 返回新数组，返回的是筛选满足条件的数组元素                   |
| `map`     | 迭代数组 | 返回新数组，返回的是处理之后的数组元素，想要使用返回的新数组 |
| `reduce`  | 累计器   | 返回累计处理的结果，经常用于求和等                           |

2. 其他方法
   - 实例方法`join`数组元素拼接为字符串，返回字符串(重点)
   - 实例方法`find`查找元素，返回符合测试条件的第一个数组元素值，如果没有符合条件的则返回`undefined`(重点)
   - 实例方法`every` 检测数组所有元素是否都符合指定条件，如果所有元素都通过检测返回`true`，否则返回`false`(重点)
   - 实例方法`some`检测数组中的元素是否满足指定条件如果数组中有元素满足条件返回`true`，否则返回`false`
   - 实例方法`concat`合并两个数组，返回生成新数组
   - 实例方法`sort`对原数组单元值排序
   - 实例方法`splice`删除或替换原数组单元
   - 实例方法`reverse`反转数组
   - 实例方法`findIndex`查找元素的索引值

### 6.4.4 String 

1. 实例属性`length`用来获取字符串的度长(重点)
2. 实例方法`split('分隔符')`用来将字符串拆分成数组(重点)
3. 实例方法`substring (需要截取的第一个字符的索引[,结束的索引号])`用于字符串截取(重点)
4. 实例方法`startsWith(检测字符串[,检测位置索引号])`检测是否以某字符开头(重点)
5. 实例方法`includes(搜索的字符串[,检测位置索引号])`判断一个字符串是否包含在另一个字符串中，根据情况返回true或 false(重点)
6. 实例方法`toUppercase`用于将字母转换成大写
7. 实例方法`toLowerCase`用于将就转换成小写
8. 实例方法`indexOf`检测是否包含某字符
9. 实例方法`endsWith`检测是否以某字符结尾
10. 实例方法`replace`用于替换字符串，支持正则匹配
11. 实例方法`match`用于查找字符串，支持正则匹配



# 7. 正则表达式

## 7.1 简介

正则表达式

- 正则表达式(Regular Expression)是用于匹配字符串中字符组合的模式。在JavaScript中，正则表达式也是对象
- 通常用来查找、替换那些符合正则表达式的文本，许多语言都支持正则表达式。

使用场景

- 例如验证表单∶用户名表单只能输入英文字母、数字或者下划线，昵称输入框中可以输入中文**(匹配**)
  - 比如用户名:`/^[a-z0-9_-]{3,16}$/`
- 过滤掉页面内容中的一些敏感词(**替换**)，或从字符串中获取我们想要的特定部分(**提取**)等。

语法

1. 定义规则

```js
const reg = /表达式/
```

- 其中`/ /`是正则表达式字面量

2. 判断是否有符合规则的字符串

```js
reg.test('正则表达式')
```

- 如果正则表达式与指定的字符串匹配，返回true，否则返回false

```js
const reg = /表达式/
console.log(reg.test('正则表达式')); // true
```

3. 检索（查找）符合规则的字符串

```js
const reg = /表达式/
console.log(reg.exec('正则表达式')); 
// [ '表达式', index: 2, input: '正则表达式', groups: undefined ]
```

## 7.2 元字符

普通字符:

- 大多数的字符仅能够描述它们本身，这些字符称作普通字符，例如所有的字母和数字。也就是说普通字符只能够匹配字符串中与它们相同的字符

元字符(特殊字符)

- 是一些具有特殊含义的字符，可以极大提高了灵活性和强大的匹配功能。
  - 比如，规定用户只能输入英文26个英文字母，普通字符的话 `abcdefghijklm.....`
  - 但是换成元字符写法:`[a-z]`

 分类

- **边界符（表示位置，开头和结尾，必须用什么开头，用什么结尾）**
- 量词(表示重复次数)
- 字符类(比如`\d`表示0~9)

### 7.2.1 边界符

| 边界符 | 说明                         |
| ------ | ---------------------------- |
| `^`    | 表示匹配行首的文本(以谁开始) |
| `$`    | 表示匹配行尾的文本(以谁结束) |

```js
// 边界符
console.log(/^你/.test('你好'));    // true

console.log(/$你/.test('你好'));    // false

console.log(/^你$/.test('你'));    // true

console.log(/^你$/.test('你你'));    // false
```

### 7.2.2 量词

| 量词    | 说明                      |
| ------- | ------------------------- |
| `*`     | 重复零次或更多次 `>=0`    |
| `+`     | 重复一次或更多次 `>=1`    |
| `?`     | 重复零次或一次 `1 || 0`   |
| `{n}`   | 重复n次  `n`              |
| `{n,}`  | 重复n次或更多次 `>=n`     |
| `{n,m}` | 重复n到m次   `n<= x < =m` |

```js
console.log(/你{3}/.test('你你'));    // false
console.log(/你{3}/.test('你你你'));  // true

console.log(/你{3,}/.test('你你'));    // false
console.log(/你{3,}/.test('你你你'));  // true

console.log(/你{3,4}/.test('你你'));    // false
console.log(/你{3,4}/.test('你你你'));  // true
```

### 7.2.3 字符类

| 字符类 | 说明                                                         |
| ------ | ------------------------------------------------------------ |
| `[]`   | 后面的字符串只要包含`[]`中任意一个字符，都返回true<br />在`[]`中可以使用连字符`-`<br />例如：`[a-z]`表示a到z 的26个英文字母<br />`[a-zA-Z]`表示大小写英文字母<br />`[0-9]`表示0~9的数字都支持<br />在`[]`中加上`^`表示取反<br />比如：`[^a-z]`匹配除了小写字母以外的字符，注意要写到`[]`里面 |
| `.`    | 匹配除换行符之外的任何单个字符                               |
| `|`    | 匹配两侧的字符                                               |

```js
console.log(/^[abc]$/.test('a')); // true
console.log(/^[abc]$/.test('b')); // true
console.log(/^[abc]$/.test('c')); // true
console.log(/^[abc]$/.test('d')); // false
console.log(/^[abc]$/.test('ab')); // false
console.log(/^[abc]{2}$/.test('ab')); // true

console.log(/^[A-Z]$/.test('a'));   // false
console.log(/^[A-Z]$/.test('A'));   // true
console.log(/^[a-zA-Z0-9]$/.test(2)); // true
```

### 7.2.4 预定义

预定义

- 指的是某些常见模式的简写方式。

| 预定类 | 说明                                                         |
| ------ | ------------------------------------------------------------ |
| `\d`   | 匹配`0-9`之间的任一数字，相当于`[0-9]`                       |
| `\D`   | 匹配所有`0-9`以外的字符，相当于`[^0-9]`                      |
| `\w`   | 匹配任意的字母、数字和下划线，相当于`[A-Za-z0-9_]`           |
| `\W`   | 除所有字母、数字和下划线以外的字符，相当于`[^A-Za-z0-9_]`    |
| `\s`   | 匹配空格（包括换行符、制表符、空格符等)，相等于`[\t\r\n\v\f]` |
| `\S`   | 匹配非空格的字符，相当于`[^\t\r\n\v\f]`                      |

例如

```js
const dateFormat = /^\d{4}-\d{1,2}-\d{1,2}/
console.log(dateFormat.test('2019-01-01')); // true
```

### 7.2.5 修饰符

修饰符约束正则执行的某些细节行为，如是否区分大小写、是否支持多行匹配等

```js
// 语法
/表达式/修饰符
```

- i是单词ignore的缩写，正则匹配时字母不区分大小写
- g是单词global的缩写，匹配所有满足正则表达式的结果

```js
console.log(/^java$/.test('java'));     // true
console.log(/^java$/.test('Java'));     // false
console.log(/^java$/i.test('Java'));    // true
```

```js
let str = 'java是世界上最好的语言.Java'
str = str.replace(/java/ig, 'js')		// 使用g，全局修改
console.log(str);
```



