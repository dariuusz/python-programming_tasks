

def middle_element(dictionary):
    """(dictionary) --> list
    Convert dictionary' objects into iterator. Return the middle
    object of passed dictionary. Function return 1 or 2
    elements in a list whether is even or odd.
    >>> middle_element('a': [1, 2], 'b': [1], 'c': [1, 2])
    ('b', [1])
    >>> middle_element('a': [1, 2], 'b': [1], 'c': [1, 2], 'd': [1])
    [('b', [1]), ('c', [ 1, 2])]
    """
    items = iter(dictionary.items())
    dic_length = dictionary_length(dictionary)
    middle_elements = []
    count = 0
    for i in items:
        count += 1
        if count == dic_length[0] or count == dic_length[1]:
            middle_elements.append(i)
    return middle_elements 

def dictionary_length(dictionary):
    """(dictionary) --> list
    Return a length of dictionary.
    >>> dictionary_length('a': [1, 2], 'b': [1], 'c': [1, 2])
    [ 1 , 0 ]
    >>> dictionary_length('a': [1, 2], 'b': [1], 'c': [1, 2], 'd': [1])
    [ 2 , 3 ]
    """
    
    dict_length = len(dictionary)
    if dict_length % 2 == 0:
        return [dict_length // 2, dict_length // 2 + 1]
    else:
        return [dict_length // 2, 0]  
    
def create_dictionary(dic1, dic2):
    """(dictionary, dictionary) --> dictionary
    Return a dictionary linked by their keys.
    """
    if len(dic1) == 0:
        dic1 = dic2
    else:
        for key, values in dic2.items():
            if key in dic1.keys():
                dic1[key].extend(values)
            else:
                dic1[key] = values
    return dic1

#Creating a nested dictionary
dic1 = {}
dic1 = create_dictionary(dic1, {'a':[]})
create_dictionary(dic1, {'a': [1, 2, 3, 4,]})
create_dictionary(dic1, {'a':[5, 6, 7, 8]})
create_dictionary(dic1, {'b':[1, 2]})
create_dictionary(dic1, {'c':[1, 2, 3, 4, 5]})
create_dictionary(dic1, {'d':[1, 2, 3, 4]})
create_dictionary(dic1, {'e':[1, 2]})
create_dictionary(dic1, {'f':[5, 6, 7, 8]})
create_dictionary(dic1, {'g':[5, 6, 7, 8]})
create_dictionary(dic1, {'h':[5, 6, 7, 8]})


print(middle_element(dic1))