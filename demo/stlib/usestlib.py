import sys

sys.path.insert(0, r'c:\classroom\july12\demo\mylib')

print(sys.path)

import str_funs as sf
from str_funs import isvalidmobile

s = "abc123"

print(sf.hasdigit(s))
print(isvalidmobile("3434343433"))
