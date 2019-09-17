from flask import render_template, flash, redirect, url_for, send_file, jsonify, make_response, request
from app import app, db
from app.models import Sand

import os, time, json

@app.route('/')
@app.route('/index')
def index():
    sandbox = Sand.query.all()
    return render_template('index.html',sandbox=sandbox)
    
@app.route('/create-entry', methods=['POST'])
def create_entry():
    if request.method == 'POST' and request.is_json:
        sand_data = request.get_json()
        new_sand = Sand(
            title = sand_data['title'],
            message = sand_data['message'],
            #sand_id = sand_data['sand_id']
        )
        db.session.add(new_sand)
        db.session.commit()
        return render_template('sand.html', sand=new_sand)
    else:
        pass