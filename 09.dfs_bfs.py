from collections import deque

# DFS vs BFS
# 프로그램적으로 데이터 구조는 행렬 또는 리스트로 구현

# 인접행렬
# 1 & 7 이 연결되어 있는지 파악 하려면 graph[1][7]
# INF = 999999999
# graph = [
# idx    0 1 2
# ----------------------------
#       [0,7,5]          // 0 -> 7 or 5
#       [7,0,INF]        // 7 -> 0
#       [5,INF,0]        // 5 -> 0
# ]

# 인접리스트
# 1 & 7 이 연결되어 있는지 파악 하려면 노드 1부터 모든 경로를 통해 7까지 확인이 필요하다.
# graph = [
# ----------------------------
#       [(1, 7), (2, 5)] // 0 -> 7 or 5
#       [(0, 7)]         // 7 -> 0
#       [(0, 5)]         // 5 -> 0
# ]
# idx 0 -> 1 -> 2   : [(1, 7), (2, 5)]
# idx 1 -> 0        : [(0, 7)]
# idx 2 -> 0        : [(0, 5)]

# * DFS 핵심
#   ㄴ> Depth 깊이
# 스택 + 재귀함수 사용.
# graph의 번호 대략 배열의 인덱스
# - 가장 가까운 노드(최저비용)로 이동 (push) , 방문하지 않은 노드로 가는 것이 아님
# - 인접노드가 없다 => 이전 노드로 돌아간다. (pop)
# - 방문하지 않는 노드가 없을 때 까지 반복.

# 예제1 2
import queue

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 8, 6],
    [1, 7]
]

# 전체 는 재귀로 처리하고, 노드정보가 담겨 있는 배열의 item을 루프 하여 다음 방문 인덱스를 처리 한다.

# 각 노드를 방문한 적이 있는지 확인처리용 아이템
# 각 노드를 방문한 적이 있는지 확인처리용 아이템

# dfs_visited = [false,false,false,false,false,false,false,false,false]
# graph index -> 0 => dfs_visited[0] = true
# graph index -> 1 => dfs_visited[1] = true => [2,3,8]

dfs_visited = [False] * len(graph)


# 시작(1) -> 방문한 포인트 저장(1) -> (1) 배열의 노드순회 -> 체크 -> 안가봤으면 재귀호출


def dfs(graph, point, dfs_visited):
    dfs_visited[point] = True
    if dfs_visited.count(True) == (len(graph) - 1):
        print(point, end='')
    else:
        print(point, end=' -> ')

    for item in graph[point]:
        if not dfs_visited[item]:
            dfs(graph, item, dfs_visited)


print('DFS\n')
dfs(graph, 1, dfs_visited)
print('\n------------------')
# 1 -> 2 -> 7 -> 8 -> 6 -> 3 -> 4 -> 5
#              ㄴ> 6 이 아니고 8인 이유는 graph에서 그렇게 정의해 두었기 때문이다.

# BFS
# 핵심
# ㄴ> Breadth
# 큐 + 루프 사용
# 데이터의 갯수가 N개인 경우 O(N)의 시간이 소요된다는 특성.
# 일반적으로 DFS보다 수행시간이 좋은편.
# 파이썬에서는 deque 라이브러리 사용

# 너비 우선 => 가장 가까운 노드 부터 탐색
# 방문한 포인트에서 갈수 있는 인접 노드를 전부 큐에 넣고 + 방문처리
# 순서대로 큐에서 꺼내서 해당 노드에서 방문한 적이 없는 노드를 큐에 넣는다.

bfs_visited = [False] * len(graph)


# 0 -> 1                    = [(True), (True), false , false , false ,false ,false  ,false  ,false]
# 1 -> (2, 3, 8, 추가)       = [false , True  , (True), (True), false ,false ,false  ,false  ,(True)]
# 2 -> 3, 8, (7, 추가)       = [false , True  , True  , True  , false ,false ,false  ,(True) ,True]
# 3 -> 8, 7, (4, 5 , 추가)   = [false , True  , True  , True  , (True),(True),false  ,True   ,True]
# 8 -> 7, 4, 5              = [false , True  , True  , True  , True  ,True  ,false  ,True   ,True]
# 7 -> 4, 5, (6 , 추가)      = [false , True  , True  , True  , True  ,True  ,(True) ,True   ,True]

def bfs(graph, point, bfs_visited):
    queue = deque([point])  # 1
    bfs_visited[point] = True
    while queue:  # queue 가 비어 있는 상태까지 반복
        next_visit = queue.popleft()  # 가장 먼저 들어 온 순서대로 인덱스(노드) 꺼내서
        print(next_visit, end=' ')
        for n in graph[next_visit]:  # 인덱스(노드)에서 방문 가능한 모든 노드를 탐색
            if not bfs_visited[n]:  # 방문하지 않았으면
                queue.append(n)     # 방문하지 않은 노드 추가 -> queue에 추가
                bfs_visited[n] = True  # 방문처리


print('\n\nBFS\n')
bfs(graph, 1, bfs_visited)
print('\n------------------')