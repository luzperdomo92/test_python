class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("Hi, I'm " + self.name)

luz = Person("Lily")
luz.talk()
