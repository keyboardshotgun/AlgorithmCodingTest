from random import randint
import time

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