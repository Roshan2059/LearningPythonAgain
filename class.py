class Person:
    def  __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")
    def code(self):
        print(f"{self.name} is coding")

person1 = Person("Roshan", 20, "male")    
person1.eat()
