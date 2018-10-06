from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    print("--"*40,"Matrix Active!!!"*4,"--"*40)
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    print("Got Post Info")
    print(request.form)
    print('strawberry', request.form['strawberry'])
    print('raspberry', request.form['raspberry'])
    print('apple', request.form['apple'])
    print('apple', request.form['blackberry'])
    print('first_name', request.form['first_name'])
    print('last_name', request.form['last_name'])
    print('student_id', request.form['student_id'])
    return render_template("checkout.html")

@app.route('/fruit')         
def fruit():
    return render_template("fruit.html")

if __name__=="__main__":   
    app.run(debug=True)    