from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        a = request.form.get('query')
        print(str(a))
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
