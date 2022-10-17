def solve(n, h, data):
    count  = 0
    for i in data:
        if int(i) > h:
            count += 2
        else:
            count += 1

    return count

n, h = list(map(int, input().split()))
data_set = list(map(int, input().split()))
print(solve(n, h, data_set))
