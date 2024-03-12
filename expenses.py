#This code allows users to input their expenses individually or in bulk, calculates the total expenses, and then prints out the total amount spent.

expenses = [10.50,8,5,15,20,5,3];

#print("you spent $", sum, sep = ''); # the comma means we dont have to convert to string and automatically adds a space

#or use sum function

total = sum(expenses);
print(str(total));

range(7); #automatic from 0 to 6
range(0,7,1); #start, stop, increment

#adding input to the expenses calculator

total1 = 0;
expenses1 = []; 
for i in range(7):
    expenses1.append(float(input("enter an expense:")));

total1 = sum(expenses1);

print(total1);

#or

total2 = 0;
expenses2 = [];
num_expenses = int(input("enter # of expenses:"))
for i in range(num_expenses):
    expenses2.append(float(input("enter an expense:")))
total = sum(expenses2);
print('you spent$', total, sep='');
