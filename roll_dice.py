#using the python standard library
# go to website docs.python.org/3/library

import random;
roll = random.randint(1,6);
print(str(roll));
guess = int(input('guess the dice roll\n'));
if guess == roll:
    print('yes');
else:
    print('no')
