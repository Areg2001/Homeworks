def numberDigitsSum():
    res = 0
    number = input("Please, enter the number. ")

    if number.isdigit():
        number = int(number)
        while number != 0:
            res += number % 10
            number = number // 10
        return res   

    return "You must be input positive integer number. "     
  
print(numberDigitsSum())