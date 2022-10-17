def solve(n, number):
    while n >= 1:
        if number % 10 == 0:
            number = shortTheNumber(number)
        else:
            number -= 1
        n -= 1

    return number

def shortTheNumber(num):
    return num // 10

number, n = list(map(int, input().split()))
print(solve(n, number))
