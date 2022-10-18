def solve(n, data_set):
    per = 100 / n
    percentage = 0
    for i in data_set:
        if i != 0:
            percentage += per / (100 / i)
        
    return "%.12f" % percentage

n = int(input())
data_set = list(map(int, input().split()))
print(solve(n, data_set))
