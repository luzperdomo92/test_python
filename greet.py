def greeting(message):
    words = message.split(" ")
    emojis = {
        ":(" : "😞",
        ":)" : "😀"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
        return output


message = input("> ")
result = greeting(message)
print(result)


"""
emoji = ctr + cmd + space 
"""
