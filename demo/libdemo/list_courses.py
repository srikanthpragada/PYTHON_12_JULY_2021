from bs4 import BeautifulSoup


f = open("courses.xml","rt")
content = f.read()
f.close()
bs = BeautifulSoup(content, 'lxml-xml')
courses = bs.find_all("course")
for course in courses:
    name = course.find("name").text
    fee = course.find("fee").text
    print(f"{name:20} {fee:6}")


