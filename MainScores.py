from flask import Flask, send_file, render_template

app = Flask(__name__)


@app.route('/')
def score_server():
    file = 'Scores.txt'
    with open('Scores.txt', 'r') as file:
        content = file.read()
    return render_template('filesite.html', SCORE=content)


if __name__ == '__main__':
    app.run()
score_server()
