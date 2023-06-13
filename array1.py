from array import *

arr=array("i",[])

x=int(input("Enter the length of the value"))

for i in range(x):
    y=int(input("Enter the value"))
    arr.append(y)

print(arr)

k=0
val=int(input("Enter the value for search"))
for e in arr:
    if e==val:
        print(k)
        break

    k+=1

print(arr.index(val)) # this is  function to print index value of the value #  if you using this function u do not need use any loop.
