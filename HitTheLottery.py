
def solve(n):
    part = 0
    while n != 0:
        if n >= 100:
            n -= 100
        elif n >= 20:
            n -= 20
        elif n >= 10:
            n -= 10
        elif n >= 5:
            n -= 5
        elif n >= 1:
            n -= 1
        part += 1

    return part

n = int(input())

print(solve(n))
    