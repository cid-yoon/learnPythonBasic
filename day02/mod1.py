def sum(a,b):
    return a+b

def safe_sum(a,b):
    if type(a) != type(b):
        print('더할 수 있는 것이 아님')
        return
    else:
        result = sum(a,b)
    return result


def sub(a,b):
    return a - b

# 모듈 임포트 시 실행 되 버림
# __name__ 체크로 방지하기, 다른곳에서 임포트 시, 모듈 이름으로 추가됨
if __name__ =="__main__":
    print(sum(1,2))
    print(sub(4,2))
    print(safe_sum(4,'a'))


## 연습문제
import sys
sys.path.append("/Users/seedyoon/queen/python/learnPythonBasic/day02/doit/")

from mymod import mysum



# 임포트 여러 방법
# import game.sound.echo => echo_test()
# import game.sound =>echo.echo_test() ...

# import 없이 사용은 불가 game.sound.echo.echo_test()
# import game을 수행하면 game 디렉터리의 모듈 또는 game 디렉터리의 __init__.py에 정의된 것들만 참조할 수 있다.


# __init__.py 해당 디렉터리가 패키지의 일부임을 알려주는 역활, 패키지에 포함된 디렉터리에 __init__.py 파일이 없으면
# 패키지로 인식되지 않음, 3.3 이후부터는 인식 되지만 호환성 위해 씁시다.

# from game.sound import *
# echo.echo_test()
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#  NameError: name 'echo' is not defined
# 특정 디렉터리의 모듈을 * 을 이용해 import 시 __init__.py 파일에 __all__이라는 변수를 설정하고
# import 할 수 있는 모듈 정의 필요
# 에코는 모듈이 아니라 구조이기에 인식 할 수 없었음











