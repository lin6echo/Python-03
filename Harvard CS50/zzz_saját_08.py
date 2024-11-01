import random

x = list(range(1,101))

m = random.sample(x, 10)

n = len(m)

for i in range(n):

    for j in range(0, n - i - 1):

        if m[j] > m[j + 1]:
            m[j], m[j + 1] = m[j + 1], m[j]

print(m)





