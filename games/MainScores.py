from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def score_server():
    try:
        with open('Scores.txt', 'r') as file:
            content = file.read()
        return render_template('filesite.html', SCORE=content)
    except Exception as err:
        return render_template('errorsite.html', ERROR=err)


if __name__ == '__main__':
    app.run(threaded=True)
