import re
ss = "I am a HBUer, and you?"
# 从字符串起始位置开始匹配一个模式
res = re.match(r'((\w)+(\W))+', ss)
# 其中 '((\w)+(\W))+' 就是一个模式
# ss 是目标字符串
# res.group() 返回整个字符串
print(res.group())
# I am a HBUer,
# res.group(1) 返回第n个对应的字符串 n从1开始
print(res.group(1))
# HBUer
# re.search()会扫描整个字符串
res = re.search(r'(\w+)(,)', ss)
print(res.group(0))
print(res.group(1))
print(res.group(2))
# HBUer,
# HBUer
# ,
# split()方法按照能够匹配的子串将字符串分割， 返回一个列表
ss_tosplit = "I am a HBUer, and you?"
res = re.split(r"\W+", ss_tosplit)
print(res)
# ['I', 'am', 'a', 'HBUer', 'and', 'you', '']
# sub()用于字符串的替换，替换其中每一个匹配的子串后返回后的字符串
res = re.sub(r"(\w+)(\?)", "her?", ss)
print(res)

