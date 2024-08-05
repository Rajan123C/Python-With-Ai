# loops are for sequential traversal. for traversing list,string,tuples etc. 

list = [1,2,3]

for value in list:
   print(value)


tuple = ("RAj","REdit","Github","Erter")

for value in tuple:
   print(value)
else:
   print("End")   


# 1. print the element of the following list useing a loop

Tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100,49)
x = 49
ind = 0
for val in Tup:
   if(val == x):
      print("Found x :", ind)
   ind += 1