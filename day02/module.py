## 모듈, import

# random 모듈 살펴보기

import random

student = ['apple', 'seed', 'cocoa', 'banana']
print(random.choice(student))

# 샘플링 해서 뽑을 수 있음
my_choice_set = random.sample(student,2)
print(my_choice_set)

# 난수 생성 ( 1~10) 모두 포함 이상 이하로 체크
my_int = random.randint(1,10)
print(my_int)


# 시드를 이용해서 시퀀스 랜덤도 동작 확인
random.seed(1,1)
my_int = random.randint(1,10)
print(my_int)



## 점프투 파이썬 모듈
# 만들 파일이 같은 경로에 있어야 일단 참조 가능
# 당연히 상대 체크 할 수 있는 뭔가 있을 듯
import mod1

# 코드 수정시, 리임포트 가능
import imp
imp.reload(mod1)
print(mod1.sum(1,2))
print(mod1.safe_sum(3,4))
print(mod1.sub(4,2))

# 모듈 임프트 시 실행을 막아 줄 수 있는 표현식
# __name__ == "__main__"
# 이것이 참인 경우라는 건 해당 인터프리터가 직접 실행 한것
# 가져오기 및 해당 모듈을 부를 시에는 불러지지 않음