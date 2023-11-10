"""
Создать страницу, на которой будет форма для ввода имени и электронной почты,
при отправке которой будет создан cookie-файл с данными пользователя,
а также будет произведено перенаправление на страницу приветствия,
где будет отображаться имя пользователя.
На странице приветствия должна быть кнопка «Выйти»,
при нажатии на которую будет удалён cookie-файл с данными пользователя
и произведено перенаправление на страницу ввода имени и электронной почты.
"""

from flask import Flask, request, make_response, render_template, redirect, url_for


app = Flask(__name__)


@app.route("/")
def form():
    return render_template("form.html")


@app.route("/welcome", methods=["POST"])
def welcome():
    name = request.form["name"]
    email = request.form["email"]
    resp = make_response(render_template("welcome.html", name=name))
    resp.set_cookie("user", "%s:%s" % (name, email))
    return resp


@app.route("/logout")
def logout():
    resp = make_response(redirect(url_for("form")))
    resp.set_cookie("user", "", expires=0)
    return resp


if __name__ == "__main__":
    app.run(debug=True)
