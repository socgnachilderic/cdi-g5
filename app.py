from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html', members=[
        " SIAKAM Omer", "SOCGNA Childéric",
        "TAOUSSET Abdoul", "TCHEUPI Jonathan",
        "TCHUEM Dimitri", "TCHUEM Nelson", "Wamba Gabin"
    ])


if __name__ == '__main__':
    app.run(debug=True)
