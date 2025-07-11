import os.path as op
import uuid as uuid
from werkzeug.utils import secure_filename

from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask_admin.form import FileUploadField # для поля работы с файлом загрузкой файла
from flask import redirect, url_for



def prefix_name(obj, file_data):
    '''Функция генерация имени файла'''
    parts = op.splitext(file_data.filename)
    return secure_filename(f'{uuid.uuid1()}_%s%s' % parts)


class AdminAccess(AdminIndexView):
    '''Проверка на админа'''
    def is_accessible(self):
        '''Если есть доступ'''
        if not current_user.is_anonymous: # Если текущий пользователь не аноним
            return current_user.is_staff  # вернуть админ тру

    def inaccessible_callback(self, name, **kwargs):
        '''Если доступа нет'''
        return redirect(url_for('index.main_page')) # перенаправить на главную


class PostAdmin(ModelView):
    '''Посты в админке'''
    form_columns = ['title', 'content', 'category', 'picture']
    form_extra_fields = {
        'picture': FileUploadField('picture',
                                   namegen=prefix_name,
                                   base_path='static/images')     # для поля выбора файла
    }



# admin.add_view(ModelView(Category, db.session)) # Для возможности работы с моделью - редактир создать удалить
#
# admin.add_view(PostAdmin(Post, db.session)) # Измененная модель постов в админке
