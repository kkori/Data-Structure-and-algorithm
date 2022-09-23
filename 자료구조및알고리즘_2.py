import sys
from collections import deque

# 1번 문제
def shortest_city(graph,n,m,k,x):

    visited = [False] * (n + 1)

    for _ in range(m):
        a, b  = map(int, input("enter link >> ").split())
        graph[a].append(b)

    q = deque([x])

    while q:
        sth = q.popleft()
        for i in graph[sth]:
            if dist[i] == -1:
                dist[i] = dist[sth] + 1
                q.append(i)

    for idx, d in enumerate(dist):
        if d == k:
            print(idx)
            break
    else:
        print("존재하지 않습니다.")

n, m, k, x = map(int, input('enter input values: ').split())
graph = [[] for _ in range(n+1)]

dist = [-1] * (n + 1)
dist[x] = 0

shortest_city(graph,n,m,k,x)

# 2번 문제
N,M= map(int,input("가래떡의 개수와 요청할 떡의 길이를 입력하세요 >> ").split())
cake = list(map(int,input("떡의 길이들을 입력하세요 >> ").split()))

def cakesum(height):
    Sum = 0
    for i in cake:
        if i-height >0:
            Sum += (i-height)

    return Sum

def binarySearch(target):
    start, end = 0, max(cake)
    ans = 0
    while start <= end:
        mid = (start+end)//2
        Sum = cakesum(mid)
        if Sum < target:
            end = mid - 1
        if Sum >= target:
            ans = mid
            start = mid + 1

    return ans

print(binarySearch(M))