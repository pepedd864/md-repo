## 1. 创建项目

在`easybbs`文件夹下运行`npm init vite@latest easybbs-front-web`命令

按照下面顺序选择

1、vue
2、Customize with create-vue
3、Add TypeScript? » No / Yes NO
4、Add JSX Support? » No / Yes NO
5、Add Vue Router for Single Page Application development? » No / Yes Yes
6、 Add Pinia for state management? » No / Yes No
7、Add Vitest for Unit Testing? » No / Yes No
8、Add an End-to-End Testing Solution? » - Use arrow-keys. Return to submit. No
9、 Add ESLint for code quality? » No / Yes Yes

**安装依赖**

- kangc/v-md-editor markdown编辑器
- axios
- element-plus
- highlight.js
- sass-loader
-  vue-cookies
- vuex

```bash
npm install @kangc/v-md-editor@next @wangeditor/editor @wangeditor/editor-for-vue@next axios element-plus highlight.js js-md5 sass sass-loader vue-cookies vuex --save
```

**配置main.js**

```js
//引入cookies
import VueCookies from 'vue-cookies'
//引入element plus
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
//我们使用sass 所以这里将base.css 改成base.scss
import '@/assets/base.scss'
//图标 图标在附件中
import '@/assets/icon/iconfont.css'

const app = createApp(App)

app.use(router)
app.use(ElementPlus);
app.config.globalProperties.VueCookies = VueCookies;


app.mount('#app')
```

