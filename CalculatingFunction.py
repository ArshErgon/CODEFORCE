def solve(n):
    even = pow(((n + 1) // 2), 2)
    odd = (n * (n + 1) // 2) - even  
    return odd - even

n = int(input())
print(solve(n))