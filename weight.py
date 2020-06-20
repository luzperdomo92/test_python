"""
weigth = int(input("Weight: "))
unit = input("(L)lb or (K)g: ")

if unit.upper() == "L":
    converter = weigth * 0.45
    print("you are {}  kilos".format(converter)) 
elif unit.upper() == "K":
    converter = weigth / 0.45
    print("you are {:.2f}  libras".format(converter)) 
"""

weigth = int(input("Weight: "))
unit = input("(L)lb or (K)g: ")

if unit.upper() == "L":
    converter = weigth * 0.45
    print(f"you are {converter}  kilos") 
elif unit.upper() == "K":
    converter = weigth // 0.45
    print(f"you are {converter}  libras")
