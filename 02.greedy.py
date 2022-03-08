from random import randint

# 2.2 큰수의 법칙 문제, 총합구하기.

# 반복횟수 : M [1~10000]
# 연속사용제한횟수 : K [1~10000]
# array_length : 배열의 크기 [2~1000]
# M >= K
# ex) array_length = 5, K = 3, M = 8
# [2,4,5,4,6] => (6+6+6+5) + (6+6+6+5)

# 인덱스가 다른 큰 동수가 나온 경우 : [7,7,x,...], K=4, M=10 가정.
# 연속 4+1       |  연속 4+4
# 7777 7 7777 7 | 7777 7777 77 -> 총합은 같다.
# 고로, (first * K) + second 형태로 처리하기로 함.
# 여기서 힌트를 얻어 K+1 마다 반복 되므로, 나누어 떨어지는 특성을 이용하기로 하였다.
# 즉, 전체반복 중 두번 째 큰수가 나오는 경우만 판단 하여 처리 하기로 하였다.

M = 10
K = 2

array_length = 10  # 배열의 크기 [2~1000]
max_value = 10  # 배열 각 항목의 크기 [1~10000]
numbers_array = []
total = 0  # 총합
total_text = ''  # 테스트용

for i in range(array_length):
    numbers_array.append(randint(1, max_value))

print('K, M =>', K, ',', M)
print('List Length =>', len(numbers_array))

numbers_array.sort(reverse=True)
first, second = numbers_array[0:2]

print('first, second =>', first, ',', second)

for index in range(1, M + 1):
    if index % (K + 1) == 0:
        total += second
    else:
        total += first

print('my_total => ', total)

# 검증
# K = 3, M = 12

# OOOX
# OOOX
# OOOX

#  전체   /  가로   =  세로길이  * 가로일부(K)  = 큰수등장 횟수
#    12  /  K+1   =       3  *         3 = 9
#  (K+1) *  X     =      12 , 4X = 12, X = 3
#   전체 - 큰수횟수 = 작은횟수
#   12   - 9개    = 3개

count = int(M / (K + 1)) * K
count += M % (K + 1)
result = 0
result += count * first  # 가장 큰 수 더하기
result += (M - count) * second  # 두 번째로 큰 수 더하기
print('his_total =>', result)  # 최종 답안 출력