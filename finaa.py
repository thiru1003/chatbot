from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    topic = request.form['topic']
    # Replace this with your actual language model function
    results = ['Fact 1', 'Fact 2', 'Fact 3']
    return render_template('result.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)