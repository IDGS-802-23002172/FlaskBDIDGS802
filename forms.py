from wtforms import Form
from wtforms import StringField, IntegerField, PasswordField
from wtforms import EmailField
from wtforms import validators

class UserForm2(Form):
    id = IntegerField('id')
    nombre = StringField('Nombre',[
        validators.DataRequired(message="Este campo es requerido"),
        validators.length(min=3, max=10, message="Longitud de 3 a 10 caracteres")
    ])
    apellidos = StringField('Apellidos',[
        validators.DataRequired(message="Este campo es requerido")
    ])
    correo = EmailField('Correo',[
        validators.DataRequired(message="Este campo es requerido")
    ])
    telefono = StringField('Telefono',[
        validators.DataRequired(message="Este campo es requerido")
    ])