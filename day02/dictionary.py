# 딕셔너리, 키와 값을 쌍으로 가지는 자료형
# 관련된 정보를 연관 시키며 뮤테이블 객체

my_dict = {}
my_dict[1] = 'a'
my_dict['b'] = 2
my_dict['c'] = 'd'

my_dict['kk'] = 'seed'
my_dict

del my_dict['kk']
my_dict[1] = 'aaaa'


## dict.values()
# 특정 객체만 사용할 수 있는 함수
# 딕셔너리에서 값만 뽑아서 돌려줌

my_dict.values()

for d in my_dict.values():
    print(d)

# keys와 dict 순회와 동일한 동작 
# kv 처럼은 안되는군
# for d in my_dict:
for d in my_dict.keys():
    print(d)


# kv pair
for k,v in my_dict.items():
    print(k,v)

