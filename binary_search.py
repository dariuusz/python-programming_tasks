import unicodedata

def binary_search(list, item):
    """"(list, item) --> number
    Return a given item in a list.
    """
    low = 0
    high = len(list) - 1
    count = 0
    while low <= high:
        count += 1
        mid = int(low + (high - low) / 2)
        guess = list[mid]
        if item == guess:
            return f"\nNumber {item} found at the step {count}" 
        if item < list[mid]:
            high = mid -1
        if item > list[mid]:
            low = mid +1
    return None 

def create_list(n):
    """(number) --> list
    Return a list for given n squared values. 
    """
    while n is str(n) or n < 2:
        n = input('\nEnter number: ')
        if n.isdigit() and (int(n) > unicodedata.numeric('1')):
            n = int(n)
            break


    number_list = []

    for i in range(1, n +1):
        i = i ** 2
        number_list.append(i)
    return number_list

def print_list(list):
    """"(list) --> number
    Return formated values of the list
    """
    for i in range(1, len(list) +1):
        print(i , " squared number is: " , list[i -1])

print_list(create_list(1))
# print(binary_search(create_list(11), 25))