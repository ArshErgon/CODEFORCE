def solve(ith_problem):
    return "HARD" if sum(ith_problem) >= 1 else "EASY"


n = int(input())
data_sets = list(map(int, input().split()))
print(solve(data_sets))