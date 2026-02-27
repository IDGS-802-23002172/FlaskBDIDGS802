from flask import Flask, render_template, request, redirect, url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from flask import g
import forms

from models import db
from models import Maestros

from flask import Blueprint
maestros_bp=Blueprint('maestros',__name__)

## @maestros_bp.route('/maestros')
##  def maestros():
    ## return "Maestros"

@maestros_bp.route("/maestros")
def dashboardMaestro():
    create_form=forms.MaestrosForm(request.form)
    #tem = Maestros.query('select * from Maestros')
    maestro=Maestros.query.all()
    return render_template("dashboardMaestro.html", form=create_form, maestro=maestro)


@maestros_bp.route("/agregarMaestro", methods=['GET','POST'])
def agregarMaestro():
    create_form=forms.MaestrosForm(request.form)
    if request.method == 'POST':
        mae = Maestros(nombre=create_form.nombre.data,
                apellidos=create_form.apellidos.data,
                especialidad=create_form.especialidad.data,
                correo=create_form.correo.data)
        db.session.add(mae)
        db.session.commit()
        return redirect(url_for('maestros.dashboardMaestro'))
    return render_template("Maestros.html",form=create_form)

@maestros_bp.route("/detallesMaestro",methods=['GET','POST'])
def detallesMaestro():
    create_form=forms.MaestrosForm(request.form)
    if request.method == 'GET':
        matricula = request.args.get('matricula')
        mae1=db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
        matricula=request.args.get('matricula')
        nombre=mae1.nombre
        apellidos=mae1.apellidos
        especialidad=mae1.especialidad
        correo=mae1.correo
    return render_template("detallesMaestro.html",form=create_form,matricula=matricula,nombre=nombre,apellidos=apellidos,correo=correo, especialidad=especialidad)

@maestros_bp.route("/modificarMaestro",methods=['GET','POST'])
def modificarMaestro():
    create_form=forms.MaestrosForm(request.form)
    if request.method == 'GET':
        matricula = request.args.get('matricula')
        mae1=db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
        create_form.matricula.data=request.args.get('matricula')
        create_form.nombre.data=mae1.nombre
        create_form.apellidos.data=mae1.apellidos
        create_form.especialidad.data=mae1.especialidad
        create_form.correo.data=mae1.correo
    if request.method == 'POST':
        matricula = create_form.matricula.data
        mae1=db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
        mae1.matricula=matricula
        mae1.nombre=str.rstrip(create_form.nombre.data)
        mae1.apellidos=create_form.apellidos.data
        mae1.especialidad=create_form.especialidad.data
        mae1.correo=create_form.correo.data
        db.session.add(mae1)
        db.session.commit()
        return redirect(url_for('maestros.dashboardMaestro'))
    return render_template("modificarMaestro.html",form=create_form)



@maestros_bp.route("/eliminarMaestro",methods=['GET','POST'])
def eliminarMaestro():
    create_form=forms.MaestrosForm(request.form)
    if request.method == 'GET':
        matricula = request.args.get('matricula')
        mae1=db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
        create_form.matricula.data=request.args.get('matricula')
        create_form.nombre.data=mae1.nombre
        create_form.apellidos.data=mae1.apellidos
        create_form.especialidad.data=mae1.especialidad
        create_form.correo.data=mae1.correo
    if request.method == 'POST':
        matricula = create_form.matricula.data
        mae1=Maestros.query.get(matricula)
        db.session.delete(mae1)
        db.session.commit()
        return redirect(url_for('maestros.dashboardMaestro'))
    return render_template("eliminarMaestro.html",form=create_form)


