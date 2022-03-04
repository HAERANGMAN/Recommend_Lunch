from flask import Flask, render_template, send_file
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/corona')
def corona():
    corona_df = pd.read_csv('corona.csv')
    corona_df.columns=['인덱스','등록일시','사망자','확진자','게시글번호','기준일',
                    '기준시간','수정일시','누적의심자','누적확진율']
    corona_df.sort_values('등록일시', inplace=True)                
    corona_df['일일확진자']=(corona_df['확진자']-corona_df['확진자'].shift()).fillna(0)    
    #일일확진자추가=전행-후행(nan경우 0삽입)
    corona_df['일일사망자']=(corona_df['사망자'].diff().fillna(0))
    #상동 다른공식
    corona_df['Class']=corona_df["누적확진율"].apply(lambda x : 'high' if (x >= 3.5) else 'low')
    corona_df.drop(['인덱스','기준일','게시글번호','기준시간','수정일시'], axis=1, inplace=True)
    corona_df.reset_index(drop=True, inplace=True)
    corona_dict = corona_df.head(50).to_dict() #헤드10개만.딕셔너리로
    cnt = len(corona_dict['등록일시'].keys())
    return render_template('corona.html', result = corona_dict, cnt = cnt)


@app.route('/img')
def img():
    corona_df = pd.read_csv('corona.csv')
    corona_df.columns=['인덱스','등록일시','사망자','확진자','게시글번호','기준일',
                    '기준시간','수정일시','누적의심자','누적확진율']
    corona_df.sort_values('등록일시', inplace=True)                 #등록일시로 정렬
    corona_df['일일사망자']=(corona_df['사망자'].diff().fillna(0))  #컬럼사망자 추가
    decide_cnt = corona_df.head(10)['일일사망자'].values.tolist() #헤드(나오는값)열개.값만.리스트로변경
    state_dt = corona_df.head(10)['등록일시'].values.tolist()
    plt.plot(state_dt, decide_cnt)
    img_1 = BytesIO()
    plt.savefig(img_1, format="png", dpi=300)
    img_1.seek(0)

    return send_file(img_1, mimetype='image/png')

app.run