

def stones_on_the_table(n, stones):
    count = 0

    for i in range(1, n):
        if stones[i-1] == stones[i]:
            count += 1
    
    return count


n = int(input())
stones = input()

print(stones_on_the_table(n, stones))