def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return n % 2 != 0

def solution():
    number = input("Please, enter the number. ")
    try:
        if isinstance(int(number), int):
            return "This is number is even." if is_even(int(number)) else "This number is odd."
    except:        
        return "You must be input integer number."

print(solution())