
# 1.Waf to print the length of a list.(list is the parameter) 


cities = ["Delhi", "Gurgaon", "Noida", "Pune", "Mumbai", "Chennai"]
heroes = ["Captain America", "Thor", "Superman", "Batman", "Iron Man"]

def print_length(lst):
    print(len(lst))

print_length(cities)
print_length(heroes)





# 2.Waf to print the elements of a list.(list is the parameter) 


def print_elements(lst):
    for element in lst:
        print(element, end=" ")

print_elements(cities)
print_elements(heroes)









# 3.Waf to find the factorial of n.(n is the parameter) 


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n+1):
            result *= i
        return result

# Example usage:
print(factorial(5))  # Output: 120









# 4.Waf to convert USD to INR.


def converter(usd_val):
    inr_val = usd_val * 82.75
    print(usd_val,"USD =",inr_val,"INR")

converter(100000)














# def usd_to_inr(usd, exchange_rate=82.75):
#     inr = usd * exchange_rate
#     return inr

# # Example usage:
# usd_amount = 10
# exchange_rate = 82.75  # As of 2024
# print(f"{usd_amount} USD is {usd_to_inr(usd_amount, exchange_rate)} INR")
