
def solve(n, data_set_one, data_set_two):
    data_set_one.update(data_set_two)
    total_sum = n * (n + 1) // 2
    return "I become the guy." if sum(data_set_one) == total_sum else "Oh, my keyboard!"

n = int(input())
data_sets = set(map(int, input().split()))
data_set_two = set(map(int, input().split()))

print(solve(n, data_sets, data_set_two))
    
# failed on test 27