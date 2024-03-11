#This code showcases dictionary creation, updating, deletion, and retrieval operations, along with string concatenation using values from dictionaries.

acronymslist = {'lol': 'laugh out loud',
                'idk': 'i dont know',
                'tbh': 'to be honest'}

#creating a dictionary from nothing

acronymslist1 = {};
acronymslist1['lol']='laugh out loud';

#updating a value
acronymslist1['lol'] = 'just laughing';

#deleting a value
del acronymslist1['lol'];

#getting an item that's not in the dictionary
definition = acronymslist.get('lol');

if definition:
    print(definition)

sentence = 'idk' + 'what happened' + 'tbh';
translation = acronymslist.get('idk') + ' what happened ' + acronymslist.get('tbh');

