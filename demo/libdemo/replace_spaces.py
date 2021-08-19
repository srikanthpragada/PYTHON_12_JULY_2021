import re

f = open("test.txt", "rt")
content = f.read()
f.close()

result = re.sub(r" +", " ", content)
f = open("test.txt", "wt")
f.write(result)
f.close()
