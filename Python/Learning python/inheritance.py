class Animal:
    def __init__(self, name):
        self.name =name
    def speak(self):
        print("generic animal sound")
class dog(Animal):
    def speak(slef):
        return "bow"
class cat(Animal):
    def speak(self):
        return "meow"
a = dog("bruno")
print(a.speak())
