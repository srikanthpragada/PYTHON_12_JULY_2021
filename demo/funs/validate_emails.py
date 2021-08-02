def isValidEmail(email):
    pos = email.find("@")
    if pos == -1:
        return False

    return pos > 0 and pos < len(email) - 1


emails = ['abc', 'abc@gmail.com', 'abc@', '@li', 'li@yahoo']

for e in filter(isValidEmail, emails):
    print(e)
