vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

def solution():
    """This function checks and prints whether the character is a consonant or a vowel."""

    character = input("Please, enter the character. ")

    if character.isalpha() and len(character) == 1:
        return "This character is vowel." if character in vowel else "This character is consonant."

    return "You must be input a character and it must be one character."

print(solution())