from flask import Flask, render_template
import random

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/random')
def random_number():
    number = random.randint(1, 100)
    return f'''
    <html>
        <head>
            <title>Random Number</title>
        </head>
        <body style="text-align: center; margin-top: 50px;">
            <h1 style="color: blue;">Your Random Number</h1>
            <p style="font-size: 20px;">The random number is: <strong>{number}</strong></p>
            <a href="/" style="color: red; text-decoration: none;">Go back to picture of mountain</a>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
