#links do site
from flask import render_template
from fakepinterest import app
from flask_login import login_required
from fakepinterest.forms import FormLogin, FormCriarConta






@app.route("/", methods = ["GET", "POST"])
def homepage():
   
    return  render_template("homepage.html")


@app.route("/criatconta", methods = ["GET", "POST"])
def criarconta():
   
    return render_template("criarconta.html")



@app.route("/perfil/<usuario>")
@login_required
def perfil(usuario):
    return render_template("perfil.html", usuario = usuario)

