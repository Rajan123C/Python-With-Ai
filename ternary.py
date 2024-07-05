# Single Line If /ternary operator

food = input("Food :")
eat = "Yes" if food == "cake" else "No"
print(eat)

food2 = input("Food :")
print("sweet") if food == "cake" or food == "jalebi" else print("Not Sweet")

# Clever If /ternary operator

age = input("age :")
vote = ("Yes","No") [age>18]
