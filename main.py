from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)


@app.route('/', methods=['post', 'get'])
def index():
    if request.method == "POST":
        return redirect('/grafics')
    else:
        return render_template("index.html")


@app.route('/grafics')
def grafics():
    return render_template("grafics.html")


@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
