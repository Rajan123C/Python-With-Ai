# 1.Write a program to ask the user to enter names of their 4 favrate movies & store them in a Movies

Movies = []
mov1 = input("Enter You'r 1st Favrate movie :")
mov2 = input("Enter You'r 2st Favrate movie :")
mov3 = input("Enter You'r 3st Favrate movie :")
mov4 = input("Enter You'r 4st Favrate movie :")

Movies.append(mov1)
Movies.append(mov2)
Movies.append(mov3)
Movies.append(mov4)

print(Movies)
print(type(Movies))

# 2.Wap to check if a list contains a plindrome of elements.(Use copy() methord)
# Palindrome is sidha pad ya ualta pad same hi lagta hai rx.(1,2,3,2,1) , (1,"abc","abc",1) , 'ma'am' , "RacecaR"


list = [1,2,3,1]

list1 = list.copy()
list1.reverse()

if(list1 == list):
    print("List Is Palindrome")
else:
    print("List Isn't Palindrome")    
   

# 3.Wap to count the number  of student with the "A" grade of the following tuple 



grade = ("C","D","A","A","B","B","A","B","A")

print(grade.count("A"))







# 4.store the above values in a list & short them from "A" to "D" 


gre = ["C","D","A","A","B","A","B","A"]
gre.sort()
print(gre)














































