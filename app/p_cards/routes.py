from flask import Blueprint, render_template, request, url_for, redirect
from flask_login import current_user
from .forms import ChoosePokemonForm, KeepPokemonForm
from app.models import Pokemon 
from .pokeFunc import getPokemon
from datetime import datetime

p_cards = Blueprint('p_card', __name__, template_folder='p_card_templates')

@p_cards.route('/pokemon/choose', methods=["GET", "POST"])
def choosePokemon():
    form = ChoosePokemonForm()
    if request.method == "POST":
        if form.validate():
            chosen_pokemon = form.chosen_pokemon.data
            pokemon_dict = getPokemon(chosen_pokemon)
            name = pokemon_dict['name']
            ability = pokemon_dict['ability']
            base_experience = pokemon_dict['base_experience']
            official_artwork = pokemon_dict['official_artwork']
            hp = pokemon_dict['hp']
            attack = pokemon_dict['attack']
            defense = pokemon_dict['defense']
            special_attack = pokemon_dict['special_attack']
            special_defense = pokemon_dict['special_defense']
            speed = pokemon_dict['speed']
            
            return render_template('pokecard.html', form=form, name=name, ability=ability, base_experience=base_experience, official_artwork=official_artwork, hp=hp, attack=attack, defense=defense, special_attack=special_attack, special_defense=special_defense, speed=speed)
    print('before try')
    try:
        print('return1')
        return render_template('choose.html', form=form, name=name, ability=ability, base_experience=base_experience, official_artwork=official_artwork, hp=hp, attack=attack, defense=defense, special_attack=special_attack, special_defense=special_defense, speed=speed)
    except:
        print('return2')
        return render_template('choose.html', form=form)

@p_cards.route('/pokecard', methods=["GET", "POST"])
def pokecard():
    form = KeepPokemonForm()
    print(request.method)
    if request.method == "POST":
        print(form.validate(), form.errors)
        if form.validate():
            print('valid')
            user_id=current_user.id
            name = form.name.data
            date_created=datetime.utcnow()
            pokemon = Pokemon(user_id, name, date_created)
            pokemon.saveToDB()
    return render_template('pokecard.html')
