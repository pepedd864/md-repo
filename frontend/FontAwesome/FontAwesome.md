## 1. 安装

### 1.1 使用npm安装

安装 svg core

```bash
npm i --save @fortawesome/fontawesome-svg-core
```

安装 Icon Packages

```bash
# Free icons styles
pnpm i --save @fortawesome/free-solid-svg-icons
pnpm i --save @fortawesome/free-regular-svg-icons
pnpm i --save @fortawesome/free-brands-svg-icons
```



### 1.2 在Vue中使用

安装Vue组件

```bash
# for Vue 2.x
npm i --save @fortawesome/vue-fontawesome@latest-2

# for Vue 3.x
npm i --save @fortawesome/vue-fontawesome@latest-3
```

设置引用-vue2

```js
/* Set up using Vue 2 */
import Vue from 'vue'
import App from './App'

/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* import specific icons */
import { faUserSecret } from '@fortawesome/free-solid-svg-icons'

/* add icons to the library */
library.add(faUserSecret)

/* add font awesome icon component */
Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  components: { App },
  template: '<App/>'
})
```

设置引用-vue3

```js
/* Set up using Vue 3 */
import { createApp } from 'vue'
import App from './App.vue'

/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* import specific icons */
import { faUserSecret } from '@fortawesome/free-solid-svg-icons'

/* add icons to the library */
library.add(faUserSecret)

createApp(App)
.component('font-awesome-icon', FontAwesomeIcon)
.mount('#app')
```

调用Icon-字符串方式

```vue
<template>
  <div id="app">

    <!-- Add the style and icon you want using the String format -->
    <font-awesome-icon icon="fa-solid fa-user-secret" />

  </div>
</template>

<script>
  export default {
    name: 'App'
  }
</script>

```

调用Icon-数组方式

```vue
<template>
  <div id="app">

    <!-- Add the style and icon you want using the Array format -->
    <font-awesome-icon :icon="['fas', 'user-secret']" />

  </div>
</template>

<script>
  export default {
    name: 'App'
  }
</script>
```

