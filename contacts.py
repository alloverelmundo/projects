#This code defines a dictionary named contacts with two keys: 'number' and 'students'.
contacts = {
    'number': 2, 
    'students': [
        {'name': 'vivian', 'email': 'lol@gmail.com'},
        {'name': 'alex', 'email': 'idk@gmail.com'}
    ]
}

for student in contacts['students']:
    print(student['email'])
