# vue-echarts

vue-echarts整合了echarts，使其在vue上可以通过使用组件的方式使用

[vue-echarts github](https://github.com/ecomfe/vue-echarts/blob/main/README.zh-Hans.md)

[echarts](https://echarts.apache.org/zh/index.html)

## 1. 安装和入门

npm

```bash
npm install echarts vue-echarts # 安装了 echarts 和 vue-echarts
```

使用demo，最基础的使用

```vue
<template>
  <v-echart class="chart" :option="option" autoresize></v-echart> <!--vue-echarts组件-->
</template>

<script setup>
// 导入echarts和vue-echarts的文件（按需导入）
// ------基础文件---------
import VEchart from 'vue-echarts'
import { use } from 'echarts/core'
import { CanvasRenderer } from 'echarts/renderers'
// ------可选文件---------
import { BarChart } from 'echarts/charts'	// 条形图（含坐标的图标需要导入坐标组件）
import { GridComponent } from 'echarts/components'	// 坐标组件

import { ref } from 'vue'	// vue的双向数据绑定

use([CanvasRenderer, BarChart, GridComponent])	// 使用echarts的组件

// 这里是基本的数据
const option = ref({
   // x、y坐标根据数据修改，更多说明查看 https://echarts.apache.org/zh/index.html
  xAxis: {
    data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
  },
  yAxis: {},
  series: [
    {
      name: '销量',
      type: 'bar',
      data: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    }
  ]
})

</script>

<style  scoped>
.chart {
  height: 70vh;
}
</style>

```

---

vue3全局注册组件

```js
const app = Vue.createApp(...)

// 全局注册组件（也可以使用局部注册）
app.component('v-chart', VueECharts)
```

## 2. 参数

**Prop**

- `init-options: object`

  初始化附加参数。请参考 `echarts.init` 的 `opts` 参数。[前往 →](https://echarts.apache.org/zh/api.html#echarts.init)

  Inject 键名：`INIT_OPTIONS_KEY`。

- `theme: string | object`

  要应用的主题。请参考 `echarts.init` 的 `theme` 参数。[前往 →](https://echarts.apache.org/zh/api.html#echarts.init)

  Inject 键名：`THEME_KEY`。

- `option: object`

  ECharts 的万能接口。修改这个 prop 会触发 ECharts 实例的 `setOption` 方法。查看[详情 →](https://echarts.apache.org/zh/option.html)

  > 💡 在没有指定 `update-options` 时，如果直接修改 `option` 对象而引用保持不变，`setOption` 方法调用时将默认指定 `notMerge: false`；否则，如果为 `option` 绑定一个新的引用，将指定 `notMerge: true`。

- `update-options: object`

  图表更新的配置项。请参考 `echartsInstance.setOption` 的 `opts` 参数。[前往 →](https://echarts.apache.org/zh/api.html#echartsInstance.setOption)

  Inject 键名：`UPDATE_OPTIONS_KEY`。

- `group: string`

  图表的分组，用于[联动](https://echarts.apache.org/zh/api.html#echarts.connect)。请参考 `echartsInstance.group`。[前往 →](https://echarts.apache.org/zh/api.html#echartsInstance.group)

- `autoresize: boolean`（默认值`false`）

  图表在组件根元素尺寸变化时是否需要自动进行重绘。

- `loading: boolean`（默认值：`false`）

  图表是否处于加载状态。

- `loading-options: object`

  加载动画配置项。请参考 `echartsInstance.showLoading` 的 `opts` 参数。[前往 →](https://echarts.apache.org/zh/api.html#echartsInstance.showLoading)

  Inject 键名：`LOADING_OPTIONS_KEY`。

- `manual-update: boolean`（默认值`false`）

  在性能敏感（数据量很大）的场景下，我们最好对于 `option` prop 绕过 Vue 的响应式系统。当将 `manual-update` prop 指定为 `true` 且不传入 `option` prop 时，数据将不会被监听。然后，需要用 `ref` 获取组件实例以后手动调用 `setOption` 方法来更新图表。

## 3. 事件

可以使用 Vue 的 `v-on` 指令绑定事件。

```
<template>
  <v-chart :option="option" @highlight="handleHighlight" />
</template>
```

> Note
>
> 仅支持 `.once` 修饰符，因为其它修饰符都与 DOM 事件机制强耦合。

Vue-ECharts 支持如下事件：

- `highlight` [→](https://echarts.apache.org/zh/api.html#events.highlight)
- `downplay` [→](https://echarts.apache.org/zh/api.html#events.downplay)
- `selectchanged` [→](https://echarts.apache.org/zh/api.html#events.selectchanged)
- `legendselectchanged` [→](https://echarts.apache.org/zh/api.html#events.legendselectchanged)
- `legendselected` [→](https://echarts.apache.org/zh/api.html#events.legendselected)
- `legendunselected` [→](https://echarts.apache.org/zh/api.html#events.legendunselected)
- `legendselectall` [→](https://echarts.apache.org/zh/api.html#events.legendselectall)
- `legendinverseselect` [→](https://echarts.apache.org/zh/api.html#events.legendinverseselect)
- `legendscroll` [→](https://echarts.apache.org/zh/api.html#events.legendscroll)
- `datazoom` [→](https://echarts.apache.org/zh/api.html#events.datazoom)
- `datarangeselected` [→](https://echarts.apache.org/zh/api.html#events.datarangeselected)
- `timelinechanged` [→](https://echarts.apache.org/zh/api.html#events.timelinechanged)
- `timelineplaychanged` [→](https://echarts.apache.org/zh/api.html#events.timelineplaychanged)
- `restore` [→](https://echarts.apache.org/zh/api.html#events.restore)
- `dataviewchanged` [→](https://echarts.apache.org/zh/api.html#events.dataviewchanged)
- `magictypechanged` [→](https://echarts.apache.org/zh/api.html#events.magictypechanged)
- `geoselectchanged` [→](https://echarts.apache.org/zh/api.html#events.geoselectchanged)
- `geoselected` [→](https://echarts.apache.org/zh/api.html#events.geoselected)
- `geounselected` [→](https://echarts.apache.org/zh/api.html#events.geounselected)
- `axisareaselected` [→](https://echarts.apache.org/zh/api.html#events.axisareaselected)
- `brush` [→](https://echarts.apache.org/zh/api.html#events.brush)
- `brushEnd` [→](https://echarts.apache.org/zh/api.html#events.brushEnd)
- `brushselected` [→](https://echarts.apache.org/zh/api.html#events.brushselected)
- `globalcursortaken` [→](https://echarts.apache.org/zh/api.html#events.globalcursortaken)
- `rendered` [→](https://echarts.apache.org/zh/api.html#events.rendered)
- `finished` [→](https://echarts.apache.org/zh/api.html#events.finished)
- 鼠标事件
  - `click` [→](https://echarts.apache.org/zh/api.html#events.Mouse events.click)
  - `dblclick` [→](https://echarts.apache.org/zh/api.html#events.Mouse events.dblclick)
  - `mouseover` [→](https://echarts.apache.org/zh/api.html#events.Mouse events.mouseover)
  - `mouseout` [→](https://echarts.apache.org/zh/api.html#events.Mouse events.mouseout)
  - `mousemove` [→](https://echarts.apache.org/zh/api.html#events.Mouse events.mousemove)
  - `mousedown` [→](https://echarts.apache.org/zh/api.html#events.Mouse events.mousedown)
  - `mouseup` [→](https://echarts.apache.org/zh/api.html#events.Mouse events.mouseup)
  - `globalout` [→](https://echarts.apache.org/zh/api.html#events.Mouse events.globalout)
  - `contextmenu` [→](https://echarts.apache.org/zh/api.html#events.Mouse events.contextmenu)
- ZRender 事件
  - `zr:click`
  - `zr:mousedown`
  - `zr:mouseup`
  - `zr:mousewheel`
  - `zr:dblclick`
  - `zr:contextmenu`

请参考支持的事件列表。[前往 →](https://echarts.apache.org/zh/api.html#events)

## 4. Provide/Inject

Vue-ECharts 为 `theme`、`init-options`、`update-options` 和 `loading-options` 提供了 provide/inject API，以通过上下文配置选项。例如：可以通过如下方式来使用 provide API 为 `init-options` 提供上下文配置：

```js
import { THEME_KEY } from 'vue-echarts'
import { provide } from 'vue'

// 组合式 API
provide(THEME_KEY, 'dark')

// 选项式 API
{
  provide: {
    [THEME_KEY]: 'dark'
  }
}
```

## 5. 方法

- `setOption` [→](https://echarts.apache.org/zh/api.html#echartsInstance.setOption)
- `getWidth` [→](https://echarts.apache.org/zh/api.html#echartsInstance.getWidth)
- `getHeight` [→](https://echarts.apache.org/zh/api.html#echartsInstance.getHeight)
- `getDom` [→](https://echarts.apache.org/zh/api.html#echartsInstance.getDom)
- `getOption` [→](https://echarts.apache.org/zh/api.html#echartsInstance.getOption)
- `resize` [→](https://echarts.apache.org/zh/api.html#echartsInstance.resize)
- `dispatchAction` [→](https://echarts.apache.org/zh/api.html#echartsInstance.dispatchAction)
- `convertToPixel` [→](https://echarts.apache.org/zh/api.html#echartsInstance.convertToPixel)
- `convertFromPixel` [→](https://echarts.apache.org/zh/api.html#echartsInstance.convertFromPixel)
- `containPixel` [→](https://echarts.apache.org/zh/api.html#echartsInstance.containPixel)
- `showLoading` [→](https://echarts.apache.org/zh/api.html#echartsInstance.showLoading)
- `hideLoading` [→](https://echarts.apache.org/zh/api.html#echartsInstance.hideLoading)
- `getDataURL` [→](https://echarts.apache.org/zh/api.html#echartsInstance.getDataURL)
- `getConnectedDataURL` [→](https://echarts.apache.org/zh/api.html#echartsInstance.getConnectedDataURL)
- `clear` [→](https://echarts.apache.org/zh/api.html#echartsInstance.clear)
- `dispose` [→](https://echarts.apache.org/zh/api.html#echartsInstance.dispose)

**静态方法**

静态方法请直接通过 [`echarts` 本身](https://echarts.apache.org/zh/api.html#echarts)进行调用。
