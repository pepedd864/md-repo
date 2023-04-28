# flask

## 1. 快速入门

### 1.1 简介

flask是一个python语言编写的，用于快速构建后端系统的框架

### 1.2 安装

flask是一个库，使用pip就可以直接安装

```bash
python -m pip install flask
```

安装完成后，使用下面代码查看是否正确安装

```py
import flask

print(flask.__version__)
```

正确安装的话，输出结果就是flask的版本

```
2.2.3
```

### 1.3 入门案例

1. 创建文件`app.py`，编写代码

```py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "我的博客系统"
```

2. 在命令提示符中输入下面命令

```bash
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
```

3. 访问`loacalhost:5000`

### 1.4 使用网页模板

1. 创建`templates`文件夹，创建`index.html`文件，写一个简单的网页
2. 导入`render_template`，编写代码

```py
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
```

3. 访问页面

### 1.5 使用样式表等静态资源

1. 创建`static`文件夹用于存放静态资源，再创建`CSS`文件夹存放`.css`文件

2. 编写代码

```css
*{
    padding: 0;
    margin: 0;
}

h1{
    color: red;
    text-align: center;
}
```

3. 在`index.html`中这样引用css文件

```html
<link rel="stylesheet" href="{{ url_for('static',filename='css/style.css')}}">
```

4. 最后访问网站即可