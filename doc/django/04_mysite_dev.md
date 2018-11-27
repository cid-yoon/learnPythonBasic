# 애플리케이션 개발



### 테이블 정의

* App 내부에 테이블 모델 정의

```python
from django.db import models

# Create your models here.

# 테이블을 하나의 클래스로 정의
# 테이블의 컬럼은 클래스의 변수(속성)으로 매핑
# django.db.models.Model 상속 후 각 클래스 변수의 타입도 장고에서 미리 정의된
# 필드 클래스 사용

# 클래스 변수명은 컬럼명 그대로 매핑
# __str__() 메소드는 객체를 문자열로 표현할 때 사용. 나중에 보게 될 Admin 사이트나
# 장고 쉘 등에서 테이블명을 보여줘야 하는데, 이때 __str__() 메소드를 정의하지 않으며
# 테이블명이 제대로 표시되지 않음. 


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

```



### admin 사이트에 테이블을 반영하기 위한 작업

* admin.py 수정

```python
from django.contrib import admin
from polls.models import Question, Choice
# Register your models here.

# 너무나도 깔끔하게 페이지에 등록
admin.site.register(Question)
admin.site.register(Choice)
```

* Migration 명령을 통해 db sync

```shell
# 디렉토리 하위에 마이그레이션 파일이 생성
# migrations/xxxx_initial.py
python mange.py makemigrations

# 해당 파일을 이용하여 마이그레이션
python manage.py migrate

## 마이그레이션 시 사용하는 SQL 문장 확인 가능
python manage.py sqlmigrate polls 0001


-- Create model Question
--
CREATE TABLE "polls_question" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "question_text" varchar(200) NOT NULL, "pub_date" datetime NOT NULL);
--
-- Add field question to choice
--
ALTER TABLE "polls_choice" RENAME TO "polls_choice__old";
CREATE TABLE "polls_choice" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "choice_text" varchar(200) NOT NULL, "votes" integer NOT NULL, "question_id"integer NOT NULL REFERENCES "polls_question" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "polls_choice" ("id", "choice_text", "votes", "question_id") SELECT "id", "choice_text", "votes", NULL FROM "polls_choice__old";
DROP TABLE "polls_choice__old";
CREATE INDEX "polls_choice_question_id_c5b4b260" ON "polls_choice" ("question_id");
COMMIT;
```





## View 및 Template  작업

### UrlConf

* URL 과 뷰는 1:1 또는 1:N으로 매핑 가능
* URLconf 처리가 urls.py를 통해 작성
* 프로젝트와 앱 간 구분하여 처리하는 것이 유지보수성을 위해 좋음
  * 네임스페이스처럼 사용 할 수 있음
* path() 메소드를 통하여 핸들러 처리
  * 필수 인자 
    * Route : URL 패턴을 표현하는 문자열. 
    * view : URL 스트링이 매칭되면 호출되는 뷰 함수, HttpRequest 객체와 URL 스트링에서 추출된 항목 전달
  * 선택 인자
    * kwargs : URL 스트링에서 추출된 항목 외에 추가적인 인자를 뷰 함수에 전달할 때 사용, dict로 인자 정의
    * Name: 각 URL 패턴별로 이름 지정, 템플릿 파일에서 많이 사용됨

```python
# mysite/urls.py

from django.contrib import admin
# include를 통해 app - polls로 url 처리 위임
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/polls/', include('polls.urls')),
]
```

```python
# mysite/polls/urls.py

from django.urls import path

# 모든 뷰를 import하여 처리
from . import views

# 상대 경로로 설정하여 간략화
# int형의 questid를 인자로 전달, views.detail과 연결, named
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>', views.detail, name='detail'),
    path('<int:question_id>', views.results, name='results'),
    path('<int:question_id>', views.vote, name='vote'),

]
```









