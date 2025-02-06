
class StringManipulator:
    def __init__(self): 
        self.s = ""

    def getString(self):
        self.s = input("Enter a string: ")

    def printString(self):
        print(self.s.upper())

class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Coordinates: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        return ((self.x - other_point.x)**2 + (self.y - other_point.y)**2)**0.5

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")





#usage

sm = StringManipulator()
sm.getString()
sm.printString()

square = Square(5)
print(square.area())

rectangle = Rectangle(4, 6)
print(rectangle.area())

p1 = Point(1, 2)
p2 = Point(4, 6)
p1.show()
p2.show()
print(p1.dist(p2))

acc = Account("John", 100)
acc.deposit(50)
acc.withdraw(20)
acc.withdraw(200)