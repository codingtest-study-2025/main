# [inuput]
# 첫째 줄: N M A B (도시 개수, 도로의 개수, 민겸 도시, 시은 도시)
# M개 줄: a, b, c (출발 도시, 도착 도시, 시간)

# [output]
# 첫째 줄: 약속 장소 후보의 도시 개수
# 둘쨰 줄: 도시 번호 출력

# [조건]
# 2 <= N <= 200,000
# 1 <= M <= 300,000
# A != B
# A와 B도 약속 장소가 될 수 있음
# 최단 경로가 여러 개일 수 있음, 간선은 양방향

# [풀이방법]
# 음의 간선이 없고, 최단 경로를 찾는 문제이므로 다익스트라 사용(N과 M도 충분히 커서 완전 탐색 불가)
# A에서 다익스트라 수행 + B에서 다익스트라 수행
# 여러 최단 경로에 걸쳐있는 모든 도시를 찾기 위해선 아래 조건으로 찾아야 함
#     -> distA[v] + distB[v] == distA[B]
#     -> v 노드가 최단 경로 위에 있음을 의미

import sys
import heapq
import math


def dijkstra(graph, start):
    INF = math.inf
    dist = [INF] * len(graph)
    dist[start] = 0
    pq = [(0, start)]  # (현재까지의 거리, 노드) 우선순위 큐

    while pq:
        cur_dist, cur_node = heapq.heappop(pq)
        # 이미 더 짧은 경로가 발견된 경우 무시
        if cur_dist > dist[cur_node]:
            continue
        # 인접한 이웃 노드 확인
        for nei, weight in graph[cur_node]:
            new_dist = cur_dist + weight
            # 새로운 경로가 더 짧으면 갱신 후 pq에 추가
            if new_dist < dist[nei]:
                dist[nei] = new_dist
                heapq.heappush(pq, (new_dist, nei))
    return dist


# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

N, M, A, B = map(int, input().split())
graph = [[] for _ in range(N+1)]

# 양방향 그래프 생성
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

distA = dijkstra(graph, A)
distB = dijkstra(graph, B)

# 최단 경로 위에 있는 도시 찾기
answer = []
for n in range(1, N+1):
    # 아래 조건을 만족하면 최단 경로 위에 있는 도시임
    if distA[n] + distB[n] == distA[B]:
        answer.append(n)

print(len(answer))
print(*answer)
