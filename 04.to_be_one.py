# 임의의 숫자 1 만들기
# 전략 두가지
# 1) -1
# 2) N을 K로 나누어 떨어질때까지, 중간에 나누어 떨어지지 않으면 게임오버.
# 2 <= N,K <= 100,000

# N을 K의 배수가 -1 전략을 유지한다.
# 배수가 되면 2번 전략 사용한다.

count, K, the_number = 0, 5, 25

while True:
    if the_number >= K and the_number % K == 0:
        if K == 1:
            print('K는 1 이상 이여야 합니다.')
            break
        the_number /= K
        count += 1
    else:
        if the_number == 1:
            break
        else:
            the_number = the_number - 1
            count += 1

print('count => ', count)