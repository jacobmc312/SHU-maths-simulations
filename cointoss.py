from random import random

C = 0
V = 1000

for i in range(V):
    H = 0
    for j in range(10):
        if random() < 0.5:
            H += 1
    if H >= 7:
        C += 1
print(C/V)
