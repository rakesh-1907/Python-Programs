#from array import *

#vals=array('i',[5,-9,10,11,16,9])
#vals.append(100)
#vals.reverse()

#for i in range(len(vals)):
#  print(vals[i])





#from array import *

#vals=array('u',['a','b','c','d'])

#for i in range(len(vals)):
#  print(vals[i])

from array import *

vals=array('i',[5,-9,10,11,16,9])

newArray= array(vals.typecode, ( a*a for a in vals))

for i in newArray:
  print(i)
