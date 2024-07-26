# 1.Wap to input uder's First name & print its lenth

First_Name = "RAj"
print(len(First_Name))




# 2.Wap to find the Occurrence of 'S' in a String

str = "MY NAME ANTHANI GONSALIV, hi, $ I $am $ symbol $"
print(str.count('$'))




# 3.Wap  to check if a number intered by user is odd or evem

num = int(input("Enter you'r nummber: "))
rem = num % 2

if(rem == 0):
    print("EVEN")

else:
    print("ODD")


# 4.Write a program to find the greatest of 3 numbers entered by the user

a = int(input("Enter You'r 1st number: "))
b = int(input("Enter You'r 2nd number: "))
c = int(input("Enter You'r 3rd number: "))
d = int(input("Enter You'r 4th number: "))

if(a>b and a>c and a>d):
      print("1st is Greatest")

elif(b>c and b>a and b>d):
     print("2nd is Greatest")

elif(c>a and c>b and c>d):
     print("3rd is Greatest")

elif(a == b == c == d):
     print("All are equal")

else:
     print("4th is Greatest")




# 5. Wap to check if a number is a multiple of 7 or not


x = int (input("Enter x number"))

if(x % 7 == 0):
     print("multiple of 7")

else:
     print("not a multiple")