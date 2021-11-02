from flask import Flask, render_template, request
import sqlite3 as sql
import smtplib
import os
from email.message import EmailMessage

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

@app.route('/sendemail')
def sendemail():
    return render_template('sendemail.html') 

@app.route('/submitemail',methods = ['POST', 'GET'])
def submitemail():
    if request.method == 'POST':
        email = request.form['Email']
        EMIAL_ADDRESS = "FoodWebsiteGenerator@gmail.com"
        EMIAL_PASSWORD = "cop452100"

        msg = EmailMessage()
        msg['From'] = EMIAL_ADDRESS
        msg['Subject'] = "Your Recipe"
        msg['To'] = email
        msg.set_content("This is a test")

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp: 
            smtp.login(EMIAL_ADDRESS,EMIAL_PASSWORD)
            smtp.send_message(msg)

        return render_template("result.html",msg = "Email was sent")

if __name__ == '__main__':
    app.run(host='0.0.0.0')
