# 1.Write a program to input 2 numbers & print their sum

a = int(input("Enter 1nd num :-"))
b = int(input("Enter 2nd num :-"))

print ("Sum Done =",a+b)

# 2.WAP to input side of a square & print its area

side = float(input("Enter the area of square :"))
area = side * side # we can also do (side ** 2) same answer
print("Area of square",area)


# 3.WAP to input flooting point numbers & print their average

a = float(input("Enter 1st value :"))
b = float(input("Enter 2nd value :"))
c = (a+b) / 2
print("Average value is :",c)


# 3.WAP to input 2 int numbers a and b.
#print true if a is greter than or equal to b. if not print false

a = int(input("Enter 1st num :"))
b = int(input("Enter 2st num :"))
c = True if a > b or a == b else False
print("Answer :",c)




