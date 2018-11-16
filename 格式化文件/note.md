# 结构化文件存储
- xml, json
- 为了解决不同设备之间信息交换
# xml文件(可扩展标记语言)
- 标记语言:语言中使用尖括号括起来的文本字符串标记
- 可扩展:用户可以自己定义需要的标记
- 例如:
    <Tercher>
        自定义标记Tercher
    </Tercher>
- 是w3c组织制定的一个标准
- XML描述的是数据本身,即数据的结构和语义
- HTML侧重于如何显示web页面中的数据
- XML文档的构成
    -  处理命令(可以认为一个文件内只有一个处理命令)
        - 最多只有一行
        - 必须在第一行
        - 内容是与XML本身处理相关的一些生命或者指令
        - 以xml关键字开头
        - 一般用于生命xml的版本和采用的
            - version属性是必须的
            - encoding属性用来指出xml解释器使用的编码
    - 根元素(一个文件内只有一个根元素)
        - 在整个xml文件中,可以把他看做一个树形结构
        - 根元素有且只能有一个
    - 子元素
    - 属性
    - 内容
        - 表明标间所存储的信息
    - 注释
        - 说明作用的信息
        - 注释不能嵌套在标签里
        - 只有在注释的开始和结尾使用双短横线
        - 三短横线只能出现在注释的开头而不能够用在结尾
            <name> <!-- aaa --> </name> # 可以
            <name <!-- aaa -->> </name> # 不可以,注释在标签内
            
            <!-- my-name-by-yang--> # 可以,注释内容可以有一个短横线
            <!-- my--name--by--yang--> #不可以,双短横线只能出现在开头或结尾
            
            <!--- my-name--> # 可以,三短横线只能出现在开头
            <!--- my-name---> #不可以,三短横线只能出现在开头
    
- 保留字符的处理
    - XML中使用的符号可能跟实际符号相冲突,典型的就是左右尖括号
    - 使用实体引用
        <score> score>80 </score> # 有错误,XMl中不能出现>
        <score> score&gt;80</score> #使用实体引用
    - 把含有保留字符的部分放在CDATA块内部,CDATA块把内部信息视为不需要转义
        <![CDATA[
            select name,age
            from Student
            where score>80
        ]]>
    - 常用的需要转义的保留字符和对应实体引用
        - %:&amp;
        - <:&lt;
        - >:&gt;
        - ':&apos;
        - ":&quot;
        - 一共五个,每个实体引用都以&开头并且以分号结尾
- XML标签的命名规则
    - Pascal的命名法
    - 用单词表示,第一个字母大写
    - 大小写严格区分
    - 配对的标签必须一致
- 命名空间
    - 为了防止命名冲突
        <Student>
            <Name>Yang</Name>
            <Age>23</Age>
        </Student>
        <Room>
            <No>2015</No>
            <Location>1-23-1</Location>
        </Room>
    - 如果归并上述两个内容信息,会产生冲突
    - 为了避免冲突,需要给可能冲突元素添加命名空间
    - xmlns: xml name space 的缩写
        <Schooler xmlns:student="http://my_student" xmlns:room="my_room">
            <student:Name>Yang</student:Name>
            <Age>23</Age>
            <room:Name>2015</room:Name>
            <Location>1-23-1</Location>
        </Schooler>

# XML访问
## 读取
- XML读取分两个主要技术,SAX, DOM
- SAX(Simple API for XML):
    - 基于事件驱动的API
    - 利用SAX解析文档设计到解析器和事件处理两部分
    - 特点:
        - 快
        - 流式读取
- DOM
    - 是W3C规定的XML的编程接口
    - 一个XML文件在缓存中以树形结构保存,读取
    - 用途
        - 定位浏览XML任何一个节点信息
        - 添加删除相应内容
    - minidom
    - etree
- XML文件写入
    - 更改
        - ele.set:修改属性
        - ele.append:添加子元素
        - ele.remove:删除元素
    - 生成创建
        - SubElement
        - minidom写入
        - etree创建
        
    
        