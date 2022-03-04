import pandas as pd


corona_df = pd.read_csv('___Big_data\practice\pandas\web\corona.csv')
corona_df.columns=['인덱스','등록일시','사망자','확진자','게시글번호','기준일',
                '기준시간','수정일시','누적의심자','누적확진율']
corona_df.sort_values('등록일시', inplace=True)                 #등록일시로 정렬
corona_df['일일사망자']=(corona_df['사망자'].diff().fillna(0))  #컬럼사망자 추가
decide_cnt = corona_df.head(20)['일일사망자'].values.tolist() #헤드(나오는값)열개.값만.리스트로변경
print(decide_cnt)
state_dt = corona_df.head(10)['등록일시'].values.tolist()
print(state_dt)