# Accessing parts of a string 

# Sintax str[starting_index : ending_index] #ending index isn't included
#positive Index

str = "rajan choudhary"
str = str.capitalize()    # str.capitalize() to 1st char capital
print("Your Index :",str[0 : 6])
print("Your Index :",str[6 : len(str)])
print("Your Index :",str[ : 6])  #[0:6]
print("Your Index :",str[6 : ])  #[6:len(str)]
print(str.endswith("ary"))
print(str)


#negitive Index
str = "Apple"
str = str.replace("Apple","Mango")  # str.replace(ols,new) useful funcation
print("Your Index :",str[-3 : -1])
print("Your Index :",str[-5 : -2])
print(str.endswith("e")) # str.endswith(last index) good funcation
print(str.find("o"))     # str.fing(any word you can serach) nice funcation
print(str.count("Mango")) # str.count("count char") nonsens funcation <how meny times that word come in the string that show>
print(str)


