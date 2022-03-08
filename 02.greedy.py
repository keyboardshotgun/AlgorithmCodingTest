from random import randint

# 큰수의 법칙
#   주어진 수들을 M(=8)번 더하여 가장 큰 수를 만드는 것.
#   동일수 더하기 K(=3) 반복 제한이 존재 한다.
##  같은수라도 인덱스가 다르면 연속해서 사용가능
### [2,4,5,4,6] => (6+6+6+5) + (6+6+6+5)

# 주어진 수들을 M(=7)번 더하여 가장 큰 수를 만드는 것.
# 동일수 더하기 K(=2) 반복 제한이 존재 한다.

# M [1~10000] >= K [1~10000]
# [3,4,3,4,3] => 44 44 44 4
# K 2nd M     | 1st               | 2nd
# ---------------------------------------------------------
# 1  1  10 -> | 5(1+1+1+1+1)      | 5 # 10 / 1+1 => 5
# 2  1  10 -> | 7(2+2+2+1)        | 3 # 10 / 2+1 => 3.3
# 3  1  10 -> | 8(3+3+2)          | 2 # 10 / 3+1 => 2.5
# 4  1  10 -> | 8(4+4)            | 2 # 10 / 3+1 => 2
# 5  1  10 -> | 9(5+4)            | 1 # 10 / 3+1 => 1.6
# 6  1  10 -> | 9(6+3)            | 1 # 10 / 3+1 => 1.4
# ---------------------------------------------------------
# 큰수로 정렬 K => numbers_array[0:2]
# M번 반복 되는 K번의 1st 연속 / 1번의 2nd 숫자의 총합

M = 10  # 반복횟수
K = 2  # 가장큰수 연속 횟수
array_size = 10000  # 총 배열의 크기 [2~1000]
max_value = 10000  # 배열 각 항목의 범위 [1~10000]
total = 0
total_text = ''
numbers_array = []

for i in range(15):
    numbers_array.append(randint(1, 10000))

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
