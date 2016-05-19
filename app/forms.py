from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, TextAreaField, SelectField, PasswordField
from wtforms.validators import DataRequired, Length


class LoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password=PasswordField('password', validators=[DataRequired()])
    is_professor = BooleanField('is_professor', default=False)
    remember_me = BooleanField('remember_me', default=False)


class RegisterForm(Form):
    name=StringField('name', validators=[DataRequired()])
    surname = StringField('surname', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    password=PasswordField('password', validators=[DataRequired()])
    email=StringField('email',validators=[DataRequired()])


class NewSubjectForm(Form):
    name = StringField('name', validators=[DataRequired()])
    year=SelectField(u'Year of teaching',
                choices=[(1, '1st'),
                         (2, '2nd'),
                         (3, '3rd')],
                coerce=int,
                validators=[DataRequired()])
    semester = SelectField(u'Semester of teaching',
                       choices=[(1, '1st'),
                                (2, '2nd')],
                       coerce=int,
                       validators=[DataRequired()])

class EditForm(Form):
    name = StringField('name', validators=[DataRequired()])
    surname = StringField('surname', validators=[DataRequired()])

    def __init__(self, original_name,original_surname, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.original_name = original_name
        self.original_surname = original_surname

    def validate(self):
        if not Form.validate(self):
            return False
        if self.name.data == self.original_name and self.surname.data==self.original_surname:
            return True
        return True