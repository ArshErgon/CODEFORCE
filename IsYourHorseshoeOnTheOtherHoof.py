
def solve(data_sets):
    return len(data_sets) - len(set(data_sets))

data_sets = (list(map(int, input().split())))
print(solve(data_sets))
    