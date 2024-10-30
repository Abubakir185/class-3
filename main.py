import random

class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def is_fresh(self):
        return random.choice([True, False])
    
    def eat(self):
        return "mevani yemoq"
    

class Apple(Fruit):
    def __init__(self, color):
        Fruit.__init__(self, "apple", color)

red_apple = Apple("red")

print(red_apple.color)
print(red_apple.is_fresh())
print(red_apple.eat())

