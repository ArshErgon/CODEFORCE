def solve(string, target):
    return "NO" if string[::-1] != target else "YES"

string = input()
target = input()
print(solve(string, target))