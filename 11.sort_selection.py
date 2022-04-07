# 가장 작은 것을 '선택' 하여 가장 처음으로 보낸다.
# [5,9,4,2,3,1,7,8,6]
import time

target_arr = [5, 9, 4, 2, 3, 1, 7, 8, 6]
test_arr = [5, 9, 4, 2, 3, 1, 7, 8, 6]


def selection_sort(arr):
    for i in range(0, len(arr)):
        selection_number = arr[i]
        for j in range(0, len(arr)):
            if selection_number > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                selection_number = arr[j]
            else:
                continue
    return arr


print('-------------------------------')
start_timeA = time.time()
print(selection_sort(target_arr))
end_timeA = time.time()
print(end_timeA - start_timeA)
print('-------------------------------')
start_time = time.time()
test_arr.sort(reverse=True)
end_time = time.time()
print(test_arr)
print(end_time - start_time)

# 후기
# 기존습성에 너무 익숙해져 있는 듯. j+1 이 index 오류가 발생할 것이라 판단...파이썬은 다르다.
# range 함수의 특성 기억하자. range(s, e) -> e는 포함되지 않는다.
# range(10) === range(0, 10) => 0 ~ 9