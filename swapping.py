#a=10
#b=20

#temp=a
#a=b
#b=temp

#print(a)
#print(b)


#second way to right same programe

#a=10            #101 3 bits
#b=20            #110 3 bits

#a=a+b            #30
#b=a-b            #10
#a=a-b            #20

#print(a)
#print(b)

#Third way to right this programe(using XOR operator)
#XOR operator does not contain the extra byte for the swapping)

#a=10
#b=20

#a=a^b
#b=a^b
#a=a^b

#print(a)
#print(b)

#Fourth way to right the programe

a=10
b=20

a,b=b,a

print(a)
print(b)

