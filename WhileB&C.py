# while break and continue

Tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 49
i = 0

while i < len(Tup):
    if Tup[i] == x:
        print("Found Index:", i)
        break
    else:
        print("Finding.....")
    i += 1

a = 0

while a <= 5:
    print(a)
    if(a == 3):
        continue
    
    i += 1