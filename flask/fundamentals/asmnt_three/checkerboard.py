from flask import Flask, render_template
import math

app = Flask(__name__)
@app.route('/')
def basic_checkerboard():
    return render_template('index.html')

@app.route('/<x>')
def pick_number_of_rows(x):
    row_correction = x
    return render_template('index2.html', numberofrows = int(row_correction))



if __name__ == "__main__":
    app.run(debug=True)