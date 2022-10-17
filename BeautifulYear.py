def solve(year):
    distinct_num = 0
    leng = 1
    while distinct_num != leng:
        year += 1
        distinct_num = len(str(year))
        leng = len(set(str(year)))

    return year

year = int(input())

print(solve(year))