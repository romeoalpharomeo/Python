from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/hi/<anything>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hi_anything(anything):
    print(anything)
    return "Hi, " + anything

"""
Create one url pattern and function that can handle the following examples (HINT: int() will come in handy! For example int("35") returns 35):
localhost:5000/repeat/35/hello - have it say "hello" 35 times
localhost:5000/repeat/80/bye - have it say "bye" 80 times
localhost:5000/repeat/99/dogs - have it say "dogs" 99 times
"""
@app.route('/repeat/<numberoftimes>/<thingtorepeat>')
def repeater(numberoftimes, thingtorepeat):
    repeat_it = thingtorepeat*int(numberoftimes)
    return repeat_it

if __name__ == "__main__":
    app.run(debug=True)