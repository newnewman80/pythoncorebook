import re
patt='[A-Za-z_]+[\w_]+'
ss='ac_eed'
print(re.match(patt,ss).group())
