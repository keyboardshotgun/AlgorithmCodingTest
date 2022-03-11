# 그리드-왕실의 나이트

# 시작위치에서 이동 전략 두가지 존재
# 맴의 크기는 8x8
# 이동제한 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기. -> 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기.
# 맵크기를 벗어날 수 없다.
# y = a~h , x = 1~8 지칭
# 임의의 위치에서 나이트가 이동할 수 있는 경우의 수를 모두 구하면?
# 2->1->2->1 이동이므로, 최대 경우의 수 8인듯.
# e4 기준 최종 갈수 있는 포인트 들 (범위)
# if x - 3 >= 0 and y - 3 >= 0:
# if x - 1 >= 0 and y - 3 >= 0:
# if x - 3 >= 0 and y + 3 <= 7:
# if x - 1 >= 0 and y + 3 <= 7:
# if x + 3 <= 7 and y - 3 >= 0:
# if x + 3 <= 7 and y + 3 <= 7:
# if x + 1 <= 7 and y - 3 >= 0:
# if x + 1 <= 7 and y + 3 <= 7:

# 시작점
start_position = '3,3'

# 맵의 생성
map_list = []
for x in range(1, 9):
    if len(map_list) == x - 1:
        map_list.append([])
    for y in range(1, 9):
        map_list[x - 1].append(str(x) + ',' + str(y))


def movement_of_knight():
    count = 0  # 이동 가능 경우의 수
    this_x = 0
    this_y = 0

    for k in range(8):  # string으로 된 시작점의 배열 인덱스 구하기
        if start_position in map_list[k]:
            print('array index :', k, map_list[k].index(start_position))
            this_x, this_y = k, map_list[k].index(start_position)

    if this_x - 3 >= 0 and this_y - 3 >= 0:
        count += 1
    if this_x - 1 >= 0 and this_y - 3 >= 0:
        count += 1
    if this_x - 3 >= 0 and this_y + 3 <= 7:
        count += 1
    if this_x - 1 >= 0 and this_y + 3 <= 7:
        count += 1
    if this_x + 3 <= 7 and this_y - 3 >= 0:
        count += 1
    if this_x + 3 <= 7 and this_y + 3 <= 7:
        count += 1
    if this_x + 1 <= 7 and this_y - 3 >= 0:
        count += 1
    if this_x + 1 <= 7 and this_y + 3 <= 7:
        count += 1

    return count


print('start_position : ', start_position)
print('my_results : ', movement_of_knight())

# 검증
row = int(start_position.split(',')[0])
column = int(start_position.split(',')[1])
# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print('his_result : ', result)

# 결론. 문제를 잘 읽자.
# 1~2번 연속 이동 후의 경우의 수가 아니라 두가지 전략 중 각각 이동 할 수 있는 모든 전략 이다.
# 4,4 시작일때, 움직일 수 있는 경우의 수
#     [2,3]   [2,5]
# [3, 2]          [3,6]
#         [4,4]
# [5,2]           [5,6]
#     [6,3]   [6,5]

new_start_position = (3, 3)
knight_path_array = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]


def new_path_of_knight(start_p):
    new_count = 0
    start_x = start_p[0]
    start_y = start_p[1]

    for path in range(len(knight_path_array)):
        start_x += knight_path_array[path][0]
        start_y += knight_path_array[path][1]
        print('Order : ', knight_path_array[path][0], ',', knight_path_array[path][1])
        print('Move : ', start_x, ',', start_y)

        if (1 <= start_x <= 8) and (1 <= start_y <= 8):
            new_count += 1

        start_x = start_p[0]
        start_y = start_p[1]
        print('reset : ', start_x, ',', start_y, '\n')
    return new_count


print('new_result :', new_path_of_knight(new_start_position))
# 새로운변수 = 처음값 + 이동값 생각을 왜 못했을까? ㅎ
