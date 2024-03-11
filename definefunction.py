#This code is my initial try of creating a function.

def greeting(name): #using the def keyword, greeting is the function name, and name is a parameter (can have 0 to infinity parameters)
    print('Hello', name);

#main program
input_name = input('Enter your name:\n');
greeting(input_name)

def addition(a, b):
    return a + b;

print(addition(1,2))
