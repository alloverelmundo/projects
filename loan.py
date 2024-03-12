#This code allows users to simulate the repayment of a loan by taking inputs such as the loan amount, annual percentage rate (APR), monthly payment, and duration in months. 
#It then iterates through each month, calculating the interest accrued, subtracting the payment, and printing the remaining balance until the loan is fully paid off or until the specified number of months elapses.

#get details of loan
money_owed = float(input("How much money do you owe, in dollars?\n")); #50,000
apr = float(input("What is the annual percentage rate of the loan?\n")) #3%
payment = float(input("How much will you pay off each month in dollars?\n")) # $1,000
months = float(input("How many months do you want to see the results for?\n")) #24

for i in range(months):
    monthly_rate = apr/100/12;

    #calculate interest ro pay
    interest_paid = money_owed*monthly_rate;

    #add in interest
    money_owed = money_owed+interest_paid
    if (money_owed-payment<0):
        print("The last payment is:", money_owed);
        print("You paid off the loan in", i+1, 'months')
        break
    #make payment
    money_owed= money_owed+payment;

    print('Paid', payment, 'of which', interest_paid, 'was interest.', end=' ')
    print('Now I owe', money_owed)
