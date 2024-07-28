# myDict.Key()  // returns all keys
# myDict.values() // returns all values
# myDict.items()  // returns all (key,value) pairs as tuple
# myDict.get("Key")    // return the Key according to value
# myDict.update(newDict) // inserts the specified items to the dictonary


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

print(student["cars"].keys())
print(student["scores"].keys())
print(student.keys())
print(student.values())
print(student.items())
print(student.get("cars"))
print(student.update(""))