import re
pattern = "cookie"
sequence = "Cake and cookie"

v1=re.search(pattern, sequence)
print(v1)
