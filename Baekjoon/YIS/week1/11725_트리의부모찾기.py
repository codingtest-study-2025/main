import sys
input = sys.stdin.readline  # 일반 input보다 훨씬 빠름

# sys.setrecursionlimit(10**6)  # 백준 입출력 관련 recursion 제한 해제

# sys.stdin = open('input.txt', 'r')


n = int(input().strip())

graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    line = list(map(int, input().split()))
    graph[line[0]].append(line[1])
    graph[line[1]].append(line[0])

print('graph', graph)

# 부모 정보
parent = [0] * (n + 1)
parent[1] = 1

# print(parent)


def dfs(s):
    for i in graph[s]:
        if parent[i] == 0:
            parent[i] = s
            dfs(i)


dfs(1)

# print(parent)

for index, item in enumerate(parent):
    if index == 0 or index == 1:
        continue
    print(item)
