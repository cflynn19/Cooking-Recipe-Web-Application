
import sys
  

sys.path.append('../Cooking-Recipe-Web-Application-feature-google-api/spoonacular_api')
sys.path.append('../Cooking-Recipe-Web-Application-feature-google-api/Google_Cloud_Vision_API')


from google_cloud_vision_api_class import google_cloud_vision_api
from spoonacular_api_class import spoonacular_api as sp

class both_api:

  # Take image input - Call Google API for object recognition - Call Spoonacular API for recipes
  def get_recipe_from_cloud(self, image_url):
    google_api = google_cloud_vision_api()
    google_api.detect_label(image_url)
    labels = google_api.get_labels()
    self.get_recipe_from_spoon(labels)
    recipe = self.ingredients(labels)
    return recipe

    
  def ingredients(self, key: str):
    temp = []
    spoon_api = sp()
    for i in key:
      temp.append(i)
    ingredients = []
    for j in temp:
        ingredients.append(spoon_api.get_top_ingredient(j))
    return ingredients
  
  # Call Spoonacular API to get recipes
  def get_recipe_from_spoon(self, keys):
    spoon_api = sp()
    search_key = ""
    for i in range(len(keys)):
      if i < len(keys)-1:
        search_key = search_key + keys[i] + ", "
      else:
        search_key = search_key + keys[i]
    data = spoon_api.search_recipe_by_ingredients(search_key)
    return data


    
    


    
