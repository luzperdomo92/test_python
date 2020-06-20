secret_number = 9
times = 0
guest_limit = 3

while times < guest_limit:
    guest_number = int(input("Guest: "))
    times += 1

    if guest_number == secret_number:
        print("Bravoo you win..!")
        break
else:
    print("try again..!")
