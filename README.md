# Southeast Feasts - Milestone Project 3

[View the live project here.](https://southeast-feasts.herokuapp.com/)

## Project Overview

The Project goal is to create a data orientated website to allow the user to find and share recipes with other users. The theme of the website is specifically targeted to an audience interested in South East Asian Cuisine.

<img src="">

## Project Goals

* The Website must be fully responsive on all devices.
* To allow the user to find and share recipes.
* Clear design presentation which allows the the user to navigate easily.
* To maximise future maintainability through documentation, code structure and organisation.
* To allow the user to add, edit and delete recipes through their profile page (CRUD functionality).
* Admin user will have full visibility of recipes added from other users and will be able to perform CRUD operations on these recipes also.
* To allow users to search for specific recipes whether that be by Country, ingredient or recipe name.
* The target users will be for anyone interested in South East Asian Cuisine.

## User Stories

### New Users:

* As a new user what service does this website provide?
* As a new user how do I register?
* As a new user how do I discover new recipes by country?
* As a new user how do I search for specific recipes?
* As a new user how do I find ingredients list and method to cook the recipe?

### Existing Users:

* As an existing user how do I log into my account?
* As an existing user how do I view my profile?
* As an existing user how do I share a new recipe?
* As an existing user how do I edit/delete an existing recipe?

## Design

### 1. Colour Scheme
* A materalize tropical green - #00e676(green accent-3) has been used as the main background color for the Navbar, Footer, font awesome icons & buttons as asian cuisine has often vibrant greens in the cuisine so ties in with the theme. 
* For the hr the same color green has been used to seperate content.
* For the recipe cards the same color green has been used for the background color for the recipe name to make the recipe stand out with a white text and text shadow.
* For the base background color a materlaize light grey (grey lighten-4) has been used so all text is easy to read.

### 2. Typography
* The font style of Be Vietnam has been chosen for all font across the website. The letterforms are clean, modern and straightforward.
* All font has a letter spacing of 0.05em to make it easier to read.
* The fallback fonts across all webpages is sans serif for any reason the main fonts do not import correctly.

### 3. Imagery
* Home Page - Home Banner at the top of the page of some rice terraces in Indonesia. The greens of the image blend nicely with the materalize green in the Nav Bar to suit the theme. Also rice is a staple across South East Asia so ties in with the recipe theme.
* Recipe Cards - Image for each recipe shown on recipe cards by inputing the URL when adding a new recipe. Can also Zoom onto the image on click to take a closer look.
* Home Page - Share recipe image shows people sharing a dish which links to the signup/signin page, If session user is logged in will take you to add recipe page.
* Home Page - Discover recipe image takes you to all recipe page.
* Home Page - Materalize Carousel displays country flags for South East Asian Countrys above the footer which fits the theme of the website.
* Recipes Page - Depending on which country is selected the appropriate flag will display in the heading.
* SignIn/Sign Up Page - Full Screen background image of a local market it Vietnam with plenty of fresh ingredients. Fits in with the theme of the website.
* Add/Edit Recipe Page - Full Screen background image of a hot chilli peppers displayed as asian cuisine often is spicy so fits in with the theme.

### 4. Icons
* Various Font Aewsome icons displayed across the entire site depending on which field you are filling in / which information is being displayed.[Font Awesome](https://fontawesome.com/v4.7.0/).

## WireFrames

Initial Wireframe designs made on Figma:

* [Desktop]() 
* [Mobile]() 

## Features / User Stories Testing

* Home Page(index.html)
    * NavBar when new user only Home, Recipes & SignIn/SignUp will display. Therefore a new user to can take a look at the recipes available and sign up if they so choose. - **As a new user how do I register?**
    * Welcome Section - a small paragraph explaining the purpose of the website. This meets the requirement of the user story - **As a new user what service does this website provide?**
    * Recently created recipes section - The 4 most recently created recipes, by clicking the the card panel the recipe description will be displayed showing ingredients, method and additional info.
    * Share & Discover Section - Links to add a new recipe or sign up depending if you are signed in or not by session user. Discover image takes to to all recipe page.
    * Carousel - displaying South Eastern Asian flags.
    * Footer - Social Font Awesome Links
    
* Recipes Page (recipes.html)
    * Displays recipes by country by the Navbar dropdown, this will also display appropriate flag within heading. - **As a new user how do I discover new recipes by country?**
    * Search functionality will allow the user to search by either recipe Name, country or ingredient. - **As a new user how do I search for specific recipes?**
    * By resetting the search button this will send the user back to all recipes.
    * Link to recipe description by clicking card panel (recipe.html). Image on Card panel will allow the user to take a closer look at the recipe image. - **As a new user how do I find ingredients list and method to cook the recipe?**

