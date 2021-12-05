# Recipe Website Python (COP 4521 - Fall 2021)
# Final Status Report (12/3)

**Team Members:** Addison Nugent (GitHub ID: sydsyd-nugs), Ashton Frias (GitHub ID: AshtonFrias), Jordan Locke (GitHub ID: jll19gGH), and Colin Houde (GitHub ID: ColinHoude)

**Group Project Name:** Recipe Website Generator

**Repository Link:** https://github.com/AshtonFrias/Website_Generator-COP4521-
*Note: Invites have been sent to both kuhnle@cs.fsu.edu and barao@cs.fsu.edu from the GitHub ID AshtonFrias

**Necessary additional python package (recipe_scrapers) to install on pyhton2.x: 

pip install recipe-scrapers

**or for python3.x:

pip3 install recipe-scrapers

**Description of the problem we are trying to solve:** Our website uses web scrapers to give the user the ability to browse local restaurants as well as find recipes that match their chosen criteria all in one place. The criteria includes cuisine (Chinese, Mexican, etc.), diet (Vegetarian, Keto, etc.), difficulty, meal type (Appetizer, Dinner, etc.), nutrition and so on. For searching for recipes, the user also has the option to input specific ingredients (such as onions, broccoli, chicken, etc.) that they want and don’t want in the results. The user can add/remove recipes to/from another database. They will also have the option to send the list of saved recipes via email, as well as the list of restaurant results via email.

**Changes to the original plan:** Originally, we were going to pull the top 10 or so search results then give the user an option to refresh the page for more. For some reason, Beautiful Soup 4 can only pull a certain number of URLS (it varies how many but usually 20-30 URLS come back) so we are unable to continually refresh the results like we thought we could do. Instead, we will display the top 10 or so results and the user will have the option to do a new search if they want different results. We also were going to allow the user to select multiple tags (aka criteria) but we limited this to only choosing one selection per category to limit complexity. Also, if the user does not put in any criteria, we do not create  a random combination of criteria for them. Other than these changes, and the extra features implemented (see below), we were able to complete everything in our project proposal.

**Extra Features Implemented:** The email feature was not in the original proposal. Ashton Frias added it between Status Report 1 and 2. We also added the feature to specify an ingredient the user does not want in their recipe results. This was added by Jordan Locke between Status Report 2 and the Final Status Report.

**List of Python Libraries being used:** Flask (Use: web development), Requests (Use: helps us get web addresses), Beautiful Soup 4 (Use: helps us scrape the recipe URLS from the search results), Recipe-Scrapers (Use: scrapes information about a recipe from a URL), Smtplib (Use: Allows us to send emails), Email Message (Use: Creates an email container, which makes formatting an email easier), lxml (Use: used as the Beautiful Soup parser to try to reduce loading times), and cchardet (Use: used to try to reduce loading times).

**Other Resources:** We used our scrapers on Yelp (https://www.yelp.com/) to find restaurants and AllRecipes (https://www.allrecipes.com/) to find recipes. All images of recipes are from AllRecipes.

**Separation of Work:** 
- Jordan Locke: Created the search for recipes page, recipe results page, save/delete feature for the recipes, table to hold the recipe results, table to hold the saved recipes, and the initial setup. Also met multiple times with the group throughout the semester.
- Ashton Frias: Created the email feature, search for restaurants page, table to hold the restaurant results, and restaurant results page. Also met multiple times with the group throughout the semester.
- Colin Houde: Improved the UI for all of the web pages and met multiple times with the group throughout the semester.
- Addison Nugent: 
