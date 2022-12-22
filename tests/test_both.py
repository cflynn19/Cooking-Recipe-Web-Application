import sys
sys.path.append('../Cooking-Recipe-Web-Application-feature-google-api/spoonacular_and_cloud')
from both_api import both_api

both_api = both_api()

def test_get_ingredients_from_img():
    image_url = 'https://www.naijaloaded.com.ng/wp-content/uploads/2019/10/featured-18.jpg'

    recipe = both_api.get_recipe_from_cloud(image_url)
    assert len(recipe) > 1

def test_get_recipe_from_spoon():
    keys = ['apple', 'banana', 'juice']
    recipe = both_api.get_recipe_from_spoon(keys)
    assert len(recipe) > 1
    
test_get_ingredients_from_img()
test_get_recipe_from_spoon()
