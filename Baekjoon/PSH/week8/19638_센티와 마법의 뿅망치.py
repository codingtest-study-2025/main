""" 
input
    뿅망치의 효과 = 뿅망치에 맞은 사람의 키 / 2
        키가 1인 경우, X
    
    센티의 전략: 
    가장 키가 큰 거인 중 하나를 때리는 것을 반복

    // 첫째 줄: 
        거인의 나라 거인 수 N (1 ≤ N ≤ 100,000)
        센티의 키 H_centi (1 ≤ H_centi ≤ 2,000,000,000)
        제한된 횟수 T (1 ≤ T ≤ 100,000)        
    // 둘째 줄 ~ N+1번째 줄: 각 거인의 키 H (1 ≤ H ≤ 2,000,000,000)

output
    // 센티의 전략대로 때려, 모든 거인이 센티보다 작은 경우
        첫째 줄: YES 출력
        둘째 줄: 최소로 때린 횟수 출력
    // 센티의 전략대로 때려도, 센티보다 크거나 같은 거인이 있는 경우
        첫째 줄: NO 출력
        둘째 줄: 거인의 나라에서 가장 키가 큰 거인의 키 출력력

process
    시간 제한 1 초, 메모리 제한 1024 MB 고려

    N H_centi T 세팅
    H_giant 배열 생성

    큰 거인부터 대상이 되어야 하므로, 최대 힙으로 변환

    T번 반복
        제일 큰 거인도 센티보다 키가 작은 경우, 더 이상 진행 필요 X
        제일 큰 거인이 키가 1인 경우, 더 이상 진행 필요 X
"""

import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

import heapq
#from collections import deque
#sys.setrecursionlimit(10**6)

N, H_centi, T = map(int, input().split())
# 첫째 줄에 입력받은 N, H_centi, T 처리
H_giant = [int(input()) for _ in range(N)]
# 둘째 줄 ~ N+1번째 줄: 각 거인의 키 H 배열 생성
hammer_count = 0
# 뿅망치 사용 횟수

heap_giant = [-h for h in H_giant]
heapq.heapify(heap_giant)
# 키가 큰 거인부터 대상이 되어야 하므로, 최대 힙으로 변환

for _ in range(T):
    tallest_giant = -heapq.heappop(heap_giant)
    if tallest_giant < H_centi:
        heapq.heappush(heap_giant, -tallest_giant)
        break
        # 제일 큰 거인도 센티보다 키가 작은 경우, 더 이상 진행 필요 X
    if tallest_giant == 1:
        heapq.heappush(heap_giant, -tallest_giant)
        break
        # 제일 큰 거인이 키가 1인 경우, 더 이상 진행 필요 X
    new_height = tallest_giant // 2
    # 제일 큰 거인의 키를 2로 나눈 몫
    heapq.heappush(heap_giant, -new_height)
    # 힙에 추가
    hammer_count += 1
    # 뿅망치 사용 횟수 증가

if -heap_giant[0] < H_centi:
    # 제일 큰 거인이 센티보다 작은 경우
    print("YES")
    print(hammer_count)
else:
    print("NO")
    print(-heap_giant[0])  
    # 현재 힙에서 가장 큰 거인을 출력