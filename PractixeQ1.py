# 1.Store following word meaning in a python dictonary

dict = {
   "table" : ["a piece of furniture", "list of facts & figgures"],
   "cat"   : "a small animal",
}

print(dict)





# 2.you are given a list of subjects for students,Assume one classroom is required for 1 subject,
# how many classrooms are needed by all student.



Subject = {
    "Python","Java","C++","Python",
    "C","JavaScript","Python","Java",
    "C++","C",

}

print(len(Subject))
print(Subject)

# 3.WAP to enter marks of 3 subjexts  from the user and store them in a Dictonary.start with 
# an empty Dictonary & add one by one .use subject name as key & marks as value.

marks = {}

x = int(input("Enter chem :"))
marks.update({"chem" : x})

y = int(input("Enter phy :"))
marks.update({"phy" : y})

z = int(input("Enter math :"))
marks.update({"math" : z})

print(marks)







# 4.figure out the way to store 9 & 9.0 as separate value in the set.
# (you can take help of build-in data types)

saparate = {9,"9.0"
            ("float", 9.0),
            ("int", 9)
            
            }

print(saparate)








































