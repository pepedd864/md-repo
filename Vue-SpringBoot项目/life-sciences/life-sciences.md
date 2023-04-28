## 1. 介绍

本项目使用ruoyi-andv修改而成

## 2. 使用的工具

### 2.1 vue-echarts

### 2.2 生成pdf

思路：

1. 先将页面转换为图片
2. 然后将图片导出为pdf

安装依赖

```bash
npm install --save html2canvas  // 页面转图片
npm install jspdf --save  // 图片转pdf
```

代码

1. 新建页面

```vue
<template>
  <div ref="pdf">
    这是待转换的页面，点击
    <button @click="handleExport">导出</button> 按钮，完成导出操作。
  </div>
</template>

<script>
import { downloadPDF } from '@/utils/pdf.js' // 工具方法，导出操作
export default {
  name: 'Pdf',
  data () {
    return {}
  },
  methods: {
    handleExport () {
      downloadPDF(this.$refs.pdf)
    }
  }
}
</script>

```

2. 创建`utils/pdf.js`

```js
import html2canvas from 'html2canvas'

export const downloadPDF = page => {
  html2canvas(page).then(function (canvas) {
    page.appendChild(canvas)
  })
}

```

3. 效果

![](https://gitee.com/pepedd864/cdn-repos/raw/master/img/f41633eda61273a0d426b84fa1da6b8c.png)

4. 补全代码 

```vue
<template>
  <div ref="pdf">
    这是待转换的页面，点击
    <button @click="handleExport">导出</button> 按钮，完成导出操作。
  </div>
</template>

<script>
import { downloadPDF } from '@/utils/pdf.js' // 工具方法，导出操作
export default {
  name: 'Pdf',
  data () {
    return {}
  },
  methods: {
    handleExport () {
      downloadPDF(this.$refs.pdf)
    }
  }
}
</script>

```

```js
import html2canvas from 'html2canvas'
import jsPDF from 'jspdf'

export const downloadPDF = page => {
  html2canvas(page).then(function (canvas) {
    canvas2PDF(canvas)
  })
}

const canvas2PDF = canvas => {
  const contentWidth = canvas.width
  const contentHeight = canvas.height

  const imgHeight = contentHeight
  const imgWidth = contentWidth

  // 第一个参数： l：横向  p：纵向
  // 第二个参数：测量单位（'pt'，'mm', 'cm', 'm', 'in' or 'px'）
  const pdf = new jsPDF('l', 'pt')

  pdf.addImage(
    canvas.toDataURL('image/jpeg', 1.0),
    'JPEG',
    0,
    0,
    imgWidth,
    imgHeight
  )

  pdf.save('导出.pdf')
}

```



### 2.3 生成word



## 8. docker部署

### 8.1 使用Azure服务器[1H1G]

### 8.2 安装docker

```bash
# 首先，更新软件包索引，并且安装必要的依赖软件，来添加一个新的 HTTPS 软件源：
sudo apt update
sudo apt install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
# 使用下面的 curl 导入源仓库的 GPG key：
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
# 将 Docker APT 软件源添加到你的系统：
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
# 1. 想要安装 Docker 最新版本，运行下面的命令
sudo apt install docker-ce docker-ce-cli containerd.io
# 2. 想要安装指定版本，首先列出 Docker 软件源中所有可用的版本
apt list -a docker-ce
# 通过在软件包名后面添加版本=<VERSION>来安装指定版本：
sudo apt install docker-ce=<VERSION> docker-ce-cli=<VERSION> containerd.io
# 验证服务启动状态
sudo systemctl status docker
# 阻止 Docker 自动更新
sudo apt-mark hold docker-ce
```

### 8.3 安装所需镜像

jdk8

```bash
sudo docker pull openjdk:8
```

