from numpy import *

arr1 = array ([

            [1,2,3,4,9,10],
            [5,6,7,8,11,12]

])

arr2 = arr1.flatten()

arr3 = arr2.reshape(2,2,3)

print(arr3)