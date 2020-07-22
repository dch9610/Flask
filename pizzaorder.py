from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/pizza")
def pizzaFn():
    return render_template('pizza.html')

@app.route("/order")
def orderFn():
    myname=request.args["myname"]
    mytel=request.args["mytel"]
    myemail=request.args["myemail"]
    mytime=request.args["mytime"]
    mysize=request.args["mysize"]
    topping=request.args["topping"]
    myde=request.args["myde"]
    s=f'고객명:{myname} </br> 전화번호:{mytel} </br> E-mail:{myemail} </br> 사이즈:{mysize} </br> 토핑:{topping} </br> 요청사항:{myde}'
    return s
    # render_template('pizzaresult.html', myname= myname, mytel=mytel ,myemail=myemail, mytime= mytime,mysize=mysize,topping=topping,myde=myde)

if __name__ == '__main__':
    app.run(debug=True)
