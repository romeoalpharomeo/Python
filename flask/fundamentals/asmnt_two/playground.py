from flask import Flask, render_template

app = Flask(__name__)
@app.route('/play')
def hello_world():
    return render_template('index.html')

# import statements, maybe some other routes
    
@app.route('/play/<x>')
def multiply_boxes(x):
    return render_template('index2.html', numberofboxes = int(x))

@app.route('/play/<x>/<color>')
def multiply_boxes_choose_color(x, color):
    return render_template('index3.html', numberofboxes = int(x), boxcolor = color)

# app.run(debug=True) should be the very last statement! 
if __name__ == "__main__":
    app.run(debug=True)

