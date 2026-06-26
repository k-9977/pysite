from flask import Flask, render_template, jsonify

app = Flask(__name__)


JOBS = [
    {
        'id': 1,
        'title': 'Palace Archivist',
        'location': 'Eastern Lotus Wing',
        'reward': '500 Gold Taels'
    },
    {
        'id': 2,
        'title': 'Court Musician',
        'location': 'Moon Pavilion',
        'reward': '450 Gold Taels'
    },
    {
        'id': 3,
        'title': 'Lantern Keeper',
        'location': 'Lantern Courtyard',
        'reward': '300 Gold Taels'
    },
    {
        'id': 4,
        'title': 'Palace Librarian',
        'location': 'Hall of Scrolls',
        'reward': '500 Gold Taels'
    }
]


@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS)


@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(debug=True)
