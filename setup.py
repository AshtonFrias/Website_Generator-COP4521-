import sqlite3

#CREATES THE DATABASE (1 table called "recipes")
conn = sqlite3.connect('recipeData.db')
conn.execute('CREATE TABLE saved_recipes (Image TEXT, RecipeName TEXT, Time TEXT, Yields TEXT, Ingredients TEXT, Instructions TEXT, URL TEXT)')
conn.execute('CREATE TABLE recipes (Image TEXT, RecipeName TEXT, Time TEXT, Yields TEXT, Ingredients TEXT, Instructions TEXT, URL TEXT)')
conn.execute('CREATE TABLE restaurant (RestName TEXT, Rating TEXT, Price TEXT, Tag TEXT)')
print ("Opened database successfully") 
print("Tables made successfully")

conn.close()