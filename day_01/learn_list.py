# 여러개 값을 함께 모아서 추가 가능
# 값들은 변경 가능하고 순서가 있음
# 가변과 불변 - 가변(리스트, 딕셔너리), 불변 - 문자열, 튜플

# 빈 리스트 생서
my_list = []

# 타입 보임
type(my_list)
type([])


# 값 추가하기 LIST.append()
students = ['seed', 'cody', 'rabbit']
students.append('kevin')
students.append('evan')

print(students)
# ['seed', 'cody', 'rabbit', 'kevin', 'evan']

# 그릇과 유사, 빈 리스트에도 값 추가 가능
# 요로케는 안됨. 일단 받고 써야 하네
# 리스트 이기는 하지만 이름이 부레이키 되니..
g = [].append('new entity')

# 인덱싱 다시 나옮
students[:]
# ['seed', 'cody', 'rabbit', 'kevin', 'evan']
students[-1:]
# ['evan']
students[-2:]
# ['kevin', 'evan']
students[-3:]
# ['rabbit', 'kevin', 'evan']
students[-4:]
# ['cody', 'rabbit', 'kevin', 'evan']
students[-5:]
# ['seed', 'cody', 'rabbit', 'kevin', 'evan']
students[:-1]
# ['seed', 'cody', 'rabbit', 'kevin']
students[:-2]
# ['seed', 'cody', 'rabbit']
students[:-3]
# ['seed', 'cody']
students[:-4]
# ['seed']
students[:-5]
# []


# list method
# LIST.sort() 우선순위 (가나다, 알파벳) 정렬
# LIST.count('name') 몇명 더 있니?
del students[1]
del students[1:4]




