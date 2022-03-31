# (x, y) 위치
# N*M 의 크기
# 바다로는 이동 못함.
# 1. 현재 위치에서 현재 방향을 기준으로 왼쪽방향(반시계 90도회전)부터 차례대로 갈 곳을 정한다.
# 이동시 방향이 다를 경우 회전의 수가 추가 되었다.
# 오른쪽바라보기 -> (왼쪽이동) -> 왼쪽 바라보기 -> 왼쪽이동 (회전의 제한은 반시계방향으로 90도 회전)
# 주변 네방향 모두 갔었던 곳이거나, 바다 인 경우, 바라 보는 방향을 유지하고, 한 칸 뒤로 가고 1.을 계속 함.
# 뒤로 한칸 간 곳이 바다라면 움직임을 멈춘다.

# 맵크기 세로 N >= 3 , 가로 M >= 50
# 0,1,2,3 (북,동,남,서)
# 시작은 언제나 육지
# N개의 줄에 맵의 상태가 북쪽 -> 남쪽, 서쪽 -> 동쪽, 맵의 외곽은 바다이다.
# 첫줄, 마지막줄, 바다, 처음, 끝 인덱스 바다.
# 나머지는 바다/육지 중 랜덤으로 처리. 0은 육지, 1은 바다
# -----
# 4 x 4
# -----
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1
# print 3
# 캐릭터가 모두 방문한 숫자, 무조건 1개 이상. (처음 시작이 무조건 육지 이므로)
import time
from random import randint

map_array = []


def land_builder(N, M, stp):
    init_position, init_direction = stp.split(':')
    init_x, init_y = init_position.split(',')
    print(init_x, init_y, init_direction)
    map_array = [[0 for col in range(N)] for row in range(M)]

    for x in range(N):
        print('', end='\n')
        for y in range(M):
            if x == 0 or x == (N - 1) or y == 0 or y == (M - 1):
                print('[~]', end=' ')
                map_array[x][y] = 1;
            else:
                if x > 0:
                    if randint(0, 1) == 1:
                        map_array[x][y] = 1
                        print('[~]', end=' ')
                    else:
                        map_array[x][y] = 0
                        print('[0]', end=' ')
                else:
                    map_array[x][y] = 0
                    print('[0]', end=' ')

    print('\n')
    return map_array


y_N = 10
x_M = 10
start_point = '3,4:0'

new_map = land_builder(y_N, x_M, start_point)
land_map = []

for i in range(y_N):
    for j in range(x_M):
        if new_map[i][j] == 0:
            land_map.append([i, j])

intX, intY = land_map[randint(0, len(land_map) - 1)]

new_map[intX][intY] = 'S'
# 위 -> 아래, 서쪽 -> 동쪽
# 초기위치, 바라보는 방향 0~3 랜덤,
print('Start position : [{0},{1}] '.format(intX, intY))
for i in range(y_N):
    print('', end='\n')
    for j in range(x_M):
        print(new_map[i][j], end=' ')
print('\n')

arrow_dic = {'0': '➡', '1': '⬆', '2': '⬅', '3': '⬇'}


def possible_check(intX, intY, view_position):
    checkRight = new_map[intX][intY + 1]
    checkUp = new_map[intX - 1][intY]
    checkLeft = new_map[intX][intY - 1]
    checkDown = new_map[intX + 1][intY]
    check_map = [checkRight, checkUp, checkLeft, checkDown]
    # array_pos = {'0': 'checkRight', '1': 'checkUp', '2': 'checkLeft', '3': 'checkDown'}

    x = 0
    while True:
        if check_map[((view_position + x) % 4)] == 1 or check_map[((view_position + x) % 4)] == 'S':
            x += 1
        elif check_map[((view_position + x) % 4)] == 0:
            position = str((view_position + x) % 4)
            if position == '0':
                new_map[intX][intY + 1] = 'S'
                return [intX, intY + 1, int(position)]
            elif position == '1':
                new_map[intX - 1][intY] = 'S'
                return [intX - 1, intY, int(position)]
            elif position == '2':
                new_map[intX][intY - 1] = 'S'
                return [intX, intY - 1, int(position)]
            elif position == '3':
                new_map[intX + 1][intY] = 'S'
                return [intX + 1, intY, int(position)]
            break
        if x == 4:
            return []


count = 0
view_p = 0
step_print = ''

while True:
    result = possible_check(intX, intY, view_p)
    if len(result) > 0:
        intX, intY, view_p = result
        step_print += ' '+arrow_dic[str(view_p)]
        count += 1
        print(str(count) + ' : ' + step_print)
    else:
        break
    time.sleep(1)

print('total_steps : ', str(count))