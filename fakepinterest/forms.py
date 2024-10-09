#formulários
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from fakepinterest.models import Usuario, Foto




class FormLogin(FlaskForm):
    email = StringField("E-mail", validators= [DataRequired(), Email()])
    senha = PasswordField("Senha", validators= [DataRequired()])
    botao = SubmitField("Fazer login")



class FormCriarConta(FlaskForm):
    email = StringField("Email", validators= [DataRequired(), Email()])
    username = StringField("Nome de usuário", validators= [DataRequired()])
    senha = PasswordField("Senha", validators= [DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField("confirme a senha", validators= [DataRequired(), EqualTo("senha")])
    botao_confirmacao = SubmitField("confirmar")


    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email = email.data).first()
        if usuario:
            return ValidationError("Email já cadastrado, faça login para continuar.")