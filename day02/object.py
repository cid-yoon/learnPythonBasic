## object
# 파이썬도 객체지향

# 다른 예제 가볍게 찾아 보기


## 최종 날짜 구하기

import time
from datetime import datetime, timedelta

from operator import mul

t_now = time.time()
print(t_now)


class Calculator:
    def __init__(self):
        self.result = 0
        
    def add(self,num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(3))

print(cal2.add(32))
print(cal2.add(13))


class FourCal:
    def __init__(self, inA, inB):
        self.num1 = inA
        self.num2 = inB
    
    def setdata(self, n1, n2):
        self.num1 = n1
        self.num2 = n2

    def sum(self):
        return self.num1 + self.num2
    
    def mul(self):
        return self.num1 * self.num2
    
    def sub(self):
        return self.num1 - self.num2
    
    def div(self):
        return self.num1 / self.num2


# 상속, 이전에 정의된 타입을 상속
# 쿨하네, 생성자 처리는?
class MoreCal(FourCal):
    def __init__(self, inA, inB):
        super().__init__(inA**2, inB**2)
    def pow(self):
        return self.num1 ** self.num2

type(MoreCal)


# 오버라이딩 지원
class SafeFourCal(FourCal):
    def div(self):
        if self.num2 == 0:
            return 0
        else:
            return self.num1 / self.num2


aa = SafeFourCal(4,0)
aa.div()


# 클래스 변수 == static 변수처럼 사용
# 인스턴스별 변수는 객체 변수를~
class Family:
    lastname = 'yoon'


a = Family()
b = Family()

print(a.lastname)
print(b.lastname)

Family.lastname = '이'

print(a.lastname)
print(b.lastname)


# 클래스 활용
userData = '홍길동,20,A'
tmp = userData.split(',')
age = tmp[1]

def print_age(data):
    tmp = data.split(',')
    age = tmp[1]
    print(age)


def print_grade(data):
    tmp = data.split(',')
    grade = tmp[2]
    print(grade)

userData = '홍길동,20,A'
print_age(userData)
print_grade(userData)

class User:
    def __init__(self, data):
        parse = data.split(',')
        self.name = parse[0]
        self.age = parse[1]
        self.grade = parse[2]


usr = User(userData)
print( usr.name )    
print( usr.age )    
print( usr.grade )    
    

## 연습문제
class ECalc:
    def __init__(self):
        self.value = 0
    def add(self, val):

        result = self.value + val
        if(result > 100):
            result = 100
        
        self.value = result

    def sub(self, val):
        self.value = self.value -val

    

cal = ECalc()
cal.add(3)
cal.add(4)
        
cal.value



class GCalc:
    def __init__(self, numList):
        self.numbers = numList
    
    def sum(self):
        result = 0
        for n in self.numbers:
            result += n
        
        return result

    # 람다
    def avg(self):
        return (self.sum() / len(self.numbers))

gcal = GCalc([1,2,3,4,5])
gcal.sum()
gcal.avg()


gcal = GCalc([6,7,8,9,10])
gcal.sum()
gcal.avg()