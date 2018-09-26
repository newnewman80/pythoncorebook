from distutils.log import warn as printf
import re
patt='[bh][aiu]t'
data='aaabatbbbbb'
printf(re.search(patt,data).group())

