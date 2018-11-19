# 正则表达式(RegularExpression,re)
- 是一个计算机科学的概念
- 用于使用单个字符串来描述,匹配符合某个规则的字符串
- 常常用来检索,替换某些模式的文本

# 正则的写法
- .(点号):表示任意一个字符,除了\n,比如查找所有的一个字符 \.
- []:匹配中括号中列举的任意字符,比如[L,Y,0], 可以LLY, Y0,不可以LIU
- \d:任意一个数字
- \D:除了数字都可以
- \s:表示空格,tab键
- \S:除了空白符号
- \w:单词字符, 就是a-z, A-Z, 0-9, _
- \W:除了  \w的都可以
- *"表示前面内容重复零次或者多次
- +:表示前面内容至少出现一次
- ?:问号可以表示重复前面内容的0次或一次，也就是要么不出现，要么出现一次。
- {m,n}:允许前面内容出现最少m次,最多n次
- ^:匹配字符串的开始
- $:匹配字符串的结尾
- \b:匹配单词的边界
- ():对正则表达式内容进行分组,从第一个括号开始,编号逐渐增大
    验证一个数字: ^\d$
    必须有一个数字,最少一位: ^\d+$
    只能出现数字,且位数为5-10位: ^\d{5,10}$
    注册者输入年龄,要求16岁以上,99岁以下: ^[16-99]$
    只能输入英文字符和数字: ^[A-Za-z0-9]$
    验证qq号码: [0-9]{5,12}
- \A:只匹配字符串开头, \Aabcd ,则abcd
- \Z:近匹配字符串末尾,abcd\Z,则abcd
- |:左右任意一个
- (?P<name>...):分组,除了原来的编号再制定一个别名,(?P<id>12345){2}
- (?P=name):引用分组


# Re使用大致步骤
- 使用compile将表示正则的字符串编译为一个patten对象
- 通过patten对象提供一系列方法对文本进行查找匹配,获得匹配结果,一个Match对象
- 最后使用Match对象提供的属性和方法获得信息,根据需要进行操作

# Re常用函数
- group():获得一个或者多个分组匹配的字符串,当要获得整个匹配的字符串时,直接使用group或者group(0)
- start:获取分组匹配的字符串在整个字符串中的起始位置,参数默认为0
- end:获取分组匹配的字符串在整个字符串中的结束位置,默认为0
- span:返回的结构技术(start(group)), end(group)

```python
import re
#查找数字
#r表示字符串不转义
p = re.compile(r'\d+')
#在字符串"one12twothree33456four78"中进行查找,按照规则p置顶的正则进行查找
m = p.match("one12twothree33456four78")
print(m)

```
```python
import re
#查找数字
#r表示字符串不转义
p = re.compile(r'\d+')
#在字符串"one12twothree33456four78"中进行查找,按照规则p置顶的正则进行查找
m = p.match("one12twothree33456four78", 3, 6)
print(m)
#上述代码说明的问题
#1.match可以输入参数表示起始位置
#2.查找到的结果只包含一个,表示第一次进行匹配成功的内容
print(m[0])
print(m.start(0))
print(m.end(0))
```
```python
import re
# I表示忽略大小写
p = re.compile(r'([a-z]+) ([a-z]+)', re.I)

m = p.match("I am really love taozi")
print(m)
```

# 查找
- search(str, [, pos[, endpos]]):在字符串中查找匹配,pos和endpos表示起始位置
- findall:查找所有
- finditer:查找,返回一个iter结果

```python
import re
p = re.compile(r'\d+')

m = p.search("one12two34three567four")
print(m.group())

```

# sub替换
- sub(rep1, str[,count])
```python
import re
p = re.compile(r'(\w+) (\w+)')
s = "hello 123 tao 456 zi, i love you" 
rst = p.sub(r'Hello world', s)
print(rst)

```

# 匹配中文
- 大部分中文内容表示范围是[u4e00-u9fa5],不包括全角标点

# 贪婪和非贪婪
- 贪婪:尽可能多的匹配, (*)表示贪婪匹配
- 非贪婪:找到符合条件的最小内容即可,(?)表示非贪婪
- 正则默认使用贪婪匹配
