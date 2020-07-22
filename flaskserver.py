from flask import Flask
from flask import render_template #템플릿을 사용하게 해
from flask import request  #헤더와 바디쪽에 객체를 꺼내

app = Flask(__name__)

@app.route("/")
def rootFn():
    return "hello flask"

@app.route("/test") # 라우팅 경로
def testFn():
    return "<h1>korea</h1>"

@app.route("/a") # 홈페이지 뒷부분에 작성
def mainFn():
    return render_template('a.html') #html 문서를 불러

@app.route("/b") # 홈페이지 뒷부분에 작성
def bFn():
    return render_template('b.html', myname='김철수',myage=30) #html 문서를 불러

@app.route("/addrform") # 홈페이지 뒷부분에 작성
def addrformFn():
    return render_template('address.html') #html 문서를 불러

@app.route("/addrproc") # 홈페이지 뒷부분에 작성
def addrprocFn():
    myname =request.args['myname'] # 입력한 값을 출
    myage =request.args['myage']
    myaddr =request.args['myaddr']
    s=f'이름:{myname} 나이:{myage} 주소:{myaddr}' # 포맷함수
    return s #html 문서를 불러



if __name__ == '__main__':
    app.run(debug=True)
