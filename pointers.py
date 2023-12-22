# num1 = 11
# num2 = num1

# print(num1, num2)
# print(id(num1), id(num2))

# num2 = 22
# print(num1, num2)
# print(id(num1), id(num2))

dict1 = {
            'value' : 11
        }
dict2 = dict1

print(dict1["value"], dict2["value"])
print(id(dict1["value"]), id(dict2["value"]))

dict2 = {
            'value' : 22
        }

print(dict1["value"], dict2["value"])
print(id(dict1["value"]), id(dict2["value"]))