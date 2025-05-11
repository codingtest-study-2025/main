""" 
input
    1 ~ N번의 번호가 부여된 N개의 도시 존재
    도시를 잇는 M개의 양방향 도로 존재
    도로마다 통행 시간 존재
    * 각 도시는 도로를 통해 항상 다른 모든 도시로 이동 가능 = 고립된 도시 X
    * 출발지 = 도착지인 도로 X 
    * 두 도시를 잇는 도로는 최대 1개

    민겸이 = A번 도시, 시은이 = B번 도시 거주
    A -> B 최단 경로 중의 도시 = 약속 장소
    * 여러 개의 최단 경로가 존재 시, 그 중 하나 위에만 존재해도 됨
    * A, B도 약속 장소가 될 수 있음
    
    첫째 줄: 
        도시의 개수 N (2 ≤ N ≤ 200,000), 
        도로의 개수 M (1 ≤ M ≤ 300,000),
        민겸이 도시의 번호 A (1 ≤ A ≤ N),
        시은이 도시의 번호 B (1 ≤ B ≤ N),
        (A ≠ B)
    둘째 줄 ~ M+1번째 줄:
        도로의 정보 a, b, c (1 ≤ a, b ≤ N; 1 ≤ c ≤ 10^9; a ≠ b)
        a, b = 도로 양 끝 도시
        c = 도로 통행 시간

output
    민겸이 기준 약속 장소로 정할 수 있는 도시
    첫째 줄: 개수 출력
    둘째 줄: 번호 공백 구분 + 오름차순 출력

process
    시간 제한 2초, 메모리 제한 	1024MB 고려
    N = 7
    M = 8
    A = 1
    B = 6

    1 3 3
    1 4 1
    4 5 1
    5 2 2
    2 6 3
    1 7 2
    7 2 2
    3 6 5
    
    1 = 3[3], 4[1], 7[2]
    2 = 5[2], 6[3], 7[2]
    3 = 1[3], 6[5]
    4 = 1[1], 5[1]
    5 = 2[2], 4[1]
    6 = 2[3], 3[5]
    7 = 1[2], 2[2]

    마을 1 -> 6 경로
        1 -> 3 -> 6 = 8
        1 -> 4 -> 5 -> 2 -> 6 = 7
        1 -> 7 -> 2 -> 6 = 7

    최단 경로
        1 -> 4 -> 5 -> 2 -> 6 = 7
        1 -> 7 -> 2 -> 6 = 7
    마을 = 6개
        1, 2, 4, 5, 6, 7

    사용 변수
        N, M, A, B
        start, end, time

    첫째 줄 input 처리
        N, M, A, B
    두번째 ~ M+1번째 줄 input 처리
        start, end, time

    이동 가능 경로 + 시간 배열
        index = 도시 번호
        value = 이동 가능 도시 번호, 이동 시간

    다익스트라 함수
        start에서 시작하여 모든 도시까지의 최단 경로 탐색
        시간 배열 초기화
            index = 도시 번호
            value = 해당 도시까지의 최단 시간
            초기값 = max_time
        
        탐색 시작
            time = 0, 도시 = start
            최대 이동 시간과 이동 가능 경로를 통해 탐색

            이미 더 짧은 시간으로 방문된 경우, 스킵
                
            인접 도시 순회
                누적 거리 계산 (현재 거리 + 이동 시간)
                기존보다 짧으면 거리 배열 갱신

        시작 도시 기준 최단 거리 배열 반환
"""

import sys

sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

import heapq
#from collections import deque
#sys.setrecursionlimit(10**6)

N, M, A, B = map(int, input().split())
# 첫째 줄 input 처리


route = [[] for _ in range(N + 1)]
# 이동 가능 경로 + 시간 배열


for _ in range(M):
    start, end, time = map(int, input().split())
    route[start].append((end, time))
    route[end].append((start, time))
    # 양방향 도로이기에, 두 도시 모두 이동 가능 경로에 추가

def dijkstra(start):
    # 전달받은 start에 따라 탐색
    max_time = int(3e14)
    # 최대 이동 시간 = M=300,000, Ti=10^9 → 300,000,000,000,000
    time = [max_time] * (N + 1)
    # 이동 시간 배열 초기화
    time[start] = 0
    # 시작 마을 이동 시간 0
    heap = [(0, start)]
    # 탐색 큐 초기화

    while heap:
        current_time, current = heapq.heappop(heap)
        # 현재 이동 시간 및 도시 번호

        if current_time > time[current]:
            continue
            # 현재 이동 시간이 더 큰 경우 스킵
        
        for neighbor, move_time in route[current]:
        # 양방향 경로에서 다음 도시 및 이동 시간 탐색
            new_time = current_time + move_time
            # 다음 도시 이동 시간
            if new_time < time[neighbor]:
                # 다음 도시 이동 시간이 더 적은 경우
                time[neighbor] = new_time
                # 이동 시간 갱신
                heapq.heappush(heap, (new_time, neighbor))
                # 탐색 큐에 추가

    return time

dist_from_A = dijkstra(A)
# 각 도시 A에서의 최단 경로
dist_from_B = dijkstra(B)     
# 각 도시 B에서의 최단 경로

result = []
# 약속 장소 후보
for i in range(1, N + 1):
    if dist_from_A[i] + dist_from_B[i] == dist_from_A[B]:
    # 도시 i가 A에서 B로 가는 최단 경로 중 하나에 포함되는지 확인
        result.append(i)
        # 포함된다면 약속 장소 후보로 추가

print(len(result))
# 약속 장소 후보 개수
print(*sorted(result))
# 약속 장소 후보 번호 오름차순 정렬