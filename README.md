# hansung-schedule-parser

## How to start
1. git clone https://github.com/2022-Hansung-WebFramework1/hansung-schedule-parser.git
2. python -m venv venv && pip install -r requirements.txt
3. vi secrets.json
4. add your id, password in secrets.json with format {"id": "YOUR_ID", "password": "YOUR_PASSWORD"}
5. python main.py

## Example
```
[
    {
        "kwamokcode": "V024005",
        "kwamokname": "웹프레임워크1",
        "isugubun": "전필",
        "hakjum": "3",
        "juya": "야",
        "bunban": "N",
        "haknean": "3",
        "haknean_limit": "",
        "prof": [
            "박승현"
        ],
        "online": "온라인강좌 1.5시간",
        "classroom": "공학관309",
        "day": "수",
        "startTime": "18:00",
        "endTime": "19:15",
        "id": "55",
        "plan": "20222110858V024005N",
        "c12": "",
        "c13": "110858",
        "suup_pyunga": "20222110858V024005N",
        "bigo": "FL＋PBL(대표교수법)",
        "kcomment": "본 교과목에서는 자바 스프링 프레임워크에 대해 학습한다. 구체적으로, 스프링 개발을 위한 시스템 구축, Maven 활용법, 의존성 주입(dependency injection), JDBC를 이용한 DB 연동, 웹 폼과 스프링 MVC를 이용한 웹 응용 프로그램 작성 방법을 학습한다. 또한 스프링 시큐리티를 활용한 사용자 계정 관리, AOP(Aspect-Oriented Programming) 기술을 소개한다. 본 과정에서는 웹 응용 서버 프로그램을 단계적으로 설계 및 구현하는 프로젝트 기반 접근 방법을 제공한다.",
        "ekname": "Web Framework I",
        "gwamokgun": "",
        "kwamokgubun": "트랙필수"
    },
	...
]
```
