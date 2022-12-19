import sys
sys.path.append('./spoonacular_api')
import spoonacular_api_class

sp = spoonacular_api_class.spoonacular_api()

def test_retrieve_title_and_id():
    data = sp.search_recipe_by_ingredients("apples, bananas")

    last_receipe = data[-1]
    last_receipe_id = last_receipe['id']
    data = sp.get_recipe_by_id(last_receipe_id)
    assert data['title'] == last_receipe['title']
    assert data['id'] == last_receipe['id']

def test_get_number_of_recipes():
    sp.search_recipe_by_ingredients("apples, bananas")
    assert sp.get_number_of_recipes() == 10

def test_get_id():
    sp.search_recipe_by_ingredients("apples, bananas")
    assert sp.get_id(0) == '665469'

def test_get_title():
    sp.search_recipe_by_ingredients("apples, bananas")
    assert sp.get_title(0) == "Xocai Healthy Chocolate Peanut Butter Bannana Dip"

def test_get_image_link():
    sp.search_recipe_by_ingredients("apples, bananas")
    assert sp.get_image_link(0) == 'https://spoonacular.com/recipeImages/665469-312x231.jpg'

def test_get_summary():
    sp.search_recipe_by_ingredients("apples, bananas")
    assert "Xocai Healthy Chocolate Peanut Butter Bannana Dip might" in sp.get_summary(0)

def test_get_used_ingredients_description():
    sp.search_recipe_by_ingredients("apples, bananas")
    assert sp.get_used_ingredients_description(0) == ['1 stem Bananas (Banana, peeled)', '1 chunk Chocolate (Xocai Nugget)']

def test_get_used_ingredients_image():
    sp.search_recipe_by_ingredients("apples, bananas")
    assert sp.get_used_ingredients_image(0) == ['https://spoonacular.com/cdn/ingredients_100x100/bananas.jpg', 'https://spoonacular.com/cdn/ingredients_100x100/milk-chocolate.jpg']

def test_get_unused_ingredients_description():
    sp.search_recipe_by_ingredients("apples, bananas")
    assert sp.get_unused_ingredients_description(0) == []

def test_get_missed_ingredients_description():
    sp.search_recipe_by_ingredients("apples, bananas")
    assert sp.get_missed_ingredients_description(0) == ['1 tbsp Peanut Butter (Natural Peanut Butter)']

def test_get_missed_ingredients_image();
    sp.search_recipe_by_ingredients("apples, bananas")
    assert sp.get_missed_ingredients_image(0) == ['https://spoonacular.com/cdn/ingredients_100x100/peanut-butter.png']

def test_get_vegetarian():
    sp.search_recipe_by_ingredients("apples, bananas")
    assert sp.get_vegetarian(0) == False

def test_get_vegan():
    sp.search_recipe_by_ingredients("apples, bananas")
    assert sp.get_vegan(0) == False

def test_get_glutenFree():
    sp.search_recipe_by_ingredients("apples, bananas")
    assert sp.get_glutenFree(0) == True

def test_get_dairyFree():
    sp.search_recipe_by_ingredients("apples, bananas")
    assert sp.get_dairyFree(0) == True

def test_get_instructions():
    sp.search_recipe_by_ingredients("apples, bananas")
    assert "Place Nugget in a custard cup" in sp.get_instructions(0)

def test_get_time():
    sp.search_recipe_by_ingredients("apples, bananas")
    assert sp.get_time(0) == 45

def test_get_servings():
    sp.search_recipe_by_ingredients("apples, bananas")
    assert sp.get_servings(0) == 1

def test_get_price():
    sp.search_recipe_by_ingredients("apples, bananas")
    assert sp.get_price(0) == 66.45
