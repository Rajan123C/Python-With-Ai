# Dictionary in Python
# Dictionaries are used to store data values in key:value pairs
# They are unordered, mutable (changeable) & don't allow duplicate keys

my_dict = {
    "name": "Rajan Choudhary",
    "cgpa": 8.4,
    "marks": [98, 97, 95],
    "age": 21,
    "is_adult": True,
    12.76: 35.90,
}

# Adding new key-value pairs and updating existing ones
my_dict[12.76] = "same as you"
my_dict["city"] = "Virar"

print(my_dict)
print(type(my_dict))

# Nested Dictionary
student = {
    "name": "Rajan Choudhary",
    "scores": {
        "chem": 98,
        "phy": 97,
        "math": 95,
    },
    "marks": [98, 97, 95],
    "age": 21,
    "is_adult": True,
    "cars": {
        "1st_car_name": "Pegassi",
        "2nd_car_name": "Rolls Royce",
        "3rd_car_name": "Jaguar",
        "4th_car_name": "Ferrari",
        "5th_car_name": "Toyota Supra",
    },
}

print(student)
print(type(student))
