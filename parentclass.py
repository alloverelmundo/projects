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
