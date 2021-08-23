from bs4 import BeautifulSoup


f = open("courses2.xml","rt")
content = f.read()
f.close()
bs = BeautifulSoup(content, 'lxml-xml')
courses = bs.find_all("course")
for course in courses:
    name = course['name']
    fee = course['fee']
    print(f"{name:20} {fee:6}")


