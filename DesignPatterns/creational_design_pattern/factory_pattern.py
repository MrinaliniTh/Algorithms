class Interface:
    def speak(self):
        pass
class English(Interface):
    def speak(self):
        print("I speak english")

class Spanish(Interface):
    def speak(self):
        print("I speak spanish")

class French(Interface):
    def speak(self):
        print("I speak french")

class InvalidInput(Interface):
    def speak(self):
        print("Invalid Input")

class Factory:
    def __init__(self):
        self.instance = {
            "English": English(),
            "Spanish": Spanish(),
            "French": French()
        }
    def get_object(self, msg):
        if msg not in self.instance:
            return InvalidInput()
        return self.instance[msg]

if __name__ == '__main__':
    factory = Factory()
    obj1 = factory.get_object("English")
    obj1.speak()
    obj2 = factory.get_object("Spanish")
    obj2.speak()
    obj3 = factory.get_object("French")
    obj3.speak()
    obj4 = factory.get_object("Freh")
    obj4.speak()
