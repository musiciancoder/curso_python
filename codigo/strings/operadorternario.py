import re

text = r"a\nz"

resuñt = re.match(r"a\nz",  text)

print("No match" if resuñt is None else resuñt.group())

