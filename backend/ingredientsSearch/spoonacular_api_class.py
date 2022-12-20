import spoonacular as sp
import json

# Spoonacular API key
api = sp.API("ENTER Spoonacular Key")

class spoonacular_api:
    # Constructor
    def __init__(self):
        self.full_recipe_retrieved = {}

    # Retrieve recipes from ingredients
    def search_recipe_by_ingredients(self, ingredients: str):
        response = api.search_recipes_by_ingredients(ingredients)
        self.recipes = response.json()
        return self.recipes

    # Retrieve recipe details given ID, for example, ID from previous search result
    def get_full_recipe(self, id_num: int):
        if not (id_num in self.full_recipe_retrieved.keys()):
            self.full_recipe_retrieved[id_num] = api.get_recipe_information(id_num).json()
        return self.full_recipe_retrieved[id_num]
    
    # Helper function to beautify printing JSON
    def print_json(self, json_data):
        print(json.dumps(json_data, indent = 4))
    
    # Return the number of recipes fetched
    def get_number_of_recipes(self):
        return len(self.recipes)

    # Return all recipes fetched
    def get_all_recipes(self):
        return self.recipes

    # Get a recipe at specified index
    def get_recipe(self, recipe_index: int):
        assert recipe_index < self.get_number_of_recipes()
        return self.recipes[recipe_index]
    
    # Get the ID of the recipe at specified index
    def get_id(self, recipe_index: int):
        recipe = self.get_recipe(recipe_index)
        return recipe.get("id")
    
    # Get the title of the recipe at specified index
    def get_title(self, recipe_index: int):
        recipe = self.get_recipe(recipe_index)
        return recipe.get("title")
    
    # Get the link to the image used in recipe at specified index
    def get_image_link(self, recipe_index: int):
        recipe = self.get_recipe(recipe_index)
        return recipe.get("image")
    
    # Get the summary of the recipe at specified index
    def get_summary(self, recipe_index: int):
        id_num = self.get_id(recipe_index)
        return self.get_full_recipe(id_num).get("summary")
    
    # Get the ingrediednts that are used
    def get_used_ingredients_description(self, recipe_index: int):
        recipe = self.get_recipe(recipe_index)
        used_ingredients_description = []
        for i in recipe["usedIngredients"]:
            used_ingredients_description.append(i.get("original"))
        return used_ingredients_description
    
    # Get the images of ingredients that are used
    def get_used_ingredients_image(self, recipe_index: int):
        recipe = self.get_recipe(recipe_index)
        used_ingredients_image = []
        for i in recipe["usedIngredients"]:
            used_ingredients_image.append(i.get("image"))
        return used_ingredients_image

    # Get the unused ingredients
    def get_unused_ingredients_description(self, recipe_index: int):
        recipe = self.get_recipe(recipe_index)
        unused_ingredients_description = []
        for i in recipe["unusedIngredients"]:
            unused_ingredients_description.append(i.get("original"))
        return unused_ingredients_description

    # Get the ingredients that the user is missing
    def get_missed_ingredients_description(self, recipe_index: int):
        recipe = self.get_recipe(recipe_index)
        missed_ingredients_description = []
        for i in recipe["missedIngredients"]:
            missed_ingredients_description.append(i.get("original"))
        return missed_ingredients_description

    # Get the image of the ingredients that the user is missing
    def get_missed_ingredients_image(self, recipe_index: int):
        recipe = self.get_recipe(recipe_index)
        missed_ingredients_image = []
        for i in recipe["missedIngredients"]:
            missed_ingredients_image.append(i.get("image"))
        return missed_ingredients_image
    
    # Get recipes for vegetarians
    def get_vegetarian(self, recipe_index: int):
        id_num = self.get_id(recipe_index)
        return self.get_full_recipe(id_num).get("vegetarian")

    # Get recipes for vegan
    def get_vegan(self, recipe_index: int):
        id_num = self.get_id(recipe_index)
        return self.get_full_recipe(id_num).get("vegan")

    # Get recipes without Gluten
    def get_glutenFree(self, recipe_index: int):
        id_num = self.get_id(recipe_index)
        return self.get_full_recipe(id_num).get("glutenFree")

    # Get recipes without diary
    def get_dairyFree(self, recipe_index: int):
        id_num = self.get_id(recipe_index)
        return self.get_full_recipe(id_num).get("dairyFree")

    # Get instructions on how to make the recipe
    def get_instructions(self, recipe_index: int):
        id_num = self.get_id(recipe_index)
        return self.get_full_recipe(id_num).get("instructions")
    
    # Get the time needed to cook the recipe
    def get_time(self, recipe_index: int):
        id_num = self.get_id(recipe_index)
        return self.get_full_recipe(id_num).get("readyInMinutes")

    # Get the amount of servings
    def get_servings(self, recipe_index: int):
        id_num = self.get_id(recipe_index)
        return self.get_full_recipe(id_num).get("servings")

    # Get the price needed in cooking this recipe
    def get_price(self, recipe_index: int):
        id_num = self.get_id(recipe_index)
        return self.get_full_recipe(id_num).get("pricePerServing")