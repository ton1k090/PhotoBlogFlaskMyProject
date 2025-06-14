from wtforms import Form, StringField, TextAreaField, SelectField
from wtforms.fields.simple import FileField
from wtforms import validators, PasswordField



class UserLogin(Form):
    '''Форма авторизации'''
    username = StringField('Логин')
    password = PasswordField('Пароль')


class Registration(Form):
    '''Форма регистрации'''
    username = StringField('логин *', validators=[validators.DataRequired()])
    email = StringField('Почта *', validators=[validators.DataRequired()])
    password = PasswordField('Пароль *', validators=[validators.Length(min=1, max=15),
                                                     validators.EqualTo('confirm',
                                                                        message='Пароли должны совпадать')])
    confirm = PasswordField('Подтверждение пароля', validators=[validators.DataRequired()])