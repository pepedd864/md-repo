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



### 2.3 对象类型和接口

#### 2.3.1 Object和object

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

#### 2.3.2 interface

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

### 2.6 联合类型|类型断言|交叉类型

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

2. 类型断言

```ts
let fn = (num:number | string) => {
  console.log((num as string).length);
  // console.log((<string>num).length)
}

fn('123456')	// 6
fn(123456)	//undefined
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

### 2.9 Class类

