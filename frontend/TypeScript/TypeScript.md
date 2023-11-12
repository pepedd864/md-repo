## 1. 简介

Typescript是Javascript的超集，包含Javascript所有内容，新增了类型注解

### 1.1 快速入门

1. 安装

```bash
npm init -y # 初始化node
npm i typescript -g # 全局安装typescript
tsc -v # 查看版本号
```

2. 初始化ts

```bash
tsc -init # 初始化ts
```

3. 编译ts代码

```bash
tsc -w
```

4. 运行编译的js代码

```bash
node index.js
```

5. 安装调试工具

```bash
npm i ts-node -g
npm i @types/node -D
```

6. 调试ts代码

```bash
ts-node index.ts # 直接调试输出
```



## 2. 数据类型

### 2.1 基本类型

在js的基础上，添加`:`和类型即可定义变量

```ts
let str: string = 'ts-string'
let num: number = 123
let b1: boolean = true
let n: null = null
let b: underfined = underfined
let v: void = underfined
```

#### 2.1.1 字符串类型

使用`string`注解

```ts
let a: string = '123'
// 使用es6字符串模板
let str: string = `string${a}`
```

#### 2.1.2 数字类型

支持十六进制、十进制、八进制和二进制

```ts
let notANumber: number = NaN;//Nan
let num: number = 123;//普通数字
let infinityNumber: number = Infinity;//无穷大
let decimal: number = 6;//十进制
let hex: number = 0xf00d;//十六进制
let binary: number = 0b1010;//二进制
let octal: number = 0o744;//八进制s
```

#### 2.1.3 布尔类型

```ts
let b: boolean = true
```

注意

- 使用构造函数`Boolean`创建的对象不是布尔值

```ts
let createBoolean: boolean = new Boolean(1)  // 报错，返回的是一个Boolean对象
```

- 修改为

```ts
let createdBoolean: Boolean = new Boolean(1)
```

#### 2.1.4 空值类型

JavaScript 没有空值（Void）的概念，在 [TypeScript](https://so.csdn.net/so/search?q=TypeScript&spm=1001.2101.3001.7020) 中，可以用 `void` 表示没有任何返回值的函数

```ts
function voidFn(): void {
    console.log('test void')
}
```

`void` 类型的用法，主要是用在我们**不希望**调用者关心函数返回值的情况下，比如通常的**异步回调函数**

**void也可以定义undefined 和 null类型**

```ts
let u: void = undefined
let n: void = null;
```

#### 2.1.5 Null和underfined类型

```ts
let u: undefined = undefined;//定义undefined
let n: null = null;//定义null
```

`void`与`underfined`和`null`的区别

- 与 `void` 的区别是，`undefined` 和 `null` 是所有类型的子类型。也就是说 `undefined` 类型的变量，可以赋值给 string 类型的变量：

```ts
//这样写会报错 void类型不可以分给其他类型
let test: void = undefined
let num2: string = "1"
 
num2 = test
```

```ts
//这样是没问题的
let test: null = null
let num2: string = "1"
 
num2 = test
 
//或者这样的
let test: undefined = undefined
let num2: string = "1"
 
num2 = test
```

#### 2.1.6 注意事项

如果你在`tsconfig.json`开启了严格模式

```ts
{
    "compilerOptions":{
        "strict": true
    }
}
```

`null`不能赋予`void`类型

### 2.2 任意类型

#### 2.2.1 Any

`Any`类型

1. 没有强制限定哪种类型，随时切换类型都可以 我们可以对`any`进行任何操作，不需要检查类型

```ts
let anys:any = 123
anys = '123'
anys = true
```

2. 声明变量的时候没有指定任意类型默认为`any`

```ts
let anys;
anys = '123'
anys = true
```

3. 弊端如果使用`any`就失去了TS类型检测的作用

#### 2.2.2 unknown

`unknown`类型

1. TypeScript 3.0中引入的 `unknown`类型也被认为是 top type，但它更安全。与`any`一样，所有类型都可以分配给`unknown`

```ts
//unknown 可以定义任何类型的值
let value: unknown;
 
value = true;             // OK
value = 42;               // OK
value = "Hello World";    // OK
value = [];               // OK
value = {};               // OK
value = null;             // OK
value = undefined;        // OK
value = Symbol("type");   // OK
```

2. `unknown`类型比`any`更加严格当你要使用`any`的时候可以尝试使用`unknown`

3. `unknown`可赋值对象只有`unknown`和`any`

```ts
//这样写会报错unknow类型不能作为子类型只能作为父类型 any可以作为父类型和子类型
//unknown类型不能赋值给其他类型
let names:unknown = '123'
let names2:string = names
 
//这样就没问题 any类型是可以的
let names:any = '123'
let names2:string = names   
 
//unknown可赋值对象只有unknown 和 any
let bbb:unknown = '123'
let aaa:any= '456'
 
aaa = bbb
```

#### 2.2.3 区别

1. `Any`类型可以调用对象的属性和方法，而`unknown`不行
2. 因此`unknown`类型更加安全

```ts
// 如果是any类型在对象没有这个属性的时候还在获取是不会报错的
let obj:any = {b:1}
obj.a
 
 
// 如果是unknow 是不能调用属性和方法
let obj:unknown = {b:1,ccc:():number=>213}
obj.b
obj.ccc()
```



### 2.3 对象类型

**Object和object**

1. 所有的**原始类型**和对象类型最终都指向`Object`，可以说都是由`Object`继承而来，`Object`还可以写成`{}`

```ts
let a:Object = 123
let a:Object = '124'
let a:Object = []
let a:Object = () => {}
```

2. `object`是除了原始类型以外的类型

```ts
let a:Object = 123	// 错误
let a:Object = '124'	// 错误
let a:Object = []	// 正确
let a:Object = () => {} // 正确
```

### 2.4 数组类型

1. `[]`类型

```ts
let arr:boolean[] = [true,false]
```

2. 泛型

```ts
let arr:Array<boolean> = [true,false]
```

3. 用接口表示数组，一般用于表示类数组

```ts
interface NumberArray {
    [index: number]: number;
}
let fibonacci: NumberArray = [1,1,2,3,5]
```

4. 多维数组

```ts
let data: number[][] = [[1,2],[2,3]]
```

5. arguments类数组

```ts
function Arr(...args:any): void {
    console.log(arguments)
    //错误的arguments 是类数组不能这样定义
    let arr:number[] = arguments
}
Arr(111, 222, 333)
 
 
 
function Arr(...args:any): void {
    console.log(arguments) 
    //ts内置对象IArguments 定义
    let arr:IArguments = arguments
}
Arr(111, 222, 333)
 
//其中 IArguments 是 TypeScript 中定义好了的类型，它实际上就是：
interface IArguments {
[index: number]: any;
length: number;
callee: Function;
}
```

### 2.5 函数类型

1. 参数类型

```ts
//注意，参数不能多传，也不能少传 必须按照约定的类型来
const fn = (name: string, age:number): string => {
    return name + age
}
fn('张三',18)
```

2. 可选参数

```ts
//通过?表示该参数为可选参数
const fn = (name: string, age?:number): string => {
    return name + age
}
fn('张三')
```

3. 参数默认值

```ts
const fn = (name: string = "我是默认值"): string => {
    return name
}
fn()
```

4. 接口定义函数参数

```ts
//定义参数 num 和 num2  ：后面定义返回值的类型
interface Add {
    (num:  number, num2: number): number
}
 
const fn: Add = (num: number, num2: number): number => {
    return num + num2
}
fn(5, 5)
 
 
interface User{
    name: string;
    age: number;
}
function getUserInfo(user: User): User {
  return user
}
```

5. 定义`this`类型

```ts
interface Obj {
    user; number[]
    add: (this:Obj,num:number)=>void
}
let obj:Obj = {
    user: [1,2,3]
	// 在js中无法使用
    add(this:Obj,num:number) {
        this.user.push(num)
    }
}
obj.add(4)
```

6. 函数重载,在一个函数里面实现增删改查

```ts
let user:number[] = [1,2,3]
function findNum(add:number[]):number[]//如果传的是一个number类型数组就做添加
function findNum(id:number):number[]//如果传入了id就是单个查询
function findNum():number[]//如果没有传入就是查询全部
function findNum(ids?:number | number[]):number[] {
    if(typeof ids == 'number') {
        return user.filter(v=>v == ids)
    }
    else if(Array.isArray(ids)){
        user.push(...ids)
        return user
    }else {
        return user
    }
}
```

### 2.6 联合类型|交叉类型

1. 联合类型

```ts
let phone:number | string = 133666666  // 或者 '010-555555'

// 将接口传入的number或boolean类型转为boolean类型
let fn = function(type:number | boolean):boolean {
    return !!type
}
let result = fn(0)	// false
console.log(result)
```

```ts
interface Person {
  name: string
  age: number
}

interface Man{
  sex:string
}

const person = (man:Person & Man) => {
  console.log(man);
}

person({
  name: 'zhangsan',
  age: 18,
  sex: 'man'
})
```

### 2.7 内置对象

1.  ECMAScript内置对象

```ts
// ECMAScript内置对象
let num:Number = new Number(1)
let date:Date = new Date()
let reg:RegExp = new RegExp(/\w/)
let error:Error = new Error('error')
let xhr:XMLHttpRequest = new XMLHttpRequest()
```

2. DOM和BOM对象

```ts
// DOM和BOM对象
let body: HTMLElement = document.body;
let allDiv: NodeList = document.querySelectorAll('div');
//读取div 这种需要类型断言 或者加个判断应为读不到返回null
let div:HTMLElement = document.querySelector('div') as HTMLDivElement
document.addEventListener('click', function (e: MouseEvent) {
})
```

3. 定义Promise

```ts
function promise():Promise<number>{
   return new Promise<number>((resolve,reject)=>{
       resolve(1)
   })
}
 
promise().then(res=>{
    console.log(res)
})
```

### 2.8 案例--代码雨

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/93ab4796c2b1a4f688033e9d75ce1f2a.png)

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    * {
      padding: 0;
      margin: 0;
    }
  </style>
</head>

<body>
  <canvas id="canvas"></canvas>
  <script src="./index.js"></script>
</body>

</html>
```

```ts
let canvas = document.querySelector('#canvas') as HTMLCanvasElement
let ctx = canvas.getContext('2d') as CanvasRenderingContext2D
canvas.height = screen.availHeight; //可视区域的高度
canvas.width = screen.availWidth; //可视区域的宽度
let str: string[] = 'XMZS%*&&979-089)()XMZ348*%%435SBXMZ*^56872&(*678ZSWSSB'.split('')
let Arr = Array(Math.ceil(canvas.width / 10)).fill(0) //获取宽度例如1920 / 10 192
// console.log(Arr);

const rain = () => {
    ctx.fillStyle = 'rgba(0,0,0,0.05)'//填充背景颜色
    ctx.fillRect(0, 0, canvas.width, canvas.height) // 覆盖屏幕矩形，用于清除屏幕
    ctx.fillStyle = "#0f0"; //文字颜色
    Arr.forEach((item, index) => {
        ctx.fillText(str[ Math.floor(Math.random() * str.length) ], index * 10, item + 10)
        Arr[index] = item >= canvas.height || item > 10000 *  Math.random() ? 0 : item + 10; //添加随机数让字符随机出现不至于那么平整
    })
    // console.log(Arr);
    
}
setInterval(rain, 40)
```



### 2.9 接口和类型别名

#### 2.9.1 interface

`interface`可以用来约束对象，定义的对象属性必须与接口一致

```ts
interface Axxs{
    name:string
    age:number
}
let a:Axxs = {
    name: 'zhangsan',
    age: 18
}
```

1. 接口重名时会进行合并

```ts
interface Axxs{
    name:string
    age:number
}
interface Axxs{
    Ikun:string
}

let a:Axxs = {
    name: 'zhangsan',
    age: 18,
    Ikun:ikun
}
```

2. 任意属性[propName:string]

```ts
//在这个例子当中我们看到接口中并没有定义C但是并没有报错
//应为我们定义了[propName: string]: any;
//允许添加新的任意属性
interface Person {
    b?:string,
    a:string,
    [propName: string]: any;
}
 
const person:Person  = {
    a:"213",
    c:"123"
}
```

注意

- 一旦定义了任意属性，那么确定属性和可选属性的类型都必须是它的类型的子集

3. 可选参数

```ts
interface Person {
    name?: string
    age?: number
}
```

4.  只读属性

```ts
//
interface Axxsxs{
    name: string
    age: number
    readonly id: number
    readonly cd: ()=>{}boolean
} 

let a:Axxsxs = {
    id: 1,
    name: 'zhangsan',
    age: 18,
    cd: ()=> {return false}
}

a.cd = () => {return ture} //错误，函数是只读的
```

5. 接口继承

```ts
interface Axxsxs extend Bxx{
    name: string
    age: number
    readonly id: number
    readonly cd: ()=>{}boolean
} 
interface Bxx{
    xxx: string
}
```



#### 2.9.2 type

类型别名（自定义类型):

- 为任意类型起别名。

使用场景:

- 当同一类型（复杂）被多次使用时，可以通过类型别名，简化该类型的使用。

```ts
type CustomArray = (number | string)[]
let arr1: CustonArray = [1,'a',3,'b']
```



#### 2.9.3 区别

interface（接口）和type（类型别名）的对比:

- 相同点:
  - 都可以给对象指定类型。
- 不同点:
  - 接口，只能为对象指定类型。
  - 类型别名，不仅可以为对象指定类型，实际上可以为任意类型指定别名。



### 2.10 类型推论

在TS中，某些没有明确指出类型的地方，TS的类型推论机制会帮助提供类型。换句话说:由于类型推论的存在，这些地方，类型注解可以省略不写!

发生类型推论的2种常见场景:

1. 声明变量并初始化时
2. 决定函数返回值时。



### 2.11 类型断言

有时候你会比TS更加明确一个值的类型，此时，可以使用类型断言来指定更具体的类型。

```js
const aLink: HTMLAnchorElement
const aLink = document.getElementById('link') as HTMLAnchorElement
```

解释： 

1. 使用 as 关键字实现类型断言。 
2. 关键字 as 后面的类型是一个更加具体的类型（HTMLAnchorElement 是 HTMLElement 的子类型）。 
3. 通过类型断言，aLink 的类型变得更加具体，这样就可以访问 a 标签特有的属性或方法了

### 2.12 字面量类型

```ts
let str1 = 'Hello TS'
const str2 = 'Hello TS'
```

1. 变量 str1 的类型为：string。 str1 是一个变量（let），它的值可以是任意字符串，所以类型为：string。
2. 变量 str2 的类型为：'Hello TS'。str2 是一个常量（const），它的值不能变化只能是 'Hello TS'，所以，它的类型为：'Hello TS'。

此处的 'Hello TS'，就是一个**字面量类型**。也就是说**某个特定的字符串也可以作为 TS 中的类型**。 除字符串外，任意的 JS 字面量（比如，对象、数字等）都可以作为类型使用

使用模式:

- 字面量类型配合联合类型一起使用。

使用场景:

- 用来表示一组明确的可选值列表。

比如，在贪吃蛇游戏中，游戏的方向的可选值只能是上、下、左、右中的任意一个。

```ts
function changeDirection(direction: 'up' | 'down' | 'left' | 'right') {
    console.log(direction)
}
```



### 2.13 枚举

枚举的功能类似于字面量类型+联合类型组合的功能，也可以表示一组明确的可选值。

 枚举：

- 定义一组命名常量。它描述一个值，该值可以是这些命名常量中的一个。

```ts
enum Direction { Up,Down,Left,Right }

function changeDirection(direction: Direction) {
	console.log(direction)
}
```

1. 使用 enum 关键字定义枚举。
2. 约定枚举名称、枚举中的值以大写字母开头。
3. 枚举中的多个值之间通过 ,（逗号）分隔。
4. 定义好枚举后，直接使用枚举名称作为类型注解

访问枚举成员

```ts
enum Direction { Up,Down,Left,Right}

function changeDirection(direction: Direction) {
    console.log(direction)
}
changeDirection(Direction.Up)
```

枚举的值

- 枚举成员是有值的，默认为：从 0 开始自增的数值。 
- 我们把枚举成员的值为数字的枚举，称为：数字枚举

字符串枚举：

- 枚举成员的值是字符串

```ts
enum Direction {
    Up = 'UP',
	Down = 'DOWN',
    Left = 'LEFT',
    Right = 'RIGHT'
}
```

枚举的特点

- 枚举是 TS 为数不多的非 JavaScript 类型级扩展（不仅仅是类型）的特性之一。 
- 因为：其他类型仅仅被当做类型，而枚举不仅用作类型，还提供值（枚举成员都是有值的）。 也就是说，其他的类型会在编译为 JS 代码时自动移除。但是，枚举类型会被编译为 JS 代码

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/59942dba7d104d1c9ffce2868adf0a84.png)

说明︰

- 枚举与前面讲到的**字面量类型+联合类型组合**的功能类似，都用来表示一组明确的可选值列表。

一般情况下，**推荐使用字面量类型+联合类型组合的方式**，因为相比枚举，这种方式更加直观、简洁、高效。



### 2.14 any类型

值的类型为 any 时，可以对该值进行任意操作，并且不会有代码提示。

```ts
let obj: any = {x: 0}

obj.bar = 100
obj()
const n: number = obj
```

尽可能的避免使用 any 类型，除非**临时使用 any** 来“避免”书写很长、很复杂的类型



### 2.15 typeof

TS 也提供了 typeof 操作符：可以在类型上下文中引用变量或属性的类型（类型查询）。 

使用场景：

- 根据已有变量的值，获取该值的类型，来简化类型书写

```ts
let p = {x: 1, y: 2}

function formatPoint(point: {x: number; y: number}) {}
formatPoint(p)
```

```ts
function formatPoint(point: typeof p) {}
```

1. 使用 typeof 操作符来获取变量 p 的类型，结果与第一种（对象字面量形式的类型）相同。 
2. typeof 出现在类型注解的位置（参数名称的冒号后面）所处的环境就在类型上下文（区别于 JS 代码）。 
3. 注意：typeof 只能用来查询变量或属性的类型，无法查询其他形式的类型（比如，函数调用的类型）



## 3. 高级类型

### 3.1 class 类

TypeScript 全面支持 ES2015 中引入的 class 关键字，并为其添加了类型注解和其他语法（比如，可见性修饰符等）

实例属性初始化：

```ts
class Person {
    age: number
    gender = '男'
}
```

1. 声明成员 age，类型为 number（没有初始值）。 
2. 声明成员 gender，并设置初始值，此时，可省略类型注解（TS 类型推论 为 string 类型）

构造函数

```ts
class Person {
    age: number
    gender: string
    
    constructor(age: number, gender: string) {
        this.age = age
        this.gender = gender
    }
}
```

1. 成员初始化（比如，age: number）后，才可以通过 this.age 来访问实例成员。 
2. 需要为构造函数指定类型注解，否则会被隐式推断为 any；构造函数不需要返回值类型

类继承的两种方式：

1. extends（继承父类） 
2. implements（实现接口）。

 说明：JS 中只有 extends，而 implements 是 TS 提供的

**extends**

```ts
class Animal {
	move() { console.log( ' Moving along ! ') }
}
class Dog extends Animal {
    bark( { console.log('汪! ')} )
}

const dog = new Dog()
```

1. 通过 extends 关键字实现继承。 
2. 子类 Dog 继承父类 Animal，则 Dog 的实例对象 dog 就同时具有了父类 Animal 和 子类 Dog 的所有属性和方法

**implements** 

```ts
interface Singable {
    sing(): void
}
class Person implements Singable {
    sing() {
		console.log( '你是我的小呀小苹果儿')
    }
}
```

1. 通过 implements 关键字让 class 实现接口。 
2. Person 类实现接口 Singable 意味着，Person 类中必须提供 Singable 接口中指定的所有方法和属性

**readonly（只读修饰符）**

- 表示只读，用来防止在构造函数之外对属性进行赋值

```ts
class Person {
    readonly age: number = 18
    constructor(age: number) {
        this.age = age
    }
}
```

1. 使用 readonly 关键字修饰该属性是只读的，注意只能修饰属性不能修饰方法。 
2. 注意：属性 age 后面的类型注解（比如，此处的 number）如果不加，则 age 的类型为 18 （字面量类型）。 
3. 接口或者 {} 表示的对象类型，也可以使用 readonly



### 3.2 类型兼容性

两种类型系统：

1. Structural Type System（结构化类型系统） 
2. Nominal Type System（标明类型系统）。

 TS 采用的是结构化类型系统，也叫做 duck typing（鸭子类型），类型检查关注的是值所具有的形状。 也就是说，在结构类型系统中，如果两个对象具有相同的形状，则认为它们属于同一类型。

```ts
class Point { x: number; y: number }
class Point2D { x: number; y: number }
const p: Point = new Point2D()
```

1. Point 和 Point2D 是两个名称不同的类。 
2. 变量 p 的类型被显示标注为 Point 类型，但是，它的值却是 Point2D 的实例，并且没有类型错误。 
3. 因为 TS 是结构化类型系统，只检查 Point 和 Point2D 的结构是否相同（相同，都具有 x 和 y 两个属性，属性类型也相同）。 
4. 但是，如果在 Nominal Type System 中（比如，C#、Java 等），它们是不同的类，类型无法兼容

除了 class 之外，TS 中的其他类型也存在相互兼容的情况，包括：

1. 接口兼容性 
2. 函数兼容性 等



### 3.3 泛型

**泛型**

- 泛型是可以在保证类型安全前提下，让函数等与多种类型一起工作，从而实现复用，常用于：函数、接口、class 中

**创建泛型函数**

```ts
function id<Type>(valueL Type): Type (return value)
```

1. 语法：在函数名称的后面添加 <>（尖括号），尖括号中添加类型变量，比如此处的 Type。 
2. 类型变量 Type，是一种特殊类型的变量，它处理类型而不是值。 
3.  该类型变量相当于一个类型容器，能够捕获用户提供的类型（具体是什么类型由用户调用该函数时指定）。 
4. 因为 Type 是类型，因此可以将其作为函数参数和返回值的类型，表示参数和返回值具有相同的类型。 
5. 类型变量 Type，可以是任意合法的变量名称

**调用泛型函数**

```ts
const num = id<number>(10)
const str = id<string>('a')
```

**简化调用泛型函数**

```ts
let num = id(10)
```

**泛型约束：**

- 默认情况下，泛型函数的类型变量 Type 可以代表多个类型，这导致无法访问任何属性

比如，id('a') 调用函数时获取参数的长度

```ts
function id<Type>(value: Type): Type {
    console.log(value.length)
    return value
}
```

Type 可以代表任意类型，无法保证一定存在 length 属性，比如 number 类型就没有 length。 此时，就需要为泛型添加约束来**收缩类型**（缩窄类型取值范围）

**添加泛型约束收缩类型，主要有以下两种方式：**

1. 指定更加具体的类型 
2. 添加约束

**指定更加具体的类型** 

```ts
function id<Type> (value: Type[]): Type[] {
    console.log(value.length)
    return value
}
```

- 比如，将类型修改为 Type[]（Type 类型的数组），因为只要是数组就一定存在 length 属性，因此就可以访问了

 **添加约束**

```ts
interface ILength { length: number }
function id<Type extends ILength>(value: Type): Type {
    console.log(value.length)
    return value
}
```

1. 创建描述约束的接口 ILength，该接口要求提供 length 属性。 
2. 通过 extends 关键字使用该接口，为泛型（类型变量）添加约束。 
3. 该约束表示：传入的类型必须具有 length 属性

**泛型的类型变量可以有多个，并且类型变量之间还可以约束**

（比如，第二个类型变量受第一个类型变量约束）。

 比如，创建一个函数来获取对象中属性的值

```ts
function getProp<Type, Key extends keyof Type>(obj: Type， key: Key){
	return obj[key]
}
let person = { name: 'jack' , age: 18 }
getProp(person, 'name')
```

1. 添加了第二个类型变量 Key，两个类型变量之间使用（,）逗号分隔。
2. keyof 关键字接收一个对象类型，生成其键名称（可能是字符串或数字）的联合类型。 
3. 本示例中 keyof Type 实际上获取的是 person 对象所有键的联合类型，也就是：'name' | 'age'。
4. 类型变量 Key 受 Type 约束，可以理解为：Key 只能是 Type 所有键中的任意一个，或者说只能访问对象中存在的属性。

**泛型接口**：

- 接口也可以配合泛型来使用，以增加其灵活性，增强其复用性

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/079213c0b4487b16fa27f8454c7b0257.png)

1. 在接口名称的后面添加 <类型变量>，那么，这个接口就变成了泛型接口。
2. 接口的类型变量，对接口中所有其他成员可见，也就是接口中所有成员都可以使用类型变量。
3. 使用泛型接口时，需要显式指定具体的类型（比如，此处的 `IdFunc<number>`）。
4. 此时，id 方法的参数和返回值类型都是 number；ids 方法的返回值类型是 number[]

### 3.4 泛型工具类型

- TS 内置了一些常用的工具类型，来简化 TS 中的一些常见操作。 说明：它们都是基于泛型实现的（泛型适用于多种类型，更加通用），并且是内置的，可以直接在代码中使用。

1. `Partial<Type>`
2. `Readonly<Type>`
3. `Pick<Type, Keys>`
4. `Record<Keys, Type>`

`Partial<Type>` 用来构造（创建）一个类型，将 Type 的所有属性设置为可选

```ts
interface Props {
    id: string
    children: number[]
}
type PartialProps = Partial<Props>
```

构造出来的新类型 PartialProps 结构和 Props 相同，但所有属性都变为可选的

`Readonly<Type>`用来构造一个类型，将 Type 的所有属性都设置为 readonly（只读）。

```ts
interface Props {
    id: string
    children: number[]
}
type ReadonlyProps = Readonly<Props>
```

`Pick<Type, Keys>`从 Type 中选择一组属性来构造新类型。

```ts
interface Props {
    id: string
    title: string
    children: number[]
}
type PickProps = Pick<Props, 'id' | 'title'>
```

`Record<Keys, Type` 构造一个对象类型，属性键为 Keys，属性类型为 Type

```ts
type RecordObj = Record<'a' | 'b' | 'c', string[]>
let obj: RecordObj = {
    a: ['1'],
    b: ['2'],
    c: ['3']
}
```



### 3.5 索引签名类型

使用场景：

- 当无法确定对象中有哪些属性（或者说对象中可以出现任意多个属性），此时，就用到索引签名类型了

```ts
interface AnyObject {
    [Key: string]: number
}

let obj: AnyObject = {
    a: 1,
    b: 2
}
```

1. 使用 [key: string] 来约束该接口中允许出现的属性名称。表示只要是 string 类型的属性名称，都可以出现在对象中。
2. 这样，对象 obj 中就可以出现任意多个属性（比如，a、b 等）。 
3. key 只是一个占位符，可以换成任意合法的变量名称。
4. 隐藏的前置知识：JS 中对象（{}）的键是 string 类型的

在 JS 中数组是一类特殊的对象，特殊**在数组的键（索引）是数值类型**。 并且，数组也可以出现任意多个元素。所以，在数组对应的泛型接口中，也用到了索引签名类型

```ts
interface MyArray<T> {
    [n: number]: T
}
let arr: MyArray<number> = [1,3,5]
```

1. MyArray 接口模拟原生的数组接口，并使用 [n: number] 来作为索引签名类型。
2. 该索引签名类型表示：只要是 number 类型的键（索引）都可以出现在数组中，或者说数组中可以有任意多个元素。
3. 同时也符合数组索引是 number 类型这一前提



### 3.6 映射类型

映射类型：

- 基于旧类型创建新类型（对象类型），减少重复、提升开发效率。 

比如，类型 PropKeys 有 x/y/z，另一个类型 Type1 中也有 x/y/z，并且 Type1 中 x/y/z 的类型相同

这个

```ts
type Type = { x: number; y: number; z: number }
```

可以写成

```ts
type PropsKeys = 'x' | 'y' | 'z'
type Type = {[key in PropKeys]: number}
```

1. 映射类型是基于索引签名类型的，所以，该语法类似于索引签名类型，也使用了 []。
2. Key in PropKeys 表示 Key 可以是 PropKeys 联合类型中的任意一个，类似于 forin(let k in obj)。
3. 使用映射类型创建的新对象类型 Type2 和类型 Type1 结构完全相同。
4. 注意：映射类型只能在类型别名中使用，不能在接口中使用。



## 4. 类型声明文件

### 4.1 文件类型

TS 中有两种文件类型：

1. ts 文件
2. d.ts 文件。

 .ts 文件： 

1. 既包含类型信息又可执行代码。
2. 可以被编译为 .js 文件，然后，执行代码。
3. 用途：编写程序代码的地方。 

.d.ts 文件：

1. 只包含类型信息的类型声明文件。
2. 不会生成 .js 文件，仅用于提供类型信息。
3. 用途：为 JS 提供类型信息

总结：.ts 是 implementation（代码实现文件）；**.d.ts 是 declaration（类型声明文件）。**



### 4.2 类型声明文件的使用

使用已有的类型声明文件

1. 内置类型声明文件
2. 第三方库的类型声明文件。
   1. 库自带类型声明文件
   2. 由 DefinitelyTyped 提供。DefinitelyTyped 是一个 github 仓库，用来提供高质量 TypeScript 类型声明。



### 4.3 TS配置tsconfig.json

tsconfig.json 指定

- 项目文件和项目编译所需的配置项。

选项

1. tsconfig.json 文件所在目录为项目根目录（与 package.json 同级）。
2. tsconfig.json 可以自动生成，命令：tsc --init

除了在 tsconfig.json 文件中使用编译配置外，还可以通过命令行来使用。 使用演示：tsc hello.ts --target es6。

注意： 

1. tsc 后带有输入文件时（比如，tsc hello.ts），将忽略 tsconfig.json 文件。
2. tsc 后不带输入文件时（比如，tsc），才会启用 tsconfig.json。
