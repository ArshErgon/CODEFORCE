
def solve(n):
    if n == 1:
        return "I hate it"

    hulk_emotion = {
        "odd":"I hate",
        "even":"I love",
    }

    new_list = []
    for i in range(1, n + 1):
        new_list.append(hulk_emotion["even" if i % 2 == 0 else "odd"])
    
    i = 0
    count = 0
    while i < (n - 1):
        if (i + 1 < n -1) and count > 0:
            new_list.insert(i - 1, "that")
            count = 0
            # i += 1
        count += 1
        i += 1
    return new_list

n = int(input())

print(solve(n))
    