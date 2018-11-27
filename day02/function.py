# function

def findName(container,  a):

    if(container ==  None):
        container = []
    
    print(a)
    print(type(a))
    
    c = container
    c.append(a)
    return a,c


ct = []
result, ct = findName(ct, 1)


def add(num1, num2):
    return num1 + num2

add(1,2)

## 여러개의 값 돌려 받기
def add_mul(num1, num2):
    return num1 + num2, num1 * num2

# 2개 이상 시 튜플로 반환 immutable
# 언패킹 해서 별도로 가져 올 수도 있음
c =add_mul(1,2)
c1, c2 = add_mul(3,4)
c1
c2







# 모듈