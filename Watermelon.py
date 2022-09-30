# the link of the problem is here: https://codeforces.com/problemset/problem/4/A

# time: O(1) || space: O(1)
def solve(weight):
    if (weight > 2 and weight % 2 == 0):
        return "YES"
    else:
        return "NO"


weight = int(input())
print(solve(weight))



