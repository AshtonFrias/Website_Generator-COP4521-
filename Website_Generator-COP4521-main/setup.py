import sqlite3

#CREATES THE DATABASE (1 table)
conn = sqlite3.connect('recipeData.db')
print ("Opened database successfully")

conn.execute('CREATE TABLE recipes (RecipeName TEXT, URL TEXT, Tags TEXT)')
#conn.execute("INSERT INTO recipes (RecipeName, URL, Tags) VALUES ('1', '2', '3'), ('3','2','1')")
records_to_insert = [('Pork Dumplings', 'https://www.allrecipes.com/recipe/14759/pork-dumplings/', 'Chinese'),
                                 ('Char Siu (Chinese BBQ Pork)', 'https://www.allrecipes.com/recipe/257428/char-siu-chinese-barbeque-pork/', 'Chinese'),
                                 ('Italian Baked Meatballs', 'https://www.allrecipes.com/recipe/268249/italian-baked-meatballs/', 'Italian'),
                                 ('Lasagne Alla Bolognese Saporite', 'https://www.allrecipes.com/recipe/257379/lasagne-alla-bolognese-saporite/',
                                  'Italian'),
                                 ('Easy, Spicy Chicken Ramen Noodle Soup',
                                  'https://www.allrecipes.com/recipe/264486/easy-spicy-chicken-ramen-noodle-soup/',
                                  'Easy'),
                                 ('Easy Baklava',
                                  'https://www.allrecipes.com/recipe/20287/easy-baklava/', 'Easy'),
                                 ('Zucchini Nachos',
                                  'https://www.allrecipes.com/recipe/268088/zucchini-nachos/',
                                  'Low Carb'),
                                 ('Pepperoni Meatza',
                                  'https://www.allrecipes.com/recipe/228652/pepperoni-meatza/', 'Low Carb'),
                                 ('Grilled Lemon Herb Pork Chops',
                                  'https://www.allrecipes.com/recipe/50848/grilled-lemon-herb-pork-chops/',
                                  'Whole30'),
                                 ('Guacamole',
                                  'https://www.allrecipes.com/recipe/14231/guacamole/', 'Whole30')]

conn.executemany("INSERT INTO recipes (RecipeName, URL, Tags) VALUES (?,?,?)", records_to_insert)
conn.commit()
print ("Reviews Table created successfully")

conn.close()