# 반복문 기본 구조
# 반복되는 지루한 작업 처리
# for, while 두가지 존재
# for는 횟수, while 은 조건을 기준으로

my_list = [1,2,3,4,5]
for v in my_list:
    print(v)

# 이렇게는 안됨
for v in range(my_list):
    print(v)

# 3까지 도는 거, 0이 기본으로 설정
# -(NUMBER) 는 안먹히는군요
for v in range(3):
    print(v)

# 1~3까지 돌아요
for v in range(1,3):
    print(v)


## 중첩 for 구구단임
for n in range(2, 10):
    for v in range(1,10):
        print('{} * {} = {}'.format(n, v, v*n))
    print('\n')


## 컴프리핸션
# 리스트를 만드는 간결한 방법
# 주어진 리스트에서 홀수만 뽑아내는 코드로 테스트

numbers = [1,2,3,4,5,6,7,8,9,10]
odd_numbers = []

for n in numbers:
    if n % 2 == 1:
        odd_numbers.append(n)
    

# 간결하게 만드는 방법
# for 안에서 처리되는 조건 식을 통하여 반환된 값을 n으로 돌려줘서 리스트로 생성
# 링큐와 비슷하면서도 다른 모습 - 내포 
# https://ddanggle.gitbooks.io/interpy-kr/ch15-comprehension.html
odd_numbers = [n for n in numbers if n % 2 == 1 ]


