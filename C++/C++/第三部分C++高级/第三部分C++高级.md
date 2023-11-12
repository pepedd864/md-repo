

[TOC]

# 第三部分:C++高级

## 一. 模板

### 1. 模板的概念

模板就是建立通用的模具，大大提高复用性

### 2. 函数模板

- C++另一种编程思想称为**泛型编程**，主要利用的技术就是**模板**
- C++提供两种模板机制:**函数模板**和**类模板**

#### 2.1 函数模板语法

**函数模板作用:**
建立一个通用函数，其函数返回值类型和形参类型可以不具体制定，用一个**虚拟的类型**来代表。

**语法:**

```c++
template<typename T>    //typename可以替换为class
函数声明或定义
```

**解释:**
`template` ---声明创建模板
`typename` ---表面其后面的符号是一种数据类型,可以用class代替
`T `---通用的数据类型,名称可以替换,通常为大写字母

**代码演示:**

```c++
//函数模板
template<typename T>
void swap(T &a,T &b)
{
    T temp = a;
    a = b;
    b = temp;
}
int main()
{
    int a = 10;
    int b = 20;
    //使用函数模板,,两种方法
    //1. 自动类型推导
    swap(a,b);
    //2. 显示指定类型
    swap<int>(a,b);
}
```

#### 2.2 函数模板注意事项

**注意事项:**

- 自动类型推导,必须推导出一致的数据类型T,才可以使用
- 模板必须要确定出T的数据类型,才可以使用

**代码演示:**

```c++
//自动类型推导,必须推导出一致的数据类型T,才可以使用
template<typename T>
void swap(T&a,T&b)
{
    T temp = a;
    a = b;
    b = temp;
}
int main()
{
    int a = 10;
    int b = 20;
    char c ='c';
    swap(a,b);//正确,类型匹配
    swap(a,c);//错误,,类型不匹配
    return 0;
}
```

```c++
template<typename T>
void func()
{
    cout<<"函数调用成功"<<endl;
}
int main()
{
    func<int>();    //指定了T的数据类型
    return 0;
}
```

#### 2.3 函数模板案例

**案例描述:**

- 利用函数模板封装一个排序的函数,可以对不同数据类型数组进行排序
- 排序规则从大到小,排序算法为选择排序
- 分别利用char数组和int数组进行测试

**实现代码:**

```c++
//使用模板函数
//交换函数
template<typename T>
void mySwap(T& a, T& b)
{
    T temp = a;
    a = b;
    b = temp;
}
//排序算法
template<typename T>
void mySort(T arr[], int len)
{
    for (int i = 0; i < len; i++)
    {
        int max = i;//认定最大值的下标
        for (int j = i + 1; j < len; j++)
        {
            //认定的最大值 比 遍历出的数组要下,说明j下标的元素才是真正的最大值
            if (arr[max] < arr[j])
            {
                max = j;//更新最大值下标
            }
        }
        if (max != i)
        {
            //交换max和i元素
            mySwap(arr[max], arr[i]);
        }
    }
}
//打印数组函数
template<typename T>
void printArray(T arr[], int len)
{
    //此处输出数组类型,使用<typeinfo>库
    cout << typeid(*arr).name() << "类型数组:\t" << endl;;
    for (int i = 0; i < len; i++)
    {
        cout << arr[i] << "\t";
    }
    cout << endl;
}
int main()
{
    char charArr[] = "badcfe";
    int intArr[] = { 2,23,41,3,45,2,1,344,2 };
    //交换char类型数组
    int num = sizeof(charArr) / sizeof(char);
    mySort(charArr, num);
    mySort(intArr, num);
    printArray(charArr, num);
    printArray(intArr, num);
    return 0;
}
```

```
输出结果:
char类型数组:
f       e       d       c       b       a
int类型数组:
45      41      23      3       2       2       1
```

#### 2.4 普通函数与函数模板的区别

**普通函数与函数模板区别:**

- **普通函数**调用时可以发生自动类型转换(**隐式类型转换->即编译器自动转换类型**)
- **函数模板**调用时,如果利用自动类型推导,**不会发生隐式类型转换**
- 如果利用**显示指定类型**的方式,**可以发生隐式类型转换**

#### 2.5 普通函数与函数模板的调用规则

**调用规则如下:**

1. 如果函数模板和普通函数都可以实现,**优先调用普通函数**
2. 可以通过**空模板参数列表**来**强制调用函数模板**
3. **函数模板**也可以发生**重载**
4. 如果**函数模板可以产生更好的匹配,优先调用函数模板**

**代码演示:**

```c++
//如果函数模板和普通函数都可以实现,优先调用普通函数
void func(int a ,int b)
{
    cout<<"调用普通函数"<<endl;
}
template<typename T>
void func(T a ,T b)
{
    cout<<"调用模板函数"<<endl;
}
int main()
{
    int a = 10;
    int b = 20;
    func(a,b);
    return 0;
}
```

```
输出结果:
调用普通函数
```

```c++
//通过空模板参数列表,强制调用函数模板
void func(int a ,int b)
{
    cout<<"调用普通函数"<<endl;
}
template<typename T>
void func(T a ,T b)
{
    cout<<"调用函数模板"<<endl;
}
int main()
{
    int a = 10;
    int b = 20;
    func<>(a,b);//通过空模板参数列表,强制调用函数模板
    return 0;
}
```

```c++
输出结果:
调用函数模板
```

```c++
//函数模板也可以发生重载
template<typename T>
void func(T a, T b)
{
    cout << "调用函数模板" << endl;
}
//函数模板重载
template<typename T>
void func(T a, T b,T c)
{
    cout << "调用重载函数模板" << endl;
}
int main()
{
    int a = 10;
    int b = 20;
    int c = 30;
    func(a, c);//传入参数为2个
    func(a,b,c);//传入参数为3个
    return 0;
}
```

```
输出结果:
调用函数模板
调用重载函数模板
```

```c++
//如果函数模板可以产生更好的匹配,优先调用函数模板
void func(int a ,int b)
{
    cout<<"调用普通函数"<<endl;
}
template<typename T>
void func(T a ,T b)
{
    cout<<"调用函数模板"<<endl;
}
int main()
{
    char a = 'a';
    char b = 'a';
       func(a,b);
    return 0;
}
```

```
输出结果:
调用函数模板
```

#### 2.6 模板的局限性

**局限性:**

不能实现所有类型的通用,对于特定类型,需要用具体化方式做特殊实现

**处理方法:**

1. 自定义类型操作符(`operator+ `等等)
2. 用普通函数重载写实现

**注意:**自定义操作符实现的通用性更高,但是更麻烦,根据实际需求使用

**代码演示:**

```c++
//函数模板对自定义类型的处理
class Person
{
public:
    string name;
    int age;
    Person(string _name, int _age) :name(_name), age(_age)
    {
    }
};
template<typename T>
bool myCompare(T a, T b)
{
    if (a == b)
    {
        return true;
    }
    else
    {
        return false;
    }
}
//其实就是普通函数重载
bool myCompare(Person& p1, Person& p2)
{
    if (p1.name == p2.name && p1.age == p2.age)
    {
        return true;
    }
    else
    {
        return false;
    }
}

int main()
{
    int a = 10;
    int b = 10;
    Person p1("Tom", 10);
    Person p2("Tom", 10);
    //常见数据类型
    bool ret_1 = myCompare(a, b);
    //自定义数据类型
    bool ret_2 = myCompare(p1, p2);
    if (ret_1)
    {
        cout << typeid(a).name() << ":a == " << typeid(b).name() << ":b" << endl;
    }
    else
    {
        cout << typeid(a).name() << ":a != " << typeid(b).name() << ":b" << endl;
    }
    if (ret_2)
    {
        cout << typeid(p1).name() << ":p1 == " << typeid(p2).name() << ":p2" << endl;
    }
    else
    {
        cout << typeid(p1).name() << ":p1 != " << typeid(p2).name() << ":p2" << endl;
    }
    return 0;
}
```

```
输出结果:
int:a == int:b
class Person:p1 == class Person:p2
```

### 3. 类模板

#### 3.1类模板语法

**类模板作用:**
建立一个**通用类**,类中的成员数据类型可以不具体制定,用一个**虚拟的类型**来代表。

**语法:**

```c++
template<class T>
//以下为类定义
```

**代码演示:**

```c++
//定义类模板
template<class NameType,class AgeType>
class Person
{
public:
    NameType name;
    AgeType age;
    Person(NameType _name,AgeType _age):name(_name),age(_age)
    {
    }
    void show()
    {
        cout<<"name:\t"<<this->name<<endl;
        cout<<"age:\t"<<this->age<<endl;
    }
};
int main()
{
    //使用类模板
    Person<string,int>p1("Tom",10);
    Person.show();
    return 0;
}
```

```
输出结果:
name:   Tom
age:    10
```

#### 3.2 类模板与函数模板区别

**类模板与函数模板区别主要有两点:**

1. 类模板没有自动类型推导的使用方式

2. 类模板在模板参数列表中可以有默认参数

#### 3.3 类模板中成员函数创建时机

#### 3.4 类模板对象做函数参数

#### 3.5 类模板与继承

#### 3.6 类模板成员函数类外实现

#### 3.7 类模板分文件编写

#### 3.8 类模板与友元

## 二.STL

### 1. STL的诞生

- 长久以来，软件界一直希望建立一种可重复利用的东西
- C++的**面向对象**和**泛型编程**思想，目的就是**复用性的提升**
- 大多情况下，数据结构和算法都未能有一套标准,导致被迫从事大量重复工作
- 为了建立数据结构和算法的一套标准,诞生了**STL**

### 2. STL基本概念

- STL(Standard Template Library,**标准模板库**)
- STL从广义上分为:**容器(container)算法(algorithm)迭代器(iterator)**
- **容器**和**算法**之间通过**迭代器**进行无缝连接。
- STL几乎所有的代码都采用了模板类或者模板函数

#### 2.1 STL六大组件

STL大体分为六大组件,分别是:**容器**、**算法**、**迭代器**、**仿函数**、**适配器(配接器)**、**空间配置器**

1. **容器:**各种数据结构,如`vector`、`list`、`deque`、`set`、`map`等,用来存放数据.
2. **算法:**各种常用的算法,如`sort`、`find`、`copy`、`for_each`等
3. **迭代器:**扮演了容器与算法之间的胶合剂.
4. **仿函数:**行为类似函数,可作为算法的某种策略.
5. **适配器:**一种用来修饰容器或者仿函数或迭代器接口的东西.
6. **空间配置器:**负责空间的配置与管理.

##### 2.1.2 STL中容器、算法、迭代器

**容器:**
**STL容器**就是将运用**最广泛的一些数据结构**实现出来.
常用的数据结构:数组,链表,树,栈,队列,集合,映射表等.
这些容器分为**序列式容器**和**关联式容器**两种:
    **序列式容器:**强调值的排序，序列式容器中的每个元素均有固定的位置.
    **关联式容器:**二叉树结构，各元素之间没有严格的物理上的顺序关系.

**算法:**
有限的步骤,解决逻辑或数学上的问题,这一门学科我们叫做算法(Algorithms)
算法分为:**质变算法**和**非质变算法**.
**质变算法:**是指运算过程中会更改区间内的元素的内容。例如拷贝，替换，删除等等
**非质变算法:**是指运算过程中不会更改区间内的元素内容，例如查找、计数、遍历、寻找极值等等

**迭代器:**
提供一种方法,使之能够依序寻访某个容器所含的各个元素,而又无需暴露该容器的内部表示方式.每个容器都有自己专属的迭代器
迭代器使用非常类拟于指针，初学阶段我们可以先理解迭代器为指针

**迭代器种类:**

| 种类         | 功能                                                     | 支持运算                                |
| ------------ | -------------------------------------------------------- | --------------------------------------- |
| 输入迭代器   | 对数据的只读访问                                         | 只读，支持++、==、! =                   |
| 输出迭代器   | 对数据的只写访问                                         | 只写，支持++                            |
| 前向迭代器   | 读写操作，并能向前推进迭代器                             | 读写，支持++、==、!=                    |
| 双向迭代器   | 读写操作，并能向前和向后操作                             | 读写，支持++、--，                      |
| 随机访问迭器 | 读写操作，可以以跳跃的方式访问任意数据，功能最强的迭代器 | 读写，支持++、--、[n]、-n、<、<=、>、>= |

常用的容器中迭代器种类为双向迭代器,和随机访问迭代器

##### 2.1.3. 容器算法迭代器初识

###### 2.1.3.1 vector存放内置数据类型

容器:`vector`
算法:`for_each`
迭代器:`vector<int>::iterator`

**代码演示:**

```c++
void myPrint(int val)
{
    cout<<val<<endl;
}
//创建vector容器,数组
vector<int> v;
//向容器中加入数据
v.push_back(10);
v.push_back(20);
v.push_back(40);
v.push_back(30);
//通过迭代器访问容器中的数据
vector<int>::iterator itBegin = v.begin();//起始迭代器
vector<int>::iterator itEnd = v.end();//结束迭代器
//常规遍历方法
while(itBegin != itEnd)
{
    cout<<*itBegin<<endl;
    itBegin++;
}
//使用 for_each
for_each(v.begin(),v.end(),myPrint);
```

###### 2.1.3.2 vector存放自定义数据类型

**代码演示:**

```c++
//vector存放自定义数据类型
class Person
{
public:
    string name;
    int age;
    Person(string _name, int _age) :name(_name), age(_age)
    {

    }
};
int main()
{
    vector<Person> v;
    Person p1("Tom", 10);
    Person p2("Tom", 20);
    Person p3("Tom", 30);
    Person p4("Tom", 50);
    Person p5("Tom", 40);

    v.push_back(p1);
    v.push_back(p2);
    v.push_back(p3);
    v.push_back(p4);
    v.push_back(p5);

    for (auto x : v)
    {
        cout << x.name << endl;
        cout << x.age << endl;
    }
    return 0;
}
```

```
输出结果:
Tom
10
Tom
20
Tom
30
Tom
50
Tom
40
```

###### 2.1.3.3 vector容器嵌套容器

**代码演示:**

```c++
vector<vector<int>>v;
vector<int>v1;
vector<int>v2;
vector<int>v3;
vector<int>v4;
//在小容器中添加数据
for (int i = 0; i < 4; i++)
{
    v1.push_back(i + 1);
    v2.push_back(i + 2);
    v3.push_back(i + 3);
    v4.push_back(i + 4);
}
//将小容器添加进大容器
v.push_back(v1);
v.push_back(v2);
v.push_back(v3);
v.push_back(v4);
//通过大容器遍历所有数据
for (auto x1 : v)
{
    for (auto x2 : x1)
    {
        cout << x2 << "\t";
    }
    cout << endl;
}
```

```
输出结果:
1       2       3       4
2       3       4       5
3       4       5       6
4       5       6       7
```

### 3. STL-常用容器

#### 3.1 string容器

##### 3.1.1 string基本概念

**本质:**
`string`是C++风格的字符串，而`string`本质上是一个类.

**string和char*区别:**

- `char*`是一个指针

- `string`是一个类，类内部封装了`char* `,管理这个字符串，是一个`char*`型的容器.

**特点:**
`string`类内部封装了很多成员方法.
例如:查找`find`，拷贝`copy`，删除`delete`替换`replace`，插入`insert`
`string`管理`char*`所分配的内存，不用担心复制越界和取值越界等，由类内部进行负责.

##### 3.1.2 string构造函数

**构造函数原型:**

| 函数                         | 描述                                         |
| ---------------------------- | -------------------------------------------- |
| `string()`                   | 创建一个空的字符串例如: `string str;`        |
| `string( const char* s )`    | 使用字符串`s`初始化                          |
| `string(const string& str);` | 使用一个`string`对象初始化另一个`string`对象 |
| `string(int n, char c);`     | 使用`n`个字符`c`初始化                       |

##### 3.1.3 string赋值操作

**赋值函数原型:**

| 函数                                    | 描述                                  |
| --------------------------------------- | ------------------------------------- |
| `string& operator=(const char* s );`    | char*类型字符串赋值给当前的字符串.    |
| `string& operator=(const string &s );`  | 把字符串s赋给当前的字符串.            |
| `string& operator=(char c);`            | 字符赋值给当前的字符串.               |
| `string& assign(const char *s);`        | 把字符串s赋给当前的字符串.            |
| `string& assign(const char *s，int n);` | 把字符串s的前n个字符赋给当前的字符串. |
| `string& assign(const string &s);`      | 把字符串s赋给当前字符串.              |
| `string& assign(int n, char c);`        | 用n个字符c赋给当前字符串.             |

##### 3.1.4 string字符串拼接

**函数原型:**

| 函数                                               | 描述                                         |
| -------------------------------------------------- | -------------------------------------------- |
| `string& operator+=(const char* str);`             | 重载+=操作符.                                |
| `string& operator+=(const char c);`                | 重载+=操作符.                                |
| `string& operator+=(const string& str);`           | 重载+=操作符.                                |
| `string& append(const char *s);`                   | 把字符串s连接到当前字符串结尾.               |
| `string& append(const char *s， int n);`           | 把字符串s的前n个字符连接到当前字符串结尾.    |
| `string& append(const string &s );`                | 同`operator+=(const string& str).`           |
| `string& append(const string &s，int pos，int n);` | 字符串s中从pos开始的n个字符连接到字符串结尾. |

##### 3.1.5 string查找和替换

**函数原型:**

| 函数                                                  | 描述                                |
| ----------------------------------------------------- | ----------------------------------- |
| `int find(const string& str, int pos = 0) const;`     | 查找str第一次出现位置,从pos开始查找 |
| `int find(const char* s, int pos = 0) const;`         | 查找s第一次出现位置,从pos开始查找   |
| `int find(const char* s, int pos, int n) const;`      | 从pos位置查找s的前n个字符第一次位置 |
| `int find(const char c, int pos = 0) const;`          | 查找字符c第一次出现位置             |
| `int rfind(const string& str, int pos = npos) const;` | 查找str最后一次位置,从pos开始查找   |
| `int rfind(const char* s, int pos = npos ) const;`    | 查找s最后一次出现位置,从pos开始查找 |
| `int rfind(const char* s, int pos，int n) const;`     | 查找s最后一次出现位置,从pos开始查找 |
| `int rfind(const char* s, int pos，int n) const;`     | 从pos查找s的前n个字符最后一次位置   |
| `string& replace(int pos,int n,const string& str);`   | 替换从pos开始n个字符为字符串str     |
| `string& replace(int pos,int n,const char* s);`       | 替换从pos开始的n个字符为字符串      |

##### 3.1.6 string字符串比较

**函数原型:**

| 函数                                  | 描述          |
| ------------------------------------- | ------------- |
| `int compare(const string &s) const;` | 与字符串s比较 |
| `int compare(const char *s) const;`   | 与字符串s比较 |

**返回值:**

- `return 0;`两字符串相等

- `return 1;`第一个字符串ASCII码和大于第二个字符串

- `return -1;`第一个字符串ASCII码和小于第二个字符串

##### 3.1.7 string字符存取

**函数原型:**

| 函数                       | 描述               |
| -------------------------- | ------------------ |
| `char& operator[](int n);` | 通过[]方式取字符   |
| `char& at(int n);`         | 通过at方法获取字符 |

##### 3.1.8 string插入和删除

**函数原型:**

| 函数                                         | 描述                   |
| -------------------------------------------- | ---------------------- |
| `string& insert(int pos，const char* s);`    | 插入字符串             |
| `string& insert(int pos,const string& str);` | 插入字符串             |
| `string& insert(int pos, int n,char c);`     | 在指定位置插入n个字符c |
| `string& erase(int pos, int n = npos);`      | 删除从Pos开始的n个字符 |

##### 3.1.9 string子串

**函数原型:**

| 函数                                              | 描述                               |
| ------------------------------------------------- | ---------------------------------- |
| `string substr(int pos = 0, int n = npos) const;` | 返回由pos开始的n个字符组成的字符串 |

#### 3.2 vector容器

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/89ad8bf3c8a8ffafe2605bb45530591c.png)



##### 3.2.1 vector基本概念

**功能:**

- `vector`数据结构和**数组非常相似**,也称为**单端数组**.

**vector与普通数组区别:**

- 不同之处在于数组是静态空间,而`vector`可以**动态扩展.**

**动态扩展:**

- 并不是在原空间之后续接新空间,而是找更大的内存空间,然后将原数据拷贝新空间，释放原空间.

- `vector`容器的迭代器是支持随机访问的迭代器.

##### 3.2.2 vector构造函数

**函数原型:**

| 函数                         | 描述                                      |
| ---------------------------- | ----------------------------------------- |
| `vector<T> v;`               | 采用模板实现类实现,默认构造函数           |
| `vector(v.begin(),v.end());` | 将v[begin(), end())区间中的元素拷贝给本身 |
| `vector(n，elem);`           | 构造函数将n个elem拷贝给本身               |
| `vector(const vector &vec);` | 拷贝构造函数                              |

##### 3.2.3 vector赋值操作

**函数原型:**

| 函数                                    | 描述                                   |
| --------------------------------------- | -------------------------------------- |
| `vector& operator=(const vector &vec);` | 重载等号操作符                         |
| `assign(beg, end);`                     | 将[beg, end)区间中的数据拷贝赋值给本身 |
| `assign(n,elem);`                       | 将n个elem拷贝赋值给本身                |

##### 3.2.4 vector容量和大小

**函数原型:**

| 函数                     | 描述                                                         |
| ------------------------ | ------------------------------------------------------------ |
| `empty();`               | 判断容器是否为空                                             |
| `capacity();`            | 容器的容量                                                   |
| `size();`                | 返回容器中元素的个数                                         |
| `resize(int num);`       | 重新指定容器的长度为num,若容器变长,则以默认值填充新位置.如果容器变短,则末尾超出容器长度的元素被删除 |
| `resize(int num，elem);` | 重新指定容器的长度为num,若容器变长,则以elem值填充新位置.如果容器变短,则末尾超出容器长度的元素被删除 |

##### 3.2.5 vector插入和删除

**函数原型:**

| 函数                                               | 描述                                |
| -------------------------------------------------- | ----------------------------------- |
| `push_back(ele);`                                  | 尾部插入元素ele                     |
| `pop_back();`                                      | 删除最后一个元素                    |
| `insert(const_iterator pos，ele);`                 | 迭代器指向位置pos插入元素ele        |
| `insert(const_iterator pos, int count,ele);`       | 迭代器指向位置pos插入count个元素ele |
| `erase(const_iterator pos);`                       | 删除迭代器指向的元素                |
| `erase(const_iterator start，const_iterator end);` | 删除迭代器从start到end之间的元素    |
| `clear();`                                         | 删除容器中所有元素                  |

##### 3.2.6 vector数据存取

**函数原型:**

| 函数             | 描述                       |
| ---------------- | -------------------------- |
| `at(int idx);`   | 返回索引idx所指的数据      |
| `operator[idx];` | 返回索引idx所指的数据      |
| `front();`       | 返回容器中第一个数据元素   |
| `back();`        | 返回容器中最后一个数据元素 |

##### 3.2.7 vector互换容器

**函数原型:**

| 函数         | 描述                  |
| ------------ | --------------------- |
| `swap(vec);` | 将vec与本身的元素互换 |

**作用:**

- 巧用swap可以收缩内存空间.

**代码演示:**

```c++
vector<int>v1;
for (int i = 0; i < 10000; i++)v1.push_back(i);
//初始
cout << "初始:" << endl;
cout << "v1的容量:\t" << v1.capacity() << endl;
cout << "v1的大小:\t" << v1.size() << endl;
//重新设置v1的大小
v1.resize(3);

cout << endl << "重新设置v1的大小:" << endl;
cout << "v1的容量:\t" << v1.capacity() << endl;
cout << "v1的大小:\t" << v1.size() << endl;
//使用swap缩小v1的容量
vector<int>(v1).swap(v1);    //创建匿名对象(vector<int>(v1)),在交换后被系统回收
cout << endl << "使用swap缩小v1的容量:" << endl;
cout << "v1的容量:\t" << v1.capacity() << endl;
cout << "v1的大小:\t" << v1.size() << endl;
```

```
输出结果:
初始:
v1的容量:       12138
v1的大小:       10000

重新设置v1的大小:
v1的容量:       12138
v1的大小:       3

使用swap缩小v1的容量:
v1的容量:       3
v1的大小:       3
```

##### 3.2.8 vector预留空间

**函数原型:**

| 函数                | 描述                                                |
| ------------------- | --------------------------------------------------- |
| `reserve(int len);` | 容器预留len个元素长度,预留位置不初始化,元素不可访问 |

**作用:**

- 预留空间,减少编译器重新寻找空间的次数.

**代码演示:**

```c++
vector<int>v;
int num = 0;//统计开辟次数
int* p = NULL;
for (int i = 0; i < 10000; i++)
{
    v.push_back(i);
    if (p != &v[0])
    {
        p = &v[0];
        num++;
    }
}
cout << "未使用reserve时:" << endl;
cout << "num =\t" << num << endl;
v.clear();
v.reserve(10000);
num = 0;
p = NULL;
for (int i = 0; i < 10000; i++)
{
    v.push_back(i);
    if (p != &v[0])
    {
        p = &v[0];
        num++;
    }
}
cout << endl << "使用reserve时:" << endl;
cout << "num =\t" << num << endl;
```

```
输出结果:
未使用reserve时:
num =   24

使用reserve时:
num =   1
```

#### 3.3 deque容器

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/fa6b4e7cb70e6f18bc9c14340c4fed19.png)

##### 3.3.1 deque容器基本概念

**功能:**

- 双端数组,可以对头端进行插入删除操作.

**deque与vector区别:**

- `vector`对于头部的插入删除效率低,数据量越大，效率越低.
- `deque`相对而言，对头部的插入删除速度回比`vector`快.
- `vector`访问元素时的速度会比`deque`快,这和两者内部实现有关.

**deque内部工作原理:**

- `deque`内部有个中控器,维护每段缓冲区中的内容,缓冲区中存放真实数据.
- 中控器维护的是每个缓冲区的地址,使得使用`deque`时像一片连续的内存空间.

**deque容器的迭代器也是支持随机访问的**

##### 3.3.2 deque构造函数

**函数原型:**

| 函数                       | 描述                                       |
| -------------------------- | ------------------------------------------ |
| `deque<T> deqT;`           | 默认构造形式.`                             |
| `deque(beg,end);`          | 构造函数将[beg,end)区间中的元素拷贝给本身. |
| `deque(n，elem);`          | 构造函数将n个elem拷贝给本身.               |
| `deque(const deque &deq);` | 拷贝构造函数.                              |

##### 3.3.3 deque赋值操作

**函数原型:**

| 函数                                  | 描述                                    |
| ------------------------------------- | --------------------------------------- |
| `deque&Toperator=(const deque &deq);` | 重载等号操作符                          |
| `assign(beg, end);`                   | 将[beg, end)区间中的数据拷贝赋值给本身. |
| `assign(n, elem);`                    | 将n个elem拷贝赋值给本身.                |

##### 3.3.4 deque大小操作

**函数原型:**

| 函数                       | 描述                                                         |
| -------------------------- | ------------------------------------------------------------ |
| `deque.empty();`           | 判断容器是否为空.                                            |
| `deque.size();`            | 返回容器中元素的个数.                                        |
| `deque.resize(num);`       | 重新指定容器的长度为num,若容器变长,则以默认值填充新位置.如果容器变短,则末尾超出容器长度的元素被删除. |
| `deque.resize(num，elem);` | 重新指定容器的长度为num,若容器变长,则以elem值填充新位置.如果容器变短,则末尾超出容器长度的元素被删除. |

##### 3.3.5 deque插入和删除

**函数原型:**

**两端插入操作:**

| 函数                | 描述                   |
| ------------------- | ---------------------- |
| `push_back(elem);`  | 在容器尾部添加一个数据 |
| `push_front(elem);` | 在容器头部插入一个数据 |
| `pop_back();`       | 删除容器最后一个数据   |
| `pop_front();`      | 删除容器第一个数据     |

**指定位置操作:**

| 函数                   | 描述                                             |
| ---------------------- | ------------------------------------------------ |
| `insert(pos,elem);`    | 在pos位置插入一个elem元素的拷贝,返回新数据的位置 |
| `insert(pos,n,elem);`  | 在pos位置插入n个elem数据,无返回值                |
| `insert(pos,beg,end);` | 在pos位置插入[beg,end)区间的数据,无返回值        |
| `clear();`             | 清空容器的所有数据                               |
| `erase(beg, end);`     | 删除[beg,end)区间的数据，返回下一个数据的位置    |
| `erase(pos);`          | 删除pos位置的数据,返回下一个数据的位置           |

##### 3.3.6 deque数据存取

**函数原型:**

| 函数             | 描述                       |
| ---------------- | -------------------------- |
| `at(int idx);`   | 返回索引idx所指的数据      |
| `operator[idx];` | 返回索引idx所指的数据      |
| `front();`       | 返回容器中第一个数据元素   |
| `back();`        | 返回容器中最后一个数据元素 |

##### 3.3.7 deque排序

**算法:**

- `sort(iterator beg,iterator end)//对beg和end区间内元素进行排序`

**代码演示:**

```c++
deque<int>d;
d.push_back(10);
d.push_back(30);
d.push_front(40);
d.push_back(24);
d.push_front(43);
//打印排序前
cout << "排序前:" << endl;;
for (auto x : d)
{
    cout << x << "\t";
}
//排序
sort(d.begin(), d.end());
//打印排序后
cout << endl << "排序后:" << endl;
for (auto x : d)
{
    cout << x << "\t";
}
```

```
输出结果:
排序前:
43      40      10      30      24
排序后:
10      24      30      40      43
```

#### 3.4 STL案例-评委打分

**案例描述:**

有5名选手:选手ABCDE,10个评委分别对每一名选手打分,去除最高分,去除评委中最低分,取平均分.

**实现步骤:**

1. 创建五名选手,放到`vector`中.
2. 遍历`vector`容器,取出来每一个选手,执行for循环,可以把10个评分打分存到`deque`容器中.
3. `sort`算法对`deque`容器中分数排序，去除最高和最低分.
4. `deque`容器遍历一遍，累加总分.
5. 获取平均分.

**实现代码:**

```c++
class Person
{
public:
    string name;
    int score;
    Person(string _name, int _score) :name(_name), score(_score)
    {

    }

};
void createPerson(vector<Person>& v)
{
    string nameSeed = "ABCDE";
    for (int i = 0; i < 5; i++)
    {
        string name = "选手";
        name += nameSeed[i];
        int score = 0;
        Person p(name, score);
        v.push_back(p);
    }
}
void setScore(vector<Person>& v)
{
    srand(time(0));//随机数种子
    for (vector<Person>::iterator x=v.begin(); x != v.end(); x++)
    {
        //用deque容器存储打分
        deque<int>d;
        for (int i = 0; i<10; i++)
        {
            int score = rand() % 41 + 60;
            d.push_back(score);
        }

        //排序
        sort(d.begin(), d.end());
        //除去最高分,除去最低分
        d.pop_back();
        d.pop_front();

        //取平均分
        int sum = 0;
        for (auto y : d)
        {
            sum += y;
        }
        int avg = sum / d.size();
        x->score = avg;
    }
}
int main()
{
    //创建存放容器
    vector<Person>v;
    createPerson(v);
    setScore(v);
    //输出
    for (auto x : v)
    {
        cout << "姓名:\t" << x.name << "\t" << "分数:\t" << x.score << endl;
    }
    return 0;
}
```

```
输出结果:
姓名:   选手A   分数:   78
姓名:   选手B   分数:   82
姓名:   选手C   分数:   74
姓名:   选手D   分数:   80
姓名:   选手E   分数:   77
```

#### 3.5 stack容器

##### 3.5.1 stack基本概念

**概念:** `stack`是一种**先进后出**(First In Last Out,FILO)的数据结构,它只有一个出口

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/be6a20bb55b5b79bfbe2255244b084b4.png)

**栈中只有顶端的元素才可以被外界使用，因此栈不允许有遍历行为**

栈中进入数据称为---**入栈**`push`
栈中弹出数据称为---**出栈**`pop`

##### 3.5.2 stack常用接口

**构造函数:**

- `stack<T> stk;//stack采用模板类实现, stack对象的默认构造形式.`
- `stack(const stack &stk); //拷贝构造函数.`

**赋值操作:**

- `stack& operator=(const stack &stk) ;//重载等号操作符.`

**数据存取:**

- `push(elem);//向栈顶添加元素.`
- `pop();//从栈顶移除第一个元素.`
- `top();//返回栈顶元素.`

**大小操作:**

- `empty();//判断堆栈是否为空.`
- `size();//返回栈的大小.`

#### 3.6 queue容器

##### 3.6.1 queue基本概念

**概念:**`queue`是一种**先进先出**(First ln First Out,FIFO)的数据结构，它有两个出口

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/785e5f2f92cde5327168d1d2cc408298.png)

##### 3.6.2 queue常用接口

**构造函数:**

- `queue<T> que;//queue采用模板类实现，queue对象的默认构造形式.`
- `queue(const queue &que);//拷贝构造函数.`

**赋值操作:**

- `queue& operator=(const queue &que);//重载等号操作符.`

**数据存取:**

- `push(elem);//往队尾添加元素.`
- `pop();//从队头移除第一个元素.`
- `back();//返回最后一个元素.`
- `front();//返回第一个元素.`

**大小操作:**

- `empty();//判断堆栈是否为空.`
- `size();//返回栈的大小.`

#### 3.7 list容器

##### 3.7.1 list基本概念

**链表（(list):**

是一种物理存储单元上非连续的存储结构，数据元素的逻辑顺序是通过链表中的指针链接实现的

**链表的组成:**

链表由—系列**结点**组成

**结点的组成:**

一个是存储数据元素的**数据域**,另一个是存储下一个结点地址的**指针域**
STL中的链表是一个**双向循环链表**

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/4f4bc183de84102d6e5f07f61bc0c88f.png)

##### 3.7.2 list构造函数

**函数原型:**

- `list<T>lst;//list采用采用模板类实现,对象的默认构造形式;`
- `list(beg,end);//构造函数将[beg,end)区间中的元素拷贝给本身.`
- `list(n,elem);//构造函数将n个elem拷贝给本身.`
- `list(const list &lst);//拷贝构造函数.`

##### 3.7.3 list赋值和交换

**函数原型:**

- `assign(beg,end);//将[beg, end)区间中的数据拷贝赋值给本身.`
- `assign(n,elem);//将n个elem拷贝赋值给本身.`
- `list& operator=(const list &lst);//重载等号操作符.`
- `swap(lst);//将lst与本身的元素互换.`

##### 3.7.4 list大小操作

**函数原型:**

- `size();//返回容器中元素的个数.`
- `empty();//判断容器是否为空.`
- `resize(num);//重新指定容器的长度为num,若容器变长,则以默认值填充新位置.如果容器变短,则末尾超出容器长度的元素被删除.`
- `resize(num，elem);//重新指定容器的长度为num,若容器变长,则以elem值填充新位置.如果容器变短,则末尾超出容器长度的元素被删除.`

##### 3.7.5 list插入和删除

**函数原型:**

- `push_back(elem);//在容器尾部加入一个元素. `
- `pop_back();//删除容器中最后一个元素.`
- `push_front(elem);//在容器开头插入一个元素. `
- `pop_front();//从容器开头移除第一个元素.`
- `insert(pos,elem);//在pos位置插elem元素的拷贝，返回新数据的位置.`
- `insert(pos,n,elem);//在pos位置插入n个elem数据，无返回值.`
- `insert(pos,beg,end);//在pos位置插入[beg,end)区间的数据，无返回值.`
- `clear();//移除容器的所有数据.`
- `erase(beg,end);//删除[beg,end)区间的数据，返回下一个数据的位置.`
- `erase(pos);//删除pos位置的数据，返回下一个数据的位置.`
- `remove(elem);//删除容器中所有与elem值匹配的元素.`

##### 3.7.6 list数据存取

**函数原型:**

- `front();//返回第一个元素.`
- `back();//返回最后一个元素.`

**注意:**

**不可以使用`[]`和`at()`访问访问list容器的元素.**

**原因:**

**list本质为链表,不是使用连续线性空间存储数据.迭代器也不支持随机访问.**

##### 3.7.7 list反转和排序

**函数原型:**

- `reverse();//反转链表.`
- `sort();//链表排序.使用list内部成员函数lst.sort()`

**注意:**

**不能使用reverse()函数来得到降序排序,时间复杂度会变大.**

```c++
bool compare(int v1, int v2)
{
    return v1 > v2;    //第一个数大于第二个数,即降序
}
int main()
{
    list<int>lst;
    lst.push_back(423);
    lst.push_back(231);
    lst.push_back(233);
    lst.push_back(342);
    lst.push_back(422);

    cout << "排序前:\t" << endl;
    for (list<int>::iterator it = lst.begin(); it != lst.end(); it++)
    {
        cout << *it << "\t";
    }
    //升序排序
    lst.sort();//默认为升序
    cout << endl << "升序排序后:\t" << endl;
    for (list<int>::iterator it = lst.begin(); it != lst.end(); it++)
    {
        cout << *it << "\t";
    }
    //降序排序
    lst.sort(compare);//回调函数
    cout << endl << "降序排序后:\t" << endl;
    for (list<int>::iterator it = lst.begin(); it != lst.end(); it++)
    {
        cout << *it << "\t";
    }
    return 0;
}
```

```
输出结果:
排序前:
423     231     233     342     422
升序排序后:
231     233     342     422     423
降序排序后:
423     422     342     233     231
```

##### 3.7.8 排序案例

**案例描述:**

将Person自定义数据类型进行排序,Person中属性有姓名、年龄、身高

**排序规则:**

按照年龄进行升序,如果年龄相同按照身高进行降序.

```c++
class Person
{
public:
    string name;
    int age;
    int height;
    Person(string _name, int _age, int _height) :name(_name), age(_age), height(_height)
    {
    }
};
//指定排序规则
bool compare(Person& p1, Person& p2)
{
    //按照年龄升序
    if(p1.age == p2.age)
    {
        //年龄相同,按照身高降序
        return p1.height>p2.height;
    }
    return p1.age < p2.age;
}
int main()
{
    list<Person>lst;
    //准备数据
    Person p1("p1", 12, 232);
    Person p2("p2", 31, 192);
    Person p3("p3", 22, 142);
    Person p4("p4", 18, 240);
    Person p5("p5", 18, 160);
    Person p6("p6", 12, 170);
    //传入数据
    lst.push_back(p1);
    lst.push_back(p2);
    lst.push_back(p3);
    lst.push_back(p4);
    lst.push_back(p5);
    lst.push_back(p6);
    //输出
    cout << "排序前:" << endl;
    for (list<Person>::iterator it = lst.begin(); it != lst.end(); it++)
    {
        cout << "姓名:\t" << it->name << "年龄:\t" << it->age << "身高:\t" << it->height<<endl;
    }
    lst.sort(compare);
    cout << endl << "升序排序后:" << endl;
    for (list<Person>::iterator it = lst.begin(); it != lst.end(); it++)
    {
        cout << "姓名:\t" << it->name << "年龄:\t" << it->age << "身高:\t" << it->height<<endl;
    }
    return 0;
}
```

```
输出结果:
排序前:
姓名:   p1年龄: 12身高: 232
姓名:   p2年龄: 31身高: 192
姓名:   p3年龄: 22身高: 142
姓名:   p4年龄: 18身高: 240
姓名:   p5年龄: 18身高: 160
姓名:   p6年龄: 12身高: 170

升序排序后:
姓名:   p1年龄: 12身高: 232
姓名:   p6年龄: 12身高: 170
姓名:   p4年龄: 18身高: 240
姓名:   p5年龄: 18身高: 160
姓名:   p3年龄: 22身高: 142
姓名:   p2年龄: 31身高: 192
```

#### 3.8 set/multiset容器

##### 3.8.1 set基本概念

**简介:**

- 所有元素都会在插入时**自动被排序**.

**本质:**

- `set/multiset`属于**关联式容器**,底层结构是用**二叉树**实现.

**set和multiset区别:**

- `set`**不允许容器中有重复**的元素.
- `multiset`**允许容器中有重复**的元素.

##### 3.8.2 set构造和赋值

**构造函数:**

- `set<T>st;//默认构造函数.`
- `set(const set &st);//拷贝构造函数.`

**赋值函数:**

- `set& operator=(const set &st);//重载等号操作符.`

##### 3.8.3 set大小和交换

**函数原型:**

- `size();//返回容器中元素的数目.`
- `empty();//判断容器是否为空.`
- `swap(st);//交换两个集合容器.`

##### 3.8.4 set插入和删除

**函数原型:**

- `insert(elem);//在容器中插入元素.`
- `clear();//清除所有元素.`
- `erase(pos);//删除pos迭代器所指的元素，返回下一个元素的迭代器.`
- `erase(beg,end);//删除区间[beg,end)的所有元素,返回下一个元素的迭代器.`
- `erase(elem);//删除容器中值为elem的元素.`

##### 3.8.5 set查找和统计

**函数原型:**

- `find(key);//查找key是否存在,若存在,返回该键的元素的迭代器;若不存在,返回set.end();`
- `count(key);//统计key的元素个数.`

##### 3.8.6 set和multiset区别

**区别:**

- `set`不可以插入重复数据,而`multiset`可以.
- `set`插入数据的同时会返回插入结果,表示插入是否成功. 
- `multiset`不会检测数据,因此可以插入重复数据.

##### 3.8.7 pair对组创建

**功能描述:**

- 成对出现的数据,利用对组可以返回两个数据.

**两种创建方式:**

- `pair<type,type> p (value1,value2);`
- `pair<type,type> p = make_pair(value1,value2);`

##### 3.8.8 set容器排序

**利用仿函数,可以改变排序规则.(set容器默认为升序排序)**

**代码演示:**

```c++
class compare
{
public:
    bool operator()(int v1,int v2)const//注意点
    {
        return v1 > v2;//降序
    }
};
int main()
{
    set<int,compare>s;
    s.insert(20);
    s.insert(34);
    s.insert(98);
    s.insert(10);
    s.insert(32);
    //输出
    for (set<int, compare>::iterator it = s.begin(); it != s.end(); it++)
    {
        cout << *it << "\t";
    }
    return 0;
}
```

```
输出结果:
98      34      32      20      10
```

###### 3.8.8.2 自定义数据类型排序

**代码演示:**

```c++
class Person
{
public:
    string name;
    int age;
    Person(string _name, int _age) :name(_name), age(_age)
    {

    }
};
class compare
{
public:
    bool operator()(const Person& p1, const Person& p2)const
    {
        return p1.age > p2.age;//年龄降序
    }
};
int main()
{
    set<Person, compare>s;
    Person p1("p1", 12);
    Person p2("p2", 32);
    Person p3("p3", 18);
    Person p4("p4", 15);
    Person p5("p5", 43);

    s.insert(p1);
    s.insert(p2);
    s.insert(p3);
    s.insert(p4);
    s.insert(p5);

    for (set<Person, compare>::iterator it = s.begin(); it != s.end(); it++)
    {
        cout << "姓名:\t" << it->name << "\t年龄:\t" << it->age<<endl;
    }
    return 0;
}
```

```
输出结果:
姓名:   p5      年龄:   43
姓名:   p2      年龄:   32
姓名:   p3      年龄:   18
姓名:   p4      年龄:   15
姓名:   p1      年龄:   12
```

#### 3.9 map/multimap容器

##### 3.9.1 map基本概念

**简介:**

- `map`中所有元素都是`pair`.
- pair中第一个元素为`key`(键值),起到索引作用,第二个元素为`value`(实值).
- 所有元素都会根据元素的键值**自动排序**.

**本质:**

- `map/multimap`属于**关联式容器**,底层结构是用二叉树实现.

**优点:**

- 可以根据`key`值快速找到`value`值.

**map和multimap区别:**

- `map`不允许容器中有重复`key`值元素.
- `multimap`允许容器中有重复key值元素.

##### 3.9.2 map构造和赋值

**函数原型:**

**构造:**

- `map<T1,T2> mp;//map默认构造函数.`
- `map(const map &mp);//拷贝构造函数.`

**赋值:**

- `map& operator=(const map &mp);//重载等号操作符.`

##### 3.9.3 map大小和交换

**函数原型:**

| 函数      | 描述                 |
| --------- | -------------------- |
| size();   | 返回容器中元素的数目 |
| empty();  | 判断容器是否为空     |
| swap(st); | 交换两个集合容器     |

##### 3.9.4 map插入和删除

**函数原型:**

| 函数              | 描述                                                |
| ----------------- | --------------------------------------------------- |
| `insert(elem);`   | 在容器中插入元素                                    |
| `clear();`        | 清除所有元素                                        |
| `erase(pos);`     | 删除pos迭代器所指的元素，返回下一个元素的迭代器     |
| `erase(beg,end);` | 删除区间[beg,end)的所有元素，返回下一个元素的迭代器 |
| `erase(key);`     | 删除容器中值为key的元素                             |

##### 3.9.5 map查找和统计

**函数原型:**

| 函数          | 描述                                                         |
| ------------- | ------------------------------------------------------------ |
| `find(key);`  | 查找key是否存在,若存在,版回该键的元素的迭代器;若不存在,返回set.end(); |
| `count(key);` | 统计key的元素个数                                            |

##### 3.9.6 map容器排序

- 利用仿函数,可以改变排序规则.

  ```c++
  class compare
  {
  public:
     bool operator()(int v1, int v2)const
     {
         return v1 > v2;//降序排序
     }
  };
  int main()
  {
     map<int, int, compare>m;
     m.insert(make_pair(1, 10));
     m.insert(make_pair(2, 40));
     m.insert(make_pair(3, 30));
     m.insert(make_pair(4, 70));
     m.insert(make_pair(5, 50));
  
     for (map<int, int>::iterator it = m.begin(); it != m.end(); it++)
     {
         cout << "Key:\t" << it->first << "\tValue:\t" << it->second << endl;
     }
     return 0;
  }
  ```

```
输出结果:
Key:    5       Value:  50
Key:    4       Value:  70
Key:    3       Value:  30
Key:    2       Value:  40
Key:    1       Value:  10
```

#### 3.10 STL案例-员工分组

##### 3.10.1案例描述

- 公司今天招聘了10个员工(ABCDEFGHI),10名员工进入公司之后,需要指派员工在那个部门工作.

- 员工信息有: 姓名 工资组成;部 门分为:策划、美术、研发.

- 随机给10名员工分配部门和工资.

- 通过`multimap`进行信息的插入`key(`部门编号) `value(`员工).

- 分部门显示员工信息.

##### 3.10.2实现步骤

1. 创建10名员工,放到`vector`中.
2. 遍历`vector`容器,取出每个员工,进行随机分组.
3. 分组后,将员工部门编号作为`key`,具体员工作为`value`,放入到`multimap`容器中.
4. 分部门显示员工信息.

**实现代码:**

```c++
class Person
{
public:
    string name;
    int salary;
};
void createPerson(vector<Person>& v)
{
    string nameSeed = "ABCDEFGHIJ";
    for (int i = 0; i < 10; i++)
    {
        Person p;
        p.name = "员工";
        p.name += nameSeed[i];
        p.salary = rand() % 100000 + 100000;
        v.push_back(p);
    }
}
void setGroup(vector<Person>& v, multimap<int, Person>& m)
{
    for (auto x : v)
    {
        int depId = rand() % 3;
        m.insert(make_pair(depId, x));
    }
}
void showGroup(multimap<int, Person>& m)
{
    cout << "策划部门:" << endl;
    //-------------------------------------------
    multimap<int, Person>::iterator pos = m.find(0);
    int count = m.count(0);
    int index = 0;
    for (; pos != m.end() && index < count; pos++, index++)
    {
        cout << "姓名:\t" << pos->second.name << "\t工资:\t" << pos->second.salary << endl;
    }
    //-------------------------------------------
    cout << "美术部门:" << endl;
    //-------------------------------------------
    pos = m.find(1);
    count = m.count(1);
    index = 0;
    for (; pos != m.end() && index < count; pos++, index++)
    {
        cout << "姓名:\t" << pos->second.name << "\t工资:\t" << pos->second.salary << endl;
    }
    //-------------------------------------------
    cout << "研发部门:" << endl;
    //-------------------------------------------
    pos = m.find(2);
    count = m.count(2);
    index = 0;
    for (; pos != m.end() && index < count; pos++, index++)
    {
        cout << "姓名:\t" << pos->second.name << "\t工资:\t" << pos->second.salary << endl;
    }
    //-------------------------------------------
}
int main()
{
    vector<Person>v;
    multimap<int, Person>m;
    createPerson(v);
    setGroup(v, m);
    showGroup(m);
    return 0;
}
```

```
输出结果:
策划部门:
姓名:   员工D   工资:   126500
姓名:   员工I   工资:   126962
姓名:   员工J   工资:   124464
美术部门:
姓名:   员工C   工资:   106334
姓名:   员工E   工资:   119169
姓名:   员工G   工资:   111478
研发部门:
姓名:   员工A   工资:   100041
姓名:   员工B   工资:   118467
姓名:   员工F   工资:   115724
姓名:   员工H   工资:   129358
```

### 4. STL-函数对象(仿函数)

#### 4.1 函数对象

##### 4.1.1 函数对象概念

**概念:**

- 重载**函数调用操作符**的类,其对象常称为**函数对象.**
- **函数对象**使用重载的`()`时,行为类似函数调用,也叫仿函数.

**本质:**

- **函数对象(仿函数)是一个类,不是一个函数.**

##### 4.1.2 函数对象使用

**特点:**

- 函数对象在使用时,可以像普通函数那样调用,可以有参数,可以有返回值.
- 函数对象超出普通函数的概念,函数对象**可以有自己的状态**.
- 函数对象可以**作为参数传递**.

**代码演示:**

```c++
class CppAdd
{
public:
    //函数对象(仿函数)
    int operator()(int v1,int v2)
    {
        return v1+v2;
    }
};
int main()
{
    CppAdd add;
    cout<<add(3,4)<<endl;
    return 0;
}
```

```
输出结果:
7
```

#### 4.2谓词

##### 4.2.1 谓词概念

**概念:**

- 返回`bool`类型的仿函数称为**谓词.**
- 如果`operator()`接受一个参数,那么叫做**一元谓词**.
- 如果`operator()`接受两个参数,那么叫做**二元谓词**.

```c++
class functor
{
public:
    bool operator()(int val)//一元谓词
    {
        return val>5;
    }
};
int main()
{
    vector<int>v;
    for(int i=0;i<10;i++)
    {
        v.push_back(i);
    }
    //查找大于5的数
    vector<int>::iterator it = find_if(v.begin(),v.end(),functor());//functor()创建匿名对象
    if(it == v.end())cout<<"未找到大于五的数"<<endl;
    else cout<<*it<<endl;
    return 0;
}
```

```
输出结果:
6
```

```c++
class functor
{
public:
    bool operator()(int v1,int v2)//二元谓词
    {
        return v1>v2;
    }
};
int main()
{
    vector<int>v;
    for(int i=0;i<5;i++)
    {
        v.push_back(rand()%10+20);
    }
    sort(v.begin(),v.end(),functor());//functor()创建匿名对象
    //输出
    for(auto x:v)cout<<x<<"\t";
    return 0;
}
```

```
输出结果：
29      27      24      21      20
```

#### 4.3 内建函数对象

##### 4.3.1 内建函数对象意义

**概念:**

STL内建了一些函数对象

**分类:**

- 算术仿函数
- 关系仿函数
- 逻辑仿函数

**用法:**

- 这些仿函数所产生的对象,用法和一般函数完全相同.
- 使用内建函数对象,需要引入头文件`#include<functional>`.

##### 4.3.2 算术仿函数

**功能描述:**

- 实现四则运算.
- 其中`negate`是一元运算，其他都是二元运算.

**仿函数原型:**

| 函数                                | 描述       |
| ----------------------------------- | ---------- |
| `template<class T> T plus<T>`       | 加法仿函数 |
| `template<class T> T minus<T>`      | 减法仿函数 |
| `template<class T> T multiplies<T>` | 乘法仿函数 |
| `template<class T> T divides<T>`    | 除法仿函数 |
| `template<class T> T modulus<T>`    | 取模仿函数 |
| `template<class T> T negate<T>`     | 取反仿函数 |

##### 4.3.3 关系仿函数

**功能描述:**
实现关系对比

**仿函数原型:**

| 函数                                      | 描述     |
| ----------------------------------------- | -------- |
| `template<class T> bool equal_to<T>`      | 等于     |
| `template<class T> bool not_equal_to<T>`  | 不等于   |
| `template<class T> bool greater<T>`       | 大于     |
| `template<class T> bool greater_equal<T>` | 大于等于 |
| `template<class T> bool less<T>`          | 小于     |
| `template<class T> bool less_equal<T>`    | 小于等于 |

**代码演示:**

```c++
vector<int>v;
for(int i=0;i<5;i++)
{
    v.push_back(rand()%10+20);
}
sort(v.begin(),v.end(),greater<int>());//使用内置函数对象
//输出
for(auto x:v)cout<<x<<"\t";
```

```
输出结果:
29      27      24      21      20
```

##### 4.3.4 逻辑仿函数

**功能描述:**

- 实现逻辑运算

**函数原型:**

| 函数                                    | 描述   |
| --------------------------------------- | ------ |
| `template<class T> bool logical_and<T>` | 逻辑与 |
| `template<class T> bool logical_or<T>`  | 逻辑或 |
| `template<class T> bool logical_not<T>` | 逻辑非 |

### 5. STL-常用算法

**概述:**

- 算法主要是由头文件`<algorithm>` `<functional>` `<numeric>`组成.
- `<algorithm>`是所有STL头文件中最大的一个,范围涉及到比较、交换、查找、遍历操作、复制、修改等等.
- `<numeric>`体积很小,只包括几个在序列上面进行简单数学运算的模板函数.
- `<functional>`定义了一些模板类,用以声明函数对象.

#### 5.1 常用遍历算法

**算法简介:**

| 函数      | 描述                   |
| --------- | ---------------------- |
| for_each  | 遍历容器               |
| transform | 搬运容器到另一个容器中 |

##### 5.1.1 for_each

**函数原型:**

- `for_each(iterator beg， iterator end，func);`

| 参数  | 描述               |
| ----- | ------------------ |
| beg1  | 源容器开始迭代器   |
| end1  | 源容器结束迭代器   |
| beg2  | 目标容器开始迭代器 |
| _func | 函数或者函数对象   |

**代码演示:**

```c++
//普通函数
void print(int val)
{
    cout<<val<<" ";
}
//仿函数
class functor
{
public:
    void operator()(int val)
    {
        cout<<val<<" ";
    }
};
int main()
{
    vector<int>v;
    for(int i=0;i<5;i++)
    {
        v.push_back(rand()%3+13);
    }
    cout<<"普通函数:"<<endl;
    for_each(v.begin(),v.end(),print);
    cout<<endl<<"仿函数:"<<endl;
    for_each(v.begin(),v.end(),functor());
    return 0;
}
```

```
输出结果:
普通函数:
15 15 14 14 15
仿函数:
15 15 14 14 15
```

##### 5.1.2 transform

**功能描述:**

- 搬运容器到另—个容器中

**函数原型:**

- `transform(iterator beg1,iterator end1,iterator beg2，_func);`

**注意:**

**搬运的目标容器要提前开辟空间.**

**代码演示:**

```c++
class Transform
{
public:
    int operator()(int v)
    {
        return v;
    }
};
class print
{
public:
    void operator()(int val)
    {
        cout<<val<<" ";
    }
};
int main()
{
    vector<int>v;
    for(int i=0;i<5;i++)
    {
        v.push_back(rand()%12+40);
    }
    vector<int>vTarget;
    vTarget.resize(v.size());//目标容器提前开辟空间
    transform(v.begin(),v.end(),vTarget.begin(),Transform());
    for_each(vTarget.begin(),vTarget.end(),print());
    cout<<endl;
    return 0;
}
```

```
输出结果:
45 51 50 44 45
```

#### 5.2 常用查找算法

**算法简介:**

| 函数          | 描述               |
| ------------- | ------------------ |
| find          | 查找元素           |
| find_if       | 按条件查找元素     |
| adjacent_find | 查找相邻重复元素   |
| binary_search | 二分查找法         |
| count         | 统计元素个数       |
| count_if      | 按条件统计元素个数 |

##### 5.2.1 find

**功能描述:**

- 查找指定元素,找到返回指定元素的迭代器,找不到返回结束迭代器`end()`.

**函数原型:**
`find(iterator beg,iterator end,value) ;`按值查找元素，找到返回指定位置迭代器，找不到返回结束迭代器`end()`位置

- `beg `开始迭代器
- `end `结束迭代器
- `value`查找的元素

**代码演示:**

```c++
//常见数据类型
int main()
{
    vector<int>v;
    for(int i=0;i<5;i++)
    {
        v.push_back(i);
    }
    //查找容器
    vector<int>::iterator it find(v.begin(),v.end(),5);
    if(it == v.end())
    {
        cout<<"未找到"<<endl:
    }
    else
    {
        cout<<"找到: "<<*it<<endl;
    }

    return 0;
}
```

```c++
//自定义数据类型
class Person
{
public:
    string name;
    int age;
    Person(string _name, int _age) :name(_name), age(_age)
    {

    }
    bool operator==(const Person& p)
    {
        if (this->name == p.name && this->age == p.age)return true;
        else return false;
    }
};
int main()
{
    srand(time(0));
    vector<Person>v;
    for (int i = 0; i < 5; i++)
    {
        Person p("123", rand() % 24 + 23);
        v.push_back(p);
    }
    Person p("123", 23);
    vector<Person>::iterator it = find(v.begin(), v.end(),p);
    if (it == v.end())
    {
        cout << "未找到" << endl;
    }
    else
    {
        cout << "找到元素:\t" << it->name << "\t年龄:\t" << it->age << endl;
    }
    return 0;
}
```

```
输出结果:
找到元素:       123     年龄:   23
```

##### 5.2.2 find_if

**功能描述:**
·按条件查找元素

函数原型:
`find_if(iterator beg, iterator end，_pred);`按值查找元素,找到返回指定位置迭代器,找不到返回结束迭代器`end()`位置

- `beg开始迭代器`
- `end结束迭代器`
- `_Pred函数或者谓词(返回bool类型的仿函数)`

**代码演示:**

```c++
class functor
{
public:
    bool operator()(int val)
    {
        return val > 5;
    }
};
int main()
{
    vector<int>v;
    for (int i = 0; i < 10; i++)v.push_back(i);
    vector<int>::iterator it = find_if(v.begin(), v.end(), functor());
    if (it == v.end())cout << "未找到" << endl;
    else cout << "找到:\t" << *it << endl;
    return 0;
}
```

```
输出结果:
找到:   6
```

##### 5.2.3 adjacent_find

**功能描述:**

·查找相邻重复元素

**函数原型:**

`adjacent_find(iterator beg, iterator end) ;`查找相邻重复元素,返回相邻元素的第一个位置的迭代器.

- `beg开始迭代器`
- `end结束迭代器`

**代码演示:**

```c++
int main()
{
    vector<int>v;
    v.push_back(10);
    v.push_back(10);
    v.push_back(40);
    v.push_back(20);
    v.push_back(30);
    v.push_back(20);
    vector<int>::iterator it = adjacent_find(v.begin(),v.end());
    if(it==v.end())cout<<"未找到"<<endl;
    else cout<<"找到相邻重复元素:\t"<<*it<<endl;
    return 0;
}
```

```
输出结果:
找到相邻重复元素:       10
```

##### 5.2.4 binary_search

**功能描述:**
查找指定元素是否存在
**函数原型:**
`bool bihary_search(iterator beg， iterator end，value) ;`查找指定的元素，查到返回true否则false.

- `beg 开始迭代器`
- `end结束迭代器`
- `value查找的元素`

**注意:**

在**无序序列中不可用**

**代码演示:**

```c++
vector<int>v;
for(int i=0;i<10;i++)
{
    v.push_back(i);
}
bool ret = binary_search(v.begin(),v.end(),9);
if(ret)
{
    cout<<"找到元素"<<endl;
}
else
{
    cout<<"未找到"<<endl;
}
```

```
输出结果:
找到元素
```

##### 5.2.5 count

**功能描述:**

统计元素个数

**函数原型:**

`count(iterator beg, iterator end, value);`统计元素出现次数

- `beg开始迭代器`
- `end结束迭代器`
- `value统计的元素`

##### 5.2.6 count_if

功能描述:

按条件统计元素个数

函数原型:

`count_if(iterator beg,iterator end,_Pred) ;`按条件统计元素出现次数

- `beg 开始迭代器`
- ` end结束迭代器`
- ` _Pred谓词`

**代码演示:**

```c++
//内置数据类型
class functor
{
public:
    bool operator()(int val)
    {
        return val > 30;
    }
};
int main()
{
    vector<int>v;
    v.push_back(20);
    v.push_back(20);
    v.push_back(30);
    v.push_back(50);
    v.push_back(40);
    int num = count_if(v.begin(), v.end(), functor());
    cout << "大于30的数:\t" << num << endl;
    return 0;
}
```

```
输出结果:
大于30的数:     2
```

```c++
//自定义数据类型
class Person
{
public:
    string name;
    int age;
    Person(string _name, int _age) :name(_name), age(_age)
    {
    }
};

class functor
{
public:
    bool operator()(const Person& p)
    {
        return p.age > 20;
    }
};

int main()
{
    vector<Person>v;
    for (int i = 0; i < 5; i++)
    {
        Person p("dsdas", rand() % 34 + 20);
        v.push_back(p);
    }
    int num = count_if(v.begin(), v.end(), functor());
    cout << "大于20岁的人的个数:\t" << num << endl;
    return 0;
}
```

```
输出结果:
大于20岁的人的个数:     5
```

#### 5.3 常用排序算法

**算法简介:**



| 函数           | 描述                              |
| -------------- | --------------------------------- |
| sort           | 对容器内元素进行排序              |
| random_shuffle | 洗牌 指定范围内的元素随机调整次序 |
| merge          | 容器元素合并,并存储到另—容器中    |
| reverse        | 反转指定范围的元素                |

##### 5.3.1 sort

**功能描述:**

- 对容器内元素进行排序

**函数原型:**

`sort(iterator beg,iterator end,_Pred);`按值查找元素,找到返回指定位置迭代器,找不到返回结束迭代器位置

- `beg开始迭代器`
- `end结束迭代器`
- `_Pred谓词`

##### 5.3.2 random_shuffle

**功能描述:**

- 洗牌指定范围内的元素随机调整次序

**函数原型:**

`random_shuffle(iterator beg, iterator end);`指定范围内的元素随机调整次序.

- `beg 开始迭代器`
- ` end结束迭代器`

##### 5.3.3 merge

**功能描述:**

- 两个容器元素合并,并存储到另—容器中

**函数原型:**

| 函数                                                         | 描述                            |
| ------------------------------------------------------------ | ------------------------------- |
| `merge(iterator beg1, iterator end1,iterator beg2,iterator end2,iterator dest);` | 容器元素合并,并存储到另一容器中 |

| 参数 | 描述               |
| ---- | ------------------ |
| beg1 | 容器1开始迭代器    |
| end1 | 容器1结束迭代器    |
| beg2 | 容器2开始迭代器    |
| end2 | 容器2结束迭代器    |
| dest | 目标容器开始迭代器 |

**注意:**
**两个容器必须是有序的**

**代码演示:**

```c++
int main()
{
    vector<int>v1;
    vector<int>v2;
    for(int i=0;i<10;i++)
    {
        v1.push_back(i);
        v2.push_back(i+1);
    }
    vector<int>vTarget;
    vTarget.resize(v1.size()+v2.size());
    merge(v1.begin(),v1.end(),v2.begin(),v2.end(),vTarget.begin());
    for(auto x:vTarget)
    {
        cout<<x<<" ";
    }

    return 0;
}
```

```
输出结果:
0 1 1 2 2 3 3 4 4 5 5 6 6 7 7 8 8 9 9 10
```

##### 5.3.4 reverse

**功能描述:**

将容器内元素进行反转

**函数原型:**

`reverse(iterator beg,iterator end );`反转指定范围的元素

- `beg 开始迭代器`
- `end结束迭代器`

##### 5.3.5 next_permutation

**功能描述:**

将容器进行全排序

**函数原型:**

`next_permutation(iterator beg,iterator end);`将指定范围的元素进行全排序

- `beg 开始迭代器`
- `end结束迭代器`

**代码演示:**

```c++
//将指定范围的元素进行全排序
vector<vector<int>> permutation(vector<int>& nums) 
{
  vector<vector<int>>ret;
  sort(nums.begin(),nums.end());
  do
  {
      ret.push_back(nums);
  }
  while(next_permutation(nums.begin(),nums.end()));
  return ret;
}
```

#### 5.4 常用拷贝和替换算法

**算法简介:**

| 函数       | 描述                                     |
| ---------- | ---------------------------------------- |
| copy       | 容器内指定范围的元素拷贝到另一容器中     |
| replace    | 将容器内指定范围的旧元素修改为新元素     |
| replace_if | 容器内指定范围满足条件的元素替换为新元素 |
| swap       | 互换两个容器的元素                       |

##### 5.4.1 copy

**功能描述:**

- 容器内指定范围的元素拷贝到另—容器中

**函数原型:**

`copy(iterator beg,iterator end,iterator dest);`//按值查找元素,找到返回指定位置迭代器,找不到返回结束迭代器位置

- `beg 开始迭代器`
- `end结束迭代器`
- `dest目标起始迭代器`

##### 5.4.2 replace

**功能描述:**
将容器内指定范围的旧元素修改为新元素
**函数原型:**
`replace(iterator beg, iterator end,oldvalue,newvalue);`将区间内旧元素替换成新元素

- `beg开始迭代器`
- `end结束迭代器`
- `oldvalue 旧元素`
- `newvalue 新元素`

##### 5.4.3 replace_if

**功能描述:**

将区间内满足条件的元素,替换成指定元素

**函数原型:**

`replace_if(iterator beg,iterator end,_pred,newvalue);`按条件替换元素,满足条件的替换成指定元素.

- `beg 开始迭代器`
- `end 结束迭代器`
- `_pred 谓词`
- `newvalue 替换的新元素`

```c++
class functor
{
public:
    bool operator()(int val)
    {
        return val > 40;
    }
};
class print
{
public:
    void operator()(int val)
    {
        cout << val << " ";
    }
};
int main()
{
    vector<int>v;
    v.push_back(10);
    v.push_back(53);
    v.push_back(76);
    v.push_back(47);
    v.push_back(32);
    v.push_back(17);
    replace_if(v.begin(), v.end(),functor(), 400);
    for_each(v.begin(), v.end(),print());
    return 0;
}
```

```
输出结果:
10 400 400 400 32 17
```

##### 5.4.4 swap

**功能描述:**

- 互换两个容器的元素

**函数原型:**

`swap(container c1.container c2);`互换两个容器的元素

- `c1容器1`
- `c2容器2`

#### 5.5 常用算术生成算法

**算法简介:**

- `accumulate`计算容器元素累计总和. 
- `fill`向容器中添加元素.

**注意:**

- 算术生成算法属于小型算法,使用时包含的头文件为`#include <numeric>`.

##### 5.5.1 accumulate

**功能描述:**

- 计算区间内容器元素累计总和

**函数原型:**

`accumulate(iterator beg,iterator end,value);`计算容器元素累计总和

- `beg 开始迭代器`
- `end结束迭代器`
- `value起始值`

**代码演示:**

```c++
vector<int>v;
for (int i = 0; i <= 100; i++)
{
    v.push_back(i);
}
int sum = accumulate(v.begin(), v.end(), 0);
cout << "总和:\t" << sum;
```

```
输出结果:
总和:   5050
```

##### 5.5.2 fill

**功能描述:**

- 向容器中填充指定的元素

**函数原型:**

`fill(iterator beg,iterator end,value);`向容器中填充元素

- `beg开始迭代器`
- `end结束迭代器`
- `value填充的值`

#### 5.6 常用集合算法

**算法简介:**

| 函数               | 描述             |
| ------------------ | ---------------- |
| `set_intersection` | 求两个容器的交集 |
| `set_union`        | 求两个容器的并集 |
| `set_difference`   | 求两个容器的差集 |

##### 5.6.1 set_intersection

**功能描述:**

- 求两个容器的交集

**函数原型:**

| 函数                                                         | 描述             |
| ------------------------------------------------------------ | ---------------- |
| `set_intersection(iterator beg1,iterator end1,iterator beg2,iterator end2,iterator dest);` | 求两个集合的交集 |

**注意:**

**两个集合必须是有序序列**

| 参数 | 描述               |
| ---- | ------------------ |
| beg1 | 容器1开始迭代器    |
| end1 | 容器1结束迭代器    |
| beg2 | 容器2开始迭代器    |
| end2 | 容器2结束迭代器    |
| dest | 目标容器开始迭代器 |

##### 5.6.2 set_union

**功能描述:**

- 求两个集合的并集

**函数原型:**

| 函数                                                         | 描述             |
| ------------------------------------------------------------ | ---------------- |
| `set_union(iterator beg1,iterator end1,iterator beg2,iterator end2,iterator dest);` | 求两个集合的并集 |

**注意:**

- 两个集合必须是有序序列

| 参数 | 描述               |
| ---- | ------------------ |
| beg1 | 容器1开始迭代器    |
| end1 | 容器1结束迭代器    |
| beg2 | 容器2开始迭代器    |
| end2 | 容器2结束迭代器    |
| dest | 目标容器开始迭代器 |

##### 5.6.3 set_difference

**功能描述:**

- 求两个集合的差集

**函数原型:**

| 函数                                                         | 描述             |
| ------------------------------------------------------------ | ---------------- |
| `set_difference(iterator beg1,iterator end1,iterator beg2,iterator end2,iterator dest);` | 求两个集合的差集 |

**注意:**

- 两个集合必须是有序序列

## 三.并发与多线程

### 1.并发、进程、线程

**并发:**

- 