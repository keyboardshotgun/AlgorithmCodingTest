from random import randint

# 큰수의 법칙 문제

# [2,4,5,4,6] => (6+6+6+5) + (6+6+6+5)
# 반복횟수 : M [1~10000]
# 연속사용제한횟수 : K [1~10000]
# array_length : 배열의 크기 [2~1000]
# M >= K

# 인덱스가 다른 큰 동수의 경우 : [7,7,x,...], K=4, M=10 가정
# 연속 4+1       |  연속 4+4
# 7777 7 7777 7 | 7777 7777 77
# 총합은 같다.
# 고로, 수의 반복은 K+1

K = 2
M = 10
array_size = 1000  # 배열의 크기 [2~1000]
max_value = 10000  # 배열 각 항목의 크기 [1~10000]
numbers_array = []
total = 0  # 총합
total_text = ''  # 테스트용

for i in range(array_size):
    numbers_array.append(randint(1, max_value))

print('List =>', numbers_array)
print('List Length =>', len(numbers_array))

numbers_array.sort(reverse=True)
first, second = numbers_array[0:2]

for index in range(1, M + 1):
    if index % (K + 1) == 0:
        total_text += ' 2nd '
    else:
        total_text += ' 1st '

print(total_text)
