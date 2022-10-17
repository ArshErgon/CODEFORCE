def solve(string):
    lowerCase, upperCase = 0, 0 
    for letter in string:
        if letter.isupper():
            upperCase += 1
        else:
            lowerCase += 1
        
    if upperCase == lowerCase:
        return string.lower()
    elif upperCase > lowerCase:
        return string.upper()
    else:
        return string.lower()


word = input()
print(solve(word))