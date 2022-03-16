from flask import Flask
from flask import request, redirect
from flask import render_template

app = Flask(__name__)

@app.route('/mypage/me', methods=['GET'])
def me():
    return render_template("me.html")

@app.route('/mypage/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        #print("We received GET")
        return render_template("contact.html")
    elif request.method == 'POST':
        #print("We received POST")
        print(request.form)
        return render_template("contact.html")