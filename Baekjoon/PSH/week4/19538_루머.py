""" 
input
    // 조건
        // 루머는 최초 유포자로부터 시작된다
            // 탐색 시작 노드
        // 최초 유포자는 여러 명일 수 있다
            // 탐색이 여러 곳에서 시작될 수 있다
        // 매 분 루머를 믿는 사람은 모든 주변인에게 루머를 동시에 퍼트리며,
            // 매 탐색마다, 모든 주변 노드를 탐색한다 = BFS
        // 군중 속 사람은 주변인의 절반 이상이 루머를 믿을 때 본인도 루머를 믿는다
            // 조건
                // 각 노드를 방문했을 때, 믿는 노드의 수수를 확인해야 한다
                // 이를 기준으로 기준 노드의 믿음 값을 갱신해야 한다
        // 루머를 믿는 순간부터 다른 말은 듣지 않기 때문에, 한번 믿은 루머는 계속 믿는다
            // 중복 탐색 방지 위해, 방문 여부 체크 필요

    // 첫번째 줄: 사람의 수 n (1 ≤ n ≤ 200,000)
    // 둘번번째 줄 ~ n 개의 줄:
        // i 번째 줄 : i번 사람의 주변인들의 번호, 입력의 마지막을 나타내는 구분자 0
        // 모든 노드는 양방향으로 연결되어 있음
    // n + 1 번째 줄: 최초 유포자의 수 (1 <= m <= n)
    // n + 2 번째 줄줄: 최초 유포자의 번호 (중복 X)

output
    // 각 i가 trust 값이 true인 순서 출력
    // trust 값이 false인 경우, -1 출력

process
    // 친구 배열
    // 과반수 판단용 배열
        // 노드가 최대 200,000개이므로 미리 계산하기기
    // 최초 유포자 배열
    // BFS 함수
        // 변수 설정
            // 믿는 시점 (출력 및 true 겸용)
            // 루머를 믿는 주변 친구 수 (과반수 판단용)
            // 방문 체크용
        // 최초 유포자 초기화
            // 다수일 수 있으니까 반복문?
        // 탐색 시작
            // 탐색의 최초 시작은 최초 유포자
                // 첫 방문이라면, 무조건 해당 노드의 "루머를 믿는 주변 친구 수"를를 증가시켜야 함
            // 과반수 판단 후, "루머를 믿는 주변 친구 수"가 과반수 이상일 때,
                // 해당 노드의 루머를 믿는 시점을 갱신
        // 탐색 종료
"""

import sys
sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

from collections import deque

n = int(input())
# 입력 처리
friends = [[] for _ in range(n + 1)]
# 인덱스=사람 번호, 값=주변인 목록

for i in range(1, n + 1):
    raw_friends = list(map(int, input().split()))
    # 2번째 부터 n번째 줄의 raw_friends 값을 받아서 배열로 정리
    for f in raw_friends[:-1]:  
    # 마지막 0 제외
        friends[i].append(f)
        # 양방향
        friends[f].append(i)  
        # 양방향

majority = [0] * (n + 1)
# 인덱스=사람 번호, 값=과반수 깂
for i in range(1, n + 1):
    majority[i] = (len(friends[i]) + 1) // 2
#bfs함수 내에서 하는 경우, 비효율적

m = int(input()) 
# input()으로 처리 가능하지만, 나중에 쓸 수도 있으니까 일단 받아둠
start_peoples = list(map(int, input().split()))
#최초 유포자가 여러 명일 수 있으니까 배열로 받음

# BFS 함수 정의
def bfs(start_nodes):
    time = [-1] * (n + 1)            
    # 루머를 믿는 시점 = true의 역할 겸용
    rumor_friend = [0] * (n + 1)     
     # 루머를 믿는 주변 친구 수 = 과반수 판단용
    trust = [False] * (n + 1)
    # 이 문제에서는 중복 방문이 존재하기 때문에 변수명이 믿음의 여부가 적절함함
    queue = deque()

    # 최초 유포자 초기화
    for start in start_nodes:
        trust[start] = True
        time[start] = 0
        queue.append(start)

    while queue:
        current = queue.popleft()
        for neighbor in friends[current]:
             if not trust[neighbor]:
                rumor_friend[neighbor] += 1
                # 최초 시작부터 무조건 믿는 사람이므로, 방문마다 증가
                if rumor_friend[neighbor] >= majority[neighbor]:
                    trust[neighbor] = True
                    time[neighbor] = time[current] + 1
                    queue.append(neighbor)

    return time

# 실행
result = bfs(start_peoples)

# 출력
for t in result[1:]:  
# 1번부터 n번까지 출력
    print(t)