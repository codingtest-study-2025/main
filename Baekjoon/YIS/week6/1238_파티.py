# [input]
# 첫 번째 줄: N, M, X (마을 개수, 간선 개수, 파티하는 마을)
# 다음 M개의 줄: s, e, t (시작점, 종료점, 시간)

# [output]
# 왕복이 가장 오래 걸리는 학생의 소요시간

# [조건]
# 간선은 단반향이다.
# A에서 B로 가는 도로의 개수는 최대 1개이다.

# [풀이방법]
# 음수 간선이 아니고, 학생들은 최단시간으로 움직이니 다익스트라 사용
# 각 마을(학생)마다 자신의 마을 -> X 마을 -> 자신의 마을 최단 시간 구하고, 그 중 최댓값 출력하기
#     - i -> X : 다익스트라 N번 수행
#     - X를 출발점으로 다익스트라 1번 수행
#     - 총 N + 1번 수행 => 시간초과
# 역방향 그래프로 다익스트라 수행횟수 줄이기
#


import sys
import heapq

sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline


def dijkstra(graph, start):
    INF = 10**9
    dist = [INF] * len(graph)
    dist[start] = 0

    # (현재까지의 거리, 노드)를 담는 우선순위 큐
    priority_queue = [(0, start)]

    while priority_queue:
        current_dist, current_node = heapq.heappop(priority_queue)
        # 이미 더 짧은 경로가 발견된 경우 무시
        if current_dist > dist[current_node]:
            continue

        # 인접한 이웃 노드들 확인
        for neighbor, weight in graph[current_node]:
            new_dist = current_dist + weight
            # 새로운 경로가 더 짧으면 갱신 후 큐에 추가
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(priority_queue, (new_dist, neighbor))

    return dist


N, M, X = list(map(int, input().split()))

# 정방향/역방향 그래프 초기화
graph = [[] for _ in range(N+1)]
rev_graph = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, t = list(map(int, input().split()))
    graph[s].append((e, t))
    rev_graph[e].append((s, t))

dist_from_X = dijkstra(graph, X)
dist_to_X = dijkstra(rev_graph, X)

# 왕복 시간 중 최댓값 계산
answer = 0
for i in range(1, N+1):
    total = dist_to_X[i] + dist_from_X[i]
    if total > answer:
        answer = total

print(answer)
