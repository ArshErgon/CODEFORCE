
def bear_and_big_brother(weight_A, weight_B):
    count = 0
    
    while weight_A <= weight_B:
        weight_A *= 3
        weight_B *= 2
        count += 1
    
    return count

weight_A, weight_B = input().split()
print(bear_and_big_brother(int(weight_A), int(weight_B)))