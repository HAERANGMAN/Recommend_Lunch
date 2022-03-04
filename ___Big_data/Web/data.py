from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('data_index.html')

@app.route('/second', methods=['GET'])
def second():
    id = request.args.get('input_id')
    return render_template('data_second.html', id=id)

@app.route('/third', methods=['POST'])
def third():
    id= request.form['input_text']
    if id=="moon":
        return render_template('data_third.html', id=id)
    else:
        return "login fail"

app.run