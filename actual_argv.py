#Example of positional arguments
def person(name,age):
    print(name)
    print(age)

person("shaurya",9)

#Example of keyword arguments
def person(name,age):
    print(name)
    print(age)

person(age=9,name='shaurya')

#Example of default arguments
def person(name,age=9):
    print(name)
    print(age)

person('shaurya')


#Example of variable length arguments
def sum(a,*b):

     c=a

     for i in b:
         c= c+i
     print(c)

sum(5,6,34,78)
