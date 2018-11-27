# mysite

* 장고 샘플 프로젝트
    * 관심목록 투표 시스템

### 사용자 스토리

* 사용자는 서비스에서 최근에 실시하는 질문 목록을 볼 수 있다.
* 사용자는 투표 목록을 선택 시, 세부 질문 항목을 볼 수 있다.
* 투표 목록은 복수 선택을 할 수 없으며, 투표 버튼을 눌러야 결정 할 수 있다
* 사용자는 다른 사용자들이 어떤 선택을 하였는지 투표수를 볼 수 있다.
* 사용자는 결과 화면에서 재 투표를 할 수 있다.



### 요구사항

- 최근에 실시하는 질문의 리스트를 보여주기
  - T : index.html
- 하나의 질문에 대해 투표할 수 있도록 답변 항목을 폼으로 보여주기
  - T : detail.html
- 질문에 따른 투표 결과를 보여주기
  - T : results.html



### 모델 정의

* 모든 컬럼은 not null로 정의하는 것이 추천
* PK는 자동 증가 속성이나, 분산 서버 환경 고려해 빼는것이 좋음(예제에서는 넣음)
* choice 테이블의 question의 경우 QuestTable과 Foreign Key 관계 설정. Index를 생성하도록 함
  * 질문에 없는 항목은 포함 될 수 없으며 검색 시 quest id를  통해 빠르게 검색 가능



* Question table
  * 질문을 저장하는 테이블

Column | type | const | desc
:-----:|:----:|:-----:|:---:
id|integer|NotNull, PK, AutoIncrement|Primary Key
question_text|varchar(200)|NotNull|질문 문장
pub_date|datetime|NotNull|질문 생성 시간



* Choice table
  * 질문별로 선택용 답변 항목을 저장

|   Column    |     type     |           const            |      desc      |
| :---------: | :----------: | :------------------------: | :------------: |
|     id      |   integer    | NotNull, PK, AutoIncrement |  Primary Key   |
| choice_text | varchar(200) |          NotNull           | 답변 항목 문구 |
|  voites           |   integer   |          NotNull           | 투표 카운트 |
|  question       | integer             |   NotNull,  FK(question, id), index          |    Foregin Key            |



