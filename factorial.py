def fact(n):
    """(number) --> number
    Return a factorial number for given n
    >>> fact(3)
    6
    >>> fact(4)
    24
    >>> fact(10)
    
    """
    if n == 1:
        return 1
    else:
        return n * fact(n -1)

def convert_str(number=''):
    """(string) --> number
    Check whether user input is valid or not, and return numeric value
    """
    while number is str(number):
        number = input("Entered value is not input, please enter a number: ")
        if number.isdigit() and int(number) > 0:
            print(fact(int(number)))
            break
    if number == int(number):
        print(fact(number))
#Default value
convert_str()
#Passing number
convert_str(10)
