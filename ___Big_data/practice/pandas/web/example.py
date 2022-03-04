from x import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def first_index():
    return render_template('index.html')

@app.route('/index/')
def index():
    return render_template('index.html')

#index에서 submint된 id, pass(name값)을 요청.인자.얻기(index에서의 name값인 id, pass)
@app.route('/second/')
def second():
    _id = request.args.get("id")
    _pass = request.args.get("pass")
    print(_id, _pass)
    return render_template('second.html', id=_id, _pass = _pass)
    # return render_template('second.html') if _id == "asd" and _pass == "qwe" else print("실패하였습니다.") and render_template('third.html')

@app.route('/third/', methods=['POST'])
def third():
    _id = request.form['id']
    _pass = request.form['pass']
    return render_template('third.html')

app.run