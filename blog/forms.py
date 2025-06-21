from wtforms import Form, StringField, TextAreaField, SelectField
from wtforms.fields.simple import FileField, SubmitField
from wtforms import validators, PasswordField



class UserLogin(Form):
    '''Форма авторизации'''
    username = StringField('Логин')
    password = PasswordField('Пароль')
    submit = SubmitField('Login')


class Registration(Form):
    '''Форма регистрации'''
    username = StringField('логин *', validators=[validators.DataRequired()])
    password = PasswordField('Пароль *', validators=[validators.Length(min=1, max=15)])
    submit = SubmitField('Registration')


class ContactForm(Form):
    '''Форма обратной связи'''
    first_name = StringField('Имя')
    last_name = StringField('Фамилия')
    email = StringField('Почта')
    subject = StringField('Тема')
    message = TextAreaField('Сообщение')
    submit = SubmitField('Send')