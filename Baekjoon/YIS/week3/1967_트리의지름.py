# [input]
# 첫째 줄 - 노드의 개수 n (1 <= n <= 10,000)
# 둘째 줄 ~ (n - 1)개 줄 - 간선 (a(부모), b(자식), c(가중치))

# [output]
# 첫째 줄 - 트리의 지름 출력 (ex. 45)

# [참고]
# 루트는 항상 1
# 0 < 간선 가중치 <= 100

# [풀이]
# 2차원 배열로 트리 생성
# 1번 노드에 대해 dfs 실행 후 가장 먼 노드 찾기
# 가장 먼 노드로부터 dfs 실행하여 가장 먼 거리 출력

import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n + 1)]
visited = [-1] * (n + 1)
visited[1] = 0


# 트리 생성
for i in range(n - 1):
    parent, child, distance = list(map(int, input().split(' ')))
    tree[parent].append([child, distance])
    tree[child].append([parent, distance])


def dfs(node, current_distance):
    for child_node, child_distance in tree[node]:
        if visited[child_node] == -1:
            visited[child_node] = child_distance + current_distance
            dfs(child_node, current_distance + child_distance)


dfs(1, 0)

farthest_node = visited.index(max(visited))
visited = [-1] * (n + 1)
visited[farthest_node] = 0

dfs(farthest_node, 0)

print(max(visited))
