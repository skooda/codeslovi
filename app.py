from flask import Flask, request, session, render_template, redirect, url_for
from app import game

flask = Flask(__name__)


@flask.route("/")
def index():
    return render_template('index.html')


@flask.route("/start")
def start():
    game.start()

    return redirect(url_for('riddle', id=0))


@flask.route("/riddle/<int:id>")
def riddle(id):
    code = game.get_hilighted_code(id)
    start_time = game.get_start_time()
    return render_template('riddle.html', code=code, id=id, repeat=request.args.get('repeat', False), start_time=start_time)


@flask.route("/answer", methods=['POST'])
def answer():
    ans = request.form['answer']
    id = int(request.form['id'])

    if not game.is_answer_ok(ans, id):
        return redirect(url_for('riddle', id=id, repeat=True))

    game.save_answer(ans, id)
    if id == 4:
        game.end()
        return redirect(url_for('finish'))

    return redirect(url_for('riddle', id=id+1))


@flask.route("/skip/<int:id>")
def skip(id):
    game.save_answer("", id)

    if id == 4:
        game.end()
        return redirect(url_for('finish'))

    return redirect(url_for('riddle', id=id+1))


@flask.route("/finish")
def finish():
    return render_template('finish.html', total_time=game.get_pretty_time(), answers=game.get_answers())


if __name__ == "__main__":
    flask.secret_key = 'heureka2016'
    flask.config['SESSION_TYPE'] = 'filesystem'

    flask.run(debug=True, host)