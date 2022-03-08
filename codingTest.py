from random import randint
import time

array = []
for _ in range(10000):
    array.append(randint(1, 100))

## 선택정렬 알고리즘 : 3.109124183654785
start_time = time.time()
for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]
end_time = time.time()

array = []
for _ in range(10000):
    array.append(randint(1, 100))

start_time = time.time()

## 기본정렬 함수ㄹ : 0.0006961822509765625
array.sort(reverse=True)
end_time = time.time()

# 선택정렬은 시간이 3초, 기본정렬은 0.0001초 걸렸다.
# 동일알고리즘 2개에서 한개의 알고리즘의 시간복잡도가 높다면 , 성능이 낮음을 의미 한다.
# 알고리즘을 테스트 할 때에는 최대한 복잡도가 낮게 프로그램을 작성해야 한다.
