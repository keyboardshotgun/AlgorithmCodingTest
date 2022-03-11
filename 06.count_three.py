import time

# 해당 시 까지의 모든 시/분/초에 3이 포함되어 있으면, 카운트 + 1
# [00:00:00] ~ [N:00:00], (0 <= N <= 23)
# 완전탐색(Brute Forcing) 유형 : 모든 데이터 확인
# 100만개 이하일때 완전 탐색 사용시 적절
# 24 *60*60 = 86,400의 경우의 수 존재

h = 23
count = 0

start_time = time.time()
for a in range(1):
    for b in range(60):
        for c in range(60):
            if (str(a)+str(b)+str(c)).find('3') > -1:
                count += 1
end_time = time.time()
print('total 3 count : ', count)
print('total elapsed time', end_time - start_time)
