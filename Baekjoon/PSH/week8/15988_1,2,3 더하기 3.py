""" 
input
    정수 n (1 ≤ n ≤ 1,000,000)의 1, 2, 3의 합으로 나타내는 방법의 수 구하기기

    // 첫째 줄: 테스트 케이스의 개수 T
    // 둘째 줄 ~ T+1번째 줄: 정수 n (1 ≤ n ≤ 1,000,000)

output
    // 각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 1,000,000,009로 나눈 나머지를 출력

process
    시간 제한 1 초 (추가 시간 없음), 메모리 제한 512 MB 고려
    1 ≤ n ≤ 1,000,000 고려

    처음 시도: 재귀 함수로 구현
    문제점: n이 1,000,000까지 가능하므로 재귀 깊이 초과 및 시간 초과 발생
    해결: DP 사용

    DP를 사용하여 해결
        dp[i] = i를 1, 2, 3의 합으로 나타내는 방법의 수

    dp[1] = 1, dp[2] = 2, dp[3] = 4 dp[4] = 7
        dp[4] (7) = dp[3] (4) + dp[2] (2) + dp[1] (1)
    
    점화식: dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
"""

import sys

#sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

#import heapq
#from collections import deque
#sys.setrecursionlimit(10**6)

MOD = 1000000009
# 모듈로 값 정의
T = int(input())
# 테스트 케이스 개수
Test_case = [int(input()) for _ in range(T)]
# 첫째 줄에 입력받은 T만큼 반복하여 테스트 케이스 배열 생성
Range = max(Test_case)
# 테스트 케이스 중 최대 값을 추출해, 사용할 값 판단

dp = [0] * (Range + 1)
# 테스트 케이스의 최대 값을 이용해, dp 배열 초기화

dp[0] = 1
if Range >= 1:
    dp[1] = 1
if Range >= 2:
    dp[2] = 2
if Range >= 3:
    dp[3] = 4
# 너무 낮은 n 예방

for i in range(4, Range + 1):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % MOD
    #점화식 적용

for i in Test_case:
    print(dp[i])
# 테스트 케이스 출력