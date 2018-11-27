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
