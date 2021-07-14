import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)
COUNTRY_FLAGS = {
    "south east asia": ('https://upload.wikimedia.org/'
                        'wikipedia/en/thumb/8/87/'
                        'Flag_of_ASEAN.svg/'
                        '510px-Flag_of_ASEAN.svg.png'),
    "thailand": ('https://upload.wikimedia.org/'
                 'wikipedia/commons/thumb/a/a9/'
                 'Flag_of_Thailand.svg/510px-'
                 'Flag_of_Thailand.svg.png'),
    "cambodia": ('https://upload.wikimedia.org/'
                 'wikipedia/commons/thumb/8/83/'
                 'Flag_of_Cambodia.svg/510px-'
                 'Flag_of_Cambodia.svg.png'),
    "vietnam": ('https://upload.wikimedia.org/'
                'wikipedia/commons/thumb/2/21/'
                'Flag_of_Vietnam.svg/500px-'
                'Flag_of_Vietnam.svg.png'),
    "laos": ('https://upload.wikimedia.org/'
             'wikipedia/commons/thumb/5/56/'
             'Flag_of_Laos.svg/510px-'
             'Flag_of_Laos.svg.png'),
    "indonesia": ('https://upload.wikimedia.org/'
                  'wikipedia/commons/thumb/9/9f/'
                  'Flag_of_Indonesia.svg/510px-'
                  'Flag_of_Indonesia.svg.png'),
    "malaysia": ('https://upload.wikimedia.org/'
                 'wikipedia/commons/thumb/6/66/'
                 'Flag_of_Malaysia.svg/510px-'
                 'Flag_of_Malaysia.svg.png'),
    "philippines": ('https://upload.wikimedia.org/'
                    'wikipedia/commons/thumb/9/99/'
                    'Flag_of_the_Philippines.svg/510px-'
                    'Flag_of_the_Philippines.svg.png'),
    "singapore": ('https://upload.wikimedia.org/'
                  'wikipedia/commons/thumb/4/48/'
                  'Flag_of_Singapore.svg/510px-'
                  'Flag_of_Singapore.svg.png'),
    "myanmar": ('https://upload.wikimedia.org/'
                'wikipedia/commons/thumb/8/8c/'
                'Flag_of_Myanmar.svg/510px-'
                'Flag_of_Myanmar.svg.png'),
    "east timor": ('https://upload.wikimedia.org/'
                   'wikipedia/commons/thumb/2/26/'
                   'Flag_of_East_Timor.svg/510px-'
                   'Flag_of_East_Timor.svg.png'),
    "brunei": ('https://upload.wikimedia.org/'
               'wikipedia/commons/thumb/9/9c/'
               'Flag_of_Brunei.svg/510px-'
               'Flag_of_Brunei.svg.png')
}


@app.route("/")
@app.route("/home")
def get_home():
    # find recipes by Latest created date limit to 4
    recipes = mongo.db.recipes.find().sort("created_date", -1).limit(4)
    # find countries flag for Carousel on Home page
    flags = COUNTRY_FLAGS.values()
    return render_template("index.html", recipes=recipes, flags=flags)


@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        # check if username exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists!")
            return redirect(url_for("sign_up"))

        sign_up = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(sign_up)

        # New user into session cookie
        session["user"] = request.form.get("username").lower()
        flash("Sign Up Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("signup.html")


@app.route("/sign_in", methods=["GET", "POST"])
def sign_in():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("sign_in"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("sign_in"))

    return render_template("signin.html")


# Return recipe & flags by country
@app.route("/recipes")
def recipes():
    """Show recipes for each country of origin"""
    country = request.args.get("country")
    query = request.args.get("query")
    country = country if country else "south east asia"
    country = country.lower()
    if country in COUNTRY_FLAGS:
        flags = COUNTRY_FLAGS[country]
    else:
        flags = COUNTRY_FLAGS["south east asia"]

    if query:
        if (query.lower() in COUNTRY_FLAGS) and COUNTRY_FLAGS[query.lower()]:
            flags = COUNTRY_FLAGS[query.lower()]
        recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    else:
        recipes = list(mongo.db.recipes.find({"$text": {"$search": country}}))

    return render_template(
        "recipes.html", recipes=recipes, country=country, flags=flags)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    flags = mongo.db.countries.find_one({"$text": {"$search": query}})
    return render_template(
        "recipes.html", recipes=recipes, flags=flags)


# find one recipe to show return recipe description
@app.route("/recipe_description/<recipe_id>")
def recipe_description(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("recipe.html", recipe=recipe)


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab session username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        if session["user"] == "admin":
            profile_recipes = list(mongo.db.recipes.find())
        else:
            profile_recipes = list(
                mongo.db.recipes.find({"created_by": session["user"]}))
        return render_template(
            "profile.html", username=username, profile_recipes=profile_recipes)
    return redirect(url_for("sign_in"))


@app.route("/signout")
def sign_out():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("sign_in"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        recipe = {
            "country": request.form.get("country"),
            "recipe_name": request.form.get("recipe_name"),
            "description": request.form.get("description"),
            "serves": request.form.get("serves"),
            "image_url": request.form.get("image_url"),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "ingredients": request.form.get("ingredients"),
            "method": request.form.get("method"),
            "created_date": request.form.get("created_date"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added!")
        return redirect(url_for('profile', username=session['user']))

    countries = mongo.db.countries.find().sort("country", 1)
    return render_template("add_recipe.html", countries=countries)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        edit_recipe = {
            "country": request.form.get("country"),
            "recipe_name": request.form.get("recipe_name"),
            "description": request.form.get("description"),
            "serves": request.form.get("serves"),
            "image_url": request.form.get("image_url"),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "ingredients": request.form.get("ingredients"),
            "method": request.form.get("method"),
            "created_date": request.form.get("created_date"),
            "created_by": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, edit_recipe)
        flash("Recipe Successfully Updated!")
        return redirect(url_for('profile', username=session['user']))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    countries = mongo.db.countries.find().sort("country", 1)
    return render_template(
        "edit_recipe.html", recipe=recipe, countries=countries)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for('profile', username=session['user']))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
