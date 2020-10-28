#from a.b.c import packages_ex
import a.b.c.packages_ex
from sys import path
path.pop(0)
for loc in path:
    print(loc)

dir(a.b.c.packages_ex.print_msg())

