import re
from distutils.log import warn as printf 
patten = '\w+\s\w+'
data = 'hello ,wang gang,li ming,cang shuya'
ss = re.findall(patten,data)
printf(ss)
