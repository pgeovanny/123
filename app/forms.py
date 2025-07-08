from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, FileField
from wtforms.validators import DataRequired, Length, Email

class LoginForm(FlaskForm):
    cpf = StringField('CPF', validators=[DataRequired(), Length(min=11, max=14)])
    password = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Entrar')

class SignupForm(FlaskForm):
    name = StringField('Nome', validators=[DataRequired()])
    cpf = StringField('CPF', validators=[DataRequired(), Length(min=11, max=14)])
    birth_date = StringField('Data de Nascimento', validators=[DataRequired()])
    state = StringField('Estado', validators=[DataRequired()])
    study_area = StringField('Área de Estudo', validators=[DataRequired()])
    preparatory = StringField('Preparatório', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField('Cadastrar')

class CSVUploadForm(FlaskForm):
    file = FileField('Arquivo CSV', validators=[DataRequired()])
    submit = SubmitField('Importar CSV')

class AIPromptForm(FlaskForm):
    prompt = TextAreaField('Prompt IA', validators=[DataRequired()])
    submit = SubmitField('Gerar Preview')
