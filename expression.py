# 1. string and numeric values can operate together with * repat
a,b=3,6
text ="@"
print(a*text*b)

# 2. string and string can operate with + concatention
a,b="3",6
text ="@"
print((a+text)*b)

# 3. numeric values can operate with all arithmetic operators
a,b=2,6
c = 3
print(a+b*c)

# 4. arithmetic expression with integer and float will result in float
a,b=2,6.5
c = a*b
print(c)

# 5. result of division operator with two integers will be float
a,b=1,2
c = a/b
print(c)

# 6.integer division with float and int will give int displayed as float
a,b=1.5,3
c = a//b
print(c,a/b)

# 7.floor gives closest integer,which is lesser than or equal to the float value
# result od (A//B) is same as floor(A/B) 

a,b=12,5
c = a//b
print(c)

a,b=-12,5
c = a//b
print(c)

a,b=12,-5
c = a//b
print(c)

# remainder is negative when denominator is negative

a,b=-5,2
c = a%b
print(c)

a,b=5,2
c = a%b
print(c)

a,b=5,-2
c = a%b
print(c)

a,b=-5,-2
c = a%b
print(c)
