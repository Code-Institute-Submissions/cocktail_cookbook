import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import json

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'cocktail_cookbook'
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
mongo = PyMongo(app)


@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    rs=mongo.db.recipes.find()
    i=0
    for r in rs:
        i+=1
    return render_template(
        'recipes.html',
        recipes=mongo.db.recipes.find().sort('name',1),
        bases=mongo.db.bases.find(),
        strengths=mongo.db.strengths.find(),
        difficulty=mongo.db.difficulty.find(),
        occasions=mongo.db.occasions.find(),
        i=i)

@app.route('/add_recipe')
def add_recipe():
    if 'user' in session:
        return render_template(
            'addrecipe.html',
            strengths = mongo.db.strengths.find(),
            occasions = mongo.db.occasions.find(),
            bases = mongo.db.bases.find(),
            difficulty = mongo.db.difficulty.find())
    else:
        return redirect(url_for('get_recipes'))

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipe = request.form.to_dict()
    del recipe['occasions-select']
    del recipe['action']
    recipe['occasions'] = recipe['occasions'].split(',')
    recipes.insert_one(recipe)
    return redirect(url_for('get_recipes'))

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id":ObjectId(recipe_id)})
    if 'user' in session:
        if session['user'] == the_recipe['author']:
            return render_template(
                'editrecipe.html',
                recipe = the_recipe,
                strengths = mongo.db.strengths.find(),
                occasions = mongo.db.occasions.find(),
                bases = mongo.db.bases.find(),
                difficulty = mongo.db.difficulty.find())
        else:
            return redirect(url_for('view_recipe',recipe_id=recipe_id))
    else:
        return redirect(url_for('view_recipe',recipe_id=recipe_id))

@app.route('/view_recipe/<recipe_id>')
def view_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id":ObjectId(recipe_id)})
    return render_template('viewrecipe.html',recipe=the_recipe)

@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    the_recipe = mongo.db.recipes.find_one({"_id":ObjectId(recipe_id)})
    author = the_recipe['author']
    recipes.update({'_id': ObjectId(recipe_id)},
    {
        'name':request.form.get('name'),
        'desc':request.form.get('desc'),
        'difficulty': request.form.get('difficulty'),
        'strength': request.form.get('strength'),
        'recipe': request.form.get('recipe'),
        'ingredients': request.form.get('ingredients'),
        'occasions': request.form.get('occasions').split(','),
        'base':request.form.get('base'),
        'author':author
    })
    return redirect(url_for('get_recipes'))

@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id":ObjectId(recipe_id)})
    if 'user' in session:
        if session['user'] == the_recipe['author']:
            mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
            return redirect(url_for('get_recipes'))
        else:
            return redirect(url_for('view_recipe',recipe_id=recipe_id))
    else:
        return redirect(url_for('view_recipe',recipe_id=recipe_id))

@app.route('/filter_recipes',methods=['POST'])
def filter_recipes():
    d = request.form.to_dict()
    s = d['sort']
    s = s.split(',')
    d.pop('sort')
    if d != {}:
        if d['base'] == '':
            del d['base']
        if d['difficulty'] == '':
            del d['difficulty']
        if d['strength'] == '':
            del d['strength']
        if d['occasions'] == '':
            del d['occasions']
    return render_template(
        'filtersortrecipes.html',
        recipes = mongo.db.recipes.find(d).sort(s[0],int(s[1])),
        bases = mongo.db.bases.find(),
        strengths = mongo.db.strengths.find(),
        difficulty = mongo.db.difficulty.find(),
        occasions = mongo.db.occasions.find())

@app.route('/login', methods=['POST', 'GET'])
def login():
    if 'user' in session:
        return redirect(url_for('get_recipes'))
    if request.method == 'POST':
        users = mongo.db.users
        login_user = users.find_one({'user' : request.form['user']})
        if login_user:
            if login_user['password'] == request.form['password']:
                session['user'] = request.form['user']
                return redirect(url_for('get_recipes'))
        return render_template('failedlogin.html')
    return render_template('login.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'user' : request.form['user']})
        if existing_user is None:
            users.insert({'user': request.form['user'], 'password' : request.form['password']})
            session['user'] = request.form['user']
            return redirect(url_for('get_recipes'))
        return render_template('failedregister.html')
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('get_recipes'))

if __name__ == '__main__':
    app.secret_key = os.getenv('secret_key','SECRET')
    app.run(host=os.environ.get('IP','0.0.0.0'),
            port=int(os.environ.get('PORT','8080')),
            debug=False)

