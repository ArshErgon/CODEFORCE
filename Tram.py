def solve(num):
    capicity = float('-inf')
    present_people = 0
    for out_po, in_po in num:
        present_people -= out_po
        present_people += in_po
        capicity = max(capicity, present_people)
    return capicity


n = int(input())
data_list = list()
for i in range(n):
    data_list += [list(map(int, input().split()))]

print(solve(data_list))
