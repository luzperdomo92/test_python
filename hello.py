name = input("enter your name: ")
if len(name) < 3:
    print("name must be al least 3 characters")
elif len(name) > 20:
    print("name can be a maximun 50 characteres")
else:
    print("name looks good!")


