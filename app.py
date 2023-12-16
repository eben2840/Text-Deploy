from flask import Flask,redirect, session,url_for,render_template,request

app=Flask(__name__)






@app.route('/',methods=['GET','POST'])
def splash():
    # session['cart'] = []
    return render_template('index.html')

@app.route('/home',methods=['GET','POST'])
def home():
    # session['cart'] = []
    return render_template('home.html')
















if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(host='0.0.0.0', port=5000,debug=True)