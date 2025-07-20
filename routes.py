# app/routes.py
from flask import Blueprint, render_template, request, redirect, url_for
import pandas as pd
import os

main = Blueprint('main', __name__)
DATA_FILE = os.path.join(os.path.dirname(__file__), '../data/students.csv')

@main.route('/')
def index():
    if os.path.exists(DATA_FILE):
        df = pd.read_csv(DATA_FILE)
        students = df.to_dict(orient='records')
    else:
        students = []
    return render_template('index.html', students=students)

@main.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        new_student = {
            'ID': request.form['id'],
            'Name': request.form['name'],
            'Age': request.form['age'],
            'Grade': request.form['grade']
        }
        if os.path.exists(DATA_FILE):
            df = pd.read_csv(DATA_FILE)
            df = df.append(new_student, ignore_index=True)
        else:
            df = pd.DataFrame([new_student])
        df.to_csv(DATA_FILE, index=False)
        return redirect(url_for('main.index'))
    return render_template('create.html')

@main.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    df = pd.read_csv(DATA_FILE)
    student = df[df['ID'] == id].to_dict(orient='records')[0]
    if request.method == 'POST':
        df.loc[df['ID'] == id, ['Name', 'Age', 'Grade']] = [request.form['name'], request.form['age'], request.form['grade']]
        df.to_csv(DATA_FILE, index=False)
        return redirect(url_for('main.index'))
    return render_template('edit.html', student=student)

@main.route('/delete/<id>')
def delete(id):
    df = pd.read_csv(DATA_FILE)
    df = df[df['ID'] != id]
    df.to_csv(DATA_FILE, index=False)
    return redirect(url_for('main.index'))

@main.route('/view/<id>')
def view(id):
    df = pd.read_csv(DATA_FILE)
    student = df[df['ID'] == id].to_dict(orient='records')[0]
    return render_template('view.html', student=student)