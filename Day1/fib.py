def fib():
    """This function returns n-th Fibonacci number."""

    number = input("Please, enter the number. ")

    try:
        if isinstance(int(number), int) and int(number) > 0:
            first = 0
            second = 1
            nextItem = 0
            counter = 0

            if int(number) in (1, 2):
                return int(number) - 1

            while counter != int(number) - 2:
                nextItem = first + second
                first = second
                second = nextItem
                counter += 1
    
            return nextItem

        return "You must be input positive integer number."
            
    except:
        return "You must be input positive integer number."    

print(fib())            


