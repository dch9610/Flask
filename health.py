from flask import Flask, render_template, request
from webCalc import Obs
app = Flask(__name__)

@app.route("/health")
def healthFn():
    return render_template('day2_test2.html')



@app.route("/bimanForm")
def bimanFn():
    return render_template('bimanForm.html')

@app.route("/bimanresult") # 홈페이지 뒷부분에 작성
def bimanprocFn():
    myh =int(request.args["myh"]) # 입력한 값을 출력
    myw =int(request.args["myw"])
    rst,rimg=Obs(myh,myw)
    return render_template("resultbiman.html",bimanresult=rst,bimanimage=rimg)


if __name__ == '__main__':
    app.run(debug=True)
