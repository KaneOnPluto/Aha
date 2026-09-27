import re
txt = "The rain in Spain"
x = re.match("^The.*Spain$", txt)
print(x)

txt = "The rain in Spain an ai"
x = re.findall("ai", txt)
print(x)

pattern = "cookie"
sequence = "Cake and cookie"

s=re.search(pattern, sequence)

if s:
    print("match found at position",s.start())
else:
    print("match not found")



pattern = r"world"
text = "Hello, world!"

match = re.search(pattern, text)

if match:
    print("Match found at position:", match.start())
else:
    print("No match!")

pattern = r"world"
text = "Hello, world!"

if re.match(pattern, text):
    print("Match found!")
else:
    print("No match!")




