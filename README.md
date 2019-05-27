# Stream 3 - Data Centric Development Milestone Project | Cocktail Cookbook

The Cocktail Cookbook is a data-driven website designed to allow people to find something a bit different from the off-the-shelf drinks of a supermarket. Featuring old classics and custom creations, there is bound to be a drink you will like, be it alcoholic or otherwise. No registration is required to search and view recipes, but doing so is simple and easy and allows to you create, edit and delete your own. All recipes on the database are shown by default, but there are five select boxes to filter and sort the recipes to find something you love. The recipes shown this way only display basic information, but clicking the eye symbol on the right hand side of each recipe will take you to a detailed view, showing the ingredients and instruction on how to make the drink.

This website makes use of Flask, Python and MongoDB for the backend and the usual trio of HTML, CSS and JavaScript for the frontend. Ajax is also used to allow for filtering and sorting.

## UX
### Scope
Reading through the breif for this project, I devised the following requirements and features as follows:
#### Necessary Content/Functionality
- Ability to add, edit and remove recipes
- Ability to filter and sort recipes based on some of their aspects
- Seperate pages for viewing a recipe in full and a list of recipes that match search criteria
- A user-friendly front-end to do all of the above

#### Important Content/Functionality
- Basic user authentication to prevent users from editing and deleting recipes that they did not create
- A count of the number of matching recipes found


### Structure
The database schema can be found [here](https://github.com/GeneralPeaceful/cocktail_cookbook/tree/master/static/schema.txt).

No wireframes or mockups were created during the design process, as the template was used from a [Code Institute lesson](https://github.com/Code-Institute-Solutions/TaskManager/tree/master/07-AddingApplicationNavigation/01-adding_a_navigation_bar) that I then added to and tweaked to suit my application.

The login, failed login, registration and failed registration pages were copied from [Alex Thirlwell's Global Online Cookbook](https://github.com/Code-Institute-Submissions/global-cookbook-application). When viewing their Heroku application for inspiration I decided that the design was very simple and effective, and fitted well with the style I was using for my project. The file names were changed in keeping with the naming convention I use, and some of the base code was also tweaked for aesthetic purposes.


## Features
### Existing Features
- All recipes shown by default, sorted A-Z
- Ability to change sorting with several options (Z-A, base, author, etc.)
- Ability to filter recipes based on characteristics (base, strength, suitable occasions, etc.)
- Ability to click on a recipe to view more details about it (ingredients, recipe itself)
- Ability to register and log in, in order to:
    - Add new recipes
    - Edit existing recipes that the user created
    - Delete existing recipes that the user created
    - Log out again

### Features Left to Implement
- Encode passwords for added security *(possibly username too?)*
- Pagination for if search results number higher than 20? 30? *(possibly make number per page a user option)*
- Age check prior to using the application (for what good that does when faced with a determined adolescent)
- Ability to remove user from the known-user database (read: delete my account)*(possibly difficult if recipes have been created. Maybe ask user if they want their recipes deleted too?)*
- Text input search bar on the 'home' page to allow users to search for more specific recipes (such as all recipes from Greg, with a Gin base, that also have Amaretto as an ingredient)
- Likes, dislikes and comments to allow further sorting by popularity, as well as create a more engaging user-to-user experience
- Image uploads to show what you think your drink should look like *(in addrecipe.html)*

## Technologies Used
As mentioned in the summary, this application makes use of Python with the Flask framework and MongoDB for the backend and HTML, Javascript with jQuery and Ajax libraries, and CSS with Materialize and Fontawesome libraries for the frontend. I also made use of [Inkscape](https://inkscape.org/) to modify the SVGs that make up the 'strength' icons for the recipes.
- [Materialize](https://materializecss.com/)
    - Used for rapid creation of a default styled layout, as well as some icons.
- [Fontawesome](https://fontawesome.com/)
    - Used to display custom eye-catching icons.
- [Flask](http://flask.pocoo.org/)
    - Used for templating in Python along with redirecting, enabling cookies and reading POST data.

## Testing
All of the testing was done manually 'in-browser', since I was usually clicking through the links each time I changed or added new functionality to make sure that everything still worked. For example I spent a long time struggling to get the 'occasions' multiple-select working in both addrecipe and editrecipe since I was unsure how to prevent Python from overwriting the previous options when the data was POSTed. The dictionary that was submitted would have multiple 'occasions' keys with different values, and the last value was what was set as the only value, as a string. I had a work colleague suggest using hidden inputs, which solved the problem by adding each 'occasion' selected into a string, which I could then separate into an array by splitting the string on the commas.

These tests were done on Google Chrome, Edge and Firefox, in both desktop and mobile formats, but I would also have liked to have done the tests mentioned above on both Safari and Opera to be able to cover all bases.

## Deployment
The application has been deploed to Heroku at http://cocktail-cookbook.herokuapp.com/get_recipes.

You can register to start using the full functionality of the app, or alternatively login with the following details:

Username: username

Password: password

Heroku needs several things doing before deployment can happen:
1. Procfile - named exactly like that, this tells Heroku what environment it needs to set up (in this case, a web env)
2. requirements.txt - named exactly that, this tells Heroku what packages it needs to install to allow the python file(s) to function
3. Environment variables - these are stored in Heroku as config variables for increased security (as I prefer my usernames and passwords to not be displayed to the world on Github):
    - MONGO_URI: the variable that specifies what MongoDB database to access. This URI includes the username and password required to access said database
    - secret key: adds security by either locking or unlocking access to the application. Should only be known by one person
    - PORT and IP: environment variables used to access the application

While all four environment variables are set in Heroku's config vars, the last three mentioned also have backup values.

## Credits
Recipes have been added from thebar.com, drinkaware.co.uk, esquire.com, wikipedia.org and Greg, the youtuber behind [How to Drink](https://www.youtube.com/channel/UCioZY1p0bZ4Xt-yodw8_cBQ)