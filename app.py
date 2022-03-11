from flask import Flask, render_template
from data import db_session
from data.users import User
from data.jobs import Jobs
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def add_user(user: User):
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()


def create_user(*args):
    user = User()
    user.surname = args[0]
    user.name = args[1]
    user.age = args[2]
    user.position = args[3]
    user.speciality = args[4]
    user.address = args[5]
    user.email = args[6]
    add_user(user)


def main():
    db_session.global_init("db/blogs.db")
    app.run()


@app.route("/")
@app.route("/index")
def index():
    db_sess = db_session.create_session()
    jobs_list = db_sess.query(Jobs).all()
    workers = db_sess.query(User).all()
    worker_dict = {i.id: f"{i.surname} {i.name}" for i in workers}
    return render_template("index.html", title="My page", jobs=jobs_list, worker_dict=worker_dict)


if __name__ == '__main__':
    main()
