# pass is a null statement that dose nothing. it is used as a placeholder for future code

for i in range(1,11):
    pass


# Qn.1 Wap find sum n number
n = int(input("Enter number : "))
sum = 0
for i in range(1,n+1):
    sum += i
print("Totle number sum = ",sum)



# Qn.2 find the first factorial of n number
n = int(input("Enter number : "))
fact = 1
for i in range(1,n+1):
    fact *= i
print("Totle number factorial = ",fact)
