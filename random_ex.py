from random import choice, sample
from collections import defaultdict, Counter

ddic = defaultdict(int)
for i in range(10000):
    for r in sample(range(1,11),5):
        ddic[r] += 1


c = Counter(ddic)
print(sorted(c.items()))
for i, j in c.items():
    print(j)