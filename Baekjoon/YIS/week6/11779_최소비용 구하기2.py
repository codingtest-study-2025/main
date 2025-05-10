# [input]
# 첫째 줄: n (도시 개수)
# 둘째 줄: m (버스의 개수)
# m개 줄: s, e, t (시작점, 종료점, 시간)
# 마지막 줄: s, e (구하고자 하느 출발점, 도착점)

# [output]
# 첫째 줄: 최소 비용
# 둘째 줄: 최소 비용 경로에 포함된 도시의 수 (출발 ,도착 포함)
# 셋째 줄: 경로를 방문하는 도시 순서대로 출력

# [조건]
# 1 <= n <= 1,000, 1 <=m <= 100,000

# [풀이방법]
# 음수 간선이 없고 최단 경로를 찾는 문제이므로 다익스트라 사용
# 최소 비용과 함께 경로도 출력해야 하므로 최단 경로의 이전 노드 저장 필요

import sys
import math
import heapq


def dijkstra_with_path(graph, start, end):
    INF = math.inf
    n = len(graph) - 1
    # 최단 거리와 이전 노드를 저장할 배열
    dist = [INF] * (n + 1)
    prev_node = [0] * (n + 1)

    dist[start] = 0
    pq = [(0, start)]  # (현재까지의 비용, 노드)

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)
        if cur_cost > dist[cur_node]:
            continue
        # 인접 노드 탐색
        for neighbor, weight in graph[cur_node]:
            new_cost = cur_cost + weight
            # 만약 최단 경로라면
            if new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                # 경로 배열에 현재 노드 저장
                prev_node[neighbor] = cur_node
                heapq.heappush(pq, (new_cost, neighbor))

    # 목적지까지의 최단 경로
    path = []
    node = end
    while node:
        path.append(node)
        if node == start:
            break
        node = prev_node[node]
    path.reverse()

    return dist[end], path


# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

n = int(input())
m = int(input())

# 인접 리스트 생성
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, cost = map(int, input().split())
    graph[s].append((e, cost))

start, end = map(int, input().split())

min_cost, path = dijkstra_with_path(graph, start, end)

# 출력
print(min_cost)
print(len(path))
print(*path)  # 언패킹 연산자
