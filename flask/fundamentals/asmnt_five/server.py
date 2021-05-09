from flask import Flask, render_template, request, redirect

app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")

from flask import Flask, render_template, request, redirect # added request
            
@app.route('/result', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    full_name_from_form = request.form['fullname']
    location_from_form = request.form['location']
    language_from_form = request.form['language']
    optional_comments_from_form = request.form['usercomments']
    return render_template("showresults.html", full_name_on_template=full_name_from_form, location_on_template=location_from_form, language_on_template=language_from_form, optional_comment_on_template=optional_comments_from_form)





if __name__ == "__main__":
    app.run(debug=True)