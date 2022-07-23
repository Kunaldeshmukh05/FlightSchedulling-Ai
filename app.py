from flask import Flask, render_template, request
from main import run

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        source = request.form.get('source')
        destination = request.form.get('destination')
        output = run(source, destination)
        return render_template('index.html', context=output)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)