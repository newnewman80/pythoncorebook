import re
data = '3120 De la Cruz Boulevard'
patten = r'\d+ .*'
print(re.match(patten,data).group())
