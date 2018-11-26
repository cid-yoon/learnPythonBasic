# 문자나 문자들을 나열
# 값을 변경 할 수 없으며, 순서가 있음, 
# 큰 따옴표나 작은 따옴표로 구분


my_str = 'python'
print(my_str)

type(my_str)

# 따옴표 세개... 여러줄을 하나의 변수로 저장 가능
multiline = '''cody
add
seed
noah
kevin
'''


# 포멧팅
input_data = 'my name is %s' % 'seed'
input_num = 'input data %d %d' % (1,2)
input_float = 'input %f' % (1.2)


# 현대적 패턴에서는 format을 더 많이 사용
# 중괄호를 이용하여 대입

print('my name is {}'.format('seed'))
# 괄호 순서에 따라 기본 정렬
# 번호를 정하면 그에 따라 순서 지정도 가능
print('{} x {} = {}'.format(2, 3, 2*3))
print('{1} x {0} = {2}'.format(2, 3, 2*3))



# 인덱싱
# 위치에 따라 각 문자에 접근 가능, 위치는 0부터 시작, 공백도 포함
alphabat = 'abcde'
print(alphabat[0])
print(alphabat[3])

# out range index
print(alphabat[5])

name = '시드윤 바보'

# 드
name[1]

# 마이너스로도 주소 표현 가능
# e
alphabat[-1]
# c
alphabat[-3]


# 슬라이싱
# 인덱싱과 비슷
# 문자열에서 여러 값을 한꺼번에 잘라오기, 콜론 : 을 이용해서 한꺼번에 가져오기
# 기존 문자열은 그대로 두고 복사해서 사용

book_name = '파이썬 웹 프로그래밍 완벽가이드'
print(book_name[1:3])
print(book_name[0:2])
print(book_name[:5])
print(book_name[3:])

# 파이썬 웹 프로그래밍 완
print(book_name[:-4])

# 이드
print(book_name[-2:])

# 파이썬 웹 프로그래밍 완벽가
print(book_name[:-2])


# 메서드 - string.split()
# 특정한 기능을 수행하기 위한 코드를 모아두고 이름을 붙인 것
# 메서드는 특정 객체만 사용할 수 있는 함수
# string.split(): 문자열을 공백 기준으로 분리하는 메서드

book_name.split()
# >>> ['파이썬', '웹', '프로그래밍', '완벽가이드']
fruit = '거봉,포도,수박,복숭아,참외,망고'
fruit.split(',')
['거봉', '포도', '수박', '복숭아', '참외', '망고']


## Docstring
# 문서화 문자열(Documentation string)
# 함수가 어떤 일을 수행하는지 설명
# 보통 끈따옴표 세개를 사용

def tempFunc():
    """설명할게요"""
    return


# print, 기본 end 설정 가능
# 출력의 끝을 맞출 수 있음
print( 'code', end='\t')







