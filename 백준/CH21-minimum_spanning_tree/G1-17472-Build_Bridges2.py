"""
코드 수 줄임
"""
from sys import stdin
from collections import deque


input = lambda: stdin.readline().rstrip()


def bfs(y, x, idx) -> None:
    dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]
    dq = deque([(y, x)])
    arr[y][x] = -idx

    while dq:
        cy, cx = dq.popleft()

        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]

            if 0 <= ny < N and 0 <= nx < M:
                if arr[ny][nx] > 0:
                    arr[ny][nx] = -idx
                    dq.append((ny, nx))
                elif arr[ny][nx] == 0 and \
                        (not borders[0][cy] or borders[0][cy][-1] != [cx, idx]):
                    borders[0][cy].append([cx, idx])
                    borders[1][cx].append([cy, idx])


def find(x: int) -> int:
    if parents[x] < 0:
        return x
    parents[x] = find(parents[x])
    return parents[x]


def union(x: int, y: int) -> bool:
    x, y = find(x), find(y)
    if x == y:
        return False

    parents[x] += parents[y]
    parents[y] = x
    return True


def kruscal():
    edges.sort()
    res = 0
    for dist, a, b in edges:
        if union(a, b):
            res += dist
        if parents[find(a)] == -cnt:
            return res
    return -1


if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = list(list(map(int, input().split())) for _ in range(N))
    borders = list(list([] for _ in range(10)) for _ in range(2))
    parents = [-1] * 7

    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                cnt += 1
                bfs(i, j, cnt)

    edges = []
    for i in range(2):
        for j in range(len(borders[i])):
            borders[i][j].sort()
            for k in range(len(borders[i][j]) - 1):
                dist = borders[i][j][k + 1][0] - borders[i][j][k][0] - 1
                if dist > 1:
                    edges.append([dist, borders[i][j][k][1], borders[i][j][k + 1][1]])

    print(kruscal())
