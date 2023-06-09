def rec_fib(n):
    """(number) -> number
    Return fibonaci sequence for given n.
    >>>rec_fib(5)
    0, 1, 1, 2, 3
    """
    if n <= 1:
        return n
    else:
        return rec_fib(n-1) + rec_fib(n-2)

def user_inp(number):
    """(number) -> number
    Accept a user input for n number
    """
    change_state = True
    while change_state:
        if number > 0:
            pr_fib(number)
            change_state = False
        else:
            number = int(input('Enter positive number: '))


def pr_fib(num):
    """(number) -> number
    Return the fibonaci sequence to the console.
    """
    for i in range(num + 1):
        print(rec_fib(i))

number = int(input('Enter positive number: '))
user_inp(number)