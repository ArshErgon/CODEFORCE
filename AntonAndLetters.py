
def solve(string):
    alpha_letters = [0] * 26
    for letter in string:
        if letter.isalpha():
            idx = ord(letter) - ord('a')
            alpha_letters[idx] = 1 if alpha_letters[idx] == 1 else 1
    
    return sum(1 for i in range(26) if alpha_letters[i] != 0)

string = input()

print(solve(string))
    