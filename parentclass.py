#This code defines two classes, `Robot` and `RobotDog`, where `RobotDog` inherits from `Robot`. 
#It initializes a `RobotDog` instance named 'Bud', moves it, makes it emit a noise, and then feeds it. 
# It invokes its overridden `eat` method, which includes the behavior of its superclass, and its unique behavior to express a preference for bacon after being fed.

class Robot:
    def __init__(self, name):
        self.name = name
        self.position = [0,0]
        print('My name is', self.name)

    def walk(self, x):
        self.position[0] =self.position[0] + x
        print ('New position:', self.position)

    def eat(self):
        print('im hungry');

class RobotDog(Robot):
    def make_noise(self):
        print('woof');

    def eat(self):
        super().eat()
        print('i like bacon');

myrobotdog = RobotDog('Bud')
myrobotdog.walk(10);
myrobotdog.make_noise();
myrobotdog.eat();
