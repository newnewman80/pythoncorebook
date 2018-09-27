import re
patten = '(\w+\.)?\w+\.[com|net]'
data = 'www.baidu.net'
print(re.search(patten,data).group())

