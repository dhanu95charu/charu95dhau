z=(list(map(lambda x:x+5,lst)))
print(z)

from functools import reduce
p=reduce(lambda x,y:x+y,a)
print(p)

b=(1,1,1,1)
c=(list(map(lambda x,y:x+y,lst,b)))
print(c)

d=(list(map(lambda x,y:x*y,lst,b)))
print(d)

fruits=['mango','orange','apple','kiwi']
e=(list(filter(lambda x:'a' not in x,fruits)))
print(e)
