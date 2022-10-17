def sol(string):
    winner = {
        'A': 0,
        'D': 0
    }

    for letter in string:
        winner[letter] += 1

    if winner['A'] > winner['D']:
        return "Anton"
    elif winner['D'] > winner['A']:
        return "Danik"
    else:
        return "Friendship"


n = int(input())
string = input()
print(sol(string))