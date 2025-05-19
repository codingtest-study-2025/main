# [input]
# 첫째 줄: T
# T개 줄: n

# [output]
# 테스트 케이스마다 방법의 수를 1,000,000,009로 나눈 나머지 출력

# [조건]
# 0 < n <= 1,000,000

# [풀이방법]
# 전형적인 DP 문제 (중복되는 부분 문제 and 최적 부분 구조)
# dp[i] = i를 1,2,3의 합으로 표현하는 방법의 수
# dp[i] = dp[i-1] + dp[i-2] + ... + dp[0]

import sys

# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

MOD = 1_000_000_009

T = int(input())
case_list = [int(input()) for _ in range(T)]
n_max = max(case_list)  # 케이스 중 가장 높은 n 찾기

# dp 배열 계산 (가장 높은 n에 대해 dp 계산)
dp = [0] * (n_max + 1)
dp[0] = 1
for i in range(1, n_max + 1):
    dp[i] = dp[i-1]
    if i >= 2:
        dp[i] = (dp[i] + dp[i-2]) % MOD
    if i >= 3:
        dp[i] = (dp[i] + dp[i-3]) % MOD

# 결과 출력
result = []
for n in case_list:
    print(dp[n])
