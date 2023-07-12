# Python
python notebook, version: python3+

**目录：**
 
----------------------------------------
- [01.基本数据类型](./Python/01.基本数据类型.md)
  - 1 整数
    - （1）比较运算符（<、>、<=、>=、 ==、 != ）
    - （2）算术运算符（+、-、*、/、%、**、//） , 平方（pow）
    - （3）赋值运算符（ = ）
    - （4）位运算符（&、|、^、~、>>、<<）
    - （5）转进制 （int、bin、oct、hex）
    - （6）判断奇偶（&1、%2）
  - 2 浮点数
    - （1）书写形式
    - （2）最大值
    - （3）无穷小、大
    - （4）取整（向上：math.ceil()，向下：math.floor()、"//"，四舍五入：round()，向0取整：int()）
    - （5）计算的不精确
  - 3 复数
  - 4 布尔值/布尔类型
    - （1）布尔类型（True、False）
    - （2）布尔运算（and、or、not）
  - 5 空值
  - 6 字符串
    - （1）新建
    - （2）拆分（.split）
    - （3）拼接（+, join）
    - （4）修改、代替（.replace）
    - （5）删除（.strip）
    - （6）查找（.find、.index）
    - （7）子字符串（计数、位置）（.count、re.finditer）
    - （8）字符串格式化(.format、zfill)
    - （9）比较
    - （10）转义字符（\）
    - （11）str  <==>  bytes 
    - （12）str  <==>  list
    - （13）正则（re.search）
    - （14）判断字符串中是否有汉字、数字（u'\u4e00' <= ch <= u'\u9fff'、.isdigit()）
    - （15）编辑距离（Levenshtein）
  - 7 类型判断（type、isinstance）
 
 
 
----------------------------------------
- [02.其他数据类型（序列、集合、字典、有序字典）](./Python/02.其他数据类型.md)
  - 1 序列（tuple 、list）
    - （1） 新建（[0] * n、range）
    - （2） 拼接成字符串（''.join(list)）
    - （3） 添加元素（.append、.extend、+）
    - （4） 删除元素（.remove、.pop、del）
    - （5） 排序（.sort、sorted）
    - （6） 反序（reversed）
    - （7） 乱序（random.shuffle）
    - （7） 随机选择（shuffle）
    - （8） 查找元素（in、.index）
    - （9） 清空list
    - （10） 合并/拼接（+）， 分片
    - （11） 去重（set）
    - （12） *list
  - 2 集合
    - （1）新建（{}，set()）
    - （2）加入（.add()，.update()）
    - （3）删除（.remove()，.discard()，pop()）
    - （4）长度（len()）
    - （5）清空（.clear()）
    - （6）是否存在（in）
    - （7）是否相等（==、！=）
    - （x）集合运算（-，|，&，^）
  - 3 字典
    - （1）新建（{}、.setdefault()、dict()、defaultdict）
    - （2）清空（.clear()）
    - （3）拷贝（.copy()）
    - （4）keys,vals ==> dict （.fromkeys()、  zip + dict()）
    - （5）items（“键值对”） ==> dict （ dict() ）
    - （6）dict ==> items（.items()）
    - （7）返回所有key （.keys()）
    - （8）返回所有value（.values()）
    - （9）返回指定key的val （.get()、 .setdefault()）
    - （10）删除key-val，并返回val。 （ .pop(), del）
    - （11）删除最后加入的元素，返回key-val。（.popitem()）
    - （12）判断是否存在key（in）
    - （13）长度（len）
    - （14）最值（max(d, key=d.get)）
    - （14）深拷贝
    - （15） 是否相同（==）
    - （16） keys、items 的 交集、并集、差集、补集 (&、|、-、^)
    - （30）排序（sorted）
    - （31）str《=》字典 （json.loads(), eval(), str()）
    - （32）拼接（dict(d1.items()+d2.tiems()), .update(d1), dict(d1, **d2)）
    - （33）字典计数 dic.get(i,0)
    - （34）字典 <==> namespace 
  - 4 有序字典（OrderedDict）
    - （1）把指定key-val移到最后。（.move_to_end()）
  - 5 计数器（Counter）
    - （1）创建Counter
    - （2）统计(序列)元素个数
    - （3）获取元素（.items）
    - （4）获取所有键key和value（.keys、.values）
    - （5）Conter 转 字典（dict）
    - （6）删除 元素(del)
    - （7）从Counter恢复序列(.elements)
    - （8）返回最多的k个数（.most_common）
    - （9）相加（.update、+）
    - （10）相减（.subtract、-）
    - （11）相交（&）
    - （12）合并（|）
    - （13）清空
    - （14）统计val的和
    - （15）移除val为0或负数的键值对（+）
    - （16）移除val为0或正数的键值对（-）
  - 6 矩阵（numpy）
    - （1）新建（全0、全1、对角、线性、无穷大小）
    - （2）修改 （条件修改、对角线赋值）
    - （3）插入 （pading）
    - （4）拼接（np.append、np.concatenate, np.stack(), np.vstack()）
    - （5）多份复制（np.repeat, np.tile）
    - （6）删除 （np.unique）
    - （7）尺寸（a.shape、 a.reshape(8,-1)）
    - （8）维度 （.ndim、np.newaxis、np.swapaxes） 
    - （9）计算（最大小/最大小索引、加减乘除、取整/求余、/绝对值/求和/平方/均值/标准差、对数/指数/范数、三角函数）
    - （10）全是Ture、存在Ture（ np.all()、 np.any() ）
    - （11）条件查找（np.where(), np.argwhere()）
    - （12）读取保存 npy（np.load、np.save） txt（np.loadtxt、np.savetxt）
    - （13）排序（np.sort  np.argsort）
    - （14）随机数（np.random）
    - （15）矩阵转置（.transpose）
    - （16）矩阵旋转（np.rot90）
    - （17）查看数据类型、转换（a.dtype、a.astype）
    - （18）异常值 NaN、Inf（np.isnan、np.isinf、np.nan_to_num）
    - （19）矩阵格式转换 （bytes：bytes()、x.tobytes()， list：x.tolist()）
  - 7 队列（queue）
    - （1）队列（）
    - （2）优先队列（.PriorityQueue）
    - （3） 双向队列（deque）
  - 8 堆（heapq）
    - （1）创建（.heapify(), .heappush()）
    - （2）插入（.heappush()）
    - （3）返回最小值（data[0]）
    - （4）删除最小值，并返回（.heappop()）
    - （5）删除最小值，再插入新元素（.heapreplace()）
    - （6）查找k个最大（小）值（.nlargest()）
    - （7）大顶堆（._heapify_max()）
  - 9 栈
  - 10 链表
    - （1） 单向链表
    - （2） 双向链表
  - 11 树
    - （1） 二叉树
    - （2） 完全二叉树
    - （3） 树
    - （4） 森林
  - 12 图
    - （1）有向图
    - （2）无向图
  - 13 LRU
    - （1）内置函数（@functools.lru_cache）
    - （2）自定义
 
 
 
----------------------------------------
- [03.关键词、变量](./Python/03.关键词、变量.md)
  - 1 关键词
  - 2 变量命名
    - （1）变量命名规则
    - （2）下划线命名(_)
  - 3 变量类型（局部、全局、非本地变量）
    - （1）局部变量
    - （2）全局变量（global）
    - （3）非本地变量（nonlocal）
  - 4 删除变量（del）
  - 5 引用传递
  - 6 变量地址（id）
  - 7 拷贝（浅拷贝、深拷贝）
    - （1）等号（=）
    - （2）浅拷贝（copy.copy）
    - （3）深拷贝（copy.deepcopy）
 
 
 
----------------------------------------
- [04.语句](./Python/04.语句.md)
  - 1 判断 （ if ） 
    - （1） 三目运算符 （ if else ）
  - 2 循环（for、while）
    - （1）两个 for 循环 在一句中
  - 3 （序列、字典、集合）推导式/循环+判断
    - （1）列表推导式
    - （2）字典推导式
    - （3）集合推导式
  - 5 一句写多行、多句写一行
    - （1）一句写多行
    - （2）多句写一行
  - 6 非法语句
 
 
 
----------------------------------------
 
 
 
----------------------------------------
- [06.函数](./Python/06.函数.md)
  - 1 普通函数
  - 2 内置函数/魔法函数
  - 4 匿名函数
  - 5 嵌套函数
  - 5 传参（*、**） 
    - （1）函数形参
    - （2）函数实参
  - 6 高阶函数
  - 7 闭包函数
 
 
 
----------------------------------------
- [07.常用函数（map、reduce、filter、lamda、列表推导式等）](./Python/07.常用函数.md)
  - 1 映射（map） 
  - 2 归纳（reduce）
  - 3 过滤（filter）
  - 4 匿名函数（lambda）
  - 5 时间、日期（time、datetime）
    - （1）time
    - （2）datetime
    - 6 打印
    - （1）打印字典（pprint）
      - （2） 打印对象
    - 6.5 枚举（enumerate、zip）
    - 6.5 next()
    - 6.5 zip()
    - 6.5 zip(*f)
    - 6.5 yield()
    - 6.5 __()
    - 6.5 不同文件间有全局变量吗？
    - 6.5 try
    - 6.2 断言函数（assert）
    - 6.4 数据增强
      - （1）augLy （facebook 开源）
    - 6.4 python 执行shell命令
    - 参数输入 到python 脚本 （argparse， sys.argv）
    - 6.4 argparse
    - 6.4 sys.argv[]
 
 
 
----------------------------------------
- [08.迭代器、生成器、装饰器](./Python/08.迭代器、生成器、装饰器.md)
  - 1 生成器
  - 2 迭代器
  - 3 装饰器 （ func(*args,**kwargs) + @ ）
    - （1）装饰器解释
    - （2）高阶函数+嵌套函数 = 装饰器 （func_timeout、lru_cache）
    - （2）类装饰器
    - （4）类方法 装饰器
 
 
 
----------------------------------------
- [09.面向对象](./Python/09.面向对象.md)
  - 1 继承/重写
    - （1） 继承
    - （2） 重写
    - （3） super重写
  - 2 多态
  - 3 类的访问控制
  - 4 接口类抽象类
  - 4 实例方法、静态方法(staticmethod) 和 类方法(classmethod)
  - 5 hasattr(), getattr(), setattr()
  - 6 查看类的方法和属性，dir()，help()   
  - 7 内建属性和方法（__str__,__repr__）
  - x 其他
    - （1） 多线程处理成员函数
 
 
 
----------------------------------------
- [10.模块、包](./Python/10.模块、包.md)
  - 1 import 导入模块
  - 2 文件__init__.py
  - 3 包__all__
 
 
 
----------------------------------------
- [11.多线程、多进程、协程](./Python/11.进程、线程、协程.md)
  - 1 多线程（multi threading）
    - （1）threading
    - （2）线程锁（Lock）
  - 2 多进程（multi processing）
    - （1）Queue
    - （2）进程池
  - 3 定时任务 + 多线程
 
 
 
----------------------------------------
- [12.编码方式](./Python/12.编码方式.md)
  - 1 编码种类（assic、GBK、Unicode、utf-8）
  - 2 url 编解码
  - 3 常见报错
    - （1）python3 打印中文时，编码报错
    - （2）python3 写入的文件名包含中文，报错
 
 
 
----------------------------------------
- [13.操作文件夹、文件、目录](./Python/13.操作文件.md)
  - 1 文件夹
    - （1）当前路径（getcwd）
    - （2）查看文件夹个数（listdir）
    - （3）文件 or 文件夹
    - （4）新建文件夹（mkdir）
    - （5）删除文件（os.rmdir()、os.rmtree()、os.remove()）
    - （6）复制文件（shutil.copyfile）
    - （7）移动文件（shutil.move）
    - （8）文件存在（os.path.exists）
    - （9）获取文件大小，创建时间和访问时间
    - （10）路径、文件、后缀分离
    - （11）获得目录
    - （12）重命名
    - （13）查看文件信息（创建时间、修改时间）
    - （14）检测文件是否更新
  - 2 文本（txt、csv）
    - （1）读（readlines）
    - （2）写（write）
  - 3 图像（jpg、bmp、png、webp、psd、gif，cv2、PIL）
    - （2）复制图片（copy）
    - （3）读取、保存（imread 、imwrite）
    - （4）格式转换
    - （5）尺度变换
    - （6）数据增强
        - 1）仿射变换、透视变换 
        - 2）剪切
        - 3）镜像
        - 4）擦除
  - 4 视频（mp4）
    - （1）读（fread）
    - （2）写（fwrite）
  - 5 音频文件（wav、mp3、acc，）
  - 6 表格（xlsx、xls）
    - （1） pandas
  - 7 文档 （word）
  - 7 字典（json、h5、yaml、pkl、pb、tfrecord）
    - （1）json 
    - （2）h5
    - yaml
    - pkl
    - pb
    - tfrecord
  - 4 mat
    - （1）保存（save）
    - （2）导入（loadmat）
 
 
 
----------------------------------------
- [14.画图](./Python/14.画图.md)
  - 1 二维
    - （1）legend () 
  - 2 三维
    - （1）plot_surface () 绘制面
    - （2）plot3() 绘制点
  - 3 图表
 
 
 
----------------------------------------
- [15.调试](./Python/15.调试.md)
  - 1 输入输出
  - 2 输出缓存（python -u） 
  - 3 退出（pass、return、sys.exit(0)）
 
 
 
----------------------------------------
- [16.注册器](./Python/16.注册器.md)
  - 1 目标检测(MMDetection)-Registry
 
 
 
----------------------------------------
- [20.常用开发工具](./Python/20.开发常用工具.md)
  - 1 数据库
    - （1） mySQL
    - （2） redis
    - （3） kafka
    - （4） 桶
  - 2 检索
    - （1） faiss
    - （2）其他检索工具
  - 3 定时任务
  - 4 日志
  - 5 python 执行 linux 命令
  - 6 查看系统平台Linux/Windows（platform）
 
 
 
----------------------------------------
  - 21.python、C++相互调用
    - 1 python调用C++
      - （1）pybind11
    - 2 C++调用python
 
 
 
----------------------------------------
- [22.Python 实现](./Python/22.Python实现（排序）.md)
  - 1 排序
    - （1） 快排
    - （2）堆排序
    - （3） 归并排序
    - （4） 桶排序
 
 
