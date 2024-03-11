#This code prompts the user to input their age, calculates the number of decades and remaining years based on that age, and then prints out the result.

age = int(input("How old are you?\n"));
decades = age//10; # two backslahes does whole number division
years = age % 10; # the % symbol gets the remainder
print("You are "+ str(decades)+" decades and " + str(years) + " years old.");
