from flask import Flask,request,render_template
from werkzeug.utils import redirect
from flask.helpers import url_for
import subprocess

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def start_login():
    if request.method == 'POST':
        productId=request.form['productId']
        return redirect(url_for('success',productId=request.form['productId']))
    else:
        return "false"

@app.route('/success')
def success():
    productId = request.args.get('productId')
    ##启动爬虫
    # subprocess.check_output(['python' 'jd_crawl_v1.0.py' '-a' 'productId=' + productId])
    subprocess.getoutput(["python","jd_crawl_v1.0.py"])
    return render_template('success.html')
    #
    # return render_template('success.html', productId=request.args.get('productId'))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5500)
    # app.run(host='0.0.0.0', port=5555)