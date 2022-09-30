
# the problem link: https://codeforces.com/problemset/problem/231/A

# O(n) ~ O(1) || O(1) 
# where n is the space of team_list
def solve(team_list):
    return sum(1 for team in team_list if sum(team) >= 2)


n = int(input())
team_list = []
for i in range(n):
    team_list += [list(map(int , input().split()))]

print(solve(team_list))