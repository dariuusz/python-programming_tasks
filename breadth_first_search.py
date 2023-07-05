from collections import deque

def capitalize_dictionary(people):
    """(dictionary) --> dictionary
    Return capitalized dictionary.
    """
    new_people ={}
    for key, value in people.items():
        new_people[key.capitalize()] = value
        for i in range(len(value)):
            value[i] = value[i].capitalize()
    return new_people

def search_dictionary(people, name):
    """(dictionary, object) --> object 
    Return True if a name is found in a dictionary, otherwise return False.
    """
    search_queue = deque()
    search_queue += people
    searched = []
    name = name.capitalize()
    while search_queue:
        person = search_queue.popleft()
        print( person)
        if not person in searched:
            if person == name:
                print(person ,'is found in')
                return True
            # elif name not in people:
            #     continue
            else:
                search_queue += people[person]
                searched.append(person)
    return False 

def create_dictionary(related_person, people):
    """(dictionary) --> dictionary
    Return a dictionary for given key values. People in a dictionaries will be assigned to their relatives.
    """
    if len(people) == 0:
        people = related_person
    else:
        for key, values in related_person.items():
            if key in people.keys():
                people[key].extend(values)
            else:
                people[key] = values
    return people

people = {}
people = create_dictionary({'darek':[]}, people)

create_dictionary({'darek':['marek','jarek']}, people)
create_dictionary({'darek':['ania', 'ala']}, people)
create_dictionary({'marek':['ania', 'ala']}, people)
create_dictionary({'ania':['ewa', 'julka']}, people)
create_dictionary({'ania':['inka', 'agnieszka']}, people)
create_dictionary({'jarek':[]}, people)
create_dictionary({'ala':[]}, people)
create_dictionary({'ewa':[]}, people)
create_dictionary({'julka':[]}, people)
create_dictionary({'inka':[]}, people)
create_dictionary({'robert':[]}, people)
create_dictionary({'jozek':[]}, people)

print(people)

search_dictionary(capitalize_dictionary(people), 'agnieszka')

