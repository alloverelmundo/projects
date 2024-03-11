#with open('acronyms.txt') as file: #open() returns a file object that has methods like read() and write ()
    #result = file.read(); #read returns the whole file as a string by default
    #print(result)
#with keyword makes sure file is properly closed even if an exception is raised
#final code

#This code provides an interface for managing a list of acronyms and their definitions stored in a text file named 'acronyms.txt'. 
#It allows users to add new acronyms and definitions or search for the definitions of existing acronyms.
    
def findacronym():

    lookup = input('What software acronym would you like to look up?\n');

    found = False;

    with open('acronyms.txt') as file:
        for line in file:
            if lookup in line:
                print(line)
                found = True
                break

    if not found:
        print('Not found')

def addacronym():
    acronym = input('What acronym do you want to add?\n');
    definition = input('What is the definition?\n');
    with open('acronyms.txt', 'a') as file:
        file.write(acronym + ' - ' + definition + '\n');

def main():
    choice = input('Do you want to add or find an acronym?\n')
    if choice == 'add':
        addacronym();
    elif choice == 'find':
        findacronym();

main();
