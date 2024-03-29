"""
참고자료: https://jyeonnyang2.tistory.com/54
"""
from sys import stdin


if __name__ == "__main__":
    n, k = map(int, stdin.readline().split())

    dp = list([0] * (k + 1) for _ in range(n + 1))
    dp[0][0] = 1
    for i in range(n + 1):
        for j in range(1, k + 1):
            dp[i][j] += dp[i - 1][j] + dp[i][j - 1]

    print(dp[n][k] % 1000000000)
