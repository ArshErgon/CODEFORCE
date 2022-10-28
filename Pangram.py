
def solve(string):
    alpha_letters = [False] * 26
    for letter in string:
        idx = ord(letter) - ord('a')
        alpha_letters[idx] = True
    return "YES" if all(alpha_letters[i] for i in range(26)) else "NO"

n = int(input())
string = input()

print(solve(string.lower()))
    