

# Pokedex

Let's build a searchable pokedex! First we'll load the data from a `json` file into our own database. Then we'll list those pokemon in the page and add search and pagination.

- [Part 1: Create Your Model](#part-1-create-your-model)
- [Part 2: Load Data into DB](#part-2-load-data-into-db)
- [Part 3: Create a View with a JsonResponse](#part-3-create-a-view-with-a-jsonresponse)
- [Part 4: Create a Vue App](#part-4-create-a-vue-app)
- [Part 5: Add Search](#part-5-add-search)
- [Part 7: Add Types (optional)](#part-7-add-types-optional)
- [Part 8: Add Pagination (optional)](#part-8-add-pagination-optional)
- [Part 9: More Pokemon (optional)](#part-9-more-pokemon-optional)


![pokedex diagram](pokedex.png)


## Part 1: Create Your Model

Create a project `pokeproj` and app `pokeapp`. In the app, create a model `Pokemon` to store our pokemon. For now, store `types` as comma-separated values (`poison,grass`, `flying,fire`).

`Pokemon`
- `number` (IntegerField)
- `name` (CharField)
- `height` (FloatField)
- `weight` (FloatField)
- `image_front` (CharField)
- `image_back` (CharField)
- `types` (CharField)


## Part 2: Load Data into DB

Write a [custom management command](../../3%20Django/docs/01%20Django%20Overview.md#custom-management-commands) `load_pokemon.py` to load the data from [pokemon.json](./pokemon.json) into your database. You can do this by saving the file next to your `.py` file and using [open](../../1%20Python/docs/File%20IO.md). In the first line of your management command, you may want to delete all the records in the table so each time you run it you start with a clean slate. To verify that the data was loaded, log into your admin panel and check that the pokemon are there.

The data was taken from the [PokeAPI](https://pokeapi.co/docs/v2#pokemon), `height` is in decimeters (divide by 10 to get meters) and `weight` is in hectograms (divide by 10 to get kilograms). You may want to convert these values before saving them.

## Part 3: Create a View with a JsonResponse

Create a view `pokemon` that gets a list of `Pokemon` out of the database and turns them into a dictionary to be passed to `JsonResponse`. Verify this works by going to `localhost:8000/pokemon/` in your browser and seeing a list of pokemon in JSON.

## Part 4: Create a Vue App

Create a second view `index` that renders a template containing a Vue app (don't forget to change the delimiters on the Vue app so it doesn't conflict with the template rendering syntax). Use Axios to send a request to the `pokemon` view and display a list of pokemon on the page with their images. In your Vue app, you'll need to [switch the delimiters](https://stackoverflow.com/questions/48125577/how-to-change-delimiters-in-vue-js) so they don't conflict with the Django template rendering syntax.

## Part 5: Add Search

Add an input and button at the top to search for pokemon. When the user hits 'enter' or presses 'search', use Axios to send a GET request containing the search term as a param. Modify the `pokemon` view to take the search term to query the database, and only turn matching pokemon into JSON ([search](https://docs.djangoproject.com/en/3.0/topics/db/search/), [icontains](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#std:fieldlookup-icontains), [stack overflow answer](https://stackoverflow.com/questions/38478635/search-using-multiple-fields-django-building-the-object-list)).


## Part 7: Add Types (optional)

Instead of storing our types as comma-separated strings we must parse every time we want to display it, it's much beter to store types as a [many-to-many](https://docs.djangoproject.com/en/3.2/topics/db/examples/many_to_many/) field.

- PokemonType
  - name (CharField)
- Pokemon
  - ...
  - types (ManyToMany with PokemonType)


## Part 8: Add Pagination (optional)

Use pagination to only show 20 pokemon at a time, allow the user to switch between pages. This can be accomplished by allowing the `pokemon` view to take additional query parameters, `page` and `limit`. Use the [Django paginator](https://docs.djangoproject.com/en/3.2/topics/pagination/) to separate the query set into pages and return only the requested page in JSON.

## Part 9: More Pokemon (optional)

Check out the [script](./pokedex.py) that creates the json file, you can use it to load even more pokemon into your database!

