Three.js是一个在浏览器上渲染3D图像的Javascript库，可以用来创建精美的3D网页

## 1. 入门

### 1.1 安装

**从npm安装**

- 此方法适用于现在主流的web工程化开发的方案（如vue，react等）推荐使用

1. 从npm安装

```bash
npm install three
```

2. 导入到项目中

```js
// 方式 1: 导入整个 three.js核心库
import * as THREE from 'three';

const scene = new THREE.Scene();


// 方式 2: 仅导入你所需要的部分
import { Scene } from 'three';

const scene = new Scene();
```



**从CDN或静态文件安装**

- 此方法适用于原生web开发中html引入three.js，你可以选择从cdn引入或者静态文件引入，所使用的标签必须使用`module`才能支持ES6语法，注意，`importmap`可以使导入模块像工程化开发一样直接导入，所以需要设置`importmap`

1. 从CDN引入

```html
<script async src="https://unpkg.com/es-module-shims@1.6.3/dist/es-module-shims.js"></script>

<script type="importmap">
	{
		"imports": {
			"three": "https://unpkg.com/three@<version>/build/three.module.js"
		}
	}
</script>
```

2. 使用

```html
<script type="module">

	import * as THREE from 'three';

	const scene = new THREE.Scene();

</script>
```

### 1.2 Addons

three.js的核心专注于3D引擎最重要的组件。其它很多有用的组件 —— 如控制器（control）、加载器（loader）以及后期处理效果（post-processing effect） —— 是 [examples/jsm](https://github.com/mrdoob/three.js/tree/dev/examples/jsm) 目录的一部分。它们被称为“示例”，虽然你可以直接将它们拿来使用，但它们也需要重新混合以及定制。这些组件和 three.js 的核心保持同步，而 npm 上类似的第三方包则由不同的作者进行维护，可能不是最新的。

示例无需被单独地*安装*，但需要被单独地*导入*。如果 three.js 是使用 npm 来安装的，你可以使用如下代码来加载轨道控制器（[OrbitControls](https://threejs.org/docs/index.html#examples/zh/controls/OrbitControls)）：

```js
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

const controls = new OrbitControls( camera, renderer.domElement );
```

如果 three.js 安装自一个 CDN ，请使用相同的 CDN 来安装其他组件：

```html
<script type="importmap">
	{
		"imports": {
			"three": "https://unpkg.com/three@<version>/build/three.module.js",
			"three/addons/": "https://unpkg.com/three@<version>/examples/jsm/"
		}
	}
</script>

<script type="module">

	import * as THREE from 'three';
	import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

	const controls = new OrbitControls( camera, renderer.domElement );

</script>
```



## 2. 基础

### 2.1 基础组成

Three.js中基本的组成为：

- 场景
- 物体 -> 材质 -> 网格
- 灯光
- 相机
- 渲染器
- 辅助工具 -> 坐标系(axes)等
- ...

1. 创建一个长方体

```js
// 首先需要导入three.js
import * as THREE from "three";
// 创建物体，BoxGeometry长方体
const box = new THREE.BoxGeometry(5, 5, 5);
// 创建材质
const material = new THREE.MeshBasicMaterial({
  color: 0x42a5f5,
});
// 创建网格
const cube = new THREE.Mesh(box, material);
cube.position.set(0, 0, 0);
```

2. 将物体添加到场景中

```js
// 场景
const scene = new THREE.Scene();
// 将网格添加到场景
scene.add(cube);
```

3. 此时还没有内容，需要创建相机和渲染器

```js
// 创建相机 (param1: fov视野宽度, param2: 宽高比, param3: 近裁切面距离, param4: 远裁切面距离) 四者构成了一个渲染四面体 (视锥体)
const camera = new THREE.PerspectiveCamera(60, width / height, 0.1, 100);
camera.position.set(10, 10, 10);
camera.lookAt(cube.position); // camera.lookAt(0, 0, 0);
// 创建WebGL渲染器
const render = new THREE.WebGLRenderer();
render.setSize(width, height);
render.render(scene, camera);
```

4. 挂载到页面的元素上，这里是页面上一个`#app`的`div`元素

```js
// 将这个元素添加到页面body中
document.querySelector("#app").appendChild(render.domElement);
```

5. 但是因为three.js是基于canvas的，所以需要设置DPI，防止出现锯齿。**设置抗锯齿**

```js
// 设置抗锯齿
render.setPixelRatio(window.devicePixelRatio)
```

6. 最终显示的画面

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/7191de04a936af92616ecec9628c4a3f.png)

**完整代码**

```html
<!--html-->

<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Basic</title>
    <style>
      body {
        margin: 0;
      }
      #app {
        height: 100vh;
        width: 100vw;
      }
    </style>
  </head>

  <body>
    <div id="app"></div>
    <script type="importmap">
      {
        "imports": {
          "three": "../three.js-r143/build/three.module.js",
          "three/addons/": "../three.js-r143/examples/jsm"
        }
      }
    </script>
    <script src="index.js" type="module"></script>
  </body>
</html>
```

```js
/**
* javascript
*/

import * as THREE from "three";
// 创建物体，BoxGeometry长方体
const box = new THREE.BoxGeometry(5, 5, 5);
// 创建材质
const material = new THREE.MeshBasicMaterial({
  color: 0x42a5f5,
});
// 创建网格
const cube = new THREE.Mesh(box, material);
cube.position.set(0, 0, 0);
// 场景
const scene = new THREE.Scene();
// 将网格添加到场景
scene.add(cube);
// 定义画布尺寸
const width = document.querySelector("#app").offsetWidth;
const height = document.querySelector("#app").offsetHeight;
// 创建相机 (param1: fov视野宽度, param2: 宽高比, param3: 近裁切面距离, param4: 远裁切面距离) 四者构成了一个渲染四面体 (视锥体)
const camera = new THREE.PerspectiveCamera(60, width / height, 0.1, 100);
camera.position.set(10, 10, 10);
camera.lookAt(cube.position); // camera.lookAt(0, 0, 0);
// 创建WebGL渲染器
const render = new THREE.WebGLRenderer();
render.setSize(width, height);
render.render(scene, camera);
// render.domElement, 即一个Canvas元素
console.log(render.domElement);
// 将这个元素添加到页面body中
document.querySelector("#app").appendChild(render.domElement);

```



再说相机

- 上面的案例中使用的是透视相机
- **透视相机**的四个参数`fov, aspect, near, far`构成一个**四棱台**3D空间，被称为**视锥体**，**只有在视锥体中的物体才会被渲染出来**

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/d68bda197314e4f3b7f13977910ac812.png)

| 参数   | 含义                                                         | 默认值 |
| ------ | ------------------------------------------------------------ | ------ |
| fov    | 相机视锥体竖直方向视野角度                                   | 50     |
| aspect | 相机视锥体水平方向和竖直方向长度比，一般设置为Canvas画布宽高比width / height | 1      |
| near   | 相机视锥体近裁截面相对相机距离                               | 0.1    |
| far    | 相机视锥体远裁截面相对相机距离，far-near构成了视锥体高度方向 | 2000   |

### 2.3 请求动画帧

使用浏览器的请求动画帧API`requestAnimationFrame`配合three.js的reander可以实现动画效果

```js
// 创建一个动画，并计算当前渲染帧率
const clock = new THREE.Clock()
function animate() {
  const spt = clock.getDelta() * 1000
  document.querySelector('#fps').innerHTML = Math.floor(1000 / spt)
  cube.rotateY(0.05)
  controls.update()
  render.render(scene, camera)
  requestAnimationFrame(animate)
}
animate()
```

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/4b457afb773647f13b4afd8cc68989f4.gif)



### 2.4 根据页面大小调整渲染器尺寸

**根据页面大小调整渲染器尺寸**

```js
// 根据页面大小调整渲染器尺寸
window.onresize = () => {
  width = document.querySelector('#app').offsetWidth
  height = document.querySelector('#app').offsetHeight
  render.setSize(width, height)
  camera.aspect = width / height
  camera.updateProjectionMatrix()
}
```



### 2.5 相机参数调整

设置位置

```js
 camera.position.set(0, 10, 0)
```

相机指向

```js
camera.lookAt(0, 0, 0)
```

调整视锥体范围

```js
  // 创建相机 (param1: fov视野宽度, param2: 宽高比, param3: 近裁切面距离, param4: 远裁切面距离) 四者构成了一个渲染四面体 (视锥体)
  const camera = new THREE.PerspectiveCamera(60, width / height, 0.1, 800)
```

- 超出视锥体范围的物体会被剪掉

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/bd7f4d51bd8af8aecf5b52c0c1e3c32a.png)



### 2.6 常见简单几何体

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/36688ac79d3e69eabb9cb56277ac4f38.png" style="zoom:50%;" />

创建一个长方体

```js
onst geometry = new THREE.BoxGeometry(5, 5, 10)
const mesh = new THREE.Mesh(geometry, material)
scene.add(mesh)
```



创建一个球体

```js
const geometry = new THREE.SphereGeometry(30)
const mesh = new THREE.Mesh(geometry, material)
scene.add(mesh)
```



创建一个圆柱体

```js
const geometry = new THREE.CylinderGeometry(5,5,10,32)
const mesh = new THREE.Mesh(geometry, material)
scene.add(mesh)
```



创建一个平面

```js
const geometry = new THREE.PlaneGeometry(5, 5, 5)
const mesh = new THREE.Mesh(geometry, material)
scene.add(mesh)
```







## 3. 渲染器

### 3.1 渲染器抗锯齿属性

设置渲染器抗锯齿属性.antialias的值可以直接在参数中设置，也可通过渲染器对象属性设置。

```js
var renderer = new THREE.WebGLRenderer({antialias:true,
});
```

或
```js
renderer.antialias = true
```



### 3.2 设备像素比

如果canvas画布输出模糊，注意设置
`renderer.setPixelRatio(window.devicePixelRatio)`

注意:注意你的硬件设备设备像素比`window.devicePixelRatio`刚好是1，那么是否执行`setPixelRatio()`不会有明显差异，不过为了适应不同的硬件设备屏幕，通常需要执行该方法。
```js
//获取你屏幕对应的设备像素比. devicePixelRatio告诉threejs,以免渲染模糊问题
renderer.setPixelRatio(window.devicePixelRatio)
```



### 3.3 设置背景颜色

```js
render.setClearColor(0xaaa000, 1.0)
```

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/e1658e4a78fd978e0a936283711e8902.png)



## 4. 交互界面

### 4.1 相机控件-轨道控制器

使用轨道控制器需要引入Addons

如果按照上面的配置好`importmap`后，应该是这样导入`OrbitControls`

```js
import { OrbitControls } from "three/addons/controls/OrbitControls.js";
```

轨道控制器的基本操作逻辑

- *旋转：拖动鼠标左键*
- *缩放：滚动鼠标滚轮*
- *平移：拖动鼠标右键*



1. 使用上面场景的代码
2. 创建相机轨道控制器

```js
// 创建相机轨道控制器
const controls = new OrbitControls(camera, render.domElement);
controls.update();
```

3. 此时还不能操作物体，因为需要设置动画
4. 创建动画

```js
// 创建动画
const animate = () => {
  requestAnimationFrame(animate);
  controls.update();
  render.render(scene, camera);
};
animate();
```

最终效果

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/691c273273862308d48f72d67d1224f9.gif)



### 4.2 性能监视器

使用性能监视器需要引入Stats

```js
// 引入stats性能监视器
import Stats from 'three/addons/libs/stats.module.js'
```

创建性能监视器，并添加到页面中

```js
// 创建性能监视器
const stats = new Stats()
document.querySelector('#app').appendChild(stats.dom)
```

在渲染函数中更新性能监视器

```js
// 创建一个动画，并计算当前渲染帧率
const clock = new THREE.Clock()
function animate() {
  stats.update()
  cube.rotateY(0.05)
  controls.update()
  render.render(scene, camera)
  requestAnimationFrame(animate)
}
animate()
```

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/9cb6b9c540d7299d2d86e06132ff93b2.png)

测试性能

```js
// 测试性能，添加10000个立方体到场景中
for (let i = 0; i < 10000; i++) {
  const mesh = new THREE.Mesh(box, material)
  // 设置大小
  mesh.scale.set(0.05, 0.05, 0.05)
  mesh.position.set(Math.random() * 10 - 5, Math.random() * 10 - 5, Math.random() * 10 - 5)
  scene.add(mesh)
}
```

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/c4576b1a7c33b32d61395118932bed9d.png)



### 4.3 可视化改变三维场景

**gui.js库（可视化改变三维场景）**
dat.gui.js是一个前端js库，对HTML、CSS和JavaScript进行了封装，学习开发的时候，借助dat.gui.js可以快速创建控制三维场景的UI交互界面

你可以通过npm或github方式获得dat.gui.js库，当然为了学习方便,threejs官方案例扩展库中也提供了gui.js，你可以直接使用。
```js
//引入dat.gui.js的一个类GUI
import { GUI } from 'three/addons/libs/lil-gui.module.min.js';
```

**`add`方法**

执行gui的.add()方法可以快速创建一个UI交互界面，比如一个拖动条，可以用来改变一个JavaScript对象属性的属性值。

格式: `.add(控制对象,对象具体属性,其他参数)`
**其他参数**，可以一个或多个，数据类型也可以不同，gui会自动根据参数形式，自动生成对应的交互界面。

参数3和参数4，分别是一个数字，交互界面是一个鼠标可以拖动的拖动条，可以在一个区间改变属性的值

执行`gui.add(obj,'x',0,100);`你可以发现右上角gui界面增加了新的内容，可以控制obj对象x属性的新交互界面。

**使用**

```js
// 创建dat.gui
const gui = new GUI()
const params = {
  color: 0x41a4f3,
  emissive: 0x072534,
  specular: 0x000000,
  shininess: 30,
  wireframe: false
}
gui.addColor(params, 'color').onChange((val) => {
  material.color.set(val)
})
gui.addColor(params, 'emissive').onChange((val) => {
  material.emissive.set(val)
})
gui.addColor(params, 'specular').onChange((val) => {
  material.specular.set(val)
})
gui.add(params, 'shininess', 0, 100).onChange((val) => {
  material.shininess = val
})
gui.add(params, 'wireframe').onChange((val) => {
  material.wireframe = val
})
```



![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/ceaa62fe3566297368ba3c7d16dec1de.png)



**改变GUI界面默认的style属性**

通过. domElement属性可以获取gui界面的HTML元素，那就意味着你可以改变默认的style样式，比如位置、宽度等。
```js
//改变交互界面style属性
gui.domElement.style.right = 'Opx';
gui.domElement.style.width = '300px';
```



### 4.4 辅助观察对象

#### 4.4.1 坐标系辅助对象

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/19a2a2136e3cf104d601c429b8b09430.png" style="zoom:50%;" />

```js
// 创建坐标系辅助对象
const axesHelper = new THREE.AxesHelper(10)
scene.add(axesHelper)
```



#### 4.4.2 网格辅助观察对象

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/0589b70147ea2632d8cdeefd23e4c573.png" alt="" style="zoom:50%;" />

```js
// 创建网格辅助对象
const gridHelper = new THREE.GridHelper(100, 100)
scene.add(gridHelper)
```



#### 4.4.3 灯光辅助观察对象

点光源

```js
// 添加点光源可视化对象
const helper = new THREE.PointLightHelper(light)
scene.add(helper)
```

平行光

```js
// 添加平行光可视化对象
const helper = new THREE.DirectionalLightHelper(light)
scene.add(helper)
```



### 4.5 鼠标交互

在Threejs中，可以使用RayCast获取鼠标发射射线与物体相交事件

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/1386f11abf51b9431469312834d24061.gif" style="zoom:50%;" />

```js
import * as THREE from 'three'
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js'

let camera, scene, renderer, controls, light, meshes

let rayCast = new THREE.Raycaster()
let mouse = new THREE.Vector2(1,1)

let amount = 10
let count = Math.pow(amount, 3)

let color = new THREE.Color()

initScene()
initRenderer()
initCamera()
initLight()
initControls()
addMeshs()

animate()

window.addEventListener('resize', () => {
  camera.aspect = window.innerWidth / window.innerHeight
  camera.updateProjectionMatrix()
  renderer.setSize(window.innerWidth, window.innerHeight)
})

document.addEventListener('mousemove', (event) => {
  mouse.x = (event.clientX / window.innerWidth) * 2 - 1 // -1 ~ 1
  mouse.y = -(event.clientY / window.innerHeight) * 2 + 1 // -1 ~ 1
})

function initScene() {
  scene = new THREE.Scene()
  scene.background = new THREE.Color(0x000)
}

function initRenderer() {
  renderer = new THREE.WebGLRenderer({ antialias: true })
  renderer.setSize(window.innerWidth, window.innerHeight)
  renderer.setPixelRatio(window.devicePixelRatio)
  document.body.appendChild(renderer.domElement)
}

function initCamera() {
  camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 1, 1000)
  camera.position.set(20, 20, 20)
  camera.lookAt(0, 0, 0)
}

function initLight() {
  light = new THREE.AmbientLight(0xffffff, 0.2)
  scene.add(light)
  light = new THREE.DirectionalLight(0xffffff, 1)
  light.position.set(1, 1, 1)
  scene.add(light)
}

function initControls() {
  controls = new OrbitControls(camera, renderer.domElement)
  controls.enableDamping = true
}

function addMeshs() {
  const geometry = new THREE.IcosahedronGeometry(0.5, 2) // 二十面体
  const material = new THREE.MeshPhongMaterial({ color: 0xffffff })
  meshes = new THREE.InstancedMesh(geometry, material, count)

  let index = 0
  const offset = (amount - 1) / 2
  const matrix = new THREE.Matrix4()
  for (let i = 0; i < amount; i++) {
    for (let j = 0; j < amount; j++) {
      for (let k = 0; k < amount; k++) {
        matrix.setPosition(i - offset, j - offset, k - offset)
        meshes.setMatrixAt(index, matrix)
        meshes.setColorAt(index, new THREE.Color().setHex(0xffffff))
        index++
      }
    }
  }

  scene.add(meshes)
}

function animate() {
  requestAnimationFrame(animate)
  rayCast.setFromCamera(mouse, camera)
  const intersectObject = rayCast.intersectObject(meshes)
  if (intersectObject.length > 0) {
    const { instanceId } = intersectObject[0]
    meshes.getColorAt(instanceId, color)
    if (color.equals(new THREE.Color(0xffffff))){
      color = new THREE.Color().setHex(Math.random() * 0xffffff)
      meshes.setColorAt(instanceId, color)
      meshes.instanceColor.needsUpdate = true
    }
  }
  controls.update()
  renderer.render(scene, camera)
}
```



## 5. 几何体

### 5.1 缓存类型几何体

`threejs`的长方体`BoxGeometry`、球体`SphereGeometry`等几何体都是基于`BufferGeometry`类构建的，`BufferGeometry`是一个没有任何形状的空几何体，你可以通过`BufferGeometry`自定义任何几何形状，具体一点说就是定义**顶点数据**。

1. 创建一个空的几何体对象

```js
//创建一个空的几何体对象
const geometry = new THREE.BufferGeometry();
```



**BufferAttribute定义几何体顶点数据**

2. 通过javascript类型化数组`Float32Array`创建一组xyz坐标数据用来表示几何体的顶点坐标。

```js
const vertices = Float32Array([
  0, 0, 0, // 顶点1
  50, 0, 0, // 顶点2
  0, 100, 0, // 顶点3
  0, 0, 10, // 顶点4
  0, 0, 100, // 顶点5
  50, 0, 0 // 顶点6
])
```

3. 通过threejs的属性缓冲区对象`BufferAttribute`表示`threejs`几何体顶点数据。

```js
const attribute = new THREE.BufferAttribute(vertices, 3)
```

4. 设置几何体顶点位置属性

```js
geometry.attributes.position = attribute
```



### 5.2 点模型

点模型`Points`和网格模型`Mesh`一样，都是threejs的一种模型对象，只是大部分情况下都是用`Mesh`表示物体。
网格模型`Mesh`有自己戏应的材质，同样点模型`Points`有自己对应的点材质`PointsMaterial`

```js
//点渲染模式
const material = new THREE.PointsMaterial({
	color: OxffffO0,
	size: 10.0//点对象像素尺寸
});
```

几何体`geometry`作为点模型`Points`参数，会把几何体渲染为点，把几何体作为`Mesh`的参数会把几何体渲染为面。

```js
// 点模型
const points = new THREE.Points(geometry, material)
```

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/c204bed27cb910503eeb3f7f735afc46.png" style="zoom:50%;" />



### 5.3 线模型

一条连续的线

`Line`是从第一个点开始到最后一个点，依次连线

```js
// 线材质
const material = new THREE.LineBasicMaterial({
  color: 0x0000ff
})

// 线模型
const line = new THREE.Line(geometry, material)
```

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/1d868e5256c981f51c4707d8374c6718.png" style="zoom:50%;" />

threejs还提供了`LineLoop`、`LineSegments`，区别在于绘制线条的规则不同

```js
//闭合线条
const line = new THREE.LineLoop(geometry,material);
```

```js
//非连续的线条
const line = new THREE.LineSegments (geometry，material);
```



### 5.4 网格模型

**三角面**

网格模型`Mesh`其实就一个一个三角形（面）拼接构成。使用使用网格模型`Mesh`渲染几何体`geometry`，就是几何体所有顶点坐标三个为一组，构成一个三角形，多组顶点构成多个三角形，就可以用来模拟表示物体的表面。

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/290f7a37a91a0a4564c8609b483820ee.png)

**网格模型三角形:正反面**

- 正面:逆时针
- 反面:顺时针

空间中一个三角形有正反两面，那么Three.JS的规则是如何区分正反面的？非常加单，你的眼睛(相机)对着三角形的一个面，如果三个顶点的顺序是逆时针方向，该面视为正面，如果三
个顶点的顺序是顺时针方向，该面视为反面。

**设置正反面可见**

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/4412a7ed0989414dc9029afb638db844.gif" style="zoom:50%;" />

```js
const material = new THREE.LineBasicMaterial({
  color: 0x0000ff,
  side: THREE.FrontSide // 正面可见
})
```

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/b430c1e6b94be3c5cb575321de0ec3b2.gif" style="zoom:50%;" />

```js
const material = new THREE.LineBasicMaterial({
  color: 0x0000ff,
  side: THREE.DoubleSide // 双面可见
})
```

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/55f00c8d92484eb863cdb2cd9aaaaa52.gif" style="zoom:50%;" />

```js
const material = new THREE.LineBasicMaterial({
  color: 0x0000ff,
  side: THREE.BackSide // 背面可见
})
```



### 5.5 构建矩形平面几何体

一个矩形平面，可以至少通过两个三角形拼接而成。而且两个三角形有两个顶点的坐标是重合的。

注意三角形的正反面问题:保证矩形平面两个三角形的正面是一样的，也就是从一个方向观察，两个三角形都是逆时针或顺时针。

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/764cdbc2751ccb82bcaf77cf14cf5832.png" style="zoom:50%;" />

```js
import * as THREE from 'three'

// 创建物体，BufferGeometry
const geometry = new THREE.BufferGeometry()

const vertices = new Float32Array([
  0,0,0,
  8,0,0,
  8,8,0,
  0,0,0,
  8,8,0,
  0,8,0
])

// 通过threejs的属性缓冲区对象`BufferAttribute`表示`threejs`几何体顶点数据。
const attribute = new THREE.BufferAttribute(vertices, 3)

// 设置几何体顶点位置属性
geometry.attributes.position = attribute

const material = new THREE.MeshBasicMaterial({
  color: 0x0000ff,
  side: THREE.DoubleSide // 背面可见
})

// 线模型
const mesh = new THREE.Mesh(geometry, material)

export default mesh
```



## 6. 材质

### 6.1 高光网格材质

高光网格材质`MeshPhongMaterial`和基础网格材质`MeshBasicMaterial`、漫反射网格材质`MeshLambertMaterial`—样都是网格模型的Mesh的材质。

高光网格材质`MeshPhongMaterial`和漫反射网格材质`MeshLambertMaterial`一样会受到光照的影响。



### 6.2 镜面反射和漫反射

`MeshPhongMaterial`可以提供一个镜面反射效果,可以类比你生活中拿一面镜子，放在太阳光下，调整角度，可以把太阳光反射到其它地方，如果反射光对着眼睛，也就是反射光线和视线平行的时候，会非常刺眼。
`MeshLambertMaterial`对应的Mesh受到光线照射，没有镜面反射的效果，只是一个漫反射，也就是光线向四周反射。

## 7. 灯光

**灯光**是Three.js中另一重要的组成，它通常配合支持光线反射的材质使用。这里使用的是**Lambert网格材质**

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/9823cea11830e7c3bd86527714e1b8a0.png)

### 7.1 点光源

1. 使用上面案例的场景，修改物体材质为`MeshLambertMaterial`

```js
// 创建材质
const material = new THREE.MeshLambertMaterial({
  color: 0x42a5f5,
});
```

2. 添加灯光

```js
// 创建点光源
const light = new THREE.PointLight(0xffffff, 2);
light.position.set(5, 10, 10);
scene.add(light);
```

效果

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/73a05d71332db54c9ba73acc60f8eaa6.png)

通过点光源辅助观察对象`PointLightHelper`可视化点光源

```js
// 添加点光源可视化对象
const helper = new THREE.PointLightHelper(light)
scene.add(helper)
```



![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/405a3db9c167741033b8e676efe8c7f3.png)

### 7.2 环境光

**环境光**

- 环境光`AmbientLight`没有特定方向，只是整体改变场景的光照明暗。

```js
// 创建环境光
const ambient = new THREE.AmbientLight(0xffffff, 0.5)
scene.add(ambient)
```

### 7.3 平行光

平行光DirectionalLight就是沿着特定方向发射。

```js
// 添加平行光
const directionalLight = new THREE.DirectionalLight(0xffffff, 0.1)
directionalLight.position.set(-10, 5, -10)
directionalLight.target.position.set(0, 0, 0) // 或者 directionalLight.target = cube
scene.add(directionalLight)
```



可视化平行光

```js
// 可视化平行光
const directionalLightHelper = new THREE.DirectionalLightHelper(directionalLight)
scene.add(directionalLightHelper)
```

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/99ee15492cedcee3eb41a7c911555188.png)



### 7.4 阴影

<img src="https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/4f9923a67fdceae92abe1d694df767f8.png" style="zoom:67%;" />

**要在Three.js中为物体添加阴影，需要完成以下步骤**

1. 将场景的`renderer`的`shadowMap`属性设置为`THREE.PCFSoftShadowMap`。这将启用阴影映射并使用软阴影。

```js
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;
```

2. 为想要投射阴影的光源设置`castShadow`属性。

```js
light.castShadow = true;
```

3. 为想要接收阴影的物体设置`receiveShadow`属性

```js
mesh.receiveShadow = true;
```

4. 为想要投射阴影的物体设置`castShadow`属性。

```js
mesh.castShadow = true;
```

