"""
custumer = {
    "name" : "luz",
    "age": 27
}
#print(custumer["age"])
print(custumer.get("name"))
"""

numbers = {
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "six",
    "7" : "seven",
    "8" : "eight",
    "9" : "nine",
    "0" : "zero"
}
phone = input("Phone: ")
output = ""
for char in phone:
    output += numbers.get(char) + " "
print (output)



