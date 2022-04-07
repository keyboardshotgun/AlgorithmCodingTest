# 가장 작은 것을 '선택' 하여 가장 처음으로 보낸다.
# [5,9,4,2,3,1,7,8,6]
import time
target_arr = [5, 9, 4, 2, 3, 1, 7, 8, 6]
test_arr = [5, 9, 4, 2, 3, 1, 7, 8, 6]


def selection_sort(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                continue
    return arr


print('-------------------------------')
start_timeA = time.time()
print(selection_sort(target_arr))
print(time.time() - start_timeA)
print('-------------------------------')
start_time = time.time()
test_arr.sort(reverse=True)
print(test_arr)
print(time.time() - start_time)
print('-------------------------------')

# 후기
# 기존습성에 너무 익숙해져 있는 듯. j+1 이 index 오류가 발생할 것이라 판단...파이썬은 다르다.
# range 함수의 특성 기억하자. range(s, e) -> e는 포함되지 않는다.
# range(10) === range(0, 10) => 0 ~ 9

# 연산횟수
# N(N-1)/2 => N^2
# 데이터가 10배면 수행시간은 100(10*10)배 증가
# 선택정렬의 경우 10,000개 이상이면 시간이 크게 증폭.