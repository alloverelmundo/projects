amount = 100;
amount1 = int(10.6);
amount2 = float(10);
storename1 = 'the boutique';
storename2 = "Vivian's Boutique"; 
hello = "Hello";
name = input("What's your name?\n"); #the \n means a special character for a new line
greeting = hello + " " + name;
print(greeting);
tax = 0.06;
total = amount + amount*tax;
print(total);
temp = 95;
temp == 95; #checking if temp is equal to 95;

#lists
# the first position is 0
acronyms = ['lol', 'idk', 'smh', 'tbh'];
print(acronyms[0]); # prints the value at that index, in this case the first position

acronyms1 = []; #creates an empty list
acronyms1.append('lol');
acronyms1.append('idk');

#append is a method, and methods are called on objects

acronyms1.remove('idk');
#or
del acronyms1[0];

#check if something exists in a list 
word = 'smh'
if word in acronyms:
    print('yes');
else:
    print('no');   

#printing a list on different lines 
for acronym in acronyms: #acronym is a temporary vairable tat holds one of the acronyms in the list for each run
    print(acronym);

#list of lists aka containers
menus = [['egg sandwish', 'bagel', 'coffee'],
         ['blt', 'pb&j', 'turkey sandwich'],
         ['soup', 'salad', 'spaghetti', 'taco']]

print('breakfast menu:\t', menus[0])
print(menus[0][1]) #gets the second item from the first list

#create a dictionary of lists

menus1 = {'Breakfast': ['egg sandwich', 'bagel', 'coffee'],
          'Lunch': ['blt', 'pb&j', 'turkey sandwich'],
          'Dinner': ['soup', 'salad', 'spaghetti', 'taco']}

print('Breakfast Menu:\t', menus1["Breakfast"]);

#getting all the values in the dictionary using a for loop

for name, menu in menus1.items():
    print(name,":", menu);

#using dictionaries to represent objects

person = {'name': 'Sarah Smith', 
          'city': "Charlotte", 
          'age': '100'};

print(person.get('name'), 'is', person.get('age'));

#try except block to catch exceptions

things = {'lol': 'laugh out loud',
            'btw': 'by the way'}

try: 
    definition = things['idk'] #any code that might cause an exception
except: 
    print('the key does not exist') #print error message and then program continues normally

#raising an exception
    
def remainderdiv(a,b):
    if b == 0:
        raise ZeroDivisionError
        #or can create custom exception with raise Exception('Divisor cannot be 0')
    result = a//b;
    remainder = a%b;
    print(a, '/', b, 'is', result, 'remainder', remainder)

remainderdiv(10,0);


#class is a object factory and defines the attributes the objects will have
#classes can also contain functions and will be available to all objects created with this class
