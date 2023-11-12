## 1. django基础

### 1.1 安装创建项目

### 1.2 项目结构

默认的项目结构

```
- mysite
	- app，用户管理【表结构、函数、HTML模板、CSS】
	- app，订单管理【表结构、函数、HTML模板、CSS】
	- app，后台管理【表结构、函数、HTML模板、CSS】
	- app，网站   【表结构、函数、HTML模板、CSS】
	- app，API    【表结构、函数、HTML模板、CSS】
	..
	- mysite
	- ├── manage.py         【项目的管理，启动项目、创建app、数据管理】【不要动】【***常常用***】
	- └── mysite
	-     ├── __init__.py
	-     ├── settings.py    【项目配置】          【***常常修改***】
	-     ├── urls.py        【URL和函数的对应关系】【***常常修改***】
	-     ├── asgi.py        【接收网络请求】【不要动】
	-     └── wsgi.py        【接收网络请求】【不要动】
```



TODO