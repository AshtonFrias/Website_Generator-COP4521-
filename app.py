from flask import Flask, render_template, request
import sqlite3 as sql
import requests
from bs4 import BeautifulSoup
from recipe_scrapers import scrape_me
import cchardet
from email.message import EmailMessage
import smtplib

app = Flask(__name__)

@app.route('/')
def mainpage():
    return render_template('mainpage.html')

@app.route('/recipe_home') #HOME PAGE, user can enter their criteria here for recipes
def recipe_home():
    return render_template('home.html')
    con.close()

@app.route('/see_saved') #Save recipes
def see_saved():
    with sql.connect("recipeData.db") as con:  # clears previous data from the table
        cur = con.cursor()
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute(f"select * from saved_recipes")
        revRows = cur.fetchall();
        return render_template("savedrecipes.html", revRows=revRows)

@app.route('/save_recipe/<id>') #Save recipes
def save_recipe(id):
    print(id)
    with sql.connect("recipeData.db") as con:  # clears previous data from the table
        cur = con.cursor()
        cur.execute("INSERT INTO saved_recipes SELECT * FROM recipes WHERE RecipeName=?", (id,))

        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute(f"select * from saved_recipes")
        revRows = cur.fetchall();
        return render_template("savedrecipes.html", revRows=revRows)

@app.route('/delete_recipe/<id>') #Save recipes
def delete_recipe(id):
    with sql.connect("recipeData.db") as con:  # clears previous data from the table
        cur = con.cursor()
        cur.execute("DELETE FROM saved_recipes WHERE RecipeName=?", (id,))

        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute(f"select * from saved_recipes")
        revRows = cur.fetchall();
        return render_template("savedrecipes.html", revRows=revRows)

@app.route('/get_recipes', methods=['POST', 'GET'])  #GET RECIPES, scrapes for recipes fitting the criteria and puts them in a database
def get_recipes():
    if request.method == 'POST':

        with sql.connect("recipeData.db") as con:   #clears previous data from the table
            cur = con.cursor()
            cur.execute("DELETE FROM recipes")

        try:
            tag = request.form['recipe_tag']    #gets the tags the user chose
        except:
            tag = "Italian" #defaults to Italian if nothing was entered

        try:
            url = 'https://www.allrecipes.com/search/results/?search='+tag  #constructing the search URL, adding the user's desired criteria
            reqs = requests.get(url)
            soup = BeautifulSoup(reqs.text, 'lxml')

            links = [link['href'] for link in soup.select('a[href*="https://www.allrecipes.com/recipe/"]')] #putting the links to recipes into a list
            unique_links=set(links) #storing the list in a set so there are only unique links

            with sql.connect("recipeData.db") as con:
                cur = con.cursor()
                i=0
                for link in unique_links:
                    if(i==10):  #cutting off results at 10 to try to cut down loading time
                        break

                    scraper = scrape_me(link)
                    ingredients=(str)(scraper.ingredients())    #turning the ingredients list into a string so it can be inserted

                    x=(int)(scraper.total_time())   #converting minutes to h:m format
                    hours=x//60
                    min=x%60
                    if(hours==0 and min==0):    #if no data on the recipe time is available, N/A is saved to the database
                        time="N/A"
                    elif(hours==0):
                        time=str(min)+" mins"
                    elif(min==0):
                        time=str(hours)+" hrs"
                    else:
                        time=str(hours)+" hrs "+str(min)+" mins"

                    image=scraper.image()

                    cur.execute("INSERT INTO recipes (Image, RecipeName, Time, Yields, Ingredients, Instructions, URL) VALUES (?,?,?,"  #inserting data into table
                            "?,?,?,?)", (image,scraper.title(), time, scraper.yields(), ingredients, scraper.instructions(), link))
                    i=i+1

        except:
            con.rollback()
            print("Error in insert operation")

        finally:
            conn = sql.connect("recipeData.db")
            conn.row_factory = sql.Row
            cur = conn.cursor()
            cur.execute(f"select * from recipes")
            revRows = cur.fetchall();
            return render_template("recipes.html", revRows=revRows)

@app.route('/restaurant_home')
def findrestaurant():
    return render_template('findrestaurant.html')

def removeSpaces(restName):
    restName = restName[2:]
    while(restName[1:] == " "):
        restName = restName[1:]

    restName = restName.replace(" ", "-")
    restName = restName.replace("'", "s")
    restName = restName.replace("&", "and")

    return restName

@app.route('/get_restaurant', methods=['POST', 'GET'])
def get_restaurant():
    if request.method == 'POST':
        with sql.connect("recipeData.db") as con:   #clears previous data from the table
            cur = con.cursor()
            cur.execute("DELETE FROM restaurant")

            city = request.form['city']
            state = request.form['state']
            tag = request.form['restaurant_tag']
            city = city.replace(" ", "%20")
            tag = tag.replace(" ", "%20")

        try:
            url = "https://www.yelp.com/search?find_desc=Restaurants&find_loc="+city+"%2C%20" + state+"&ns=1&cflt="+tag
            reqs = requests.get(url)
            soup = BeautifulSoup(reqs.content, 'lxml')

            for item in soup.select('[class*=container]'):
                if item.find('h4'):
                    name = item.find('h4').get_text()
                    name = name[3:]
                    rating = soup.select('[aria-label*=rating]')[0]['aria-label']
                    price = soup.select('[class*=priceRange]')[0].get_text()

                    with sql.connect("recipeData.db") as con:
                        cur = con.cursor()
                        #cur.execute('CREATE TABLE resturant (RestName TEXT, URL TEXT, Rating TEXT, Price TEXT, Tag TEXT)')
                        cur.execute("INSERT INTO restaurant (RestName, Rating, Price, Tag) VALUES (?,?,?,?)", (name, rating, price, tag))

        except:
            con.rollback()
            print("Error in insert operation")

        finally:
            conn = sql.connect("recipeData.db")
            conn.row_factory = sql.Row
            cur = conn.cursor()
            cur.execute(f"select * from restaurant")
            revRows = cur.fetchall();
            return render_template("restaurant.html", revRows=revRows, city = city, state = state)

@app.route('/sendrecipe')
def sendrecipe():
    return render_template('recipeemail.html') 

@app.route('/sendrestaurant')
def sendrestaurant():
    return render_template('restaurantemail.html') 

@app.route('/recipeemail',methods = ['POST', 'GET'])
def recipeemail():
    if request.method == 'POST':
        conn = sql.connect("recipeData.db")
        cur = conn.cursor()
        cur.execute(f"select * from recipes")
        #revRows = cur.fetchall();
        revRows = "This is a test"

        print(revRows)
        email = request.form['Email']
        EMIAL_ADDRESS = "FoodWebsiteGenerator@gmail.com"
        EMIAL_PASSWORD = "cop452100"

        msg = EmailMessage()
        msg['From'] = EMIAL_ADDRESS
        msg['Subject'] = "Your Recipe"
        msg['To'] = email
        msg.set_content(revRows)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp: 
            smtp.login(EMIAL_ADDRESS,EMIAL_PASSWORD)
            smtp.send_message(msg)

        return render_template("result.html",msg = "Email was sent")

@app.route('/restaurantemail',methods = ['POST', 'GET'])
def restaurantemail():
    if request.method == 'POST':
        conn = sql.connect("recipeData.db")
        cur = conn.cursor()
        cur.execute(f"select * from restaurant")
        revRows = cur.fetchall();

        revRows = "This is a test"
 
        email = request.form['Email']
        EMIAL_ADDRESS = "FoodWebsiteGenerator@gmail.com"
        EMIAL_PASSWORD = "cop452100"

        msg = EmailMessage()
        msg['From'] = EMIAL_ADDRESS
        msg['Subject'] = "Your Recipe"
        msg['To'] = email
        msg.set_content(revRows)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp: 
            smtp.login(EMIAL_ADDRESS,EMIAL_PASSWORD)
            smtp.send_message(msg)

        return render_template("result.html",msg = "Email was sent")

if __name__ == '__main__':
    app.run(host='0.0.0.0');