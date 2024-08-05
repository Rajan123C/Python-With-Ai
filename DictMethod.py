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

print("Cars Keys:", student["cars"].keys())
print("Scores Keys:", student["scores"].keys())
print("Student Keys:", student.keys())
print("Student Values:", student.values())
print("Student Items:", student.items())
print("Student Cars:", student.get("cars"))

# To demonstrate the update method, we'll create a new dictionary to update the student dictionary
new_info = {"hobby": "coding"}
student.update(new_info)
print("Updated Student Dictionary:", student)
