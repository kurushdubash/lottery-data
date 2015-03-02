from flask import Flask, request, render_template
from random import randint
import os
from data import*
app = Flask(__name__)


@app.route("/")
def hello():
    return app.send_static_file('index.html')


@app.route("/api/lottery", methods=["POST"])
def update_data():
    print(request.form['value'])
    val = request.form['value']
    if(val == 'NY'):
        ny = 'checked'
        ca = ''
    else:
        ny = ''
        ca = 'checked'

    data = frequency_winning_numbers(check(val))
    # data = []
    # x = 0
    # while x < 25:
    #     data.append(randint(1, 25))
    #     x+=1
    print (data)
    return render_template('data.html', data=data, size=len(data), ny=ny, ca=ca)

if __name__ == "__main__":
    app.debug = True
    app.run()