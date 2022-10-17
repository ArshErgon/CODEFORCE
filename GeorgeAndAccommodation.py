def solve(data_sets):
    room_left = 0
    for peo, cap in data_sets:
        if peo < cap and (peo + 2) <= cap:
            room_left += 1
    
    return room_left

n = int(input())
data_sets = []
for i in range(n):
    data_sets += [list(map(int, input().split()))]
print(solve(data_sets))
