# N=X, M=Y (4 ~ 200)
# start(1, 1)
# monster = 0
# vacancy = 1
# 미로는 반드시 탈출 할수 있는 형태로 제공됨. => 문제 만들기를 어떻게 처리 해야 하나?
# 첫째칸(1,1) 마지막칸(N,M) 은 항상 1
# (1,1)에서 몇칸을 이동 가능한지 파악.
# 포인트는 방문지역을 저장하는 것.

import random
from collections import deque


def maze_buider(n, m):
    maze_prison = []
    for y in range(0, n):
        maze_prison.append([])
        for x in range(0, m):
            if (y == 0 and x == 0) or (y == n - 1 and x == m - 1):
                maze_prison[y].append(1)
            else:
                maze_prison[y].append(random.randint(0, 1))
    return maze_prison


NX = 4
NY = 4
amaze_prison = maze_buider(NX, NY)

for i in amaze_prison:
    print("\n")
    for j in i:
        print(j, end=" ")

print('\n')
NX = 4
NY = 4

direction_array = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1]
]

# 1. 방문한 포인트에서 갈 수 있는 모든 포인트를 큐에 넣는다.
# 2.

visited = [[True for _ in range(0, NY)] for i in range(0, NX)]


def bfs(s_point, maze_prison):
    dq = deque([s_point])
    # maze_prison[s_point[0]][s_point[1]]
    cnt = 0
    while len(dq) > 0:
        this_point = dq.popleft()  # 현재 포인트를 꺼낸다.
        visited[this_point[0]][this_point[1]] = False
        cnt += 1
        print(this_point)
        for y in direction_array:  # 현재 포인트에서 4방향을 체크 한다.
            thisX, thisY = this_point[0] + y[0], this_point[1] + y[1]
            if (-1 < thisX < NX) and (-1 < thisY < NY) and visited[thisX][thisY] == True:
                if maze_prison[thisX][thisY] == 1:  # 방문 한적이 없고 방문 가능한 지역이면 큐에 넣는다.
                    dq.append((thisX, thisY))
    return cnt


start_point = (0, 0)
result = bfs(start_point, amaze_prison)
print('result : ' + str(result))

# 방문지역 저장을 따로 만드는 것보다. 0이면 넘기는 것으로 처리 하는 것이 프로그램적으로 넘기는 것이 효율적인가?