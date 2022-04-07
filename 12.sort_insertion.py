# 선택 : 하나씩 서로의 자리교환
# 삽입 : 자리바꿈 x 배열의 길이
# 순서가 앞에서 부터가 아니라 뒤에서 부터!

import time
target_arr = [9, 5, 4, 2, 3, 1, 7, 8, 6]

for i in range(0, len(target_arr)):
    # 현재 선택된
    for j in range(i, 0, -1): # 조회 범위가 selection 보다 확실히 작다. 1/2
        print(f'{i} , {target_arr[j]} , {target_arr[j-1]}')
        if target_arr[j] < target_arr[j - 1]:
            target_arr[j], target_arr[j - 1] = target_arr[j - 1], target_arr[j]
            # back_up = target_arr.pop(j)
            # target_arr.insert(i, back_up)
        else:
            break

print(target_arr)
# 조회 범위가 selection 보다 확실히 작다. 1/2
# 복잡도 O(N^2/2) 최선 O(N), 최하 O(N^2)