from random import randint

# 가장 높은 숫자 카드 뽑기
# W * H 크기
# 1. 행선택
# 2. 그 행의 가장 낮은 수를 가진 카드가 최종카드
# ex)
# --W--
# 3 1 2 |
# 4 1 4 H
# 2 2 2 |
# ------
# 1, 2행은 결론적으로 1이 뽑힌다.
# 3행은 2가 뽑힌다. 3행이 승자.
# N,M = range(1,100) , randInt(1,10000)

# 세팅
W = randint(1, 100)
H = randint(1, 100)
array = []

for i in range(H):
    array.append([])
    for j in range(W):
        array[i].append(randint(1, 10000))

# 풀이
array_of_min = []  # 각 행의 최소 값 배열
min_value = 0  # 각 행의 최소 값 중 최대 값
min_H = 0  # 선택의 대상이 되는 행

for x in range(H):
    if x == 0:
        min_value = min(array[x])
        array_of_min.append(min(array[x]))
    else:
        if min_value < min(array[x]):
            min_value = min(array[x])
            min_H = x
        array_of_min.append(min(array[x]))

print("array : ", array)
print("array_of_min : ", array_of_min)
print("min_value : ", min_value)
print("min_H_Index : ", min_H)

# 검증
# min = 0 가 습관적으로 몸에 배어 있긴 하나 보다.
# 교재의 답에서는 max = 10001 로 처리하였다.
# max(현재배열의 값, 저장한 최저값) 로직사용 if else 파트가 없다.