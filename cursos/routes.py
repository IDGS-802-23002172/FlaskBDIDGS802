from flask import render_template, request, redirect, url_for, flash, Blueprint
import forms
from models import db, Cursos, Maestros, Alumnos

cursos_bp = Blueprint('cursos', __name__)

@cursos_bp.route("/cursos")
def dashboardCursos():
    cursos = Cursos.query.all()
    return render_template("dashboardCursos.html", cursos=cursos)

@cursos_bp.route("/agregarCurso", methods=['GET', 'POST'])
def agregarCurso():
    form = forms.CursosForm(request.form)
    form.maestro_id.choices = [(m.matricula, f"{m.nombre} {m.apellidos}") for m in Maestros.query.all()]
    if request.method == 'POST':
        nuevo_curso = Cursos(
            nombre=form.nombre.data,
            descripcion=form.descripcion.data,
            maestro_id=form.maestro_id.data
        )
        db.session.add(nuevo_curso)
        db.session.commit()
        return redirect(url_for('cursos.dashboardCursos'))
    return render_template("Cursos.html", form=form)

@cursos_bp.route("/modificarCurso/<int:id>", methods=['GET', 'POST'])
def modificarCurso(id):
    curso = Cursos.query.get_or_404(id)
    form = forms.CursosForm(request.form)
    form.maestro_id.choices = [(m.matricula, f"{m.nombre} {m.apellidos}") for m in Maestros.query.all()]
    
    if request.method == 'GET':
        form.id.data = curso.id
        form.nombre.data = curso.nombre
        form.descripcion.data = curso.descripcion
        form.maestro_id.data = curso.maestro_id
        
    if request.method == 'POST':
        curso.nombre = form.nombre.data
        curso.descripcion = form.descripcion.data
        curso.maestro_id = form.maestro_id.data
        db.session.commit()
        return redirect(url_for('cursos.dashboardCursos'))
        
    return render_template("modificarCurso.html", form=form, curso=curso)

@cursos_bp.route("/eliminarCurso/<int:id>", methods=['GET', 'POST'])
def eliminarCurso(id):
    curso = Cursos.query.get_or_404(id)
    if request.method == 'POST':
        db.session.delete(curso)
        db.session.commit()
        return redirect(url_for('cursos.dashboardCursos'))
    return render_template("eliminarCurso.html", curso=curso)

@cursos_bp.route("/detallesCurso/<int:id>")
def detallesCurso(id):
    curso = Cursos.query.get_or_404(id)
    return render_template("detallesCurso.html", curso=curso)

@cursos_bp.route("/asignar/<int:id_curso>", methods=['GET', 'POST'])
def asignar(id_curso):
    curso = Cursos.query.get_or_404(id_curso)
    form = forms.AsignarCursoForm(request.form)
    form.maestro_id.choices = [(m.matricula, f"{m.nombre} {m.apellidos}") for m in Maestros.query.all()]
    form.alumno_id.choices = [(a.id, f"{a.nombre} {a.apellidos}") for a in Alumnos.query.all()]

    if request.method == 'POST':
        if form.tipo.data == 'maestro':
            curso.maestro_id = form.maestro_id.data
        else:
            alumno = Alumnos.query.get(form.alumno_id.data)
            if alumno and alumno not in curso.alumnos:
                curso.alumnos.append(alumno)
        db.session.commit()
        return redirect(url_for('cursos.dashboardCursos'))

    return render_template("asignarCurso.html", form=form, curso=curso)