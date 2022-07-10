import sys
input = sys.stdin.readline
N, S = map(int, input().split())
lst = list(map(int, input().split()))
d = [0] * 6000100

for i in range(1, 1 << (N // 2)):
    a = 0
    for j in range(N // 2):
        if (1 << j) & i:
            a += lst[j]
    d[a + 3000000] += 1

cnt = d[S + 3000000]
d[3000000] += 1


for i in range(1, 1 << (N - N // 2)):
    a = 0
    for j in range(N - N // 2):
        if (1 << j) & i:
            a += lst[N//2 + j]
    cnt += d[S - a + 3000000]
print(cnt)