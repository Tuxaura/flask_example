from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check')
def check():
    is_upper = False
    is_lower = False
    is_end_num = False
    username = request.args.get('username')
    is_upper = any(c.isupper() for c in username)
    is_lower = any(c.islower() for c in username)
    is_end_num = username[-1].isdigit()
    result = is_upper and is_lower and is_end_num
    return render_template('check.html', result=result, is_upper=is_upper, is_lower=is_lower, is_end_num=is_end_num)

if __name__ == '__main__':
    app.run(debug=True)