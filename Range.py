# Range function returns a squence of numbers, starting from 0 by Defuilt,and increments by 
# 1 (by defuild),and stops before a specified number.



seq = range(11)  # stop

for i in seq:
    print(i)      

for i in range(2,10): # (Star,Stop)
    print(i)      

for i in range(2,12,2): # multyplcation
    print(i)          

for i in range(2,101,2): # even number
    print(i)          

for i in range(1,101,2):   # odd
    print(i)          

for i in range(1,101):   # 1 to hundred print
    print(i)          

for i in range(100,0,-1):   # 100 to 1 print
    print(i)          

n = int(input(" enter number : "))
for i in range(1,11):
    print(n*i)    