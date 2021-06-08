import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash,check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_home")
def get_home():
    recipes = mongo.db.recipes.find()
    return render_template("index.html", recipes=recipes)


@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    return render_template("signup.html")

# Return recipe by country
@app.route("/get_recipes/<country>")
def get_recipes(country):
    """Show recipes for each country of origin"""
    if country == "all":
        recipes = list(mongo.db.recipes.find())
    elif country == "Thailand":
        recipes = list(mongo.db.recipes.find({"country": "Thailand"}))
    elif country == "Thailand":
        recipes = list(mongo.db.recipes.find({"country": "Thailand"}))
    elif country == "Thailand":
        recipes = list(mongo.db.recipes.find({"country": "Thailand"}))
    elif country == "Thailand":
        recipes = list(mongo.db.recipes.find({"country": "Thailand"}))
    else:
        recipes = list(mongo.db.recipes.find())

    return render_template(
        "recipes.html", recipes=recipes, country=country)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
