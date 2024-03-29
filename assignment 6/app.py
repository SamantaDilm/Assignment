from controler import check_password, password_complexity, find_single_user, save_new_user
from flask import Flask, request, render_template, make_response

app = Flask(__name__)


INVALID_MESSAGE = "Invalid username or password"

# https://flask.palletsprojects.com/en/2.0.x/quickstart
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/


@app.route("/user/<user_id>")
def get_user(user_id: int):
    user = find_single_user(id=user_id)
    if user:
        return make_response({"username": user.username, "email": user.email}, 200)
    else:
        return make_response({"error": f"User with id {user_id} does not exist"})


@app.route("/create", methods=["POST"])
def create_user():
    username = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]

    the_user = find_single_user(username=username)
    if the_user is not None:
        return make_response({"error": "Please select a different username."}, 400)

    the_user = find_single_user(email=email)
    if the_user is not None:
        return make_response({"error": "A user with this e-mail address already exists."}, 400)

    # returns a message is the password does not meet complexity standards
    if msg := password_complexity(password):
        return make_response({"error": "password does not meet complexity requirements.", "failed": msg}, 400)

    try:
        save_new_user(username, email, password)
    except Exception as ex:
        return make_response({"error": f"could not create user {str(ex)}"}, 400)

    return make_response({"result": "success"}, 200)


@app.route("/login", methods=["POST"])
def process_login():
    username = request.form["username"]
    password = request.form["password"]

    # First, let's check if the user exists
    the_user = find_single_user(username=username)
    if the_user is None:
        return make_response({"error": INVALID_MESSAGE}, 400)

    # Now let's compare the stored password with the given password
    if check_password(the_user, password):
        return make_response({"result": "Login successful"}, 200)
    else:
        return make_response({"error": INVALID_MESSAGE}, 400)

# -- Here start template methods to present the correct template based on requests


@app.route("/create", methods=["GET"])
def create_user_template():
    return render_template("create_user.html")


@app.route("/login", methods=["GET"])
def show_login():
    return render_template("login.html", logged_in=False)


@app.route("/login/template", methods=["POST"])
def process_login_template():
    username = request.form["username"]
    password = request.form["password"]

    # First, let's check if the user exists
    the_user = find_single_user(username=username)
    if the_user is None:
        return render_template("login.html", logged_in=False, message=INVALID_MESSAGE)

    # Now let's compare the stored password with the given password
    if check_password(the_user, password):
        return render_template("login.html", logged_in=True, username=username)
    else:
        return render_template("login.html", logged_in=False, message=INVALID_MESSAGE)
