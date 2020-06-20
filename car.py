command = ""
started = False
stoppped = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("car already started")
        else:
            started = True
            print("car started")
    elif command == "stop":
        if  not started:
            print("car is already stopped")
        else:
            started = False
            print("Car stopped")
    elif command == "help":
        print("""  
start - 
stop - 
quit - 
        """)
    elif command == "quit":
        break

    else:
        print("sorry, I dont undersatnd that ..!!") 
