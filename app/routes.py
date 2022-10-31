from flask import render_template, request, redirect, url_for
from app import app

from app.models import User
from .p_cards.pokeFunc import getPokemon

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/future')
def future():
    return render_template('future.html')

@app.route('/hide_em_all')
def hide_em_all():
    return render_template('hide_em_all.html')