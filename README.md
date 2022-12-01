# Python
python notebook（笔记）
运行环境为 python3


**目录：**

------------------------------------------------
- [01.基本数据类型](#01基本数据类型)
  - [1 整数](#1-整数)
    - [（1）比较运算符（\<、\>、\<=、\>=、 ==、 != ）](#1比较运算符---)
    - [（2）算术运算符（+、-、\*、/、%、\*\*、//） , 平方（pow）](#2算术运算符---平方pow)
    - [（3）赋值运算符（ = ）](#3赋值运算符--)
    - [（4）位运算符（\&、|、^、~、\>\>、\<\<）](#4位运算符)
    - [（5）转进制 （int、bin、oct、hex）](#5转进制-intbinocthex)
    - [（6）判断奇偶（\&1、%2）](#6判断奇偶12)
  - [2 浮点数](#2-浮点数)
    - [（1）书写形式](#1书写形式)
    - [（2）最大值](#2最大值)
    - [（3）无穷小、大](#3无穷小大)
    - [（4）取整](#4取整)
    - [（5）计算的不精确](#5计算的不精确)
  - [3 复数](#3-复数)
  - [4 布尔值/布尔类型](#4-布尔值布尔类型)
    - [（1）布尔类型（True、False）](#1布尔类型truefalse)
    - [（2）布尔运算（and、or、not）](#2布尔运算andornot)
  - [5 空值](#5-空值)
  - [6 字符串](#6-字符串)
    - [（1）新建](#1新建)
    - [（2）拆分（.split）](#2拆分split)
    - [（3）拼接（+）](#3拼接)
    - [（4）代替（.replace）](#4代替replace)
    - [（5）删除（.strip）](#5删除strip)
    - [（6）查找（.find、.index）](#6查找findindex)
    - [（7）计数（.count）（子字符串）](#7计数count子字符串)
    - [（8）字符串格式化(.format、zfill)](#8字符串格式化formatzfill)
    - [（9）比较](#9比较)
    - [（10）转义字符（\\）](#10转义字符)
    - [（11）str  \<==\>  bytes](#11str----bytes)
    - [（12）str  \<==\>  list](#12str----list)
    - [（13）正则（re.search）](#13正则research)
    - [（14）判断字符串中是否有汉字](#14判断字符串中是否有汉字)
    - [（15）编辑距离（Levenshtein）](#15编辑距离levenshtein)
  - [7 类型判断（type、isinstance）](#7-类型判断typeisinstance)


------------------------------------------------
- [02.其他数据类型](#其他数据类型)
  - [1 序列（tuple 、list）](#1-序列tuple-list)
    - [（1） 新建（\[0\] \* n、range）](#1-新建0--nrange)
    - [（2） 拼接成字符串（''.join(list)）](#2-拼接成字符串joinlist)
    - [（3） 添加元素（.append、.extend、+）](#3-添加元素appendextend)
    - [（4） 删除元素（.remove、.pop、del）](#4-删除元素removepopdel)
    - [（5） 排序（.sort、sorted）](#5-排序sortsorted)
    - [（6） 反序（reversed）](#6-反序reversed)
    - [（7） 乱序（random.shuffle）](#7-乱序randomshuffle)
    - [（7） 随机选择（shuffle）](#7-随机选择shuffle)
    - [（8） 查找元素（in、.index）](#8-查找元素inindex)
    - [（9） 清空list](#9-清空list)
    - [（10） 合并/拼接（+）， 分片](#10-合并拼接-分片)
    - [（11） 去重（set）](#11-去重set)
    - [（12） \*list](#12-list)
  - [2 集合](#2-集合)
    - [（1）新建（{}，set()）](#1新建set)
    - [（2）加入（.add()，.update()）](#2加入addupdate)
    - [（3）删除（.remove()，.discard()，pop()）](#3删除removediscardpop)
    - [（4）长度（len()）](#4长度len)
    - [（5）清空（.clear()）](#5清空clear)
    - [（6）是否存在（in）](#6是否存在in)
    - [（7）集合运算（-，|，\&，^）](#7集合运算-)
  - [3 字典](#3-字典)
    - [（1）新建（{}、.setdefault()、dict()、defaultdict）](#1新建setdefaultdictdefaultdict)
    - [（2）清空（.clear()）](#2清空clear)
    - [（3）拷贝（.copy()）](#3拷贝copy)
    - [（4）keys,vals ==\> dict （.fromkeys()、  zip + dict()）](#4keysvals--dict-fromkeys--zip--dict)
    - [（5）items（“键值对”） ==\> dict （ dict() ）](#5items键值对--dict--dict-)
    - [（6）dict ==\> items（.items()）](#6dict--itemsitems)
    - [（7）返回所有key （.keys()）](#7返回所有key-keys)
    - [（8）返回所有value（.values()）](#8返回所有valuevalues)
    - [（9）返回指定key的val （.get()、 .setdefault()）](#9返回指定key的val-get-setdefault)
    - [（10）删除key-val，并返回val。 （ .pop() ）](#10删除key-val并返回val--pop-)
    - [（11）删除最后加入的元素，返回key-val。（.popitem()）](#11删除最后加入的元素返回key-valpopitem)
    - [（12）判断是否存在key（in）](#12判断是否存在keyin)
    - [（13）长度（len）](#13长度len)
    - [（14）最值（max(d, key=d.get)）](#14最值maxd-keydget)
    - [（14）深拷贝](#14深拷贝)
    - [（15） 是否相同（==）](#15-是否相同)
    - [（16） keys、items 的 交集、并集、差集、补集 (\&、|、-、^)](#16-keysitems-的-交集并集差集补集--)
    - [（30）排序（sorted）](#30排序sorted)
    - [（31）str《=》字典 （json.loads(), eval(), str()）](#31str字典-jsonloads-eval-str)
    - [（32）拼接（dict(d1.items()+d2.tiems()), .update(d1), dict(d1, \*\*d2)）](#32拼接dictd1itemsd2tiems-updated1-dictd1-d2)
    - [（33）字典计数 dic.get(i,0)](#33字典计数-dicgeti0)
    - [（34）字典 \<==\> namespace](#34字典--namespace)
  - [4 有序字典（OrderedDict）](#4-有序字典ordereddict)
    - [（1）把指定key-val移到最后。（.move\_to\_end()）](#1把指定key-val移到最后move_to_end)
  - [5 计数器（Counter）](#5-计数器counter)
    - [（1）创建Counter](#1创建counter)
    - [（2）统计(序列)元素个数](#2统计序列元素个数)
    - [（3）获取元素（.items）](#3获取元素items)
    - [（4）获取所有键key和value（.keys、.values）](#4获取所有键key和valuekeysvalues)
    - [（5）Conter 转 字典（dict）](#5conter-转-字典dict)
    - [（6）删除 元素(del)](#6删除-元素del)
    - [（7）从Counter恢复序列(.elements)](#7从counter恢复序列elements)
    - [（8）返回最多的k个数（.most\_common）](#8返回最多的k个数most_common)
    - [（9）相加（.update、+）](#9相加update)
    - [（10）相减（.subtract、-）](#10相减subtract-)
    - [（11）相交（\&）](#11相交)
    - [（12）合并（|）](#12合并)
    - [（13）清空](#13清空)
    - [（14）统计val的和](#14统计val的和)
    - [（15）移除val为0或负数的键值对（+）](#15移除val为0或负数的键值对)
    - [（16）移除val为0或正数的键值对（-）](#16移除val为0或正数的键值对-)
  - [6 矩阵（numpy）](#6-矩阵numpy)
    - [（1）新建（全0、全1、对角、线性、无穷大小）](#1新建全0全1对角线性无穷大小)
    - [（2）修改 （条件修改、对角线赋值）](#2修改-条件修改对角线赋值)
    - [（3）插入 （pading）](#3插入-pading)
    - [（4）拼接（np.append、np.concatenate, np.stack(), np.vstack()）](#4拼接npappendnpconcatenate-npstack-npvstack)
    - [（5）多份复制（np.repeat, np.tile）](#5多份复制nprepeat-nptile)
    - [（6）删除 （np.unique）](#6删除-npunique)
    - [（7）尺寸（a.shape、 a.reshape(8,-1)）](#7尺寸ashape-areshape8-1)
    - [（8）维度 （.ndim、np.newaxis、np.swapaxes）](#8维度-ndimnpnewaxisnpswapaxes)
    - [（9）计算（最大小、最大小索引、加减乘除余、绝对值/求和/平方/均值/标准差、对数/指数/范数、三角函数）](#9计算最大小最大小索引加减乘除余绝对值求和平方均值标准差对数指数范数三角函数)
    - [（10）全是Ture、存在Ture（ np.all()、 np.any() ）](#10全是ture存在ture-npall-npany-)
    - [（11）条件查找（np.where(), np.argwhere()）](#11条件查找npwhere-npargwhere)
    - [（12）读取保存 npy（np.load、np.save） txt（np.loadtxt、np.savetxt）](#12读取保存-npynploadnpsave-txtnploadtxtnpsavetxt)
    - [（13）排序（np.sort  np.argsort）](#13排序npsort--npargsort)
    - [（14）随机数（np.random）](#14随机数nprandom)
    - [（15）矩阵转置（.transpose）](#15矩阵转置transpose)
    - [（16）矩阵旋转（np.rot90）](#16矩阵旋转nprot90)
    - [（17）元素数据类型、转换（a.dtype、a.astype）](#17元素数据类型转换adtypeaastype)
    - [（18）异常值 NaN、Inf（np.isnan、np.isinf、np.nan\_to\_num）](#18异常值-naninfnpisnannpisinfnpnan_to_num)
    - [（19）矩阵格式转换 （《==》 bytes、list）](#19矩阵格式转换--byteslist)
  - [7 队列（queue）](#7-队列queue)
    - [（1）队列（）](#1队列)
    - [（2）优先队列（.PriorityQueue）](#2优先队列priorityqueue)
    - [（3） 双向队列（deque）](#3-双向队列deque)
  - [8 堆（heapq）](#8-堆heapq)
    - [（1）创建（.heapify(), .heappush()）](#1创建heapify-heappush)
    - [（2）插入（.heappush()）](#2插入heappush)
    - [（3）返回最小值（data\[0\]）](#3返回最小值data0)
    - [（4）删除最小值，并返回（.heappop()）](#4删除最小值并返回heappop)
    - [（5）删除最小值，再插入新元素（.heapreplace()）](#5删除最小值再插入新元素heapreplace)
    - [（6）查找k个最大（小）值（.nlargest()）](#6查找k个最大小值nlargest)
    - [（7）大顶堆（.\_heapify\_max()）](#7大顶堆_heapify_max)
  - [9 栈](#9-栈)
  - [10 链表](#10-链表)
    - [（1） 单向链表](#1-单向链表)
    - [（2） 双向链表](#2-双向链表)
  - [11 树](#11-树)
    - [（1） 二叉树](#1-二叉树)
    - [（2） 完全二叉树](#2-完全二叉树)
    - [（3） 树](#3-树)
    - [（4） 森林](#4-森林)
  - [12 图](#12-图)
    - [（1）有向图](#1有向图)
    - [（2）无向图](#2无向图)
  - [13 LRU](#13-lru)
    - [（1）内置函数（@functools.lru\_cache）](#1内置函数functoolslru_cache)
    - [（2）自定义](#2自定义)


------------------------------------------------
* [03.关键词、变量](/Python/03.关键词、变量.md)
  - [1 关键词]
  - [2 变量命名]
  - [3 变量类型（局部、全局、非本地变量）]
  - [4 删除变量（del）]
  - [5 引用传递]
  - [6 变量地址（id）]
  - [7 拷贝（浅拷贝、深拷贝）]

------------------------------------------------
* [04.语句](/Python/04.语句.md)
  - [1 判断 （ if ）]
  - [2 循环（for、while）]
  - [3 （序列、字典、集合）推导式/循环+判断]
  - [5 一句写多行、多句写一行]
  - [6 非法语句]


------------------------------------------------
* [05.运算符](/Python/05.运算符.md)



------------------------------------------------
* [06.函数](/Python/06.函数.md)
  - [1 普通函数]
  - [2 内置函数/魔法函数]
  - [4 匿名函数]
  - [5 嵌套函数]
  - [5 传参（*、**）]
  - [6 高阶函数]
  - [7 闭包函数]


------------------------------------------------
* [07.常用函数](/Python/07.常用函数.md)
  - [1 映射（map）]
  - [2 归纳（reduce）]


------------------------------------------------
* [08.迭代器、生成器、装饰器](/Python/08.迭代器、生成器、装饰器.md)
  - [1 生成器]
  - [2 迭代器]
  - [3 装饰器 （ func(*args,**kwargs) + @ ）]


------------------------------------------------
* [09.面向对象](/Python/09.面向对象.md)
  - [1 继承/重写]
  - [2 多态]
  - [3 类的访问控制]
  - [4 接口类抽象类]
  - [5 hasattr(), getattr(), setattr()]
  - [6 查看类的方法和属性，dir()，help()]
  - [x 其他]

------------------------------------------------
* [10.模块、包](/Python/10.模块、包.md)
  - [x.1 import 导入模块]


------------------------------------------------

* [13.操作文件夹、文件](#13操作文件夹文件)
  - [1 文件夹](#1-文件夹)
    - [（1）当前路径（getcwd）](#1当前路径getcwd)
    - [（2）查看文件夹个数（listdir）](#2查看文件夹个数listdir)
    - [（3）查看指定格式的文件](#3查看指定格式的文件)
    - [（4）新建文件夹（mkdir）](#4新建文件夹mkdir)
    - [（5）删除文件（os.rmdir()、os.rmtree()、os.remove()）](#5删除文件osrmdirosrmtreeosremove)
    - [（6）复制文件（shutil.copyfile）](#6复制文件shutilcopyfile)
    - [（7）移动文件（shutil.move）](#7移动文件shutilmove)
    - [（8）文件存在（os.path.exists）](#8文件存在ospathexists)
    - [（9）获取文件大小，创建时间和访问时间](#9获取文件大小创建时间和访问时间)
    - [（10）路径、文件、后缀分离](#10路径文件后缀分离)
    - [（11）获得目录](#11获得目录)
    - [（12）重命名](#12重命名)
    - [（13）查看文件信息](#13查看文件信息)
    - [（14）检测文件是否更新](#14检测文件是否更新)
  - [2 文本（txt、csv）](#2-文本txtcsv)
    - [（1）读（readlines）](#1读readlines)
    - [（2）写（write）](#2写write)
  - [3 图像（jpg/bmp）](#3-图像jpgbmp)
    - [（2）复制图片（copy）](#2复制图片copy)
    - [（3）读取、保存（imread 、imwrite）](#3读取保存imread-imwrite)
    - [（4）格式转换](#4格式转换)
    - [（5）尺度变换](#5尺度变换)
    - [（6）数据增强](#6数据增强)
        - [1）仿射变换、透视变换](#1仿射变换透视变换)
        - [2）剪切](#2剪切)
        - [3）镜像](#3镜像)
        - [4）擦除](#4擦除)
  - [4 视频（mp4）](#4-视频mp4)
    - [（1）读（fread）](#1读fread)
    - [（2）写（fwrite）](#2写fwrite)
  - [5 音频文件（wav、mp3）](#5-音频文件wavmp3)
  - [6 表格（xlsx、xls）](#6-表格xlsxxls)
    - [（1） pandas](#1-pandas)
  - [7 文档 （word）](#7-文档-word)
  - [7 字典（json、h5）](#7-字典jsonh5)
    - [（1）json](#1json)
    - [（2）h5](#2h5)
    - [yaml](#yaml)
    - [pkl](#pkl)
    - [pb](#pb)
    - [tfrecord](#tfrecord)
  - [4 mat](#4-mat)
    - [（1）保存（save）](#1保存save)
    - [（2）导入（loadmat）](#2导入loadmat)



