"""
통과
"""
from sys import stdin
from collections import deque, defaultdict


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
                elif arr[ny][nx] == 0:
                    rows[cy].append((cx, idx))
                    cols[cx].append((cy, idx))


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
    rows, cols = defaultdict(list), defaultdict(list)
    parents = [-1] * 7

    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                cnt += 1
                bfs(i, j, cnt)

    edges = []
    for y in rows:
        rows[y].sort()

        for i in range(len(rows[y]) - 1):
            dist = rows[y][i + 1][0] - rows[y][i][0] - 1
            if dist > 1:
                edges.append((dist, rows[y][i][1], rows[y][i + 1][1]))

    for x in cols:
        cols[x].sort()
        for i in range(len(cols[x]) - 1):
            dist = cols[x][i + 1][0] - cols[x][i][0] - 1
            if dist > 1:
                edges.append((dist, cols[x][i][1], cols[x][i + 1][1]))

    print(kruscal())
