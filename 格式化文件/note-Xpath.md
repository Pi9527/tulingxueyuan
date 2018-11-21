# XPath
- 在XMl文件中查找信息的一套规则/语言,根据XML的元素或者属性进行遍历
# XPath开发工具
- 开源XPath表达式编辑工具:XMLQuire
- Chrome插件:XPath Helper
- Firefox插件:XPath Checker

# 选取节点
- nodename:选取此节点的所有子节点
- /: 从根节点开始选取
- //: 选取节点,不考虑位置,选取多个节点,一般组成列表返回
- .:选取当前节点
- ..:选取当前节点的父节点
- @:选取属性
- XPath中查找一般按照路径方法查找,

# 谓语-Predicates
- /School/Student[1]:选取School下面的第一个Student节点
- /School/Student[last()]:选取School下面的最后一个Student节点
- /School/Student[last()-1]:选取School下面的倒数第二个Student节点
- /School/Student[last()<3]:选取School下面的前二个Student节点
- //School/Student[@score]:选取带有属性score的Student节点
- //School/Student[@score="99"]:选取带有属性score并且属性值是99的Student节点
- //School/Student[@score]/Age:选取带有属性score的Student节点的子节点Age

# XPath的一些操作
- ｜:或者
.
.
.
.


