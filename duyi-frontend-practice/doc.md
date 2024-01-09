## 元素平滑上移

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/8d1d24e964f0f73c5e7306a1c276431f.gif)

**App.vue**

```vue
<template>
  <div class="container">
    <div v-slide-in="{distance: 200}" class="item">1</div>
    <div v-slide-in class="item">2</div>
    <div v-slide-in class="item">3</div>
    <div v-slide-in class="item">4</div>
    <div v-slide-in class="item">5</div>
    <div v-slide-in="{distance: 200, duration: 1000}" class="item">6</div>
    <div v-slide-in class="item">7</div>
    <div v-slide-in class="item">8</div>
    <div v-slide-in class="item">9</div>
    <div v-slide-in class="item">10</div>
  </div>
</template>

<script setup>

</script>


<style lang="scss" scoped>
.container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
}
.item {
  width: 900px;
  height: 430px;
  margin: 10px;
  border-radius: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
  color: #fff;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
  font-size: 50px;
  font-weight: bold;
  background-color: rgb(255, 39, 39);
  &:nth-child(2) {
    background-color: #ff7f00;
  }
  &:nth-child(3) {
    background-color: #ffff00;
  }
  &:nth-child(4) {
    background-color: #00ff00;
  }
  &:nth-child(5) {
    background-color: #00ffff;
  }
  &:nth-child(6) {
    background-color: #0000ff;
  }
  &:nth-child(7) {
    background-color: #8b00ff;
  }
  &:nth-child(8) {
    background-color: #ff0000;
  }
  &:nth-child(9) {
    background-color: #ff7f00;
  }
  &:nth-child(10) {
    background-color: #ffff00;
  }
}
</style>
```

**directives/vSlideIn.js**

```js
const DURATION = 500
const DISTANCE = 100
const animationMap = new WeakMap()
const ob = new IntersectionObserver(entries => {
  for (const entry of entries) {
    if (entry.isIntersecting) {
      const animation = animationMap.get(entry.target)
      animation.play()
      ob.unobserve(entry.target)
    }
  }
})
const isBelowViewport = (el) => {
  const rect = el.getBoundingClientRect()
  return rect.top > window.innerHeight
}
export default {
  mounted(el, binding) {
    if (!isBelowViewport(el)) {
      return
    }
    const animation = el.animate([
      {
        transform: `translateY(${(binding && binding.value && binding.value.distance) || DISTANCE}px)`,
        opacity: 0.5
      },
      {
        transform: 'translateY(0)',
        opacity: 1
      }
    ], {
      duration: (binding && binding.value && binding.value.duration) || DURATION,
      exsing: 'ease-in-out',
    })
    animation.pause()
    animationMap.set(el, animation)
    ob.observe(el)
  },
  unmounted(el) {
    ob.unobserve(el)
  }
}
```



## JS函数重载

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/5c966d13e213b4820058f0e5c60b1ec4.png)

**main.js**

```js
import { getUsers } from './impl.js'

getUsers()
getUsers(1)
getUsers(1, 10)
getUsers('张三')
getUsers('张三', '男')
```



**impl.js**

```js
// impl.js
import createOverload from "./overload.js"

const getUsers = createOverload()

getUsers.addImpl(() => {
  console.log('查询所有用户')
})

const searchPage = (page, size = 10) => {
  console.log('按照页码和数量查询用户')
}

getUsers.addImpl('number', searchPage)
getUsers.addImpl('number', 'number', searchPage)

getUsers.addImpl('string', (name) => {
  console.log('按照姓名查询用户')
})

getUsers.addImpl('string', 'string', (name, sex) => {
  console.log('按照姓名和性别查询用户')
})

export { getUsers }
```



**overload.js（核心）**

```js
function createOverload() {
  const callMap = new Map()
  function overload(...args) {
    const key = args.map(arg => typeof arg).join(',')
    const fn = callMap.get(key)
    if (fn) {
      return fn.apply(this, args)
    }
    throw new Error('没有找到匹配的函数')
  }
  overload.addImpl = function (...args) {
    const fn = args.pop()
    if (!fn || typeof fn !== 'function') {
      return
    }
    const types = args
    callMap.set(types.join(','), fn)
  }
  return overload
}

export default createOverload
```



## 二进制权限管理

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/c809b3146d2bb84ea0e81fda50c05e3e.png)

```js
/**常见写法 */

/*
const READ = 1
const CREATE = 2
const UPDATE = 3
const DELETE = 4
const READ_AND_UPDATE = 5
*/

/**位运算写法 */

const READ = 1 // 0001
const CREATE = 2 // 0010
const UPDATE = 4 // 0100
const DELETE = 8 // 1000
const READ_AND_UPDATE = READ | UPDATE // 0101
// 判断是否有权限
const xxx = 14
console.log('xxx: ', xxx)
if (xxx & READ) {
  console.log('有读权限')
} else {
  console.log('无读权限')
}
// 去除权限
const yyy = xxx & ~READ
if (yyy & READ) {
  console.log('有读权限')
} else {
  console.log('无读权限')
}
// 切换权限
const zzz = xxx ^ READ
if (zzz & READ) {
  console.log('有读权限')
} else {
  console.log('无读权限')
}
// 添加权限
const aaa = xxx | READ
if (aaa & READ) {
  console.log('有读权限')
} else {
  console.log('无读权限')
}
```



## 给Fetch设置超时时间

```js
// 给fetch 添加超时功能

/** 1. 传入参数设置超时 */
function requst(url, options) {
  const timeout = options.timeout || 5000
}
/** 2. 修改默认的fetch */
const oldFetch = window.fetch
window.fetch = function () {
}
/** 3. 创建一个高阶函数 */
function createFetchWithTimeout(timeout = 1000) {
  return function (url, options) {
    return new Promise((resolve, reject) => {
      const singalController = new AbortController() // 创建一个终止信号
      fetch(url, {
        ...options,
        signal: singalController.signal
      }).then(resolve, reject)
      setTimeout(() => {
        reject(new Error('fetch timeout'))
        // 超时后终止请求
        singalController.abort()
      }, timeout)
    })
  }
}

```


## 判断属性在对象中是否存在

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/32ae445504382b416718faf5703302e2.png)

```js
function OBJ() {}
OBJ.prototype.a = 1

const obj = new OBJ()

// 只能判断有a属性时，a属性的值是否为undefined，不能判断a属性是否存在
console.log('------------------------------------')
console.log('方式1：对比undefined')
if(obj.a !== undefined) {
  console.log('obj.a存在')
} else {
  console.log('obj.a不存在')
}

// Object.keys(obj)返回一个数组，包含对象自身的所有可枚举属性的名称, 不可枚举的属性不会被返回
console.log('------------------------------------')
console.log('方式2：使用Object.keys')
if(Object.keys(obj).includes('a')) {
  console.log('obj.a存在')
} else {
  console.log('obj.a不存在')
}

// hasOwnProperty()判断对象自身属性中是否具有指定的属性
console.log('------------------------------------')
console.log('方式3：使用hasOwnProperty')
if(obj.hasOwnProperty('a')) {
  console.log('obj.a存在')
} else {
  console.log('obj.a不存在')
}

// in运算符判断对象自身或继承的属性中是否具有指定的属性
console.log('------------------------------------')
console.log('方式4：使用in')
if('a' in obj) {
  console.log('obj.a存在')
} else {
  console.log('obj.a不存在')
}
```



## sass媒体查询实现响应式（自适应）布局

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/7c32aa9d793e5a8ce4128b8316724899.gif)

**vite项目配置**

安装sass

```bash
npm  install sass sass-loader -D
```

vite-config.js

```js
import { fileURLToPath, URL } from 'node:url'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    port: 3000
  },
  // 配置'@'
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  // 配置全局sass样式
  css: {
    preprocessorOptions: {
      scss: {
        additionalData: '@import "@/assets/sass/response.scss";'
      }
    }
  },
})

```



**response.scss**

```scss
// 断点列表
$breakpoints: (
  'xs': (0, 319px),
  'sm': (320px, 479px),
  'md': (480px, 767px),
  'lg': (768px, 991px),
  'xl': (992px, 1199px),
  'xxl': 1200px
) !default;

// 媒体查询
@mixin respond-to($breakname) {
  $bp: map-get($breakpoints, $breakname);
  @if type-of($bp) == 'list' {
    $min: nth($bp, 1);
    $max: nth($bp, 2);
    @media (min-width: $min) and (max-width: $max) {
      @content;
    }
  } @else {
    @media (min-width: $bp) {
      @content;
    }
  }
}
```



**app.vue**使用

```vue
<script setup>
</script>

<template>
  <div class="header">
    <h1>Header</h1>
  </div>
</template>

<style lang="scss" scoped>
.header {
  background-color: red;
  height: 100px;
  width: 100%;
  @include respond-to('xs') {
    background-color: blue;
  }
  @include respond-to('sm') {
    background-color: green;
  }
  @include respond-to('md') {
    background-color: yellow;
  }
  @include respond-to('lg') {
    background-color: orange;
  }
  @include respond-to('xl') {
    background-color: purple;
  }
  @include respond-to('xxl') {
    background-color: pink;
  }
}
</style>
```



## css边缘融合

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/e7588cdf39be4fa8ab8f058fdf967891.gif)

通过`contrast`和`blur`来实现边缘融合效果

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CSS edge fusion</title>
  <style>
    * {
      padding: 0;
      margin: 0;
    }

    body {
      background: #000;
    }

    .container {
      position: relative;
      margin: 0 auto;
      width: 100%;
      top: 40vh;
      display: flex;
      background: #000;
      /*注意要添加背景，否则filter不生效 */
      justify-content: center;
      align-items: center;
      filter: contrast(50);
      overflow: hidden; /* 隐藏blur模糊超出部分 */
    }

    .box {
      width: 100px;
      height: 100px;
      background: #fff;
      border-radius: 50%;
      filter: blur(5px);
    }

    .box1 {
      animation: move1 2s linear infinite alternate;
    }

    .box2 {
      animation: move2 2s linear infinite alternate;
    }

    @keyframes move1 {
      0% {
        transform: translateX(-75px);
      }

      100% {
        transform: translateX(150px);
      }
    }

    @keyframes move2 {
      0% {
        transform: translateX(75px);
      }

      100% {
        transform: translateX(-150px);
      }
    }
  </style>
</head>

<body>
  <div class="container">
    <div class="box box1"></div>
    <div class="box box2"></div>
  </div>
</body>

</html>
```



## 渐变阴影

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/5612fa01005ca419d5a390fedf45b1a9.gif)



html

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>gradual_change_shadow</title>
  <link rel="stylesheet" href="index.css">
</head>
<body>
  <div class="box"></div>
</body>
</html>
```



css

```css
.box {
  position: relative;
  width: 250px;
  height: 400px;
  background: transparent;
  margin: 2em auto;
  /* 偏移量使用css变量表示 */
  --sx: 0px;
  --sy: 0px;
  /* 偏移 */
  transform: translate(var(--sx),var(--sy));
}

.box::after {
  content: '';
  position: absolute;
  left: var(--sx);
  top: var(--sy);
  width: 100%;
  height: 100%;
  z-index: -1;
  filter: blur(10px);
  background: conic-gradient(#ffd700,
      #f79d03,
      #ee6907,
      #e6390a,
      #de0d0d,
      #d61039,
      #cf1261,
      #c71585,
      #cf1261,
      #d61039,
      #de0d0d,
      #e6390a,
      #ee6907,
      #f79d03,
      #ffd700,
      #ffd700);
  clip-path: polygon( /* 背景裁切，不能使用元素遮盖的方式，要考虑到背景透明情况 */
    -100vmax -100vmax,
      100vmax -100vmax,
      100vmax 100vmax,
      -100vmax 100vmax,
      -100vmax -100vmax,
      calc(0px - var(--sx)) calc(0px - var(--sy)) ,
      calc(0px - var(--sx)) calc(100% - var(--sy)),
      calc(100% - var(--sy)) calc(100% - var(--sy)),
      calc(100% - var(--sy)) calc(0px - var(--sy)),
      calc(0px - var(--sy)) calc(0px - var(--sy))
      );
}
```



## vscode正则插件

正则测试插件

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/d50a1464b4a0fe890c3d920e1b884be5.png)



正则插件

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/a72508e7f0ddc36a85f8761617481479.png)



使用

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/7328f3393903ff89416115f07f1be635.gif)



## 过渡结束事件防抖

**正常情况下，会多次触发**

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/d499b10a02c9231c428fc203bfbf561e.gif)

**只触发一次**

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/84eff0740510bab16743f6b26378e228.gif)

```js
box.addEventListener('transitionend', () => {
  console.log('transitionend')
},{
  once: true // 只触发一次
}) 
```

**防抖**

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/c4db209f633ef82a67059042234f99fb.gif)

```js
function debounce(fn) { // 防抖
  let timer = null
  return function() {
    clearTimeout(timer)
    timer = setTimeout(() => {
      fn.apply(this, arguments)
    }, 20)
  }
}

box.addEventListener('transitionend', debounce(() => {
  console.log('transitionend')
}))
```

## vue自定义ref实现防抖

通常的防抖方案

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/7859ec76170fda38a730ff934f4de0e4.gif)

```vue
// vue
<template>
  <div>
    <input type="text" @input="debouncehandler">
    <p class="result">{{ text }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { debounce } from './debounce/debounce.js'
const text = ref('')
const inputHandler = (e) => {
  text.value = e.target.value
}
const debouncehandler = debounce(inputHandler, 1000)
</script>

<style scoped>
</style>
```

```js
// debounce
export function debounce(fn, time) {
  let timeout
  return function () {
    clearTimeout(timeout)
    timeout = setTimeout(() => {
      fn.apply(this, arguments)
    }, time)
  }
}
```



自定义ref实现防抖

![gif](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/6bb196b3e0fdd4509b0b1f96b998ca86.gif)

```vue
// vue
<template>
  <div>
    <input type="text" v-model="text">
    <p class="result">{{ text }}</p>
  </div>
</template>

<script setup>
import { debounceRef } from './debounce/debounceRef.js'
const text = debounceRef('')
</script>

<style scoped>
</style>
```

```js
// debounceRef
import { customRef } from 'vue'
export function debounceRef(value, duration = 1000) {
  let timeout
  return customRef((track, trigger) => {
    return {
      get() {
        // 收集依赖
        track()
        return value
      },
      set(val) {
        clearTimeout(timeout)
        timeout = setTimeout(() => {
          // 派送更新
          trigger()
          value = val
        }, duration)
      }
    }
  })
}
```



## CSS文字填充动画

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/f3dc459d621dee7f391d1b687b6cd561.gif)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    body {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: black;
}

h1 {
  color: white;
  font-family: Helvetica;
  font-size: 150px;
  letter-spacing: -4px;
  position: relative;
  color: transparent;
  background-image: linear-gradient(to right, white, white, transparent);
  background-size: 200% 100%;
  background-repeat: no-repeat;
  -webkit-background-clip: text;
  background-position-x: 200%;
  animation: 2s fillup ease-in-out 2s forwards;
}

h1::after {
  content: 'Incredible';
  position: absolute;
  top: 0;
  left: 0;
  -webkit-text-stroke: 2px;
  -webkit-text-stroke-color: white;
  -webkit-text-fill-color: transparent;
  opacity: 0;
  animation: 2s fadein ease-in-out forwards;
}

@keyframes fillup {
  from {
    background-position-x: 200%;
  }
  to {
    background-position-x: 0%;
  }
}

@keyframes fadein {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
  </style>
  <title></title>
</head>
<body>
  <h1>Incredible</h1> 
</body>
</html>
```



## gsap滚动插件

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/ada08f39aae1dc06571fdb57b6b4131c.gif)

npm 安装 gsap

```bash
npm install gsap
```

main.js

```js
import './style.css'
import gsap from 'gsap'
import { ScrollTrigger } from "gsap/ScrollTrigger" //导入scrolltrigger插件

gsap.registerPlugin(ScrollTrigger) // 注册插件
const box = document.querySelector('.box')
gsap.fromTo(
  box,
  { x: 0 },
  {
    x: function (_, target) {
      return document.documentElement.clientWidth - target.offsetWidth
    },
    rotation: function (_, target) {
      const r = target.offsetWidth / 2
      const long = 2 * Math.PI * r
      return (document.documentElement.clientWidth - target.offsetWidth) / long * 360 // 计算出旋转角度
    },
    duration: 3,
    ease: 'none',
    scrollTrigger: {
      trigger: box,
      scrub: true,
      start: 'center center',
      pin: true, // 定格元素在center center的位置
    }
  }
)
```

style.css

```css
* {
  padding: 0;
  margin: 0;
}

body {
  background: #000;
  height: 250vh;
}
.box {
  position: relative;
  background: #fff;
  top: 100vh;
  width: 100px;
  height: 100px;
}
```



## 鼠标移动高亮边框效果

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/46ef1d1075b97c8ebc1e32082ef441c2.gif)



**index.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mouse movement highlights border effect</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <div class="container">
    <div class="card">
      <div class="inner">1</div>
    </div>
    <div class="card">
      <div class="inner">2</div>
    </div>
    <div class="card">
      <div class="inner">3</div>
    </div>
    ...
    <div class="card">
      <div class="inner">60</div>
    </div>
  </div>
  <script src="./index.js"></script>
</body>
</html>
```



**style.css**

```css
* {
  padding: 0;
  margin: 0;
}

body {
  background: #000;
  color: #fff;
}

.container {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  gap: 1rem;
  padding: 1rem;

}

.card {
  aspect-ratio: 6/3;
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.1);
  position: relative;
  overflow: hidden;
}

.inner {
  position: absolute;
  background: #171717;
  inset: 2px;
  /* 2px的缝隙 */
  border-radius: inherit;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: -1;
}

.card::before {
  content: '';
  position: absolute;
  width: 100%;
  height: 100%;
  z-index: -2;
  left: var(--x, -1000px);
  /* 第一个参数为css变量，第二个参数为默认值 */
  top: var(--y, -1000px);
  background: radial-gradient(closest-side circle, rgba(255, 255, 255, 0.6) 0%, transparent);
  /* closest-side以最小边为半径 */
  border-radius: inherit;
  transform: translate(-50%, -50%);
}
```



**index.js**

```js
const container = document.querySelector('.container')
const cards = document.querySelectorAll('.card')

container.addEventListener('mousemove', (e) => {
  for (const card of cards) {
    const rect = card.getBoundingClientRect()
    const x = e.clientX - rect.left
    const y = e.clientY - rect.top
    card.style.setProperty('--x', `${ x }px`)
    card.style.setProperty('--y', `${ y }px`)
  }
})
```



## 网页访问文件夹（仿vscode文件浏览功能）

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/01e6e6cd3575a9d7ca3f25286c74e3f9.gif)

使用`showDirectoryPicker`函数访问电脑的文件夹

函数返回值为一个文件句柄，第一个属性为文件类型，第二个为名字

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/3f88fca905b31492967afc3300882bf0.png)

要生成文件树结构，可以使用一个单独的函数进行处理

```js
// 处理句柄
async function processHandle(handle) {
  if (handle.kind === 'file') {
    // 不是文件夹
    return handle
  }
  handle.children = []
  const iter = await handle.entries()
  // iter 异步迭代器
  for await (const info of iter) {
    const subHandle = await processHandle(info[1]) // 递归处理
    handle.children.push(subHandle)
  }
  return handle
}
```

生成树形结构

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/f52f6ebc6c2104e9a38df6a03b8d55db.png)

然后根据生成的树形结构句柄，渲染出目录来

```js
// 渲染目录 ul 默认为文件夹  li 默认为文件
function renderCatalogue(handle, dom, subNode) {
  // 清空目录
  dom.innerHTML = ''
  let ulWrapper = null
  if (subNode === null || subNode === undefined) {
    ulWrapper = document.createElement('div')
    ulWrapper.className = 'ul-wrapper'
    ulWrapper.innerText = handle.name
  } else {
    ulWrapper = subNode
  }
  const ulInner = document.createElement('div')
  ulInner.className = 'ul-inner'
  ulWrapper.appendChild(ulInner)
  ulWrapper.addEventListener('click', (event) => {
    event.stopPropagation(); // 阻止冒泡
    renderContent(handle, contents.querySelector('.content'));
    // 展开或者收起 让ul下的所有元素隐藏或者显示
    ulInner.style.display = ulInner.style.display === 'none' ? 'block' : 'none'
  })
  if (!('children' in handle)) {
    // 如果没有子文件
    dom.appendChild(ulWrapper)
  }
  handle.children.forEach(item => {
    // 如果是文件
    if (item.kind === 'file') {
      const listItem = document.createElement('div')
      listItem.className = 'list-item'
      listItem.innerText = item.name
      listItem.addEventListener('click', (event) => {
        event.stopPropagation() // 阻止冒泡, 防止点击 li 时触发 ul 的点击事件
        renderContent(item, contents.querySelector('.content'))
      })
      ulInner.appendChild(listItem)
    } else {
      // 如果是文件夹
      const subNode = document.createElement('div')
      subNode.className = 'ul-wrapper'
      subNode.innerText = item.name
      renderCatalogue(item, dom, subNode)
      ulInner.appendChild(subNode)
    }
  })
  dom.appendChild(ulWrapper)
}
```

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/7556e002a351c50a12e32cbb68630d8f.png" style="zoom:50%;" />

根据文件类型渲染出具体内容来

```js
// 渲染内容
async function renderContent(handle, dom) {
  if (handle.kind === 'file') {
    // 渲染文件内容
    const file = await handle.getFile()
    const content = await file.text()
    dom.innerText = content
  } else {
    // 显示文件夹名称
    dom.innerText = handle.name
  }
}
```

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/8515bb66f83959bc354ff3e19489cee1.png)

完整代码

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>网页访问文件夹</title>
  <style>
    * {
      margin: 0;
      padding: 0;
    }

    body {
      background-color: #f5f5f5;
      font-family: Arial, sans-serif;
    }

    button {
      font-size: 1rem;
      font-weight: bold;
      color: #fff;
      background-color: #007bff;
      padding: 5px 10px;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      transition: background-color 0.3s ease;
    }

    button:hover {
      background-color: #0069d9;
    }

    .contents {
      display: flex;
      justify-content: space-between;
      width: calc(100% - 20px);
      height: calc(100vh - 60px);
      margin: 10px auto;
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }

    .left {
      width: 30%;
      max-height: calc(100vh - 60px);
      background-color: #fff;
      border: 1px solid #ccc;
      overflow: auto;
    }

    .ul-wrapper {
      width: auto;
      padding: 5px 10px;
      background-color: #fff;
      border-left: 1px solid #ccc;
      cursor: pointer;
    }

    .list-item {
      width: auto;
      padding: 5px 10px;
      transition: background-color 0.3s ease;
      border-left: 1px solid #ccc;
      list-style: none;
      cursor: pointer;
    }

    .list-item:hover {
      background-color: #f5f5f5;
    }

    .right {
      width: 68%;
      padding: 10px;
      max-height: calc(100vh - 60px);
      background-color: #fff;
      border: 1px solid #ccc;
      overflow: auto;
    }

    .card-container {
      display: flex;
      flex-wrap: wrap;
    }

    .card {
      width: 100px;
      height: 100px;
      background-color: #ddd;
      margin: 10px;
      display: inline-block;
      transition: all 0.3s;
      overflow: hidden;
      cursor: pointer;
    }

    .card:hover {
      background-color: #ccc;
    }
  </style>
</head>

<body>
  <button>访问文件夹</button>
  <div class="contents">
    <div class="left catalogue">
    </div>
    <div class="right content"></div>
  </div>
  <script>
    const btn = document.querySelector('button')
    const contents = document.querySelector('.contents')
    btn.addEventListener('click', async () => {
      try {
        const handle = await showDirectoryPicker()
        // 处理句柄
        const root = await processHandle(handle)
        // 渲染目录
        renderCatalogue(root, contents.querySelector('.catalogue'))
      } catch (e) {
        // 用户拒绝查看文件夹内容
      }
    })

    // 处理句柄
    async function processHandle(handle) {
      if (handle.kind === 'file') {
        // 不是文件夹
        return handle
      }
      handle.children = []
      const iter = await handle.entries()
      // iter 异步迭代器
      for await (const info of iter) {
        const subHandle = await processHandle(info[1]) // 递归处理
        handle.children.push(subHandle)
      }
      return handle
    }

    // 渲染内容
    async function renderContent(handle, dom) {
      dom.innerHTML = ''
      if (handle.kind === 'file') {
        // 渲染文件内容
        const file = await handle.getFile()
        const content = await file.text()
        dom.innerText = content
      } else {
        // 渲染文件列表
        const ul = document.createElement('div')
        ul.className = 'card-container'
        handle.children.forEach(item => {
          const li = document.createElement('div')
          li.className = 'card'
          li.innerText = item.name
          li.addEventListener('click', (event) => {
            event.stopPropagation() // 阻止冒泡, 防止点击 li 时触发 ul 的点击事件
            renderContent(item, dom)
          })
          ul.appendChild(li)
        })
        dom.appendChild(ul)
      }
    }

    // 渲染目录 ul 默认为文件夹  li 默认为文件
    function renderCatalogue(handle, dom, subNode) {
      // 清空目录
      dom.innerHTML = ''
      let ulWrapper = null
      if (subNode === null || subNode === undefined) {
        ulWrapper = document.createElement('div')
        ulWrapper.className = 'ul-wrapper'
        ulWrapper.innerText = handle.name
      } else {
        ulWrapper = subNode
      }
      const ulInner = document.createElement('div')
      ulInner.className = 'ul-inner'
      ulWrapper.appendChild(ulInner)
      ulWrapper.addEventListener('click', (event) => {
        event.stopPropagation(); // 阻止冒泡
        renderContent(handle, contents.querySelector('.content'));
        // 展开或者收起 让ul下的所有元素隐藏或者显示
        ulInner.style.transition = 'all 0.3s'
        ulInner.display = ulInner.display === 'none' ? 'block' : 'none'
        // 展开收起动画
        if (ulInner.display === 'none') {
          ulInner.style.height = '0px'
          ulInner.style.opacity = '0'
          ulInner.style.visibility = 'hidden'
        } else {
          ulInner.style.height = 'auto'
          const { height } = ulInner.getBoundingClientRect()
          ulInner.style.height = '0px'
          ulInner.offsetHeight
          ulInner.style.height = height + 'px'
          ulInner.style.opacity = '1'
          ulInner.style.visibility = 'visible'
        }
      })
      if (!('children' in handle)) {
        // 如果没有子文件
        dom.appendChild(ulWrapper)
      }
      handle.children.forEach(item => {
        // 如果是文件
        if (item.kind === 'file') {
          const listItem = document.createElement('div')
          listItem.className = 'list-item'
          listItem.innerText = item.name
          listItem.addEventListener('click', (event) => {
            event.stopPropagation() // 阻止冒泡, 防止点击 li 时触发 ul 的点击事件
            renderContent(item, contents.querySelector('.content'))
          })
          ulInner.appendChild(listItem)
        } else {
          // 如果是文件夹
          const subNode = document.createElement('div')
          subNode.className = 'ul-wrapper'
          subNode.innerText = item.name
          renderCatalogue(item, dom, subNode)
          ulInner.appendChild(subNode)
        }
      })
      dom.appendChild(ulWrapper)
    }

  </script>
</body>

</html>
```

## 自动高度过渡

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/c7264395636339e9653f747916342acf.gif)

传统使用max-height或者transform-y的方式效果不好，可以使用flip方式实现

**代码演示**

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>自动高度过渡</title>
  <style>
    .view {
      position: relative;
      width: 130px;
    }

    .btn {
      width: 130px;
      height: 35px;
      background-color: #00bfff;
      text-align: center;
      line-height: 35px;
      color: #fff;
      font-size: 18px;
      border-radius: 7px;
    }

    .detail {
      position: absolute;
      top: 50px;
      left: 0;
      width: auto;
      height: 0px;
      text-align: left;
      background-color: #ddd;
      color: #000;
      overflow: hidden;
    }

    .content {
      padding: 10px;
    }
  </style>
</head>

<body>
  <div class="view">
    <div class="btn">hover me</div>
    <div class="detail">
      <div class="content">
        13131313131313141414
        asfas
        124124125125
        asfafasfgags
        asfasf133141
        asfasgsgteew
        13415141
        sdgsdgsdasda
      </div>
    </div>
  </div>
  <script>
    const detail = document.querySelector('.detail')
    const btn = document.querySelector('.btn')
    btn.addEventListener('mouseenter', () => {
      detail.style.height = 'auto'
      const { height } = detail.getBoundingClientRect()
      detail.style.height = '0px'
      detail.offsetHeight
      detail.style.transition = 'height 0.3s'
      detail.style.height = height + 'px'
    })
    btn.addEventListener('mouseleave', () => {
      detail.style.height = '0px'
    })
  </script>
</body>

</html>
```



## 自定义CSS属性

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/17c283f3385d5ecb4bf0e32000a02994.gif)

这里使用了CSS自定义属性，可以使用transition或者anination去执行动画属性

自定义CSS属性

```css
@property --p {
  syntax: '<percentage>';
  initial-value: 0%;
  inherits: false;
}
```

通过行盒元素的渐变实现动画

```css
.text {
  --p: 0%;
  background: linear-gradient(to right, #0000 var(--p), #000 calc(var(--p) + 100px));
  color: transparent;
  animation: erase 5s forwards;
}
```

加上动画@keyframes

```css
.text {
  --p: 0%;
  background: linear-gradient(to right, #0000 var(--p), #000 calc(var(--p) + 100px));
  color: transparent;
  animation: erase 5s forwards;
}

@property --p {
  syntax: '<percentage>';
  initial-value: 0%;
  inherits: false;
}

@keyframes erase {
  to {
    --p: 100%;
  }
}
```

完整代码

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>自定义CSS属性</title>
  <style>
    body {
      background: #000;
      color: #fff;
    }

    .container {
      width: 80%;
      margin: 1em auto;
      position: relative;
      font-family: 'Courier New', Courier, monospace;
      line-height: 2;
    }

    .eraser {
      position: absolute;
      margin: 0;
      left: 0;
      top: 0;
    }

    .text {
      --p: 0%;
      background: linear-gradient(to right, #0000 var(--p), #000 calc(var(--p) + 100px));
      color: transparent;
      animation: erase 5s forwards;
    }

    @property --p {
      syntax: '<percentage>';
      initial-value: 0%;
      inherits: false;
    }

    @keyframes erase {
      to {
        --p: 100%;
      }
    }
  </style>
</head>

<body>
  <div class="container">
    <p>
      NovelAI uses GPT-based large language models (LLMs)[8][9] to generate storywriting prose.[10] The service also
      offer
      encrypted servers and customizable editors.[10][11]

      For AI art generation, NovelAI uses a custom implementation of the source-available Stable Diffusion[2][12]
      text-to-image diffusion model that is specifically trained on a Danbooru-based[5][1][13][14] dataset to generate
      images
      from text prompts called NovelAI Diffusion.

      There is also the ability to generate a new image based on an existing image.[15] The NovelAI terms of service
      states
      that all generated content belong to the user, regardless if the user is an individual or a corporation.[5]
      Anlatan
      states that generated images are not stored locally on their servers.[1]
    </p>
    <p class="eraser">
      <span class="text">
        NovelAI uses GPT-based large language models (LLMs)[8][9] to generate storywriting prose.[10] The service also
        offer
        encrypted servers and customizable editors.[10][11]

        For AI art generation, NovelAI uses a custom implementation of the source-available Stable Diffusion[2][12]
        text-to-image diffusion model that is specifically trained on a Danbooru-based[5][1][13][14] dataset to generate
        images
        from text prompts called NovelAI Diffusion.

        There is also the ability to generate a new image based on an existing image.[15] The NovelAI terms of service
        states
        that all generated content belong to the user, regardless if the user is an individual or a corporation.[5]
        Anlatan
        states that generated images are not stored locally on their servers.[1]
      </span>
    </p>
  </div>
</body>

</html>
```



## 封装命令式组件

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/2acc1d13afa4cc028ecf677f7584f5d2.gif)

命令式组件，像elments ui中的message就是一个命令式组件

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/5f2d7cb0c99dadbb67109606350d3daa.gif)

```ts
import { ElMessage } from 'element-plus'

const open = () => {
  ElMessage('this is a message.')
}
```





自定义命令式组件

```jsx
import Button from '@/components/Button.vue';
import { createApp, defineComponent } from "vue";
import { styled } from '@styils/vue'
const DivModal = styled('div', {
  position: 'fixed',
  top: 0,
  left: 0,
  zIndex: 100,
  width: '100%',
  height: '100%',
  backgroundColor: 'rgba(0, 0, 0, .5)',
  display: 'flex',
  justifyContent: 'center',
  alignItems: 'center'
})

const DivBox = styled('div', {
  width: '300px',
  height: '200px',
  backgroundColor: '#fff',
  borderRadius: '10px',
  display: 'flex',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center'
})

const DivText = styled('div', {
  fontSize: '20px',
  color: '#333'
})

export const MessageBox = defineComponent({
  props: {
    msg: String,
  },
  render(ctx) {
    const { $props, $emit } = ctx
    return (
      <DivModal class="modal">
        <DivBox class="box">
          <DivText class="text">{$props.msg}</DivText>
          <Button click="{ $emit('onClick') }">确定</Button>
        </DivBox>
      </DivModal >
    )
  }
})

function showMsg(msg, clickHandler) {
  const div = document.createElement("div");
  document.body.appendChild(div);
  // 渲染一个MessageBox组件
  const app = createApp(MessageBox, {
    msg,
    onclick() {
      clickHandler && clickHandler(() => {
        app.unmount(div);
        div.remove();
      });
    }
  })
  app.mount(div);
}

export default showMsg;
```



使用

```vue
<script setup>
import showMsg from './utils/showMsg';
import Button from './components/Button.vue';
function showMsgBox() {
  showMsg('hello world', (close) => {
    close()
  })
}
</script>

<template>
  <div>
    <Button @click="showMsgBox">显示提示框</Button>
  </div>
</template>
```



## 大文件分片

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/1415636f4ef73644e6e61dbeb2fcdfc8.gif)

在做网盘类项目时，上传超过100MB的大文件时，如果不进行文件分片直接上传，在网络不稳定时容易造成数据丢失，导致上传失败，因此我们可以使用文件分片的方式，使得文件可以稳定上传。

首先是一个基础HTML结构

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>大文件分片</title>
</head>

<body>
  <input class="inputFile" type="file" />
  <script src="./main.js" type="module"></script>
</body>

</html>
```



在main.js中，获取input的change事件，获得文件时，执行文件分片函数

```js
import { cutFile } from './cutFile.js'

const inpFile = document.querySelector('.inputFile')

inpFile.addEventListener('change', async (e) => {
  const file = e.target.files[0]
  console.time('cutFile')
  const chunks = await cutFile(file)
  console.timeEnd('cutFile')
  console.log(chunks)
})
```



对应cutFile函数，有两种实现，一种是单线程实现，一种是多线程。单线程实现会影响主线程的速度，导致页面显示卡顿，可以使用多线程的方式来优化性能的同时改善页面卡顿

1. 单线程

```js
import { createChunk } from './createChunk.js'

const CHUNKE_SIZE = 1024 * 1024 * 5 // 5MB

export async function cutFile(file) {
  const count = Math.ceil(file.size / CHUNKE_SIZE)
  const result = []
  //  单线程分片
  for (let i = 0; i < count; i++) {
    const chunk = await createChunk(file, i, CHUNKE_SIZE)
    result.push(chunk)
  }
  return result
}
```

2. 多线程

```js
import { createChunk } from './createChunk.js'

const CHUNKE_SIZE = 1024 * 1024 * 5 // 5MB
const THREAD_COUNT = 4 // 线程数量

// 多线程分片
export function cutFile(file) {
  return new Promise((resolve) => {
    const count = Math.ceil(file.size / CHUNKE_SIZE)
    const result = []
    // 线程区间数量
    const workerCount = Math.ceil(count / THREAD_COUNT)
    // 完成的线程数量
    let finishCount = 0
    // 使用多线程进行分片
    for (let i = 0; i < THREAD_COUNT; i++) {
      // 创建一个 worker 线程
      const worker = new Worker('./worker.js', {
        type: 'module'
      })
      // 计算每个线程的计算区间
      const startIndex = i * workerCount
      const endIndex = startIndex + workerCount
      worker.postMessage({
        file,
        chunkSize: CHUNKE_SIZE,
        startIndex,
        endIndex
      })
      worker.onmessage = (e) => {
        for (let i = startIndex; i < endIndex; i++) {
          result[i] = e.data[i - startIndex]
        }
        worker.terminate()
        finishCount++
        if (finishCount == THREAD_COUNT) {
          resolve(result)
        }
      }
    }
  })
}
```



简单写一个创建分片的函数

```js
import './sparkmd5.js'
export function createChunk(file, index, chunkeSize) {
  return new Promise((resolve) => {
    const start = index * chunkeSize
    const end = start + chunkeSize
    const spark = new SparkMD5.ArrayBuffer()
    const fileReader = new FileReader()
    fileReader.onload = (e) => {
      spark.append(e.target.result)
      resolve({
        start,
        end,
        index,
        hash: spark.end()
      })
    }
    fileReader.readAsArrayBuffer(file.slice(start, end))
  })
}
```



结合之前的单线程代码，整体代码已经可以运行了，但是存在效率问题，因此，我们使用多线程进行优化

首先我们定义多线程的线程数量，这里的线程数量取决于电脑实际的线程数量，线程多的可以使用更多的线程提高速度，但是如果本身线程数量不多的话，盲目增加线程数量可能降低效率（参考多线程原理）

```js
const THREAD_COUNT = 4 // 线程数量
```

随后我们根据定义的线程数量创建对应数量的线程

```js
for (let i = 0; i < THREAD_COUNT; i++) {
  // 创建一个 worker 线程
  const worker = new Worker('./worker.js', {
    type: 'module'
  })
}
```

我们通过`postMessage`和`onmessage`和线程进行通信

```js
// 向线程传递我们需要分片的文件信息
worker.postMessage({
  file,
  chunkSize: CHUNKE_SIZE,
})

// 接收线程传递回来的信息
worker.onmessage = (e) => {

}
```

对于多线程，我们需要在给线程分配任务之前计算每个线程需要分片的区间

```js
// 线程区间数量
const workerCount = Math.ceil(count / THREAD_COUNT)
for (let i = 0; i < THREAD_COUNT; i++) {
	// 计算每个线程的计算区间
    const startIndex = i * workerCount
    const endIndex = startIndex + workerCount
}
```

然后传递给线程

```js
worker.postMessage({
  file,
  chunkSize: CHUNKE_SIZE,
  startIndex,
  endIndex
})
```

在线程`worker.js`中接收参数

```js
import { createChunk } from './createChunk.js'

onmessage = async (e) => {
  const { file, chunkSize, startIndex, endIndex } = e.data
}
```

根据现有代码创建分片

```js
import { createChunk } from './createChunk.js'

onmessage = async (e) => {
  const chunks = []
  const { file, chunkSize, startIndex, endIndex } = e.data
  for (let i = startIndex; i < endIndex; i++) {
    chunks.push(await createChunk(file, i, chunkSize))
  }
}
```

但是如果是这样的话，就和单线程执行没有什么区别了，我们可以使用Promise.all同时执行所有的异步操作，最后将结果返回回去

```js
onmessage = async (e) => {
  const proms = []
  const { file, chunkSize, startIndex, endIndex } = e.data
  for (let i = startIndex; i < endIndex; i++) {
    proms.push(createChunk(file, i, chunkSize))
  }
  const chunks = await Promise.all(proms)
  postMessage(chunks)
}
```

在`cutFile.js`中，我们可以通过获取`e.data`获取线程返回的数据，但是因为线程完成的时间是不一定的，所以我们需要对所有分片进行排序然后添加到结果数组中去

```js
 worker.onmessage = (e) => {
  for (let i = startIndex; i < endIndex; i++) {
   result[i] = e.data[i - startIndex]
 }
 worker.terminate() //  线程完成之后就可以结束了
 finishCount++
 if (finishCount == THREAD_COUNT) { // 当所有线程结束时，返回结果数组
   resolve(result)
 }
}
```

这样一个大文件分片就完成了



## 前端组件级权限控制

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/295ecffd5097d107473e6cbe5787105f.gif" style="zoom: 50%;" />

前端的权限控制分为

1. 页面级权限控制
2. 组件级权限控制
3. 函数级权限控制（少见）

其中页面级权限控制可以使用路由守卫实现，下面介绍的组件级权限控制使用自定义组件控制

```vue
<div class="buttons">
  <Authority>
    <template #default="{ userPermissions }">
      <el-button :disabled="!userPermissions.includes('sys:user:add')" type="primary">新增用户</el-button>
    </template>
  </Authority>
  <Authority permission="sys:user:view">
    <el-button type="primary">查询用户</el-button>
  </Authority>
  <Authority permission="sys:user:update">
    <el-button type="primary">修改用户</el-button>
  </Authority>
  <Authority permission="sys:user:delete">
    <el-button type="danger">删除用户</el-button>
  </Authority>
  <Authority :permission="['sys:user:update', 'sys:user:view']">
    <el-button type="danger">禁用用户</el-button>
  </Authority>
</div>
```

 在需要细粒到组件的权限控制项目中，我们可以自定义一个通用组件，具体需要按照业务需求来决定是否能够使用通用组件来控制，这里定义的组件可以根据传入的权限控制组件的显示，或者自定义显示需求

下面是`Authority`组件的代码

```vue
<template>
  <slot v-if="showSlot" :userPermissions="auth.permissions"></slot>
</template>

<script setup>
import { computed } from 'vue'
import { useAuthStore } from '@/stores'
const props = defineProps({
  permission: {
    type: [String, Array]
  }
});
const auth = useAuthStore()
const showSlot = computed(() => {
  if (!props.permission) {
    // 没有传入权限直接显示
    return true
  }
  if (!auth.permissions) {
    // store中没有权限，不显示
    return false
  }
  // 有值的情况
  if (Array.isArray(props.permission)) {
    return props.permission.every((p) => auth.permissions.includes(p))
  } else {
    return auth.permissions.includes(props.permission)
  }
})
</script>
```

下面是`auth`的代码

```js
import { defineStore } from "pinia";
import { ref } from "vue";

export const useAuthStore = defineStore('authStore', () => {
  const authMap = {
    'admin': ['sys:user:view', 'sys:user:update', 'sys:user:delete', 'sys:user:add'],
    'editor': ['sys:user:view', 'sys:user:update', 'sys:user:add'],
    'visitor': ['sys:user:view']
  }
  const role = ref('visitor')
  const permissions = ref(authMap[role.value])
  const changeAuth = (auth) => {
    permissions.value = authMap[auth] || []
  }
  return {
    role,
    permissions,
    changeAuth
  }
})
```

`App.vue`中的完整代码

```vue
<script setup>
import { ref } from 'vue';
import Authority from './components/Authority/Authority.vue';
import { useAuthStore } from './stores/modules/auth';
const auth = useAuthStore()

const options = ref([
  'admin',
  'editor',
  'visitor'
])
const onChange = (authName) => {
  console.log(authName)
  auth.changeAuth(authName)
  console.log(auth.permissions)
}
</script>

<template>
  <div class="app">
    <div class="select">
      <el-row style="display: flex; align-items: center;">
        <el-col :span="8">
          <p>选择身份</p>
        </el-col>
        <el-col :span="16">
          <el-select v-model="auth.role" @change="onChange">
            <el-option v-for="item in options" :label="item" :value="item" />
          </el-select>
        </el-col>
      </el-row>
    </div>
    <div class="buttons">
      <Authority>
        <template #default="{ userPermissions }">
          <el-button :disabled="!userPermissions.includes('sys:user:add')" type="primary">新增用户</el-button>
        </template>
      </Authority>
      <Authority permission="sys:user:view">
        <el-button type="primary">查询用户</el-button>
      </Authority>
      <Authority permission="sys:user:update">
        <el-button type="primary">修改用户</el-button>
      </Authority>
      <Authority permission="sys:user:delete">
        <el-button type="danger">删除用户</el-button>
      </Authority>
      <Authority :permission="['sys:user:update', 'sys:user:view']">
        <el-button type="danger">禁用用户</el-button>
      </Authority>
    </div>
  </div>
</template>

<style scoped>
.app {
  display: flex;
  height: 100vh;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.select {
  margin-bottom: 20px;
}
</style>
```



## 虚拟列表

虚拟列表：只对`可视区域`进行渲染，对`非可视区域`中的区域不渲染或只渲染一部分（渲染的部分叫`缓冲区`，不渲染的部分叫`虚拟区`），从而达到极高的性能

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/06ac5e146d0fb9f9f6aabe46fb76cb44.webp)

我们可以将列表分为三个区域：**可视区**、**缓冲区**、**虚拟区**，而我们主要针对`可视区`和`缓冲区`进行渲染

针对列表项目的高度，我们可以将虚拟列表分为**定高列表**和**不定高列表**	

对于简单的需求可以使用定高进行处理，但是在实际的项目中，大部分滚动列表项目中的列表项都是不定高的，因此，这里针对不定高虚拟列表进行设计

对于列表项的动态高度，我们可以使用两种方式进行处理

1. 第一是将高度作为参数传递过来，可以通过作为列表数据数组的成员进行传递，在虚拟列表组件的插槽中传递出来给列表项使用
2. 预算高度，我们可以假定列表项的高度为一个虚假高度，当我们进行渲染时，再更新对应高度

设计虚拟列表

**TODO**



在vue3中有一个通用的虚拟列表包，提供一个通用的虚拟列表组件（即既可定高也可不定高）

**虚拟列表属性和方法**

必须的属性

| **属性**       | **类型**         | **描述**                                                     |
| -------------- | ---------------- | ------------------------------------------------------------ |
| `data-key`     | String\|Function | 从`data-sources`中的每个数据对象获取唯一键。或者使用每个数据源调用函数并返回其唯一键。其值在数据源中必须是唯一的，用于标识每一项的尺寸。 |
| `data-sources` | Array[Object]    | 为列表生成的源数组，每个数组数据必须是一个对象，并且具有唯一的key get或generate for`data key`属性。 |

其他属性

| 属性                | 类型     | 默认值   | 描述                                                         |
| ------------------- | -------- | -------- | ------------------------------------------------------------ |
| `keeps`             | Number   | 30       | 您期望虚拟列表在真实 dom 中保持渲染的项目数量。              |
| `extra-props`       | Object   | {}       | 分配给组件一些不在`data-sources`中的属性. 注意: `index` 和 `source` 都被内部占用了. |
| `estimate-size`     | Number   | 50       | 每个`Item`的估计大小，如果它更接近平均大小，滚动条长度看起来更准确。建议指定自己计算的平均值。 |
| `start`             | Number   | 0        | 设置滚动位置保持开始索引。                                   |
| `offset`            | Number   | 0        | 设置滚动位置保持偏移。                                       |
| `scroll`            | Event    |          | 滚动时触发, 参数 `(event, range)`。                          |
| `totop`             | Event    |          | 当滚动到顶部或者左边时触发, 无参数。                         |
| `tobottom`          | Event    |          | 当滚动到底部或者右边时触发，无参数。                         |
| `resized`           | Event    |          | 当大小改变时触发 (mounted), 参数 `(id, size)`。              |
| `direction`         | String   | vertical | 滚动的方向, 可选值为 `vertical` 和 `horizontal`。            |
| `top-threshold`     | Number   | 0        | 发出`totop` 事件的阈值, 注意多个调用。                       |
| `bottom-threshold`  | Number   | 0        | 发出`tobottom` 事件的阈值, 注意多个调用。                    |
| `container-class`   | String   |          | 容器的类名，一般需要添加高度/或者宽度来让内容滚动，1.5.0版本新增 |
| `root-tag`          | String   | div      | 根节点的名称。                                               |
| `wrap-tag`          | String   | div      | 列表包裹元素名称`(role=group)`。                             |
| `wrap-class`        | String   |          | 列表包裹元素类名。                                           |
| `wrap-style`        | Object   | {}       | 列表包裹元素内联样式。                                       |
| `item-tag`          | String   | div      | 项目包裹元素名称。                                           |
| `item-class`        | String   |          | 项目包裹元素类名。                                           |
| `item-class-add`    | Function |          | 一个函数，您可以将额外的类（字符串）返回给项包装器元素， 参数 `(index)`。 |
| `item-style`        | Object   | {}       | 项目包裹元素内联样式。                                       |
| `item-scoped-slots` | Object   | {}       | Item组件的 slot。                                            |

公共方法

| 方法                     | 描述                                                         |
| ------------------------ | ------------------------------------------------------------ |
| `reset()`                | 将所有状态重置回初始状态。                                   |
| `scrollToBottom()`       | 手动将滚动位置设置为底部。                                   |
| `scrollToIndex(index)`   | 手动将滚动位置设置为指定索引。                               |
| `scrollToOffset(offset)` | 手动将滚动位置设置为指定的偏移量。                           |
| `getSize(id)`            | 按id（从`data-key`）获取指定的项目大小。如果已渲染列表中没有该项，则返回`undefined`。 |
| `getSizes()`             | 获取存储（渲染）项的总数。                                   |
| `getOffset()`            | 获取当前滚动偏移量。                                         |
| `getClientSize()`        | 获取包装器元素客户端视口大小（宽度或高度）。                 |
| `getScrollSize()`        | 获取所有滚动大小（滚动高度或滚动宽度）。                     |

安装依赖

```bash
npm install vue-virtual-list-v3
```

示例代码

1. 在main中引入

```js
import {createApp} from 'vue'
import App from './App.vue'
import VirtualList from 'vue-virtual-list-v3'

createApp(App).use(VirtualList).mount('#app')
```

2. 使用

```vue
<template>
  <div class="container">
    <button @click="addItem">添加</button>
    <VirtualList ref="virtualList" :data-key="'id'" :data-sources="items"
                 containerClass="list-dynamic">
      <template #="{ source }">
        <!--<div class="item-inner" :style="{ height: source.size + 'px' }">-->
        <div class="item-inner">
          <div class="head">
            <span># {{ source.index }}</span>
            <span>{{ source.name }}</span>
          </div>
          <div class="desc">
            {{ source.desc }}
          </div>
        </div>
      </template>
    </VirtualList>
  </div>
</template>
<script setup>
import {ref} from 'vue'

const genUniqueId = (prefix) => {
  return `${prefix}$${Math.random().toString(16).substr(9)}`;
};
const sentence3 = [
  'BFC(Block formatting context)直译为"块级格式化上下文"。它是一个独立的渲染区域，只有Block-level box参与， 它规定了内部的Block-level Box如何布局，并且与这个区域外部毫不相干。BFC(Block formatting context)直译为"块级格式化上下文"。它是一个独立的渲染区域，只有Block-level box参与， 它规定了内部的Block-level Box如何布局，并且与这个区域外部毫不相干。BFC(Block formatting context)直译为"块级格式化上下文"。它是一个独立的渲染区域，只有Block-level box参与， 它规定了内部的Block-level Box如何布局，并且与这个区域外部毫不相干。',
  'IFC(Inline Formatting Contexts)直译为”内联格式化上下文”，IFC的line box（线框）高度由其包含行内元素中最高的实际高度计算而来（不受到竖直方向的padding/margin影响)BFC(Block formatting context)直译为"块级格式化上下文"。它是一个独立的渲染区域，只有Block-level box参与， 它规定了内部的Block-level Box如何布局，并且与这个区域外部毫不相干。BFC(Block formatting context)直译为"块级格式化上下文"。它是一个独立的渲染区域，只有Block-level box参与， 它规定了内部的Block-level Box如何布局，并且与这个区域外部毫不相干。',
  'margin 重合，margin 塌陷',
  'css3',
  'html5',
  'es6',
];
const getSentences = () => {
  let index = Math.floor(Math.random() * (sentence3.length - 1));
  return sentence3[index];
};
// const sizes = [60, 80, 100, 150, 180, 500];
const DataItems = [];
const TOTAL_COUNT = 40;
let count = TOTAL_COUNT;
while (count--) {
  const index = TOTAL_COUNT - count;
  DataItems.push({
    index,
    name: `\n${Math.random()}`,
    id: genUniqueId(index),
    desc: getSentences(),
    // size: sizes[Math.floor(Math.random() * 5)],
  });
}

let items = ref(DataItems);

const addItem = () => {
  DataItems.push({
    index: Math.random() * 1000 + 1,
    name: 'Brad' + Math.random() * 1000 + 1,
    id: Date.now(),
    desc: 'html5',
    // size: 150,
  });
  items.value = JSON.parse(JSON.stringify(DataItems));
};
</script>
<style lang="less">
.container {
  border: 1px solid #eee;
  padding: 20px;
  margin-top: 20px;
  width: 1000px;
}

.list-dynamic {
  width: 100%;
  height: 500px;
  overflow-y: auto;

  .list-item-dynamic {
    display: flex;
    align-items: center;
    padding: 1em;
    border-bottom: 1px solid;
    border-color: lightgray;
    background: rgba(83, 132, 255, 0.06) none repeat scroll 0% 0%;
    border-bottom: 2px solid rgb(255, 255, 255);
  }
}

.item-inner {
  .head {
    font-weight: 500;
    text-align: left;
  }

  span:first-child {
    margin-right: 1em;
  }

  .desc {
    padding-top: 0.5em;
    text-align: justify;
  }
}

.list-horizontal {
  width: 100%;
  height: 300px;
  overflow-x: auto;
  display: flex;

  .wrapper {
    display: flex;
    flex-direction: row;
  }

  .list-item-horizontal {
    border-right: 2px solid rgb(255, 255, 255);
    background: rgba(83, 132, 255, 0.06) none repeat scroll 0% 0%;
  }
}

.item-inner-horizontal {
  display: flex;
  align-items: center;
  flex-direction: column;
  padding: 2em 0;

  .index {
    width: 100%;
    text-align: center;
  }

  .size {
    text-align: right;
    color: darkgray;
    font-size: 16px;
  }
}

.wrap-list {
  display: flex;
}
</style>
```



## 浏览器指纹

在网页中可以通过使用浏览器API计算出一个哈希值，得到一个该浏览器独一无二的值，这个值称为浏览器的指纹。

比如可以通过下面网址查看当前浏览器的指纹。

[Canvas Fingerprinting - BrowserLeaks](https://browserleaks.com/canvas)

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/66a02002187ca3e7d8c0be243e4acc5a.png)

浏览器指纹的原理是各个浏览器和系统环境的微小差距造成使用浏览器提供的API时会产生细小的差距，通过特殊计算可以得到一个独一无二的值。

在项目中使用，可以使用[fingerprintjs](https://github.com/fingerprintjs/fingerprintjs)这个库

使用

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>浏览器指纹</title>
</head>

<body>
  <script>
    // Initialize the agent at application startup.
    const fpPromise = import('https://openfpcdn.io/fingerprintjs/v4')
      .then(FingerprintJS => FingerprintJS.load())

    // Get the visitor identifier when you need it.
    fpPromise
      .then(fp => fp.get())
      .then(result => {
        // This is the visitor identifier:
        const visitorId = result.visitorId
        console.log(visitorId)
      })
  </script>
</body>

</html>
```

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/1dd58fe044dc1d4c81a624cc19b2e315.png)



## 任务执行的洋葱模型



## 跨标签通信

推特上一位大神的创意代码火了，看了让人直呼脑洞大开

[𝕭𝖏ø𝖗𝖓 𝕾𝖙𝖆𝖆𝖑 (@_nonfigurativ_) / X (twitter.com)](https://twitter.com/_nonfigurativ_)

作者发布了一个简易版本到github上https://github.com/bgstaal/multipleWindow3dScene

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/a78a4a3dcdac134d987af65b984a336c.gif)

这里面除了Threejs实现的炫酷粒子星球效果以外，另一个重要的点就是跨标签通信

跨标签页通信常见方案

- BroadCast Channel
- Service Worker
- LocalStorage window.onstorage 监听
- Shared Worker 定时器轮询( setInterval)
- IndexedDB 定时器轮询(setInterval)
- cookie 定时器轮询 ( setInterval)
- window.open、window.postMessage
- Websocket

这里作者使用的是LocalStorage监听

LocalStorage监听的原理是通过事件监听`storage`，当其他标签页修改了LocalStorage时，事件触发

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/fd7136bb2ad7a8ca0ef29bc8f55e7852.png)



了解原理之后，我们可以编写一个类来管理浏览器窗口和`storage`事件

最终达到这种效果

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/5f6f44eba4c8541060ea5e1fec7e56cc.png)

首先定义一个类，我们需要将每个窗口的数据存储在数组中在存入`localStorage`，同时定义窗口位置大小改变时的回调函数`winShapeChangeCallback`，窗口关闭（窗口列表改变）时的回调函数`winChangeCallback`，同时需要获取当前有多少窗口`count`，当前窗口id，当前窗口数据`winData`

```js
class WindowManager {
	#windows; // 窗口列表
	#count; // 窗口计数
	#id; // 当前窗口ID
	#winData; // 当前窗口数据
	#winShapeChangeCallback; // 窗口形状改变回调函数
	#winChangeCallback; // 窗口列表改变回调函数
}
```

在构造函数中监听两个事件，

一个是`storage`更新的事件，需要判断是否有新的窗口数据被添加，如果窗口更改，执行窗口列表更改回调函数

二是页面刷新时（关闭也会触发）移除当前窗口的数据

```js
constructor() {
	// localStorage更新时
	addEventListener("storage", (event) => {
		// 键名为windows时
		if (event.key == "windows") {
			let newWindows = JSON.parse(event.newValue);
			let winChange = this.#didWindowsChange(this.#windows, newWindows);

			this.#windows = newWindows;

			if (winChange) {
				if (this.#winChangeCallback) this.#winChangeCallback();
			}
		}
	});

	// 页面刷新时
	window.addEventListener("unload", (e) => {
		let index = this.getWindowIndexFromId(this.#id);

		// 从列表中移除当前窗口并更新localStorage
		this.#windows.splice(index, 1);
		this.#count--;
		localStorage.setItem("count", this.#count);
		localStorage.setItem("windows", JSON.stringify(this.#windows));
	});
}
```

同时需要一个检查窗口列表是否变化的函数

```js
// 检查窗口列表是否有变化
#didWindowsChange(pWins, nWins) {
	if (pWins.length != nWins.length) {
		return true;
	} else {
		let isChange = false;

		for (let i = 0; i < pWins.length; i++) {
			if (pWins[i].id != nWins[i].id) isChange = true;
		}

		return isChange;
	}
}
```

获取当前窗口相对屏幕的位置和窗口大小

```js
// 获取当前窗口的尺寸
getWinShape() {
	let shape = {
		x: window.screenLeft,
		y: window.screenTop,
		w: window.innerWidth,
		h: window.innerHeight,
	};
	return shape;
}
```

初始化，从localStorage读入数据，**metaData在这个示例中没有使用，但是它其实是多窗口通信的意义之一，即传递有效信息**，当然shape在实现这个示例的效果中也是重要信息。

```js
init(metaData) {
	// 从localStorage读取数据
	this.#windows = JSON.parse(localStorage.getItem("windows")) || [];
	this.#count = localStorage.getItem("count") || 0;
	this.#count++;
	
	this.#id = this.#count;
	let shape = this.getWinShape();
	// 当前窗口的所有数据
	this.#winData = { id: this.#id, shape: shape, metaData: metaData };
	this.#windows.push(this.#winData);

	localStorage.setItem("count", this.#count);
	localStorage.setItem("windows", JSON.stringify(this.#windows));
}
```

通过id获取窗口信息的索引

```js
// 通过id获取窗口的索引
getWindowIndexFromId(id) {
	let index = -1;

	for (let i = 0; i < this.#windows.length; i++) {
		if ((this.#windows[i].id == id)) index = i;
	}

	return index;
}
```

最重要的就是更新窗口位置大小数据，这个函数在外部可以放在渲染函数中使用`requestAnimationFrame`实时更新

```js
// 更新窗口位置大小数据
update() {
	let winShape = this.getWinShape();

	if (
		winShape.x != this.#winData.shape.x ||
		winShape.y != this.#winData.shape.y ||
		winShape.w != this.#winData.shape.w ||
		winShape.h != this.#winData.shape.h
	) {
		this.#winData.shape = winShape;

		let index = this.getWindowIndexFromId(this.#id);
		this.#windows[index].shape = winShape;

		// 调用回调函数
		if (this.#winShapeChangeCallback) this.#winShapeChangeCallback();
		localStorage.setItem("windows", JSON.stringify(this.#windows));
	}
}
```

最后由于我们定义的是私有字段（`#`开头的字段名），所以需要对外提供访问函数

```js
setWinShapeChangeCallback(callback) {
	this.#winShapeChangeCallback = callback;
}

setWinChangeCallback(callback) {
	this.#winChangeCallback = callback;
}

getWindows() {
	return this.#windows;
}

getThisWindowData() {
	return this.#winData;
}

getThisWindowID() {
	return this.#id;
}
```

最后导出WindowManager对象即可

```js
export default WindowManager;
```



现在实现一个简化版本，没错就是作者简化版本再简化的版本🤣



按照上面的代码编写完成WindowsManager后，我们在一个简单的页面中进行测试

创建main.js文件，写入如下内容

```js
import WindowManager from "./windowManager.js";
let windowManager;
(function() {
	windowManager = new WindowManager();
	windowManager.init();
})()
function render() {
	requestAnimationFrame(render);
	windowManager.update();
}
render();
```

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/484ed733f6f26edb423506aa9bf75595.gif)



我们编写一个创建立方体div的函数

```js
function mountBox(x, y, color) {
	let box = document.createElement("div");
	box.classList.add("box");
	document.body.appendChild(box);
	boxes.push(box);
	boxes[index].style.transform = `translate(${x}px, ${y}px)`;
	boxes[index].style.backgroundColor = color;
	boxes[index].innerHTML = index;
	boxPos.push({ x: x, y: y });
	index++;
}

mountBox(
	0,
	0,
	"red"
);
```

这个时候会创建一个红色的立方体

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/73bb7ae9851289ef1d16973b1c18f505.png)

当然，在至此之前，你需要添加以下样式

```css
* {
	padding: 0;
	margin: 0;
}

body {
	background: #000;
}

.box {
	display: flex;
	justify-content: center;
	align-items: center;
	width: 100px;
	height: 100px;
	color: white;
	background-color: red;
	transform: none;
	transition: all 1s;
}
```

再编写一个更新位置的函数

```js
function updateBox(index, x, y) {
	boxes[index].style.transform = `translate(${x}px, ${y}px)`;
	boxPos[index].x = x;
	boxPos[index].y = y;
}

updateBox(0, 100, 100);
```

此时立方体在这里

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/90c0cc0846df0de5e209db190d6a0829.png)

我们在之前的render函数中加上更新立方体位置的函数，它就变成了这样，立方体在你拖拽窗口改变大小时都始终在屏幕中间

```js
mountBox(
	windowManager.getWinShape().w / 2 - 50,
	windowManager.getWinShape().h / 2 - 50,
	"red"
);

function render() {
	requestAnimationFrame(render);
	windowManager.update();
	updateBox(
		0,
		windowManager.getWinShape().w / 2 - 50,
		windowManager.getWinShape().h / 2 - 50
	);
}
render();
```

再编写一个卸载立方体的函数

```js
function unmountBox(index) {
	boxes[index].remove();
	boxes.splice(index, 1);
	boxPos.splice(index, 1);
}

unmountBox(0);
```



立方体位置的计算方式

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/0de6329474f93e76884c951a649749c3.png)



## 使用computed解决v-model问题

正常使用vue 组件传参需要实现双向数据流，对于对象传参，直接使用v-model可能打断双向数据流，故可以使用computed加proxy实现对象传参的双向数据流

```vue
<script setup lang="ts">
import { computed } from "vue";
const emit = defineEmits(["update:modelValue"]);
const props = defineProps<{
	modelValue: {
		username: string;
		password: string;
	};
}>();
const model = computed({
	get() {
		return new Proxy(props.modelValue, {
			set(obj, name, val) {
				emit("update:modelValue", {
					...obj,
					[name]: val,
				});
				return true;
			},
		});
	},
	set(val) {
		emit("update:modelValue", val);
	},
});
</script>

<template>
	用户名：<input type="text" v-model="model.username" /><br />
	密码：<input type="password" v-model="model.password" />
</template>

<style scoped></style>
```

可以封装成useVModel

```ts
import { computed } from "vue";
export function useVModel(props: any, propName: string, emit: Function) {
	return computed({
		get() {
			return new Proxy(props[propName], {
				set(obj, name, val) {
					console.log(1);
					emit("update:" + propName, {
						...obj,
						[name]: val,
					});
					return true;
				},
			});
		},
		set(val) {
			emit("update:" + propName, val);
		},
	});
}
```

然后再使用

```vue
<script setup lang="ts">
import { useVModel } from "../hooks/useVModel";
const emit = defineEmits(["update:modelValue"]);
const props = defineProps<{
	modelValue: {
		username: string;
		password: string;
	};
}>();
const model = useVModel(props, "modelValue", emit);
</script>

<template>
	用户名：<input type="text" v-model="model.username" /><br />
	密码：<input type="password" v-model="model.password" />
</template>

<style scoped></style>
```

