from flask import Blueprint, render_template, g, request, redirect, flash
from app.services.login_services import LoginServices
from app.model.user_login import UserLogin

login = Blueprint("login", __name__)

@login.before_request
def inicializar():
    bd = LoginServices()
    g.bd = bd
    bd.crear_tablas()

@login.route("/")
def index():
    bd = g.get("bd")
    usuario = UserLogin("b30050", "megahack")
    bd.agregar_usuario(usuario.usuario, usuario.passw)
    print(usuario.to_dict())

    return render_template("index.html")

@login.route("/validar-login", methods = ["GET", "POST"])
def validar_login():
    bd = g.get("bd")

    if request.method == "POST":
        usuario = request.form["usuario"]
        passw = request.form["pass"]
        log = UserLogin(usuario, passw)

        usuario = bd.obtener_usuario(log.usuario, log.passw)
        # print(usuario[0][1])

        if usuario:
            print("Existe")
            flash("Login exitoso!", "success")
        else:
            print("Usuario o contraseña incorrectos.")
            flash("Usuario o contraseña incorrectos.", "error")

    return redirect("/")


