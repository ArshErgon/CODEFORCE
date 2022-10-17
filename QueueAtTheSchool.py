def solve(n, t, queue):
    queue = list(queue)
    i = 0
    while t != 0:
        while i < len(queue):
            if queue[i] == 'B':
                boy = queue.pop(i)
                queue.insert(i + 1, boy)
                i += 1
            i += 1
        t -= 1

    return "".join(queue)

leng, time = list(map(int, input().split()))
queue = input()
print(solve(leng, time, queue))

# not solved