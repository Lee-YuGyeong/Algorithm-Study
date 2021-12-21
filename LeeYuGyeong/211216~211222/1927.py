import heapq
import sys
input = sys.stdin.readline

n = int(input())
h = []
for _ in range(n):
    x = int(input())
    if x: heapq.heappush(h,x)
    else:
        print(heapq.heappop(h)) if h else print(0)