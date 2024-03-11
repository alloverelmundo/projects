#This code creates a class called "robotdog" and also creates an object called "mydog" named 'spot' with a breed of 'pitbull', prints its name ('spot'), and makes it bark ('woof').

class robotdog:
    def __init__(self, nameval, breedval) -> None: #init method lets us initialize our robot's properties such as name or breed
        #self is always the first parameter and refers to instance of the class being created or the current object
        self.name = nameval
        self.breed = breedval
    def bark(self): #a method is a function that belongs to a class
        print('woof')

#creating an object
mydog = robotdog('spot', 'pitbull')
print(mydog.name)
mydog.bark()
