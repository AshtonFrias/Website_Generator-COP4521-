import public as public
from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)

@app.route('/') #HOME PAGE
def home():
    return render_template('home.html')
    con.close()


@app.route('/get_recipes', methods=['POST', 'GET'])  #ADD REVIEW
def get_recipes():

    if request.method == 'GET':
        conn = sql.connect("recipeData.db")
        conn.row_factory = sql.Row
        cur = conn.cursor()
        try:
            tag = request.args['recipe_tag']
            cur.execute(f"select * from recipes where Tags='{tag}'")  # only gets the reviews for the Restaurant entered
        except:
            cur.execute(f"select * from recipes")  # only gets the reviews for the Restaurant entered


        revRows = cur.fetchall();

        return render_template("recipes.html", revRows=revRows)


if __name__ == '__main__':
    app.run(host='0.0.0.0');