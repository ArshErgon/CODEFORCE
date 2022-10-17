def solve(magnets_list):
    count = 0
    for idx in range(1, len(magnets_list)):
        print(magnets_list[idx - 1][-1], magnets_list[idx][-1])
        if magnets_list[idx - 1][-1] != magnets_list[idx][-1]:
            count += 1
    
    return count if count > 0 else 1
n = int(input())

data_sets = list()
for i in range(n):
    data_sets.append(input())

print(solve(data_sets))
# not done yet