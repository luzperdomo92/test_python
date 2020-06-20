"""
a = [11, 3, 8, 5, 22]
b = [6, 7, 11, 22, 27]

a_set = set(a)
b_set = set(b)

if (a_set & b_set):
    print ( a_set & b_set)
else :
    print("no concidence")
"""
for idx, letter in enumerate(range(97, 123)):
    letter = chr(letter) 
    res = ''
    if not idx % 2 : 
        res = res + letter.upper() 
    else: 
       res = res + letter.lower()
    res = res[::-1]
    print(res, end= '')
