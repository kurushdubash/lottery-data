from flask import Flask, request, render_template
import os
app = Flask(__name__)


@app.route("/")
def hello():
	return app.send_static_file('index.html')

@app.route('/<path:path>')
def static_proxy(path):
    # send_static_file will guess the correct MIME type
    return app.send_static_file(os.path.join('jcss', path))


@app.route("/api/lottery", methods=["POST"])
def update_data():
    print(request.form['value'])
    data = request.form['value']
    if(data == 'NY'):
    	ny = 'checked'
    	ca = ''
    else:
    	ny = ''
    	ca = 'checked'

    return render_template('data.html', data=data, ny=ny, ca=ca)


if __name__ == "__main__":
    app.debug = True
    app.run()