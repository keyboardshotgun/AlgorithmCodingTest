from random import randint
import time

# -----------------------------------------------------------
# 빠르다                                                  느리다
# -----------------------------------------------------------
# O(1) > O(logN) > O(N) > O(NlogN) > O(N^2) > O(N^3) > O(2^N)
# -----------------------------------------------------------

# 파이썬 기본라이브러리의 경우 O(NlogN)을 보장한다.
# 선택정렬은 10,000개 이상의 항목일 경우 급격히 느려진다.
# 배열의 크기에 따라 .sort() 사용 판단.

array = []
array_b = []

for _ in range(10000):
    array.append(randint(1, 100))
    array_b.append(randint(1, 100))

start_time = time.time()

for i in range(len(array)):
    main_index = i
    for j in range(i+1, len(array)):
        if array[main_index] > array[j]:
            main_index = j
    array[i], array[main_index] = array[main_index], array[i]
end_time = time.time()

print("Algo Selection : ", end_time - start_time)

start_time = time.time()
array_b.sort()
end_time = time.time()

print("Python Default : ", end_time - start_time)
