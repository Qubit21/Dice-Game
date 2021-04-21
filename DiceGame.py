import random

def dice():
    final_sum = 0
    for i in range(0, 5):
        final_sum += random.randint(1,6)
    return final_sum

print(dice)