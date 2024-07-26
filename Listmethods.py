
list = [2,1,3,6,8,9,4]

list.append(4) # adds one element at the end [2.1.3.4]
print(list,"<- 4 is appended(added)") 

list.sort() # sorts in ascending order  [1.2.3]
print(list,"<- Sorting in ascending order")

list.sort(reverse = True)
print(list,"<- Sorting in disascending order")

list.reverse()
print(list,"<- Full kist is reversed")

list.insert(1,4)
print(list,"<- 4 is insert on index 1")

list.remove(1)
print(list,"<- removes first occurrence of element")

list.pop(5)
print(list,"<- removes element at index")