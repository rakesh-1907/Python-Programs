#i = 1
#while i <= 10:
#    if i % 3 != 0:
#     print(i)
#    i+=1



for i in range(1,101):
    if i%3==0 or i%5==0:
        continue
    print(i)

print("Bye")