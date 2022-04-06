import random

# N * M
# open  : 0
# close : 1
# 상하좌우 연결된 블록이 0이면 1덩어리 (0 1개도 1덩어리)
# 배울점, 재귀함수의 호출에 제한을 두지 말자. 중지 조건 확인

nX = 10
nY = 10
ice_graph = []


def randint_zero_or_one():
    return random.randint(0, 1)


for _ in range(nY):
    ice_graph.append([randint_zero_or_one() for _ in range(nX)])

print('\n-----------------before')
for i in range(nY):
    print('\n')
    for j in range(nX):
        print(ice_graph[i][j], end=' ')
print('\n-----------------------')


def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= nX or y <= -1 or y >= nY:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if ice_graph[x][y] == 0:
        # 해당 노드 방문 처리
        ice_graph[x][y] = 'O'
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    elif ice_graph[x][y] == 1:
        ice_graph[x][y] = 'X'
    return False


# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(nY):
    for j in range(nX):
        # 현재 위치에서 DFS 수행
        if dfs(i, j):
            result += 1

print('\n------------------after')
for i in range(nY):
    print('\n')
    for j in range(nX):
        print(ice_graph[i][j], end=' ')
print('\n-----------------------')

print('\n\nresult : ' + str(result))  # 정답 출력
