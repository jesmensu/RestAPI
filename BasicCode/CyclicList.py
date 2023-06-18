from itertools import cycle
arr = [1,2,3,4,5,6]
n=7
k=4
for index, *ans in zip(range(n), *[cycle(arr)] * k):
    print(ans)
