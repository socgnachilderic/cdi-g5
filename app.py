from flask import Flask, render_template

app = Flask(__name__)


def generate_members():
    return [
        " SIAKAM Omer", "SOCGNA Childéric",
        "TAOUSSET Abdoul", "TCHEUPI Jonathan",
        "TCHUEM Dimitri", "TCHUEM Nelson", "Wamba Gabin"
    ]


@app.route('/')
def hello_world():
    return render_template('index.html', members=generate_members())


if __name__ == '__main__':
    app.run(debug=True)
