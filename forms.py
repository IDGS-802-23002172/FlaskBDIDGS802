from wtforms import Form
from wtforms import StringField, IntegerField, PasswordField, SelectField, SubmitField
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
    
    
class MaestrosForm(Form):
    matricula = IntegerField('id')
    nombre = StringField('Nombre',[
        validators.DataRequired(message="Este campo es requerido")
    ])
    apellidos = StringField('Apellidos',[
        validators.DataRequired(message="Este campo es requerido")
    ])
    especialidad = StringField('Especialidad',[
        validators.DataRequired(message="Este campo es requerido")
    ])
    correo = EmailField('Correo',[
        validators.DataRequired(message="Este campo es requerido")
    ])
    
    
class CursosForm(Form):
    id = IntegerField('id')
    nombre = StringField('Nombre',[
        validators.DataRequired(message="Este campo es requerido")
    ])
    descripcion = StringField('Descripcion',[
        validators.DataRequired(message="Este campo es requerido")
    ])
    maestro_id = SelectField('Maestro Titular', coerce=int)
    
    
class AsignarCursoForm(Form):
    tipo = SelectField('Asignar como:', choices=[('maestro', 'Maestro'), ('alumno', 'Alumno')])
    maestro_id = SelectField('Seleccionar Maestro', coerce=int)
    alumno_id = SelectField('Seleccionar Alumno', coerce=int)
    submit = SubmitField('Guardar cambios')