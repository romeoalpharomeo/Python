from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'guessit'

@app.route('/')
def index():
    session['computer_number'] = random.randint(1,100)
    print(session['computer_number'])
        
    return render_template("index.html")

@app.route('/checknumber', methods=['POST'])
def check_number():
    session['userguess'] = int(request.form['userGuess'])
    cnum = session.get('computer_number')
    print(session['userguess'])
    print(cnum)
    return render_template('gameinprogress.html', usernumber=session['userguess'], compnum=int(cnum))


if __name__ == "__main__":
    app.run(debug=True)