import urllib.request
urllib.request.urlopen("http://example.com").read().decode('utf-8')
urllib.request.urlopen("http://example.com/book/shakespeare").read().decode('utf-8')

# urllib.parse
# url의 분해, 조립, 변경 및 url 문자 인코딩, 디코딩 등을 처리

from urllib.parse import urlparse
result = urlparse('http://www.python.org:80/guido/python.html;philosophy?overall=3#n10')
result

## url.request
# urlopen(url, data=none, [timeout])
# 문자열 혹은 request 클래스 인스턴스
# url에 file scheme 지정 시 로컬 파일을 열 수 있음
# 디폴트로 get, pos의 경우 data 인자에 질의 문자열 지정
# timeout..

from urllib.request import urlopen
f = urlopen("http://www.example.com")
print(f.read(500).decode('utf-8'))


