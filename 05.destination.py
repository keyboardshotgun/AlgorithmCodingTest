# 일반적인 제한
# 1초 이내 실행, 128MB 메모리 제한을 가짐.
# Python 3.7 기준 1초에 2천만번 수준의 연산, 문풀이 목표

# 메모리 제약
# C/C++, JAVA
# - int 자료형의 크기 : 4 byte
# - long 자료형의 크기 : 8 byte
# - BigInteger 자료형의 크기 : 가변적, 무제한
# Python
# - 리스트의 길이, 1000개당 4KB 차지.
# - 결과가 천만단위 이상의 리스트 길이를 가진다면 문제발생 가능성 있음.

# 시간제한 1초, 데이터 개수가 100만개의 문제 라면, O(NlogN) 이내의 알고리즘 선택이 필수

map_list = [
    [['1,1'], ['1,2'], ['1,3'], ['1,4'], ['1,5']],
    [['2,1'], ['2,2'], ['2,3'], ['2,4'], ['2,5']],
    [['3,1'], ['3,2'], ['3,3'], ['3,4'], ['3,5']],
    [['4,1'], ['4,2'], ['4,3'], ['4,4'], ['4,5']],
    [['5,1'], ['5,2'], ['5,3'], ['5,4'], ['5,5']]
]

start_point = [0, 0]
order_map = ['R', 'R', 'R', 'R', 'R', 'R', 'L', 'D', 'D', 'D', 'D', 'D']


def dest(start, order):
    move_y, move_x = start
    max_x = len(map_list[0]) - 1
    max_y = len(map_list) - 1

    print(max_x, max_y)

    for o in order:
        if o == 'R':  # y의 증가
            if move_y < max_y:
                move_y += 1
                print('moved R', move_y)
            else:
                print('out R')
        elif o == 'D':  # x의 증가
            if move_x < max_x:
                move_x += 1
                print('moved D', move_x)
            else:
                print('out D')
        elif o == 'L':  # y의 감소
            if move_y > 0:
                move_y -= 1
                print('moved L', move_y)
            else:
                print('out L')
        elif o == 'U':  # x의 감소
            if move_x > 0:
                move_x -= 1
                print('moved U', move_x)
            else:
                print('out U')
        else:
            print('wrong order')

    print('Destination is ', map_list[move_x][move_y])


dest(start_point, order_map)
