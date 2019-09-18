from flask import render_template, flash, redirect, url_for, send_file, jsonify, make_response, request
from app import app, db
from app.models import Sand
from app.support import get_js_version_hash

import os, time, json

def sandbox_index(sandbox=False): # for use with every rendering of sand.html
    if not sandbox:
        sandbox = Sand.query.all()
    index = {}
    for sand in sandbox:
        index[sand.id] = True
    return index

@app.route('/')
@app.route('/index')
def index():
    sandbox = Sand.query.all()
    print(sandbox_index,flush=True)
    return render_template(
        'index.html',
        sandbox=sandbox,
        sandbox_index=sandbox_index(sandbox=sandbox),
        js_version=get_js_version_hash()
        )
    
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
        return render_template('sand.html',sand=new_sand,sandbox_index=sandbox_index())
    else:
        pass
        
@app.route('/create-reply', methods=['POST'])
def create_reply():
    if request.method == 'POST' and request.is_json:
        sand_data = request.get_json()
        new_sand = Sand(
            title = sand_data['title'],
            message = sand_data['message']
        )
        new_sand.og_sand = sand_data['og_sand']
        db.session.add(new_sand)
        db.session.commit()
        return render_template('sand.html',sand=new_sand,sandbox_index=sandbox_index())
    else:
        pass