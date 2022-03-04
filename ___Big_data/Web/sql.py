from flask import Flask, render_template
import pymysql

app = Flask(__name__)

sample_db = pymysql.connect(
    user = 'root',
    passwd = '1234',
    host = 'localhost',
    db = 'test',
    charset = 'utf8'
)
"""
user: user name
passwd: 설정한 패스워드
host: DB가 존재하는 host
db: 연결할 데이터베이스 이름
charset: 인코딩 설정
"""

cursor = sample_db.cursor(pymysql.cursors.DictCursor)

@app.route('/')
def index():
    sql = "SELECT * FROM `board`;"
    cursor.execute(sql)
    result = cursor.fetchall()
    return render_template('sql_index.html', result=result)

app.run