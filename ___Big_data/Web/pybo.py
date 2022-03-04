from flask import Flask


app = Flask(__name__)
# 플라스크 애플리케이션을 생성하는 코드
# __name__은 모듈명이 담긴다. 파일이 실행되면 pybo라는 문자열이 담긴다.

@app.route('/')
# app.route는 특정 URL에 접속하면 다음줄의 함수를 호출하는 플라스크 데코레이터이다.
# 데코레이터는 기존 함수를 변경하지 않고 추가 기능을 덧붙일수 있는 함수
def hello_pybo():
    return 'Hello, Pybo!'

@app.route('/second')
def second():
    return 'Second Page'



app.run