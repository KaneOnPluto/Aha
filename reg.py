import re

pattern = r"world"
text = "Hello, world!"

if re.match(pattern, text):
    print("Match found!")
else:
    print("No match!")
