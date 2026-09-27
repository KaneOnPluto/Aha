import re
pattern = "C"
sequence1 = "IceCream"

# No match since "C" is not at the start of "IceCream" re.match(pattern, sequence1)
sequence2 = "Cake"

v2=re.match(pattern,sequence2)

print(v2)


txt = "The rain in Spain"
x = re.match("^The.*Spain$", txt)
print(x)

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
