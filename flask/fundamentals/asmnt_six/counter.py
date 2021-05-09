from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'yourkeys'
# our index route will handle rendering our form
@app.route('/')
def index():
    if 'yourkeys' in session:
        print('key exists!')
        session['yourkeys'] = session.get('yourkeys') + 1
    else:
        print("key 'yourkeys' does NOT exist")
        session['yourkeys'] = 1
    return render_template('index.html')

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
